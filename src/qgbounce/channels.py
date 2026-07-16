"""Finite-dimensional quantum channels used by the stress-test suite.

All channels are represented by dense Kraus operators. The routines are
intended for low-dimensional validation and transparent counterexamples, not
large-scale many-body numerics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np

from .quantum import (
    density_matrix,
    maximally_entangled_pair,
    partial_trace,
    von_neumann_entropy,
)

Array = np.ndarray


def _as_kraus(kraus: Iterable[Array]) -> tuple[Array, ...]:
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    if not operators:
        raise ValueError("at least one Kraus operator is required")
    shape = operators[0].shape
    if len(shape) != 2 or any(k.shape != shape for k in operators):
        raise ValueError("all Kraus operators must have one common matrix shape")
    return operators


def validate_kraus(kraus: Iterable[Array], *, atol: float = 1e-10) -> tuple[int, int]:
    """Validate a Kraus representation as trace preserving.

    Complete positivity follows from the Kraus representation. Trace
    preservation is checked through ``sum_i K_i^\dagger K_i = I``.
    """
    operators = _as_kraus(kraus)
    output_dim, input_dim = operators[0].shape
    completeness = sum(
        (k.conj().T @ k for k in operators),
        np.zeros((input_dim, input_dim), dtype=np.complex128),
    )
    if not np.allclose(completeness, np.eye(input_dim), atol=atol):
        raise ValueError("Kraus operators are not trace preserving")
    return input_dim, output_dim


def apply_channel(rho: Array, kraus: Iterable[Array]) -> Array:
    """Apply a CPTP map to one density matrix."""
    operators = _as_kraus(kraus)
    input_dim, output_dim = validate_kraus(operators)
    rho = np.asarray(rho, dtype=np.complex128)
    if rho.shape != (input_dim, input_dim):
        raise ValueError(f"rho must have shape {(input_dim, input_dim)}")
    return sum(
        (k @ rho @ k.conj().T for k in operators),
        np.zeros((output_dim, output_dim), dtype=np.complex128),
    )


def compose_channels(after: Iterable[Array], before: Iterable[Array]) -> tuple[Array, ...]:
    """Return Kraus operators for ``after o before``."""
    before_ops = _as_kraus(before)
    after_ops = _as_kraus(after)
    _, before_out = validate_kraus(before_ops)
    after_in, _ = validate_kraus(after_ops)
    if before_out != after_in:
        raise ValueError("channel dimensions do not compose")
    composed = tuple(r @ k for r in after_ops for k in before_ops)
    validate_kraus(composed)
    return composed


def stinespring_isometry(kraus: Iterable[Array]) -> Array:
    """Build ``V:X -> A tensor E`` with the Kraus index stored in ``E``."""
    operators = _as_kraus(kraus)
    input_dim, output_dim = validate_kraus(operators)
    env_dim = len(operators)
    isometry = np.zeros(
        (output_dim * env_dim, input_dim),
        dtype=np.complex128,
    )
    for environment_index, operator in enumerate(operators):
        for output_index in range(output_dim):
            isometry[output_index * env_dim + environment_index, :] = operator[
                output_index,
                :,
            ]
    if not np.allclose(
        isometry.conj().T @ isometry,
        np.eye(input_dim),
        atol=1e-10,
    ):
        raise AssertionError("internal Stinespring construction failed")
    return isometry


def channel_choi_state(kraus: Iterable[Array]) -> Array:
    """Return the normalized Choi state on reference ``R`` and output ``A``."""
    operators = _as_kraus(kraus)
    input_dim, output_dim = validate_kraus(operators)
    phi = maximally_entangled_pair(input_dim)
    rho = density_matrix(phi)
    result = np.zeros(
        (input_dim * output_dim, input_dim * output_dim),
        dtype=np.complex128,
    )
    for operator in operators:
        lifted = np.kron(
            np.eye(input_dim, dtype=np.complex128),
            operator,
        )
        result += lifted @ rho @ lifted.conj().T
    return result


def complementary_choi_state(kraus: Iterable[Array]) -> Array:
    """Return the normalized Choi state on reference ``R`` and environment ``E``."""
    operators = _as_kraus(kraus)
    input_dim, output_dim = validate_kraus(operators)
    isometry = stinespring_isometry(operators)
    state_rae = (
        np.kron(np.eye(input_dim, dtype=np.complex128), isometry)
        @ maximally_entangled_pair(input_dim)
    )
    rho_rae = density_matrix(state_rae)
    return partial_trace(
        rho_rae,
        (input_dim, output_dim, len(operators)),
        {0, 2},
    )


def coherent_information(kraus: Iterable[Array]) -> float:
    """Return ``I_c(R> A) = S(A) - S(RA)`` for maximally mixed input."""
    operators = _as_kraus(kraus)
    input_dim, output_dim = validate_kraus(operators)
    choi = channel_choi_state(operators)
    rho_a = partial_trace(choi, (input_dim, output_dim), {1})
    return von_neumann_entropy(rho_a) - von_neumann_entropy(choi)


def holevo_information(
    probabilities: Sequence[float],
    states: Sequence[Array],
    kraus: Iterable[Array],
) -> float:
    """Compute the Holevo information of an input ensemble after a channel."""
    probabilities = np.asarray(probabilities, dtype=float)
    if probabilities.ndim != 1 or len(probabilities) != len(states):
        raise ValueError(
            "probabilities and states must have equal one-dimensional length"
        )
    if np.any(probabilities < 0) or not np.isclose(probabilities.sum(), 1.0):
        raise ValueError("probabilities must be nonnegative and sum to one")
    outputs = [apply_channel(state, kraus) for state in states]
    average = sum(
        (
            probability * state
            for probability, state in zip(probabilities, outputs, strict=True)
        ),
        np.zeros_like(outputs[0]),
    )
    return von_neumann_entropy(average) - float(
        sum(
            probability * von_neumann_entropy(state)
            for probability, state in zip(probabilities, outputs, strict=True)
        )
    )


def identity_channel(dim: int = 2) -> tuple[Array, ...]:
    if dim <= 0:
        raise ValueError("dim must be positive")
    return (np.eye(dim, dtype=np.complex128),)


def erasure_channel(probability: float, dim: int = 2) -> tuple[Array, ...]:
    """Qudit erasure channel with an orthogonal output flag state."""
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must lie in [0, 1]")
    if dim <= 0:
        raise ValueError("dim must be positive")
    operators: list[Array] = []
    transmitted = np.zeros((dim + 1, dim), dtype=np.complex128)
    transmitted[:dim, :] = np.sqrt(1.0 - probability) * np.eye(dim)
    operators.append(transmitted)
    for basis_index in range(dim):
        erased = np.zeros((dim + 1, dim), dtype=np.complex128)
        erased[dim, basis_index] = np.sqrt(probability)
        operators.append(erased)
    result = tuple(operators)
    validate_kraus(result)
    return result


def erasure_recovery(dim: int = 2) -> tuple[Array, ...]:
    """Decode the unerased sector and replace an erasure by ``I/d``."""
    if dim <= 0:
        raise ValueError("dim must be positive")
    operators: list[Array] = []
    transmitted = np.zeros((dim, dim + 1), dtype=np.complex128)
    transmitted[:, :dim] = np.eye(dim)
    operators.append(transmitted)
    for basis_index in range(dim):
        replacement = np.zeros((dim, dim + 1), dtype=np.complex128)
        replacement[basis_index, dim] = 1.0 / np.sqrt(dim)
        operators.append(replacement)
    result = tuple(operators)
    validate_kraus(result)
    return result


def dephasing_channel(probability: float) -> tuple[Array, ...]:
    """Qubit phase-flip channel ``(1-p)rho + p Z rho Z``."""
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must lie in [0, 1]")
    z = np.diag([1.0, -1.0]).astype(np.complex128)
    return (
        np.sqrt(1.0 - probability) * np.eye(2),
        np.sqrt(probability) * z,
    )


def dephasing_pauli_recovery(probability: float) -> tuple[Array, ...]:
    """Best fixed Pauli correction for the known phase-flip probability."""
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must lie in [0, 1]")
    if probability <= 0.5:
        return identity_channel(2)
    return (np.diag([1.0, -1.0]).astype(np.complex128),)


def depolarizing_channel(probability: float) -> tuple[Array, ...]:
    """Qubit channel ``N(rho)=(1-p)rho+p I/2``."""
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability must lie in [0, 1]")
    identity = np.eye(2, dtype=np.complex128)
    x = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
    z = np.diag([1.0, -1.0]).astype(np.complex128)
    return (
        np.sqrt(1.0 - 3.0 * probability / 4.0) * identity,
        np.sqrt(probability / 4.0) * x,
        np.sqrt(probability / 4.0) * y,
        np.sqrt(probability / 4.0) * z,
    )


def amplitude_damping_channel(gamma: float) -> tuple[Array, ...]:
    """Qubit amplitude-damping channel with excited-state decay ``gamma``."""
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must lie in [0, 1]")
    k0 = np.array(
        [[1.0, 0.0], [0.0, np.sqrt(1.0 - gamma)]],
        dtype=np.complex128,
    )
    k1 = np.array(
        [[0.0, np.sqrt(gamma)], [0.0, 0.0]],
        dtype=np.complex128,
    )
    return (k0, k1)


@dataclass(frozen=True)
class ChannelInformation:
    """Reference/output diagnostics for the maximally mixed channel input."""

    coherent_information: float
    output_entropy: float
    exchange_entropy: float


def channel_information(kraus: Iterable[Array]) -> ChannelInformation:
    operators = _as_kraus(kraus)
    input_dim, output_dim = validate_kraus(operators)
    choi = channel_choi_state(operators)
    output = partial_trace(choi, (input_dim, output_dim), {1})
    output_entropy = von_neumann_entropy(output)
    exchange_entropy = von_neumann_entropy(choi)
    return ChannelInformation(
        coherent_information=output_entropy - exchange_entropy,
        output_entropy=output_entropy,
        exchange_entropy=exchange_entropy,
    )
