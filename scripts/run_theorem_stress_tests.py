"""Generate certified recovery, duality, and energy-bound products."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from qgbounce.channels import (
    amplitude_damping_channel,
    dephasing_channel,
    erasure_channel,
)
from qgbounce.energy import (
    energy_constrained_radiation_information_lower_bound,
    maximum_entropy_under_energy,
)
from qgbounce.optimization import certify_information_disturbance


def write_csv(path: Path, header: list[str], rows: list[tuple[object, ...]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def main() -> None:
    output = Path("outputs/theorem_stress_tests")
    output.mkdir(parents=True, exist_ok=True)

    parameters = np.linspace(0.0, 1.0, 5)
    rows: list[tuple[object, ...]] = []
    for family, constructor in (
        ("erasure", erasure_channel),
        ("dephasing", dephasing_channel),
        ("amplitude_damping", amplitude_damping_channel),
    ):
        for parameter in parameters:
            certificate = certify_information_disturbance(
                constructor(float(parameter))
            )
            if family == "erasure":
                analytic_or_baseline = 1.0 - 3.0 * parameter / 4.0
            elif family == "dephasing":
                analytic_or_baseline = max(parameter, 1.0 - parameter)
            else:
                analytic_or_baseline = (
                    1.0 + np.sqrt(1.0 - parameter)
                ) ** 2 / 4.0
            rows.append(
                (
                    family,
                    float(parameter),
                    certificate.recovery.entanglement_fidelity,
                    certificate.environment.squared_fidelity,
                    certificate.formulation_gap,
                    float(analytic_or_baseline),
                    certificate.recovery.trace_preservation_residual,
                    certificate.recovery.minimum_choi_eigenvalue,
                    certificate.environment.trace_residual,
                    certificate.environment.minimum_environment_eigenvalue,
                    certificate.recovery.solver_status,
                    certificate.environment.solver_status,
                )
            )

    write_csv(
        output / "certified_recovery.csv",
        [
            "channel_family",
            "noise_parameter",
            "optimal_entanglement_fidelity",
            "environment_dual_squared_fidelity",
            "formulation_gap",
            "analytic_optimum_or_identity_baseline",
            "recovery_trace_preservation_residual",
            "recovery_minimum_choi_eigenvalue",
            "environment_trace_residual",
            "environment_minimum_eigenvalue",
            "recovery_solver_status",
            "environment_solver_status",
        ],
        rows,
    )

    fig, ax = plt.subplots()
    for family in ("erasure", "dephasing", "amplitude_damping"):
        family_rows = [row for row in rows if row[0] == family]
        ax.semilogy(
            [row[1] for row in family_rows],
            [max(float(row[4]), 1e-16) for row in family_rows],
            marker="o",
            label=family.replace("_", " "),
        )
    ax.set_xlabel("noise parameter")
    ax.set_ylabel("recovery/environment formulation gap")
    ax.set_title("Independent SDP formulations agree within solver tolerance")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "information_disturbance_gap.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots()
    amplitude_rows = [row for row in rows if row[0] == "amplitude_damping"]
    ax.plot(
        [row[1] for row in amplitude_rows],
        [row[2] for row in amplitude_rows],
        marker="o",
        label="certified optimum",
    )
    ax.plot(
        [row[1] for row in amplitude_rows],
        [row[5] for row in amplitude_rows],
        marker="o",
        label="identity-decoder baseline",
    )
    ax.set_xlabel("amplitude-damping strength")
    ax.set_ylabel("entanglement fidelity")
    ax.set_title("Certified recovery versus an explicit baseline decoder")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "amplitude_damping_optimal_recovery.png", dpi=180)
    plt.close(fig)

    energies = np.array([0.0, 1.0, 2.0, 3.0])
    energy_caps = np.linspace(0.0, float(np.mean(energies)), 101)
    energy_rows: list[tuple[float, ...]] = []
    for energy_cap in energy_caps:
        gibbs = maximum_entropy_under_energy(energies, float(energy_cap))
        lower = energy_constrained_radiation_information_lower_bound(
            entropy_reference=2.0,
            energies=energies,
            energy_cap=float(energy_cap),
        )
        energy_rows.append(
            (
                float(energy_cap),
                gibbs.beta,
                gibbs.mean_energy,
                gibbs.entropy_bits,
                lower,
            )
        )
    write_csv(
        output / "energy_constrained_bound.csv",
        [
            "energy_cap",
            "gibbs_beta",
            "gibbs_mean_energy",
            "maximum_entropy_bits",
            "radiation_mutual_information_lower_bound_bits",
        ],
        energy_rows,
    )

    fig, ax = plt.subplots()
    ax.plot(
        energy_caps,
        [row[3] for row in energy_rows],
        label="maximum remnant entropy",
    )
    ax.plot(
        energy_caps,
        [row[4] for row in energy_rows],
        label="radiation mutual-information lower bound",
    )
    ax.set_xlabel("mean-energy cap in declared level units")
    ax.set_ylabel("bits")
    ax.set_title("Finite Hamiltonian converts an energy cap into an entropy bound")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "energy_constrained_bound.png", dpi=180)
    plt.close(fig)

    summary = {
        "solver": "CLARABEL",
        "cvxpy_problem": "maximally-mixed-input entanglement recovery",
        "maximum_formulation_gap": float(max(float(row[4]) for row in rows)),
        "maximum_trace_preservation_residual": float(
            max(float(row[6]) for row in rows)
        ),
        "minimum_recovery_choi_eigenvalue": float(
            min(float(row[7]) for row in rows)
        ),
        "scope": (
            "state-specific average entanglement fidelity; channel-wide "
            "worst-case or energy-constrained diamond-norm certification remains separate"
        ),
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
