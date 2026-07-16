"""Baseline black-hole scale calculations with explicit SI units.

These are semiclassical Schwarzschild baselines. They are not a bounce emission
model and must not be used as detector-level durations or event-rate forecasts.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 299_792_458.0  # m s^-1
HBAR = 1.054_571_817e-34  # J s
K_B = 1.380_649e-23  # J K^-1
SECONDS_PER_JULIAN_YEAR = 365.25 * 24.0 * 3600.0


@dataclass(frozen=True)
class SchwarzschildScales:
    mass_kg: float
    radius_m: float
    light_crossing_time_s: float
    hawking_temperature_k: float
    leading_evaporation_time_s: float

    @property
    def leading_evaporation_time_years(self) -> float:
        return self.leading_evaporation_time_s / SECONDS_PER_JULIAN_YEAR


def schwarzschild_radius(mass_kg: float) -> float:
    """Schwarzschild radius r_s = 2GM/c^2."""
    if mass_kg <= 0 or not math.isfinite(mass_kg):
        raise ValueError("mass_kg must be positive and finite")
    return 2.0 * G * mass_kg / C**2


def light_crossing_time(mass_kg: float) -> float:
    """Horizon light-crossing baseline r_s/c = 2GM/c^3."""
    return schwarzschild_radius(mass_kg) / C


def hawking_temperature(mass_kg: float) -> float:
    """Schwarzschild Hawking temperature hbar*c^3/(8*pi*G*M*k_B)."""
    if mass_kg <= 0 or not math.isfinite(mass_kg):
        raise ValueError("mass_kg must be positive and finite")
    return HBAR * C**3 / (8.0 * math.pi * G * mass_kg * K_B)


def leading_evaporation_time(mass_kg: float) -> float:
    """Leading textbook lifetime 5120*pi*G^2*M^3/(hbar*c^4).

    This omits spin, charge, greybody factors, changing particle content, and
    any quantum-gravity modification.
    """
    if mass_kg <= 0 or not math.isfinite(mass_kg):
        raise ValueError("mass_kg must be positive and finite")
    return 5120.0 * math.pi * G**2 * mass_kg**3 / (HBAR * C**4)


def baseline_scales(mass_kg: float) -> SchwarzschildScales:
    """Return all baseline scales for a positive mass."""
    return SchwarzschildScales(
        mass_kg=mass_kg,
        radius_m=schwarzschild_radius(mass_kg),
        light_crossing_time_s=light_crossing_time(mass_kg),
        hawking_temperature_k=hawking_temperature(mass_kg),
        leading_evaporation_time_s=leading_evaporation_time(mass_kg),
    )
