import numpy as np

from qgbounce.quantum import apply_input_isometry, maximally_entangled_pair
from qgbounce.remnants import (
    radiation_information_lower_bound,
    random_remnant_points,
    remnant_diagnostics,
    store_in_radiation_isometry,
    store_in_remnant_isometry,
)


def test_dimension_bound_for_random_isometries():
    rng = np.random.default_rng(20260715)
    points = random_remnant_points(4, 4, 2, 100, rng)
    assert max(abs(point.sum_residual) for point in points) < 1e-10
    assert max(point.remnant_cap_residual for point in points) < 1e-10
    assert all(
        point.i_reference_a
        >= radiation_information_lower_bound(
            point.entropy_reference,
            2,
        )
        - 1e-10
        for point in points
    )


def test_extremal_storage_channels():
    phi = maximally_entangled_pair(2)

    state_a = apply_input_isometry(
        phi,
        store_in_radiation_isometry(2, 2, 2),
    )
    point_a = remnant_diagnostics(state_a, (2, 2, 2))
    assert np.isclose(point_a.i_reference_a, 2.0, atol=1e-10)
    assert np.isclose(point_a.i_reference_b, 0.0, atol=1e-10)

    state_b = apply_input_isometry(
        phi,
        store_in_remnant_isometry(2, 2, 2),
    )
    point_b = remnant_diagnostics(state_b, (2, 2, 2))
    assert np.isclose(point_b.i_reference_a, 0.0, atol=1e-10)
    assert np.isclose(point_b.i_reference_b, 2.0, atol=1e-10)


def test_one_dimensional_remnant_forces_full_reference_correlation_into_radiation():
    assert np.isclose(
        radiation_information_lower_bound(2.0, 1),
        4.0,
    )
