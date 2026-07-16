"""Finite-dimensional energy-constrained entropy and correlation bounds.

The functions in this module are deliberately finite dimensional. They provide
an exact Gibbs-variational benchmark for a declared Hamiltonian spectrum and
mean-energy cap. They do not infer a remnant Hamiltonian from geometry.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

Array = np.ndarray


def _validate_energies(energies: Array) -> Array:
    values = np.asarray(energies, dtype=float).reshape(-1)
    if values.size == 0:
        raise ValueError("energies must contain at least one level")
    if not np.all(np.isfinite(values)):
        raise ValueError("energies must be finite")
    return np.sort(values)


def _gibbs_probabilities(energies: Array, beta: float) -> Array:
    shifted = energies - energies.min()
    exponents = -beta * shifted
    exponents -= exponents.max()
    weights = np.exp(exponents)
    return weights / weights.sum()


def shannon_entropy_bits(probabilities: Array, *, atol: float = 1e-15) -> float:
    probabilities = np.asarray(probabilities, dtype=float).reshape(-1)
    if np.any(probabilities < -atol):
        raise ValueError("probabilities must be nonnegative")
    total = probabilities.sum()
    if not np.isfinite(total) or total <= 0:
        raise ValueError("probabilities must have positive finite sum")
    probabilities = np.clip(probabilities / total, 0.0, None)
    nonzero = probabilities[probabilities > atol]
    return float(-np.sum(nonzero * np.log2(nonzero)))


@dataclass(frozen=True)
class GibbsEntropyResult:
    """Maximum-entropy state under a finite-dimensional energy cap."""

    beta: float
    probabilities: Array
    mean_energy: float
    entropy_bits: float
    constraint_active: bool


def maximum_entropy_under_energy(
    energies: Array,
    energy_cap: float,
    *,
    atol: float = 1e-12,
    max_iterations: int = 256,
) -> GibbsEntropyResult:
    """Maximize entropy subject to ``Tr(H rho) <= energy_cap``.

    For a finite Hamiltonian spectrum, the optimizer is Gibbs whenever the
    energy constraint is active. If the uniform state already satisfies the
    cap, the maximum is ``log2(d)`` and ``beta=0``.
    """
    values = _validate_energies(energies)
    if not np.isfinite(energy_cap):
        raise ValueError("energy_cap must be finite")

    minimum = float(values.min())
    if energy_cap < minimum - atol:
        raise ValueError("energy_cap lies below the ground-state energy")

    dimension = values.size
    uniform = np.full(dimension, 1.0 / dimension)
    uniform_energy = float(uniform @ values)
    if energy_cap >= uniform_energy - atol:
        return GibbsEntropyResult(
            beta=0.0,
            probabilities=uniform,
            mean_energy=uniform_energy,
            entropy_bits=float(np.log2(dimension)),
            constraint_active=False,
        )

    ground_mask = np.isclose(values, minimum, atol=atol, rtol=0.0)
    if energy_cap <= minimum + atol:
        probabilities = ground_mask.astype(float)
        probabilities /= probabilities.sum()
        return GibbsEntropyResult(
            beta=float("inf"),
            probabilities=probabilities,
            mean_energy=float(probabilities @ values),
            entropy_bits=shannon_entropy_bits(probabilities),
            constraint_active=True,
        )

    def mean_energy(beta: float) -> float:
        probabilities = _gibbs_probabilities(values, beta)
        return float(probabilities @ values)

    beta_low = 0.0
    beta_high = 1.0
    while mean_energy(beta_high) > energy_cap:
        beta_high *= 2.0
        if beta_high > 1e16:
            raise RuntimeError("failed to bracket the Gibbs inverse temperature")

    for _ in range(max_iterations):
        beta_mid = 0.5 * (beta_low + beta_high)
        observed = mean_energy(beta_mid)
        if abs(observed - energy_cap) <= atol:
            beta_low = beta_high = beta_mid
            break
        if observed > energy_cap:
            beta_low = beta_mid
        else:
            beta_high = beta_mid

    beta = 0.5 * (beta_low + beta_high)
    probabilities = _gibbs_probabilities(values, beta)
    observed_energy = float(probabilities @ values)
    return GibbsEntropyResult(
        beta=beta,
        probabilities=probabilities,
        mean_energy=observed_energy,
        entropy_bits=shannon_entropy_bits(probabilities),
        constraint_active=True,
    )


def energy_constrained_remnant_information_cap(
    entropy_reference: float,
    energies: Array,
    energy_cap: float,
) -> float:
    """Upper-bound ``I(R:B)`` from a declared Hamiltonian and mean energy."""
    if entropy_reference < 0 or not np.isfinite(entropy_reference):
        raise ValueError("entropy_reference must be finite and nonnegative")
    maximum = maximum_entropy_under_energy(energies, energy_cap)
    return float(2.0 * min(entropy_reference, maximum.entropy_bits))


def energy_constrained_radiation_information_lower_bound(
    entropy_reference: float,
    energies: Array,
    energy_cap: float,
) -> float:
    """Lower-bound ``I(R:A)`` for pure ``RAB`` under an energy cap on B."""
    cap = energy_constrained_remnant_information_cap(
        entropy_reference,
        energies,
        energy_cap,
    )
    return float(max(0.0, 2.0 * entropy_reference - cap))
