# Publication Roadmap

## Publication principle

The project will produce scoped papers whose assumptions and evidence remain separated. Quantum-channel theorems, explicit geometry, holographic reconstruction, and observational phenomenology are not combined into one oversized claim.

---

## Paper 1 — Quantum-channel localization and certified recovery

**Working title:** *Information Localization and Approximate Recoverability in Bipartite Quantum Channels*

### Core content

- Reference-system formulation.
- Exact pure-state localization identity.
- Counterexamples to equal partition and universal no-filtering.
- Erasure, dephasing, damping, random-isometry, and adversarial channel families.
- Finite-dimension correlation lemma.
- Finite-Hamiltonian/energy correlation lemma.
- State-specific complementary decoupling.
- Optimal maximally mixed-input recovery SDP.
- Independent environment-fidelity SDP.
- Explicit distinction between fixed-input certification and worst-case channel theorems.

### Release gate

- Every theorem and certificate is classified in `docs/THEOREM_LEDGER.md`.
- Norm, fidelity, and Choi conventions are fixed.
- Analytic erasure and dephasing optima pass the pinned optimization CI.
- Solver feasibility and positivity residuals pass declared tolerances.
- Recovery/environment cross-formulation gaps are reported.
- Adversarial tests accompany every proposed single-number diagnostic.
- A quantum-information specialist reviews the statements and convention mapping.

### Release

`v1.0-qit`

---

## Paper 2 — HRS/Bianchi remnant capacity or underdetermination

**Working title:** *Information-Capacity Constraints in a Single-Asymptotic-Region Black-to-White-Hole Remnant Scenario*

### Core content

- Han–Rovelli–Soltani effective geometry and validity domain.
- Bianchi et al. remnant life cycle.
- Horizon, bounce, and transition parameters.
- Candidate time slices and observer algebras.
- Source-provenance table separating supplied, free, and missing inputs.
- Finite-dimension or finite-Hamiltonian bounds under explicitly added assumptions.
- Proof that geometry alone does or does not determine an information-capacity statement.

### Admissible outcomes

- model-specific capacity bound;
- conditional recovery proposition;
- no-go parameter region;
- rigorous underdetermination theorem.

### Release gate

- HRS formulas and asymptotics pass regression tests.
- No interior-volume-to-capacity substitution is made without derivation.
- Hawking radiation, tunnelling probability, Hamiltonian, and channel assumptions are explicit.
- A gravity/domain expert reviews the geometry and parameter interpretation.

### Release

`v2.0-remnant`

---

## Paper 3 — JT-bath reconstruction benchmark

**Working title:** *Recovery and Reconstruction Diagnostics in an Evaporating JT-Gravity Bath Model*

### Core content

- One specified JT-plus-bath setup.
- Declared code subspace and bath radiation algebra.
- Generalized entropy and QES/island transition.
- Entanglement-wedge reconstruction assumptions and error.
- Finite-dimensional surrogate channel.
- Comparison of entropy transitions, complementary decoupling, and certified recovery.

### Release gate

- The exact gravitational setup and boundary conditions are fixed.
- Reconstruction theorem assumptions are mapped into repository conventions.
- The surrogate is labeled as a benchmark, not a numerical JT solution.
- No conclusion is transferred to the HRS/Bianchi track without an assumption map.

### Release

`v3.0-jt`

---

## Paper 4A — Phenomenology feasibility limit

**Working title:** *Feasibility Conditions for Observational Tests of Black-to-White-Hole Transition Models*

This is the default phenomenology output.

### Core content

- Minimum source-model requirements.
- Mass, lifetime, transition, spectrum, duration, and rate distinctions.
- Contemporary PBH-to-white-hole constraints and assumption sensitivity.
- Detector-level overlap or proof of non-identifiability.
- Missing theoretical information required before a search.

### Release gate

- Unit-tested forward model.
- Primary-source parameter provenance.
- No generic FRB, optical, or gamma-ray association.
- Clear distinction among Hawking evaporation, tunnelling, remnant decay, and ejecta.

### Release

`v4.0-feasibility`

---

## Paper 4B — Observational search

**Working title:** determined only by a validated signal and instrument.

This replaces Paper 4A only if the full phenomenology gate passes.

### Core content

- Signal injection and recovery.
- Instrument response and data-quality cuts.
- Background and contaminant population.
- Search statistic, trials correction, and efficiency.
- Parameter-space limits or detection inference.
- Public code and derived products where licensing permits.

### Release gate

- Complete signal and population model.
- Detectable parameter region.
- Reproducible data access.
- Null result maps to model parameters.

---

## Paper 5 — Synthesis

**Working title:** *Information Localization Across Quantum-Gravitational Transition Models*

### Core content

- Global unitarity versus subsystem entropy versus operational recovery.
- Finite state-space and energy constraints.
- Certified fixed-input recovery versus channel-wide theorems.
- Comparison of abstract channels, HRS/Bianchi remnants, and JT-bath reconstruction.
- Conditions under which observational claims become meaningful.

### Release gate

- Papers 1 and 2 are technically stable.
- JT benchmark is complete or clearly excluded.
- Phenomenology is represented by a feasibility result or validated search.
- Every synthesis claim cites a proof, certificate, or primary source.

### Release

`v5.0-synthesis`

---

## Versioning plan

| Version | Meaning |
|---|---|
| `v0.x` | Internal formalization, stress testing, and model audit |
| `v1.0-qit` | Paper 1 theorem/certificate reproducibility release |
| `v2.0-remnant` | HRS/Bianchi model-analysis release |
| `v3.0-jt` | Controlled holographic benchmark release |
| `v4.0-feasibility` | Phenomenology feasibility release |
| `v4.x-search` | Optional validated observational release |
| `v5.0-synthesis` | Integrated publication package |

## Evidence requirements for every release

- manuscript source and compiled PDF;
- complete bibliography;
- platform-specific environment lock;
- scripts/notebooks generating every reported result;
- automated mathematical, solver, and dimensional tests;
- solver artifacts for numerical certificates;
- source and parameter provenance;
- limitations and negative-results section;
- archived release identifier and checksum manifest.
