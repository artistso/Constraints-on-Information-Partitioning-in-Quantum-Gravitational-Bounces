# Constraints on Information Localization in Quantum-Gravitational Bounces

> **Research scaffold v0.2 — conditional, falsifiable, and publication-oriented.**
>
> This repository does **not** claim a universal “no-filtering theorem.” Generic isometric quantum channels can localize information asymmetrically. The project asks which **additional physical assumptions** constrain where information is recoverable in black-to-white-hole transitions, remnant models, and holographic toy models.

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

> Under specified assumptions about causal accessibility, conservation laws, semiclassical validity, code-subspace reconstruction, and remnant degrees of freedom, when is the infalling quantum state approximately recoverable from the asymptotic radiation?

## Executable stress tests

The tested Python package now covers:

- explicit isometries that move information continuously between output sectors;
- Haar-random isometry checks of the pure-state mutual-information identity;
- erasure, dephasing, depolarizing, and amplitude-damping channels;
- Stinespring dilations, normalized Choi states, coherent information, and Holevo information;
- entanglement fidelity, average state fidelity, Choi trace distance, and purified distance for explicit recovery maps;
- finite-remnant dimensional caps and radiation mutual-information lower bounds;
- unit-explicit Schwarzschild radius, light-crossing time, Hawking temperature, and leading evaporation-time baselines;
- regression tests preventing rejected formulas and unsupported interpretations from returning.

```bash
python -m pip install -e ".[test]"
pytest
python scripts/run_stress_tests.py
python scripts/run_channel_stress_tests.py
```

### Current mathematical findings

For a pure state on `RAB` with remnant dimension `d_B`,

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\},
\]

so

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

This is a valid correlation bound. It is **not** a recovery-fidelity theorem by itself. A decoder guarantee still requires a decoupling, code, complementary-channel, or approximate-correctability condition.

The channel benchmarks also demonstrate that mutual information, coherent information, classical accessibility, energy loss, and decoder fidelity are distinct quantities. They must not be substituted for one another in a gravitational argument.

The gravity calculations remain semiclassical baselines, not a bounce signal model. They cannot be promoted into burst durations, spectra, or detector forecasts without a model-specific forward calculation.

## Repository map

| Path | Purpose |
|---|---|
| [`proposal/ABSTRACT.md`](proposal/ABSTRACT.md) | Agency-neutral formal abstract |
| [`proposal/PROPOSAL.md`](proposal/PROPOSAL.md) | Corrected concept proposal and work packages |
| [`docs/RESEARCH_MANIFOLD.md`](docs/RESEARCH_MANIFOLD.md) | Assumption-to-publication research manifold and stage gates |
| [`docs/VALIDITY_LEDGER.md`](docs/VALIDITY_LEDGER.md) | Accepted, rejected, conditional, and unresolved claims |
| [`docs/PUBLICATION_ROADMAP.md`](docs/PUBLICATION_ROADMAP.md) | Paper sequence, evidence requirements, and release criteria |
| [`docs/SIMULATION_PROTOCOL.md`](docs/SIMULATION_PROTOCOL.md) | Pure-isometry and physical-scale stress-test definitions |
| [`docs/CHANNEL_STRESS_TEST_PROTOCOL.md`](docs/CHANNEL_STRESS_TEST_PROTOCOL.md) | Open-channel, recovery, and finite-remnant protocol |
| [`src/qgbounce/`](src/qgbounce/) | Tested quantum-information and gravity utilities |
| [`scripts/run_stress_tests.py`](scripts/run_stress_tests.py) | Isometry and gravitational-scale simulation runner |
| [`scripts/run_channel_stress_tests.py`](scripts/run_channel_stress_tests.py) | Channel and remnant simulation runner |
| [`tests/`](tests/) | Regression tests and counterexample assertions |
| [`manuscript/main.tex`](manuscript/main.tex) | LaTeX manuscript scaffold |
| [`references/references.bib`](references/references.bib) | Primary-source bibliography |
| [`notebooks/README.md`](notebooks/README.md) | Notebook roadmap linked to the executable package |
| [`data/README.md`](data/README.md) | Data provenance and phenomenology gate |

## Scientific guardrails

1. **Reference systems are explicit.** Mutual information with an input is defined using a purifying reference retained outside the channel.
2. **Kinematics and dynamics are separated.** Identities true for all quantum channels are not presented as consequences of gravity.
3. **Correlation and recovery are separated.** A mutual-information bound is not called a decoder or fidelity theorem.
4. **Holographic claims are conditional.** AdS/CFT conclusions are used only where a boundary dual and code subspace are specified.
5. **Bounce models are not interchangeable.** Each effective geometry must state its asymptotics, lifetime law, degrees of freedom, and domain of validity.
6. **Phenomenology is feasibility-gated.** No telescope forecast proceeds without a dimensionally consistent emission model, event-rate prescription, and instrument response.
7. **Analogue gravity is benchmark-only.** Laboratory horizons may test channel-reconstruction methods, not Planck-scale gravitational dynamics.
8. **Failed tests block claims.** Numerical disagreements enter the validity ledger rather than being hidden through tolerance or plotting changes.

## Target outputs

- A validated quantum-information classification of admissible radiation/remnant channels.
- Conditional recoverability theorems or explicit counterexamples under clearly stated assumptions.
- Model-specific analyses of selected black-to-white-hole scenarios.
- Open symbolic and numerical notebooks reproducing every central equation and scale estimate.
- An observational feasibility paper only if a concrete signal model passes the predefined gate.

## Current status

The repository is in the **open-channel and finite-remnant validation phase**. Earlier PDFs are source material and a claim inventory, not submission-ready science. Draft PR #1 contains the canonical project direction, executable validation layers, and research manifold.
