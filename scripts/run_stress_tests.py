"""Run the first reproducible mathematical and physical stress-test suite."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from qgbounce.gravity import baseline_scales
from qgbounce.quantum import (
    apply_input_isometry,
    haar_random_isometry,
    localization_diagnostics,
    localization_isometry,
    maximally_entangled_pair,
)


def save_localization_path(output_dir: Path) -> float:
    phi = maximally_entangled_pair(2)
    theta = np.linspace(0.0, np.pi / 2.0, 301)
    i_ra = []
    i_rb = []
    residuals = []
    for value in theta:
        state = apply_input_isometry(phi, localization_isometry(value))
        diagnostics = localization_diagnostics(state)
        i_ra.append(diagnostics.i_reference_a)
        i_rb.append(diagnostics.i_reference_b)
        residuals.append(diagnostics.identity_residual)

    fig, ax = plt.subplots()
    ax.plot(theta, i_ra, label=r"$I(R:A)$")
    ax.plot(theta, i_rb, label=r"$I(R:B)$")
    ax.plot(theta, np.asarray(i_ra) + np.asarray(i_rb), label="sum")
    ax.set_xlabel(r"$\theta$ (radians)")
    ax.set_ylabel("mutual information (bits)")
    ax.set_title("Unitary localization can move information between outputs")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "localization_path.png", dpi=180)
    plt.close(fig)
    return float(np.max(np.abs(residuals)))


def save_random_isometry_cloud(output_dir: Path, samples: int, seed: int) -> float:
    phi = maximally_entangled_pair(2)
    rng = np.random.default_rng(seed)
    points = []
    residuals = []
    for _ in range(samples):
        isometry = haar_random_isometry(4, 2, rng)
        state = apply_input_isometry(phi, isometry)
        diagnostics = localization_diagnostics(state)
        points.append((diagnostics.i_reference_a, diagnostics.i_reference_b))
        residuals.append(diagnostics.identity_residual)

    points = np.asarray(points)
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], s=10, alpha=0.5)
    x = np.linspace(0.0, 2.0, 200)
    ax.plot(x, 2.0 - x, label=r"$I(R:A)+I(R:B)=2S(R)$")
    ax.set_xlim(0.0, 2.0)
    ax.set_ylim(0.0, 2.0)
    ax.set_xlabel(r"$I(R:A)$ (bits)")
    ax.set_ylabel(r"$I(R:B)$ (bits)")
    ax.set_title("Haar-random qubit isometries: information-localization line")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "random_isometry_localization.png", dpi=180)
    plt.close(fig)

    with (output_dir / "random_isometry_points.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["i_reference_a_bits", "i_reference_b_bits"])
        writer.writerows(points.tolist())

    return float(np.max(np.abs(residuals)))


def save_gravity_scales(output_dir: Path) -> None:
    masses = np.logspace(8, 15, 400)
    scales = [baseline_scales(float(mass)) for mass in masses]
    crossing = np.asarray([item.light_crossing_time_s for item in scales])
    temperature = np.asarray([item.hawking_temperature_k for item in scales])
    lifetime_years = np.asarray([item.leading_evaporation_time_years for item in scales])

    fig, ax = plt.subplots()
    ax.loglog(masses, crossing)
    ax.scatter([1.0e12], [baseline_scales(1.0e12).light_crossing_time_s])
    ax.set_xlabel("mass (kg)")
    ax.set_ylabel("2GM/c^3 (s)")
    ax.set_title("Schwarzschild light-crossing baseline")
    fig.tight_layout()
    fig.savefig(output_dir / "light_crossing_time.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.loglog(masses, temperature)
    ax.set_xlabel("mass (kg)")
    ax.set_ylabel("Hawking temperature (K)")
    ax.set_title("Semiclassical Schwarzschild Hawking temperature")
    fig.tight_layout()
    fig.savefig(output_dir / "hawking_temperature.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.loglog(masses, lifetime_years)
    ax.set_xlabel("mass (kg)")
    ax.set_ylabel("leading evaporation time (Julian years)")
    ax.set_title("Leading Schwarzschild evaporation-time baseline")
    fig.tight_layout()
    fig.savefig(output_dir / "evaporation_time.png", dpi=180)
    plt.close(fig)

    with (output_dir / "gravity_scales.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "mass_kg",
                "schwarzschild_radius_m",
                "light_crossing_time_s",
                "hawking_temperature_k",
                "leading_evaporation_time_years",
            ]
        )
        for item in scales:
            writer.writerow(
                [
                    item.mass_kg,
                    item.radius_m,
                    item.light_crossing_time_s,
                    item.hawking_temperature_k,
                    item.leading_evaporation_time_years,
                ]
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="outputs/stress_tests_v0_1")
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260715)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    path_residual = save_localization_path(output_dir)
    random_residual = save_random_isometry_cloud(output_dir, args.samples, args.seed)
    save_gravity_scales(output_dir)

    mass_point = baseline_scales(1.0e12)
    summary = output_dir / "SUMMARY.md"
    summary.write_text(
        "\n".join(
            [
                "# Stress-test summary v0.1",
                "",
                f"- localization-path maximum identity residual: `{path_residual:.3e}` bits",
                f"- random-isometry maximum identity residual: `{random_residual:.3e}` bits",
                f"- `2GM/c^3` at `10^12 kg`: `{mass_point.light_crossing_time_s:.16e} s`",
                f"- Schwarzschild radius at `10^12 kg`: `{mass_point.radius_m:.16e} m`",
                f"- Hawking temperature at `10^12 kg`: `{mass_point.hawking_temperature_k:.16e} K`",
                f"- leading evaporation time at `10^12 kg`: `{mass_point.leading_evaporation_time_years:.16e} years`",
                "",
                "The gravity values are semiclassical baselines, not a bounce signal model.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(summary.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
