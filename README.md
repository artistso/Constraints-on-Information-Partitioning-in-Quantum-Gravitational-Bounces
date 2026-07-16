# Constraints on Information Localization in Quantum-Gravitational Bounces

> **Research scaffold v0.1 — conditional, falsifiable, and publication-oriented.**
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

This identity conserves the total reference correlations but does **not** require equal partitioning. The research problem is therefore:

> Under specified assumptions about causal accessibility, conservation laws, semiclassical validity, code-subspace reconstruction, and remnant degrees of freedom, when is the infalling quantum state approximately recoverable from the asymptotic radiation?

## Repository map

| Path | Purpose |
|---|---|
| [`proposal/ABSTRACT.md`](proposal/ABSTRACT.md) | Agency-neutral formal abstract |
| [`proposal/PROPOSAL.md`](proposal/PROPOSAL.md) | Corrected concept proposal and work packages |
| [`docs/RESEARCH_MANIFOLD.md`](docs/RESEARCH_MANIFOLD.md) | Assumption-to-publication research manifold and stage gates |
| [`docs/VALIDITY_LEDGER.md`](docs/VALIDITY_LEDGER.md) | Accepted, rejected, conditional, and unresolved claims |
| [`docs/PUBLICATION_ROADMAP.md`](docs/PUBLICATION_ROADMAP.md) | Paper sequence, evidence requirements, and release criteria |
| [`manuscript/main.tex`](manuscript/main.tex) | LaTeX manuscript scaffold |
| [`references/references.bib`](references/references.bib) | Primary-source bibliography |
| [`notebooks/README.md`](notebooks/README.md) | Planned symbolic and numerical validation notebooks |
| [`data/README.md`](data/README.md) | Data provenance and phenomenology gate |

## Scientific guardrails

1. **Reference systems are explicit.** Mutual information with an input is defined using a purifying reference retained outside the channel.
2. **Kinematics and dynamics are separated.** Identities true for all quantum channels are not presented as consequences of gravity.
3. **Holographic claims are conditional.** AdS/CFT conclusions are used only where a boundary dual and code subspace are specified.
4. **Bounce models are not interchangeable.** Each effective geometry must state its asymptotics, lifetime law, degrees of freedom, and domain of validity.
5. **Phenomenology is feasibility-gated.** No telescope forecast proceeds without a dimensionally consistent emission model, event-rate prescription, and instrument response.
6. **Analogue gravity is benchmark-only.** Laboratory horizons may test channel-reconstruction methods, not Planck-scale gravitational dynamics.

## Target outputs

- A validated quantum-information classification of admissible radiation/remnant channels.
- Conditional recoverability theorems or explicit counterexamples under clearly stated assumptions.
- Model-specific analyses of selected black-to-white-hole scenarios.
- Open symbolic and numerical notebooks reproducing every central equation and scale estimate.
- An observational feasibility paper only if a concrete signal model passes the predefined gate.

## Current status

The repository is in the **formalization phase**. Earlier PDFs are treated as source material and a claim inventory, not as submission-ready science. The canonical project direction is defined by the abstract, proposal, validity ledger, and research manifold in this branch.
