"""Generate deterministic diamond-norm and KSW diagnostic products."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from qgbounce.channels import dephasing_channel, depolarizing_channel, identity_channel
from qgbounce.diamond import (
    certify_ksw_diamond_tradeoff,
    channel_diamond_distance,
    closest_constant_channel_diamond_distance,
    optimal_recovery_diamond_error,
)


def _certificate_summary(certificate) -> dict[str, float | str | int | None]:
    return {
        "solver_status": certificate.solver_status,
        "solver_name": certificate.solver_name,
        "solve_time_s": certificate.solve_time_s,
        "iterations": certificate.iterations,
        "minimum_plus_eigenvalue": certificate.minimum_plus_eigenvalue,
        "minimum_minus_eigenvalue": certificate.minimum_minus_eigenvalue,
        "partial_trace_upper_residual": certificate.partial_trace_upper_residual,
    }


def main() -> None:
    output = Path("outputs/diamond_stress_tests")
    output.mkdir(parents=True, exist_ok=True)

    probabilities = np.linspace(0.0, 0.5, 11)
    rows: list[dict[str, float | str]] = []
    for probability in probabilities:
        dephasing = dephasing_channel(float(probability))
        identity_distance = channel_diamond_distance(
            dephasing,
            identity_channel(2),
        )
        recovery = optimal_recovery_diamond_error(dephasing)
        ksw = certify_ksw_diamond_tradeoff(dephasing)
        rows.append(
            {
                "probability": float(probability),
                "identity_distance": identity_distance.diamond_norm,
                "analytic_identity_distance": 2.0 * float(probability),
                "optimal_recovery_error": recovery.diamond_error,
                "analytic_recovery_error": 2.0
                * min(float(probability), 1.0 - float(probability)),
                "environment_constant_distance": (
                    ksw.environment.diamond_distance
                ),
                "ksw_lower_margin": ksw.lower_margin,
                "ksw_upper_margin": ksw.upper_margin,
                "recovery_status": recovery.solver_status,
                "environment_status": ksw.environment.solver_status,
            }
        )

    csv_path = output / "dephasing_ksw_sweep.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    fig, ax = plt.subplots()
    ax.plot(
        probabilities,
        [float(row["identity_distance"]) for row in rows],
        label="distance from identity",
    )
    ax.plot(
        probabilities,
        [float(row["optimal_recovery_error"]) for row in rows],
        label="optimal recovery diamond error",
    )
    ax.plot(
        probabilities,
        [float(row["environment_constant_distance"]) for row in rows],
        label="complement distance to constants",
    )
    ax.set_xlabel("dephasing probability")
    ax.set_ylabel("diamond norm")
    ax.set_title("Channel-wide recovery and environmental leakage")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "dephasing_ksw_sweep.png", dpi=180)
    plt.close(fig)

    depolarizing = channel_diamond_distance(
        depolarizing_channel(1.0),
        identity_channel(2),
    )
    constant_identity = closest_constant_channel_diamond_distance(
        identity_channel(2)
    )
    maximum_analytic_error = max(
        abs(float(row["identity_distance"]) - float(row["analytic_identity_distance"]))
        for row in rows
    )
    maximum_recovery_analytic_error = max(
        abs(float(row["optimal_recovery_error"]) - float(row["analytic_recovery_error"]))
        for row in rows
    )
    summary = {
        "dephasing_points": len(rows),
        "maximum_dephasing_identity_analytic_error": maximum_analytic_error,
        "maximum_dephasing_recovery_analytic_error": (
            maximum_recovery_analytic_error
        ),
        "minimum_ksw_lower_margin": min(
            float(row["ksw_lower_margin"]) for row in rows
        ),
        "minimum_ksw_upper_margin": min(
            float(row["ksw_upper_margin"]) for row in rows
        ),
        "identity_to_fully_depolarizing_qubit_distance": (
            depolarizing.diamond_norm
        ),
        "identity_to_closest_constant_qubit_distance": (
            constant_identity.diamond_distance
        ),
        "depolarizing_certificate": _certificate_summary(depolarizing),
        "constant_identity_certificate": {
            **_certificate_summary(constant_identity),
            "constant_state_trace_residual": (
                constant_identity.constant_state_trace_residual
            ),
            "minimum_constant_state_eigenvalue": (
                constant_identity.minimum_constant_state_eigenvalue
            ),
        },
        "scope": (
            "finite-dimensional unnormalized Choi matrices in input-output "
            "ordering; no energy-constrained or infinite-dimensional claim"
        ),
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
