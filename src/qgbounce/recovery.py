"""Operational recovery diagnostics for low-dimensional quantum channels."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from .channels import channel_choi_state, compose_channels, validate_kraus
from .quantum import density_matrix, maximally_entangled_pair

Array = np.ndarray


def entanglement_fidelity(kraus: Iterable[Array]) -> float:
    """Entanglement fidelity for the maximally mixed input.

    The channel must have equal input and output dimensions. The exact Kraus
    formula is ``F_e = d^-2 sum_i |Tr K_i|^2``.
    """
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, output_dim = validate_kraus(operators)
    if input_dim != output_dim:
        raise ValueError(
            "entanglement fidelity requires equal input/output dimensions"
        )
    value = sum(abs(np.trace(k)) ** 2 for k in operators) / (input_dim**2)
    return float(np.clip(value.real, 0.0, 1.0))


def average_state_fidelity(kraus: Iterable[Array]) -> float:
    """Haar-average pure-state fidelity from entanglement fidelity."""
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, output_dim = validate_kraus(operators)
    if input_dim != output_dim:
        raise ValueError("average fidelity requires equal input/output dimensions")
    fidelity = entanglement_fidelity(operators)
    return float((input_dim * fidelity + 1.0) / (input_dim + 1.0))


def trace_distance(rho: Array, sigma: Array) -> float:
    """Return ``0.5 ||rho-sigma||_1`` for Hermitian density matrices."""
    rho = np.asarray(rho, dtype=np.complex128)
    sigma = np.asarray(sigma, dtype=np.complex128)
    if (
        rho.shape != sigma.shape
        or rho.ndim != 2
        or rho.shape[0] != rho.shape[1]
    ):
        raise ValueError("rho and sigma must be square matrices of equal shape")
    delta = 0.5 * ((rho - sigma) + (rho - sigma).conj().T)
    return float(0.5 * np.sum(np.abs(np.linalg.eigvalsh(delta))))


def purified_distance_from_pure_target(rho: Array, target: Array) -> float:
    """Purified distance when ``target`` is a pure state vector."""
    rho = np.asarray(rho, dtype=np.complex128)
    target = np.asarray(target, dtype=np.complex128).reshape(-1)
    target = target / np.linalg.norm(target)
    if rho.shape != (target.size, target.size):
        raise ValueError("rho and target dimensions do not match")
    fidelity = float(np.real(target.conj() @ rho @ target))
    return float(
        np.sqrt(max(0.0, 1.0 - np.clip(fidelity, 0.0, 1.0)))
    )


@dataclass(frozen=True)
class RecoveryDiagnostics:
    """Operational diagnostics for a recovered channel relative to identity."""

    entanglement_fidelity: float
    average_state_fidelity: float
    choi_trace_distance: float
    choi_purified_distance: float


def recovery_diagnostics(
    channel: Iterable[Array],
    recovery: Iterable[Array],
) -> RecoveryDiagnostics:
    """Compose a recovery after a channel and compare its Choi state to identity."""
    effective = compose_channels(recovery, channel)
    input_dim, output_dim = validate_kraus(effective)
    if input_dim != output_dim:
        raise ValueError("recovered channel must return to the input dimension")
    choi = channel_choi_state(effective)
    phi = maximally_entangled_pair(input_dim)
    target = density_matrix(phi)
    fidelity = entanglement_fidelity(effective)
    return RecoveryDiagnostics(
        entanglement_fidelity=fidelity,
        average_state_fidelity=average_state_fidelity(effective),
        choi_trace_distance=trace_distance(choi, target),
        choi_purified_distance=purified_distance_from_pure_target(choi, phi),
    )
