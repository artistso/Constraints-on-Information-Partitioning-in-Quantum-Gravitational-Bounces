"""Generate deterministic open-channel and finite-remnant stress-test products."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from qgbounce.channels import (
    amplitude_damping_channel,
    channel_information,
    coherent_information,
    compose_channels,
    dephasing_channel,
    dephasing_pauli_recovery,
    erasure_channel,
    erasure_recovery,
    holevo_information,
    identity_channel,
)
from qgbounce.recovery import entanglement_fidelity, recovery_diagnostics
from qgbounce.remnants import (
    radiation_information_lower_bound,
    random_remnant_points,
)


def _write_csv(
    path: Path,
    header: list[str],
    rows: list[tuple[float, ...]],
) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/channel_stress_tests"),
    )
    parser.add_argument("--samples", type=int, default=500)
    args = parser.parse_args()
    if args.samples <= 0:
        raise ValueError("--samples must be positive")
    args.output.mkdir(parents=True, exist_ok=True)

    probabilities = np.linspace(0.0, 1.0, 201)

    erasure_rows: list[tuple[float, ...]] = []
    for probability in probabilities:
        channel = erasure_channel(float(probability))
        diagnostics = recovery_diagnostics(
            channel,
            erasure_recovery(),
        )
        erasure_rows.append(
            (
                float(probability),
                coherent_information(channel),
                diagnostics.entanglement_fidelity,
                diagnostics.average_state_fidelity,
                diagnostics.choi_trace_distance,
                diagnostics.choi_purified_distance,
            )
        )
    _write_csv(
        args.output / "erasure_recovery.csv",
        [
            "erasure_probability",
            "coherent_information_bits",
            "entanglement_fidelity",
            "average_state_fidelity",
            "choi_trace_distance",
            "choi_purified_distance",
        ],
        erasure_rows,
    )

    fig, ax = plt.subplots()
    ax.plot(
        probabilities,
        [row[2] for row in erasure_rows],
        label="entanglement fidelity",
    )
    ax.plot(
        probabilities,
        [row[3] for row in erasure_rows],
        label="average state fidelity",
    )
    ax.plot(
        probabilities,
        [row[1] for row in erasure_rows],
        label="coherent information (bits)",
    )
    ax.axvline(
        0.5,
        linestyle="--",
        label="qubit erasure capacity threshold",
    )
    ax.set_xlabel("erasure probability")
    ax.set_ylabel("diagnostic value")
    ax.set_title(
        "Erasure: correlations, capacity witness, and recovery are distinct"
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(args.output / "erasure_recovery.png", dpi=180)
    plt.close(fig)

    zero = np.array(
        [[1.0, 0.0], [0.0, 0.0]],
        dtype=np.complex128,
    )
    one = np.array(
        [[0.0, 0.0], [0.0, 1.0]],
        dtype=np.complex128,
    )
    dephasing_rows: list[tuple[float, ...]] = []
    for probability in probabilities:
        channel = dephasing_channel(float(probability))
        recovery = dephasing_pauli_recovery(float(probability))
        effective = compose_channels(recovery, channel)
        dephasing_rows.append(
            (
                float(probability),
                coherent_information(channel),
                holevo_information(
                    [0.5, 0.5],
                    [zero, one],
                    channel,
                ),
                entanglement_fidelity(effective),
            )
        )
    _write_csv(
        args.output / "dephasing_classical_quantum.csv",
        [
            "phase_flip_probability",
            "coherent_information_bits",
            "z_basis_holevo_bits",
            "best_fixed_pauli_entanglement_fidelity",
        ],
        dephasing_rows,
    )

    fig, ax = plt.subplots()
    ax.plot(
        probabilities,
        [row[1] for row in dephasing_rows],
        label="coherent information",
    )
    ax.plot(
        probabilities,
        [row[2] for row in dephasing_rows],
        label="Z-basis Holevo information",
    )
    ax.plot(
        probabilities,
        [row[3] for row in dephasing_rows],
        label="best fixed-Pauli fidelity",
    )
    ax.set_xlabel("phase-flip probability")
    ax.set_ylabel("bits or fidelity")
    ax.set_title(
        "Dephasing: a classical basis survives while quantum recovery degrades"
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(
        args.output / "dephasing_classical_quantum.png",
        dpi=180,
    )
    plt.close(fig)

    damping_rows: list[tuple[float, ...]] = []
    for gamma in probabilities:
        channel = amplitude_damping_channel(float(gamma))
        information = channel_information(channel)
        effective = compose_channels(identity_channel(), channel)
        damping_rows.append(
            (
                float(gamma),
                information.coherent_information,
                information.output_entropy,
                information.exchange_entropy,
                entanglement_fidelity(effective),
            )
        )
    _write_csv(
        args.output / "amplitude_damping.csv",
        [
            "damping_gamma",
            "coherent_information_bits",
            "output_entropy_bits",
            "exchange_entropy_bits",
            "identity_recovery_entanglement_fidelity",
        ],
        damping_rows,
    )

    fig, ax = plt.subplots()
    ax.plot(
        probabilities,
        [row[1] for row in damping_rows],
        label="coherent information",
    )
    ax.plot(
        probabilities,
        [row[4] for row in damping_rows],
        label="identity-recovery entanglement fidelity",
    )
    ax.axhline(0.0, linestyle="--")
    ax.set_xlabel("amplitude-damping strength")
    ax.set_ylabel("bits or fidelity")
    ax.set_title(
        "Energy loss and quantum recoverability are not the same quantity"
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(args.output / "amplitude_damping.png", dpi=180)
    plt.close(fig)

    rng = np.random.default_rng(20260715)
    remnant_rows: list[tuple[float, ...]] = []
    fig, ax = plt.subplots()
    input_dim = 4
    radiation_dim = 4
    for remnant_dim in (1, 2, 4):
        points = random_remnant_points(
            input_dim,
            radiation_dim,
            remnant_dim,
            args.samples,
            rng,
        )
        ax.scatter(
            [point.i_reference_a for point in points],
            [point.i_reference_b for point in points],
            s=8,
            alpha=0.35,
            label=f"dim B={remnant_dim}",
        )
        for point in points:
            remnant_rows.append(
                (
                    float(remnant_dim),
                    point.i_reference_a,
                    point.i_reference_b,
                    point.entropy_reference,
                    point.sum_residual,
                    point.remnant_cap_residual,
                )
            )
    line_x = np.linspace(0.0, 4.0, 200)
    ax.plot(
        line_x,
        4.0 - line_x,
        label="pure-state sum identity",
    )
    ax.set_xlim(0.0, 4.0)
    ax.set_ylim(0.0, 4.0)
    ax.set_xlabel("I(R:A) (bits)")
    ax.set_ylabel("I(R:B) (bits)")
    ax.set_title(
        "Finite remnant dimension restricts correlation localization"
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(args.output / "finite_remnant_regions.png", dpi=180)
    plt.close(fig)
    _write_csv(
        args.output / "finite_remnant_points.csv",
        [
            "remnant_dimension",
            "i_reference_radiation_bits",
            "i_reference_remnant_bits",
            "reference_entropy_bits",
            "sum_identity_residual_bits",
            "remnant_cap_residual_bits",
        ],
        remnant_rows,
    )

    remnant_dims = np.arange(1, 17)
    fig, ax = plt.subplots()
    for entropy_reference in (1.0, 2.0, 3.0, 4.0):
        bounds = [
            radiation_information_lower_bound(
                entropy_reference,
                int(dim_b),
            )
            for dim_b in remnant_dims
        ]
        ax.plot(
            remnant_dims,
            bounds,
            marker="o",
            label=f"S(R)={entropy_reference:g} bits",
        )
    ax.set_xlabel("remnant Hilbert-space dimension")
    ax.set_ylabel("guaranteed lower bound on I(R:A) (bits)")
    ax.set_title(
        "Dimension alone gives a correlation bound, not a recovery theorem"
    )
    ax.legend()
    fig.tight_layout()
    fig.savefig(args.output / "finite_remnant_bound.png", dpi=180)
    plt.close(fig)

    summary = {
        "seed": 20260715,
        "random_samples_per_remnant_dimension": args.samples,
        "max_erasure_formula_residual": float(
            max(
                abs(row[2] - (1.0 - 0.75 * row[0]))
                for row in erasure_rows
            )
        ),
        "max_dephasing_classical_information_residual": float(
            max(abs(row[2] - 1.0) for row in dephasing_rows)
        ),
        "max_remnant_sum_identity_residual": float(
            max(abs(row[4]) for row in remnant_rows)
        ),
        "max_remnant_dimension_cap_residual": float(
            max(row[5] for row in remnant_rows)
        ),
        "interpretation": {
            "erasure": (
                "coherent information crosses zero at p=1/2 while "
                "replacement recovery degrades continuously"
            ),
            "dephasing": (
                "one classical Z-basis bit survives even when quantum "
                "coherent information vanishes"
            ),
            "finite_remnant": (
                "dimensional bounds constrain mutual information but do not "
                "alone specify a decoder or fidelity"
            ),
        },
    }
    (args.output / "summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
