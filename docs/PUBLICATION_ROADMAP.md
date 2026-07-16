# Publication Roadmap

## Publication principle

The repository is organized to produce a sequence of scoped papers rather than one oversized proposal that mixes universal quantum-information claims, speculative gravity, analogue experiments, and observational forecasts.

---

## Paper 1 — Information localization in bipartite isometric channels

**Working title:** *Information Localization and Recoverability in Bipartite Quantum Channels: Identities, Counterexamples, and Conditional Bounds*

### Core content

- Reference-system formulation of the input-output problem.
- Exact identity \(I(R:A)+I(R:B)=2S(R)\) for pure \(RAB\).
- Counterexamples to equal-partition and universal no-filtering claims.
- Feasible regions for mutual information, coherent information, and recovery fidelity.
- Conditional bounds under finite dimension, symmetry, conservation, or energy constraints.
- Reproducible symbolic and numerical validation.

### Release gate

- All theorem assumptions appear in the statement.
- At least one extremal or saturating example is supplied.
- Automated counterexample search has been run against each universal claim.
- A quantum-information specialist has reviewed the definitions and proof.

### Likely venue class

Quantum information, mathematical physics, or foundations journal; venue selected only after the theorem strength is known.

---

## Paper 2 — Model-specific gravitational recoverability

**Working title:** *Recoverability of Infalling Quantum Information in a Specified Black-to-White-Hole Transition Model*

### Core content

- One named model with equations and boundary conditions.
- Causal diagram and subsystem/algebra definitions.
- Explicit statement of whether the treatment is holographic, semiclassical, effective, or phenomenological.
- Translation from the geometry to channel constraints.
- Derived recoverability bound, obstruction, or counterexample.
- Limitations and neighboring models to which the result does not apply.

### Release gate

- A model card is complete.
- The microscopic channel is derived or the absence of one is handled as a bound problem.
- Holographic assumptions are not transferred to a non-holographic model without a duality argument.
- Backreaction and remnant assumptions are explicit.
- A domain expert in the chosen model has reviewed the setup.

---

## Paper 3A — Phenomenology feasibility limit

**Working title:** *Feasibility Conditions for Observational Tests of Black-to-White-Hole Transition Models*

This is the default observational output if no robust detectable signal is established.

### Core content

- Source-model requirements.
- Correct mass, lifetime, duration, spectrum, and rate scaling.
- Detector-level sensitivity comparison.
- Identification of parameter regions that are inaccessible or underdetermined.
- Minimum theoretical information required before a real search is justified.

### Release gate

- Unit-tested forward model.
- Primary-source parameter provenance.
- No unsupported sensitivity-improvement claim.
- Clear distinction between Hawking evaporation, tunneling, remnant decay, and any ejecta process.

---

## Paper 3B — Observational search

**Working title:** To be determined from the model and instrument.

This paper replaces Paper 3A only when the phenomenology gate passes.

### Core content

- Injection–recovery simulations.
- Instrument response and data-quality cuts.
- Background and contaminant model.
- Search statistic and trials correction.
- Detection efficiency.
- Frequentist or Bayesian upper limits mapped to model parameters.
- Public code and derived data products where licensing permits.

### Release gate

- Complete signal and rate model.
- Non-negligible detectable parameter region.
- Data access and reproducible pipeline confirmed.
- Null result has model-discriminating value.

---

## Paper 4 — Synthesis

**Working title:** *Information Localization Across Quantum-Gravitational Transition Models*

### Core content

- Distinction among global unitarity, subsystem entropy, and operational recovery.
- Comparison of abstract channels, holographic models, and non-holographic bounce models.
- Conditions under which radiation recovery is established.
- Conditions under which remnants or inaccessible sectors remain admissible.
- Observational implications supported by the completed feasibility work.

### Release gate

- Papers 1 and 2 are complete or technically stable.
- Phenomenology is represented by Paper 3A or 3B, not by preliminary speculation.
- Every synthesis claim cites a derivation or a primary source.

---

## Versioning plan

| Version | Meaning |
|---|---|
| `v0.x` | Internal formalization and claim audit |
| `v1.0-qit` | Paper 1 reproducibility release |
| `v2.0-model` | Paper 2 model-analysis release |
| `v3.0-pheno` | Feasibility or observational release |
| `v4.0-synthesis` | Integrated publication package |

## Repository evidence requirements

Each paper release must include:

- manuscript source and compiled PDF;
- bibliography;
- environment lock file;
- notebooks or scripts producing all reported calculations;
- tests for dimensional and mathematical identities;
- data provenance statement;
- limitations and negative-results section;
- archived release identifier.
