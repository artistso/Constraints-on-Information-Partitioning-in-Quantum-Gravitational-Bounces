import numpy as np

from qgbounce.energy import (
    energy_constrained_radiation_information_lower_bound,
    maximum_entropy_under_energy,
)


def binary_entropy(probability: float) -> float:
    if probability in {0.0, 1.0}:
        return 0.0
    return float(
        -probability * np.log2(probability)
        - (1.0 - probability) * np.log2(1.0 - probability)
    )


def test_two_level_gibbs_entropy_matches_binary_entropy():
    energies = np.array([0.0, 1.0])
    for energy_cap in np.linspace(0.0, 0.5, 11):
        result = maximum_entropy_under_energy(energies, float(energy_cap))
        assert np.isclose(result.mean_energy, energy_cap, atol=1e-10)
        assert np.isclose(
            result.entropy_bits,
            binary_entropy(float(energy_cap)),
            atol=1e-10,
        )


def test_uniform_state_when_energy_constraint_is_inactive():
    result = maximum_entropy_under_energy([0.0, 1.0], 0.75)
    assert not result.constraint_active
    assert np.isclose(result.entropy_bits, 1.0, atol=1e-12)
    assert np.allclose(result.probabilities, [0.5, 0.5])


def test_degenerate_ground_state_entropy():
    result = maximum_entropy_under_energy([0.0, 0.0, 1.0], 0.0)
    assert result.constraint_active
    assert np.isinf(result.beta)
    assert np.isclose(result.entropy_bits, 1.0, atol=1e-12)
    assert np.allclose(result.probabilities, [0.5, 0.5, 0.0])


def test_energy_bound_forces_reference_correlation_into_radiation():
    bound = energy_constrained_radiation_information_lower_bound(
        entropy_reference=1.0,
        energies=[0.0, 1.0],
        energy_cap=0.0,
    )
    assert np.isclose(bound, 2.0, atol=1e-12)
