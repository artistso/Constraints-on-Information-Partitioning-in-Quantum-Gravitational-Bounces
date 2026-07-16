import numpy as np

from qgbounce.gravity import baseline_scales, light_crossing_time


def test_light_crossing_regression_at_1e12_kg():
    # Regression test for the discarded 10^-5 s normalization.
    actual = light_crossing_time(1.0e12)
    assert np.isclose(actual, 4.954200861930066e-24, rtol=1e-12)
    assert actual < 1.0e-20


def test_expected_mass_scalings():
    low = baseline_scales(1.0e10)
    high = baseline_scales(1.0e11)
    assert np.isclose(high.radius_m / low.radius_m, 10.0)
    assert np.isclose(high.light_crossing_time_s / low.light_crossing_time_s, 10.0)
    assert np.isclose(high.hawking_temperature_k / low.hawking_temperature_k, 0.1)
    assert np.isclose(
        high.leading_evaporation_time_s / low.leading_evaporation_time_s,
        1000.0,
    )
