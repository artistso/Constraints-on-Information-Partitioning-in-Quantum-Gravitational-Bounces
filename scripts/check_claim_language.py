"""Block known false or overstated claims in public-facing project documents."""

from __future__ import annotations

import re
from pathlib import Path

PUBLIC_DOCUMENTS = (
    Path("README.md"),
    Path("proposal/ABSTRACT.md"),
    Path("proposal/PROPOSAL.md"),
    Path("manuscript/main.tex"),
)

FORBIDDEN_PATTERNS = {
    "universal no-filtering theorem": re.compile(
        r"\bno[- ]filtering theorem\b",
        re.IGNORECASE,
    ),
    "monogamy forbids biased partition": re.compile(
        r"\bmonogamy of entanglement\b.{0,160}\bforbid(?:s|den)?\b",
        re.IGNORECASE | re.DOTALL,
    ),
    "full initial information must enter radiation": re.compile(
        r"\b(?:must|will) return (?:all|the full)(?: of)? the initial "
        r"information\b",
        re.IGNORECASE,
    ),
    "all information eventually escapes": re.compile(
        r"\ball(?: of)? (?:the )?information eventually escapes\b",
        re.IGNORECASE,
    ),
    "Page curve proves universal radiation recovery": re.compile(
        r"\bPage curve\b.{0,180}\b(?:prove|proves|proved|proof)\b"
        r".{0,180}\b(?:all|full|every)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    "island formula proves universal recovery": re.compile(
        r"\bisland formula\b.{0,180}\b(?:prove|proves|proved|proof)\b",
        re.IGNORECASE | re.DOTALL,
    ),
    "universal repulsive quantum pressure": re.compile(
        r"\brepulsive quantum pressure\b",
        re.IGNORECASE,
    ),
    "all physical black holes bounce": re.compile(
        r"\ball physical black holes\b.{0,100}\bbounce\b",
        re.IGNORECASE | re.DOTALL,
    ),
    "generic present-epoch bursting": re.compile(
        r"\bbursting in the present epoch\b",
        re.IGNORECASE,
    ),
    "observatories actively preparing a white-hole search": re.compile(
        r"\bactively preparing to search\b",
        re.IGNORECASE,
    ),
    "incorrect decoding gate count": re.compile(
        r"\b10\s*\^?\s*\{?77\}?\s+gates\b",
        re.IGNORECASE,
    ),
    "unsupported Quantum Darwinism mechanism": re.compile(
        r"\bQuantum Darwinism\b",
        re.IGNORECASE,
    ),
    "selective filtration conclusion": re.compile(
        r"\bselective(?:ly)?\s+(?:filter|filtration|partition)\b",
        re.IGNORECASE,
    ),
    "geometry defines a quantum channel": re.compile(
        r"\bgeometry (?:itself )?(?:defines|determines) (?:a |the )?"
        r"(?:microscopic )?quantum channel\b",
        re.IGNORECASE,
    ),
    "interior volume equals information capacity": re.compile(
        r"\binterior volume (?:is|equals|determines) (?:the )?"
        r"(?:quantum )?information capacity\b",
        re.IGNORECASE,
    ),
    "consensus-from-analogy language": re.compile(
        r"\bphysics (?:highly )?agrees with your intuition\b",
        re.IGNORECASE,
    ),
    "modern physics consensus language": re.compile(
        r"\bmodern physics consensus\b",
        re.IGNORECASE,
    ),
}


def find_violations(root: Path) -> list[str]:
    violations: list[str] = []
    for relative_path in PUBLIC_DOCUMENTS:
        path = root / relative_path
        if not path.exists():
            violations.append(f"missing public document: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            match = pattern.search(text)
            if match is None:
                continue
            line_number = text.count("\n", 0, match.start()) + 1
            excerpt = " ".join(match.group(0).split())
            violations.append(
                f"{relative_path}:{line_number}: {label}: {excerpt!r}"
            )
    return violations


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    violations = find_violations(root)
    if violations:
        print("Claim-language validation failed:")
        for violation in violations:
            print(f"- {violation}")
        return 1
    print("Claim-language validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
