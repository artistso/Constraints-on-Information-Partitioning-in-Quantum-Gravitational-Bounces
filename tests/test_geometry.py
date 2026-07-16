import numpy as np

from qgbounce.geometry import (
    hrs_bounce_radius,
    hrs_exterior_function,
    hrs_geometry_scales,
    hrs_scale_factor,
)


def test_effective_scale_factor_is_symmetric_and_bounces_at_zero():
    mass = 100.0
    area_scale = 1.0
    times = np.linspace(-10.0, 10.0, 201)
    scale = hrs_scale_factor(times, mass, area_scale)
    assert np.allclose(scale, scale[::-1])
    assert np.isclose(scale.min(), hrs_bounce_radius(mass, area_scale))
    assert np.argmin(scale) == len(times) // 2


def test_large_mass_geometry_has_inner_and_outer_horizons():
    scales = hrs_geometry_scales(mass=100.0, area_scale=1.0)
    assert len(scales.horizon_radii) == 2
    assert scales.inner_horizon is not None
    assert scales.outer_horizon is not None
    assert abs(hrs_exterior_function(scales.inner_horizon, 100.0, 1.0)) < 1e-9
    assert abs(hrs_exterior_function(scales.outer_horizon, 100.0, 1.0)) < 1e-9


def test_large_mass_horizon_asymptotics():
    mass = 1000.0
    area_scale = 1.0
    scales = hrs_geometry_scales(mass, area_scale)
    assert np.isclose(scales.outer_horizon, 2.0 * mass, rtol=1e-6)
    assert np.isclose(
        scales.inner_horizon,
        scales.bounce_radius,
        rtol=2e-3,
    )
