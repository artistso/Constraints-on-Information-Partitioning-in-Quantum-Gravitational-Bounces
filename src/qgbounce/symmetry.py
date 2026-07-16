"""Finite-dimensional charge-sector and superselection correlation bounds.

The module assumes that the retained system decomposes as a direct sum of
orthogonal charge sectors and that the physical state is block diagonal across
those sectors. It does not infer the sectors, their dimensions, or their
probabilities from a gravitational geometry.
"""

from __future__ import annotations

import numpy as np

from .energy import shannon_entropy_bits

Array = np.ndarray


def _validate_sector_data(
    probabilities: Array,
    sector_dimensions: Array,
    *,
    atol: float = 1e-12,
) -> tuple[Array, Array]:
    probabilities = np.asarray(probabilities, dtype=float).reshape(-1)
    dimensions_raw = np.asarray(sector_dimensions).reshape(-1)

    if probabilities.size == 0:
        raise ValueError("at least one charge sector is required")
    if probabilities.size != dimensions_raw.size:
        raise ValueError("probabilities and sector_dimensions must have equal length")
    if not np.all(np.isfinite(probabilities)):
        raise ValueError("probabilities must be finite")
    if np.any(probabilities < -atol):
        raise ValueError("probabilities must be nonnegative")
    if not np.isclose(probabilities.sum(), 1.0, atol=atol):
        raise ValueError("probabilities must sum to one")

    if not np.all(np.isfinite(dimensions_raw.astype(float))):
        raise ValueError("sector dimensions must be finite")
    dimensions = dimensions_raw.astype(int)
    if np.any(dimensions <= 0) or not np.allclose(
        dimensions_raw.astype(float),
        dimensions.astype(float),
        atol=0.0,
        rtol=0.0,
    ):
        raise ValueError("sector dimensions must be positive integers")

    probabilities = np.clip(probabilities, 0.0, None)
    probabilities /= probabilities.sum()
    return probabilities, dimensions


def superselection_entropy_cap(
    probabilities: Array,
    sector_dimensions: Array,
) -> float:
    """Upper-bound retained entropy for a block-diagonal sector state.

    For ``rho_B = direct_sum_q p_q rho_q`` with ``dim(H_q)=d_q``,

    ``S(B) = H(p) + sum_q p_q S(rho_q)``

    and therefore

    ``S(B) <= H(p) + sum_q p_q log2(d_q)``.
    """
    probabilities, dimensions = _validate_sector_data(
        probabilities,
        sector_dimensions,
    )
    classical = shannon_entropy_bits(probabilities)
    within_sector = float(probabilities @ np.log2(dimensions))
    return float(classical + within_sector)


def fixed_charge_entropy_cap(sector_dimension: int) -> float:
    """Entropy cap when one charge sector is known exactly."""
    if isinstance(sector_dimension, bool) or int(sector_dimension) != sector_dimension:
        raise ValueError("sector_dimension must be a positive integer")
    sector_dimension = int(sector_dimension)
    if sector_dimension <= 0:
        raise ValueError("sector_dimension must be a positive integer")
    return float(np.log2(sector_dimension))


def superselection_remnant_information_cap(
    entropy_reference: float,
    probabilities: Array,
    sector_dimensions: Array,
) -> float:
    """Upper-bound ``I(R:B)`` under declared charge-sector data."""
    if not np.isfinite(entropy_reference) or entropy_reference < 0:
        raise ValueError("entropy_reference must be finite and nonnegative")
    entropy_cap = superselection_entropy_cap(
        probabilities,
        sector_dimensions,
    )
    return float(2.0 * min(entropy_reference, entropy_cap))


def superselection_radiation_information_lower_bound(
    entropy_reference: float,
    probabilities: Array,
    sector_dimensions: Array,
) -> float:
    """Lower-bound ``I(R:A)`` for pure ``RAB`` under sector constraints on B."""
    remnant_cap = superselection_remnant_information_cap(
        entropy_reference,
        probabilities,
        sector_dimensions,
    )
    return float(max(0.0, 2.0 * entropy_reference - remnant_cap))
