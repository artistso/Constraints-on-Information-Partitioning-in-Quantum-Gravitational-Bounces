# Constraints on Information Localization in Quantum-Gravitational Bounces

> **Research scaffold v0.3 — conditional, falsifiable, and publication-oriented.**
>
> This repository does **not** claim a universal “no-filtering theorem.” Generic isometric quantum channels can localize information asymmetrically. The project asks which **additional physical assumptions** constrain where information is recoverable in black-to-white-hole transitions, remnant models, and controlled holographic benchmarks.

## Project thesis

Let an input system `X`, purified by a reference `R`, evolve through an isometry

\[
V:\mathcal H_X\rightarrow \mathcal H_A\otimes\mathcal H_B.
\]

For the resulting pure state on `RAB`,

\[
I(R:A)+I(R:B)=2S(R).
\]

This identity conserves total reference correlations but does **not** require equal partitioning. The research problem is:

> Under specified assumptions about causal accessibility, conservation laws, energy, semiclassical validity, code-subspace reconstruction, and remnant degrees of freedom, when is the infalling quantum state approximately recoverable from the asymptotic radiation?

## Executable validation layers

### v0.1 — Kinematics and physical scales

- explicit biased and Haar-random isometries;
- pure-state mutual-information identity;
- Schwarzschild radius, light-crossing time, Hawking temperature, and leading evaporation-time baselines;
- regression protection for rejected numerical scales.

### v0.2 — Open channels and finite remnants

- erasure, dephasing, depolarizing, and amplitude damping;
- Kraus, Stinespring, normalized Choi, coherent-information, and Holevo diagnostics;
- explicit recovery maps, entanglement fidelity, average fidelity, trace distance, and purified distance;
- finite-remnant dimension bounds and adversarial channel comparisons.

### v0.3 — Certified recovery, energy constraints, and geometry

- state-specific environmental decoupling diagnostics;
- pinned CVXPY/Clarabel semidefinite programs for optimal entanglement recovery;
- independent environment-side fidelity optimization and a cross-formulation gap;
- finite-Hamiltonian Gibbs entropy and energy-constrained correlation bounds;
- Han–Rovelli–Soltani effective geometry, horizon-root, and large-mass asymptotic checks;
- theorem, norm, model, and parameter-provenance ledgers.

## Reproduction

Base validation:

```bash
python -m pip install -e ".[test]"
pytest -m "not optimization"
python scripts/run_stress_tests.py
python scripts/run_channel_stress_tests.py
python scripts/run_geometry_stress_tests.py
```

Pinned optimization validation:

```bash
python -m pip install -e ".[test,optimization]"
pytest -m optimization
python scripts/run_theorem_stress_tests.py
```

The optimization extra pins CVXPY and Clarabel. A platform-complete transitive lock remains a release gate before a tagged numerical-certificate archive.

## Current mathematical findings

### Finite dimension

For pure `RAB` with remnant dimension `d_B`,

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\},
\]

hence

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

### Finite Hamiltonian and energy cap

For a declared finite-dimensional remnant Hamiltonian `H_B` and

\[
\operatorname{Tr}(H_B\rho_B)\leq E,
\]

let \(S_{\max}(E,H_B)\) be the Gibbs maximum entropy. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\},
\]

and

\[
I(R:A)\geq\max\{0,2S(R)-2S_{\max}(E,H_B)\}.
\]

Both are correlation bounds. Neither supplies a decoder by itself.

### Recovery certification

The optional SDP layer evaluates

\[
\max_{\mathcal R\ \mathrm{CPTP}}F_e(\mathcal R\circ\mathcal N)
\]

and independently optimizes the complementary-state fidelity to a constant environment channel. The repository records solver status, CPTP residuals, positivity residuals, and the gap between the two formulations.

This is maximally mixed-input entanglement recovery. It is not yet a channel-wide worst-case or energy-constrained diamond-norm theorem.

## Selected physical tracks

### Non-holographic track

- **Geometry:** Han–Rovelli–Soltani single-asymptotic-region transition.
- **Remnant endpoint:** Bianchi et al. white-hole remnant scenario.
- **Research output:** geometric validation, parameterized information-capacity constraints, or a rigorous underdetermination result.

The geometry does not determine a Hilbert-space dimension, Hamiltonian, microscopic channel, or radiation decoder.

### Controlled holographic benchmark

- **Model:** JT gravity coupled to quantum matter and a non-gravitating bath.
- **Research output:** reconstruction/decoupling calibration in a declared code subspace.

No JT/island conclusion is transferred to the non-holographic remnant track without an explicit assumption map.

## Repository map

| Path | Purpose |
|---|---|
| [`proposal/ABSTRACT.md`](proposal/ABSTRACT.md) | Agency-neutral formal abstract |
| [`proposal/PROPOSAL.md`](proposal/PROPOSAL.md) | Corrected concept proposal and work packages |
| [`docs/RESEARCH_MANIFOLD.md`](docs/RESEARCH_MANIFOLD.md) | Assumption-to-publication research manifold |
| [`docs/VALIDITY_LEDGER.md`](docs/VALIDITY_LEDGER.md) | Accepted, rejected, conditional, and unresolved claims |
| [`docs/THEOREM_LEDGER.md`](docs/THEOREM_LEDGER.md) | Proof, imported-theorem, and numerical-certificate status |
| [`docs/NORM_CONVENTIONS.md`](docs/NORM_CONVENTIONS.md) | Entropy, fidelity, Choi, norm, and SDP conventions |
| [`docs/SIMULATION_PROTOCOL.md`](docs/SIMULATION_PROTOCOL.md) | Pure-isometry and physical-scale protocol |
| [`docs/CHANNEL_STRESS_TEST_PROTOCOL.md`](docs/CHANNEL_STRESS_TEST_PROTOCOL.md) | Open-channel and finite-remnant protocol |
| [`models/`](models/) | HRS, Bianchi-remnant, and JT-bath model cards |
| [`src/qgbounce/`](src/qgbounce/) | Tested quantum-information, energy, geometry, and gravity utilities |
| [`scripts/`](scripts/) | Deterministic simulation and certificate runners |
| [`tests/`](tests/) | Regression, adversarial, geometry, and optimization tests |
| [`manuscript/main.tex`](manuscript/main.tex) | LaTeX manuscript scaffold |
| [`references/references.bib`](references/references.bib) | Primary-source bibliography |
| [`notebooks/README.md`](notebooks/README.md) | Publication-facing notebook roadmap |
| [`data/README.md`](data/README.md) | Data provenance and phenomenology gate |

## Scientific guardrails

1. **Reference systems are explicit.**
2. **Kinematics, dynamics, and geometry are separated.**
3. **Correlation, coherent transmission, and recovery are distinct.**
4. **State-specific certificates are not called channel-wide theorems.**
5. **Holographic claims require a specified dual and code subspace.**
6. **Geometry is not converted into information capacity without a state-space model.**
7. **Phenomenology remains feasibility-gated.**
8. **Failed tests block claims and enter the ledgers.**

## Current status

The repository is in the **certified-recovery, energy-bound, and explicit-geometry validation phase**. Earlier PDFs remain source material and a claim inventory, not submission-ready science. Draft PR #1 remains open until the v0.3 optimization suite and independent technical review pass.
