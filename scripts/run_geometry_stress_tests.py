"""Generate deterministic Han--Rovelli--Soltani geometry baselines."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from qgbounce.geometry import (
    hrs_exterior_function,
    hrs_geometry_scales,
    hrs_scale_factor,
)


def main() -> None:
    output = Path("outputs/geometry_stress_tests")
    output.mkdir(parents=True, exist_ok=True)

    area_scale = 1.0
    masses = np.logspace(1.0, 6.0, 250)
    rows: list[tuple[float, ...]] = []
    for mass in masses:
        scales = hrs_geometry_scales(float(mass), area_scale)
        if scales.inner_horizon is None or scales.outer_horizon is None:
            continue
        rows.append(
            (
                float(mass),
                area_scale,
                scales.bounce_radius,
                scales.inner_horizon,
                scales.outer_horizon,
                hrs_exterior_function(scales.inner_horizon, mass, area_scale),
                hrs_exterior_function(scales.outer_horizon, mass, area_scale),
                scales.inner_horizon / scales.bounce_radius - 1.0,
                scales.outer_horizon / (2.0 * mass) - 1.0,
            )
        )

    with (output / "hrs_geometry_scales.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "mass_natural_units",
                "area_scale_natural_units_squared",
                "bounce_radius",
                "inner_horizon",
                "outer_horizon",
                "inner_F_residual",
                "outer_F_residual",
                "inner_vs_bounce_fractional_error",
                "outer_vs_2m_fractional_error",
            ]
        )
        writer.writerows(rows)

    fig, ax = plt.subplots()
    ax.loglog(
        [row[0] for row in rows],
        [row[2] for row in rows],
        label="bounce radius",
    )
    ax.loglog(
        [row[0] for row in rows],
        [row[3] for row in rows],
        label="inner horizon",
    )
    ax.loglog(
        [row[0] for row in rows],
        [row[4] for row in rows],
        label="outer horizon",
    )
    ax.set_xlabel("mass in natural units")
    ax.set_ylabel("radius in natural units")
    ax.set_title("Large-scale radii in the HRS effective geometry")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "hrs_characteristic_radii.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.loglog(
        [row[0] for row in rows],
        [abs(row[7]) for row in rows],
        label="inner horizon vs bounce radius",
    )
    ax.loglog(
        [row[0] for row in rows],
        [abs(row[8]) for row in rows],
        label="outer horizon vs 2m",
    )
    ax.set_xlabel("mass in natural units")
    ax.set_ylabel("absolute fractional asymptotic error")
    ax.set_title("Approach to the large-mass horizon approximations")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "hrs_asymptotic_errors.png", dpi=180)
    plt.close(fig)

    mass = 100.0
    bounce_radius = hrs_geometry_scales(mass, area_scale).bounce_radius
    times = np.linspace(-20.0, 20.0, 401)
    radii = hrs_scale_factor(times, mass, area_scale)
    with (output / "hrs_scale_factor.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["proper_time_natural_units", "stellar_radius"])
        writer.writerows(zip(times, radii, strict=True))

    fig, ax = plt.subplots()
    ax.plot(times, radii)
    ax.axhline(bounce_radius, linestyle="--", label="minimum radius")
    ax.set_xlabel("stellar proper time in natural units")
    ax.set_ylabel("stellar boundary radius")
    ax.set_title("Effective Oppenheimer--Snyder/LQC bounce baseline")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "hrs_scale_factor.png", dpi=180)
    plt.close(fig)

    summary = {
        "units": "G=c=1",
        "area_scale": area_scale,
        "mass_range": [float(masses.min()), float(masses.max())],
        "maximum_horizon_root_residual": float(
            max(max(abs(row[5]), abs(row[6])) for row in rows)
        ),
        "scope": (
            "effective geometric baseline outside the tunnelling region; "
            "no Hawking evaporation, transition amplitude, quantum state, or channel"
        ),
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
