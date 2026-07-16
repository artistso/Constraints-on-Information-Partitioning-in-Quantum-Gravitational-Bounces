"""Large-scale Han--Rovelli--Soltani geometry baselines.

The formulas use natural units ``G=c=1`` and reproduce the effective
Oppenheimer--Snyder/LQC scale factor and the static exterior function presented
outside the horizon-tunnelling region. They do not model Hawking evaporation,
transition amplitudes, quantum states, or information channels.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def _positive_finite(name: str, value: float) -> float:
    value = float(value)
    if not np.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite")
    return value


def hrs_scale_factor(proper_time: float | np.ndarray, mass: float, area_scale: float):
    """Return ``a(T)=((9 m T^2 + A m)/2)^(1/3)`` in natural units."""
    mass = _positive_finite("mass", mass)
    area_scale = _positive_finite("area_scale", area_scale)
    proper_time = np.asarray(proper_time, dtype=float)
    if not np.all(np.isfinite(proper_time)):
        raise ValueError("proper_time must be finite")
    result = ((9.0 * mass * proper_time**2 + area_scale * mass) / 2.0) ** (
        1.0 / 3.0
    )
    return float(result) if result.ndim == 0 else result


def hrs_bounce_radius(mass: float, area_scale: float) -> float:
    """Minimum stellar radius ``a(0)=(A m/2)^(1/3)``."""
    return float(hrs_scale_factor(0.0, mass, area_scale))


def hrs_exterior_function(
    radius: float | np.ndarray,
    mass: float,
    area_scale: float,
):
    """Return ``F(r)=1-2m/r+A m^2/r^4`` in natural units."""
    mass = _positive_finite("mass", mass)
    area_scale = _positive_finite("area_scale", area_scale)
    radius = np.asarray(radius, dtype=float)
    if not np.all(np.isfinite(radius)) or np.any(radius <= 0.0):
        raise ValueError("radius must be positive and finite")
    result = 1.0 - 2.0 * mass / radius + area_scale * mass**2 / radius**4
    return float(result) if result.ndim == 0 else result


def hrs_horizon_radii(
    mass: float,
    area_scale: float,
    *,
    imaginary_tolerance: float = 1e-9,
) -> tuple[float, ...]:
    """Return positive real zeros of the exterior function.

    Zeros are roots of ``r^4-2 m r^3+A m^2=0``. The large-mass regime has two
    positive roots, conventionally denoted ``r_-`` and ``r_+``.
    """
    mass = _positive_finite("mass", mass)
    area_scale = _positive_finite("area_scale", area_scale)
    coefficients = np.array(
        [1.0, -2.0 * mass, 0.0, 0.0, area_scale * mass**2],
        dtype=float,
    )
    roots = np.roots(coefficients)
    positive = sorted(
        float(root.real)
        for root in roots
        if abs(root.imag) <= imaginary_tolerance * max(1.0, abs(root.real))
        and root.real > 0.0
    )
    return tuple(positive)


@dataclass(frozen=True)
class HRSGeometryScales:
    """Characteristic natural-unit radii for one parameter point."""

    mass: float
    area_scale: float
    bounce_radius: float
    horizon_radii: tuple[float, ...]

    @property
    def inner_horizon(self) -> float | None:
        return self.horizon_radii[0] if len(self.horizon_radii) >= 2 else None

    @property
    def outer_horizon(self) -> float | None:
        return self.horizon_radii[-1] if len(self.horizon_radii) >= 2 else None


def hrs_geometry_scales(mass: float, area_scale: float) -> HRSGeometryScales:
    """Collect the bounce radius and real positive horizon radii."""
    mass = _positive_finite("mass", mass)
    area_scale = _positive_finite("area_scale", area_scale)
    return HRSGeometryScales(
        mass=mass,
        area_scale=area_scale,
        bounce_radius=hrs_bounce_radius(mass, area_scale),
        horizon_radii=hrs_horizon_radii(mass, area_scale),
    )
