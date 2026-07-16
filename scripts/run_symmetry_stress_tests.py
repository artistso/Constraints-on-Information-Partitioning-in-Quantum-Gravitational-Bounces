"""Generate deterministic charge-sector and superselection-bound products."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from qgbounce.symmetry import (
    superselection_entropy_cap,
    superselection_radiation_information_lower_bound,
    superselection_remnant_information_cap,
)


def main() -> None:
    output = Path("outputs/symmetry_stress_tests")
    output.mkdir(parents=True, exist_ok=True)

    entropy_reference = 2.0
    sector_dimensions = np.array([1, 4])
    probabilities = np.linspace(0.0, 1.0, 201)

    rows: list[tuple[float, ...]] = []
    for probability_high_sector in probabilities:
        distribution = np.array(
            [1.0 - probability_high_sector, probability_high_sector]
        )
        entropy_cap = superselection_entropy_cap(
            distribution,
            sector_dimensions,
        )
        remnant_cap = superselection_remnant_information_cap(
            entropy_reference,
            distribution,
            sector_dimensions,
        )
        radiation_lower = superselection_radiation_information_lower_bound(
            entropy_reference,
            distribution,
            sector_dimensions,
        )
        rows.append(
            (
                float(probability_high_sector),
                entropy_cap,
                remnant_cap,
                radiation_lower,
            )
        )

    csv_path = output / "charge_sector_bounds.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "probability_dimension_4_sector",
                "retained_entropy_cap_bits",
                "remnant_mutual_information_cap_bits",
                "radiation_mutual_information_lower_bound_bits",
            ]
        )
        writer.writerows(rows)

    fig, ax = plt.subplots()
    ax.plot(
        probabilities,
        [row[1] for row in rows],
        label="retained entropy cap",
    )
    ax.plot(
        probabilities,
        [row[2] for row in rows],
        label="remnant mutual-information cap",
    )
    ax.plot(
        probabilities,
        [row[3] for row in rows],
        label="radiation mutual-information lower bound",
    )
    ax.set_xlabel("probability assigned to the dimension-4 charge sector")
    ax.set_ylabel("bits")
    ax.set_title("Charge distribution and sector degeneracy constrain storage")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output / "charge_sector_bounds.png", dpi=180)
    plt.close(fig)

    total_dimension = int(sector_dimensions.sum())
    maximizing_distribution = sector_dimensions / total_dimension
    summary = {
        "entropy_reference_bits": entropy_reference,
        "sector_dimensions": sector_dimensions.tolist(),
        "distribution_maximizing_unconstrained_entropy": (
            maximizing_distribution.tolist()
        ),
        "maximum_sector_entropy_cap_bits": superselection_entropy_cap(
            maximizing_distribution,
            sector_dimensions,
        ),
        "unrestricted_total_dimension_cap_bits": float(
            np.log2(total_dimension)
        ),
        "scope": (
            "finite direct-sum sectors with a declared block-diagonal state; "
            "sector structure and probabilities are physical inputs"
        ),
    }
    (output / "summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
