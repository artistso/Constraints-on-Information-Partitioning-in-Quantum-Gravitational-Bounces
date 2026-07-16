import numpy as np
import pytest

from qgbounce.symmetry import (
    fixed_charge_entropy_cap,
    superselection_entropy_cap,
    superselection_radiation_information_lower_bound,
    superselection_remnant_information_cap,
)


def test_single_fixed_sector_reduces_to_dimension_bound():
    assert np.isclose(fixed_charge_entropy_cap(8), 3.0)
    assert np.isclose(
        superselection_entropy_cap([1.0], [8]),
        3.0,
    )


def test_sector_entropy_cap_includes_classical_charge_uncertainty():
    probabilities = np.array([0.25, 0.75])
    dimensions = np.array([2, 4])
    expected = (
        -(0.25 * np.log2(0.25) + 0.75 * np.log2(0.75))
        + 0.25 * 1.0
        + 0.75 * 2.0
    )
    assert np.isclose(
        superselection_entropy_cap(probabilities, dimensions),
        expected,
        atol=1e-12,
    )


def test_sector_information_and_radiation_bounds_are_complementary():
    entropy_reference = 2.0
    probabilities = [0.5, 0.5]
    dimensions = [1, 1]
    remnant_cap = superselection_remnant_information_cap(
        entropy_reference,
        probabilities,
        dimensions,
    )
    radiation_lower = superselection_radiation_information_lower_bound(
        entropy_reference,
        probabilities,
        dimensions,
    )
    assert np.isclose(remnant_cap, 2.0)
    assert np.isclose(radiation_lower, 2.0)
    assert np.isclose(remnant_cap + radiation_lower, 2.0 * entropy_reference)


def test_unconstrained_sector_distribution_recovers_total_dimension_cap():
    dimensions = np.array([1, 3, 4])
    probabilities = dimensions / dimensions.sum()
    assert np.isclose(
        superselection_entropy_cap(probabilities, dimensions),
        np.log2(dimensions.sum()),
        atol=1e-12,
    )


@pytest.mark.parametrize(
    ("probabilities", "dimensions"),
    [
        ([0.4, 0.4], [1, 1]),
        ([0.5, 0.5], [1]),
        ([-0.1, 1.1], [1, 1]),
        ([0.5, 0.5], [1, 0]),
        ([0.5, 0.5], [1, 1.5]),
    ],
)
def test_invalid_sector_data_are_rejected(probabilities, dimensions):
    with pytest.raises(ValueError):
        superselection_entropy_cap(probabilities, dimensions)
