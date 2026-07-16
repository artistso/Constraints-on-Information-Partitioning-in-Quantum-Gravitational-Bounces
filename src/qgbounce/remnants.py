"""Finite-remnant dimension bounds and random-isometry stress tests."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .quantum import (
    apply_input_isometry,
    density_matrix,
    haar_random_isometry,
    maximally_entangled_pair,
    mutual_information,
    partial_trace,
    von_neumann_entropy,
)

Array = np.ndarray


def remnant_information_cap(
    dim_b: int,
    entropy_reference: float | None = None,
) -> float:
    """Upper bound on ``I(R:B)`` from the remnant Hilbert-space dimension.

    For any state, ``I(R:B) <= 2 min(S(R), log2(dim B))``. When ``S(R)`` is
    omitted, the dimension-only cap ``2 log2(dim B)`` is returned.
    """
    if dim_b <= 0:
        raise ValueError("dim_b must be positive")
    cap = 2.0 * np.log2(dim_b)
    if entropy_reference is None:
        return float(cap)
    if entropy_reference < 0:
        raise ValueError("entropy_reference must be nonnegative")
    return float(min(2.0 * entropy_reference, cap))


def radiation_information_lower_bound(
    entropy_reference: float,
    dim_b: int,
) -> float:
    """Lower bound on ``I(R:A)`` for a pure state on ``RAB``.

    It follows only from ``I(R:A)+I(R:B)=2S(R)`` and
    ``I(R:B)<=2 log2(dim B)``. This is a correlation bound, not by itself an
    operational recovery-fidelity theorem.
    """
    if entropy_reference < 0:
        raise ValueError("entropy_reference must be nonnegative")
    if dim_b <= 0:
        raise ValueError("dim_b must be positive")
    return float(
        max(
            0.0,
            2.0 * entropy_reference - 2.0 * np.log2(dim_b),
        )
    )


@dataclass(frozen=True)
class RemnantPoint:
    """Reference/radiation/remnant correlation diagnostics."""

    i_reference_a: float
    i_reference_b: float
    entropy_reference: float
    sum_residual: float
    remnant_cap_residual: float


def remnant_diagnostics(
    state_rab: Array,
    dims: tuple[int, int, int],
) -> RemnantPoint:
    """Evaluate pure-state localization and the finite-remnant cap."""
    _, _, dim_b = dims
    rho = density_matrix(state_rab)
    i_ra = mutual_information(rho, dims, {0}, {1})
    i_rb = mutual_information(rho, dims, {0}, {2})
    entropy_reference = von_neumann_entropy(partial_trace(rho, dims, {0}))
    sum_residual = i_ra + i_rb - 2.0 * entropy_reference
    cap = remnant_information_cap(dim_b, entropy_reference)
    return RemnantPoint(
        i_reference_a=i_ra,
        i_reference_b=i_rb,
        entropy_reference=entropy_reference,
        sum_residual=sum_residual,
        remnant_cap_residual=i_rb - cap,
    )


def random_remnant_points(
    input_dim: int,
    radiation_dim: int,
    remnant_dim: int,
    samples: int,
    rng: np.random.Generator,
) -> list[RemnantPoint]:
    """Sample Haar-random isometries ``X -> A tensor B``."""
    if min(input_dim, radiation_dim, remnant_dim, samples) <= 0:
        raise ValueError("dimensions and samples must be positive")
    if radiation_dim * remnant_dim < input_dim:
        raise ValueError("output Hilbert space is too small for an isometry")
    phi = maximally_entangled_pair(input_dim)
    points: list[RemnantPoint] = []
    for _ in range(samples):
        isometry = haar_random_isometry(
            radiation_dim * remnant_dim,
            input_dim,
            rng,
        )
        state = apply_input_isometry(phi, isometry)
        points.append(
            remnant_diagnostics(
                state,
                (input_dim, radiation_dim, remnant_dim),
            )
        )
    return points


def store_in_radiation_isometry(
    input_dim: int,
    radiation_dim: int,
    remnant_dim: int,
) -> Array:
    """Extremal isometry storing the full input in radiation and fixing B."""
    if radiation_dim < input_dim or remnant_dim <= 0:
        raise ValueError(
            "radiation_dim must fit the input and remnant_dim must be positive"
        )
    isometry = np.zeros(
        (radiation_dim * remnant_dim, input_dim),
        dtype=np.complex128,
    )
    for input_index in range(input_dim):
        isometry[input_index * remnant_dim, input_index] = 1.0
    return isometry


def store_in_remnant_isometry(
    input_dim: int,
    radiation_dim: int,
    remnant_dim: int,
) -> Array:
    """Extremal isometry storing the full input in B and fixing radiation."""
    if remnant_dim < input_dim or radiation_dim <= 0:
        raise ValueError(
            "remnant_dim must fit the input and radiation_dim must be positive"
        )
    isometry = np.zeros(
        (radiation_dim * remnant_dim, input_dim),
        dtype=np.complex128,
    )
    for input_index in range(input_dim):
        isometry[input_index, input_index] = 1.0
    return isometry
