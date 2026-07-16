# Publication Roadmap

## Publication principle

The project will produce scoped papers whose assumptions and evidence remain separated. Quantum-channel identities, finite-resource lemmas, recovery certificates, explicit geometry, holographic reconstruction, and observational phenomenology are not combined into one oversized claim.

---

## Paper 1A — Quantum-channel localization and finite resources

**Working title:** *Information Localization and Finite-Resource Constraints in Bipartite Quantum Channels*

### Core content

- Reference-system formulation.
- Exact pure-state localization identity.
- Counterexamples to equal partition.
- Erasure, dephasing, damping, random-isometry, and adversarial channel families.
- Finite-dimension correlation lemma.
- Finite-Hamiltonian and energy correlation lemma.
- Charge-sector and superselection lemma.
- Separation of correlation storage from operational recovery.

### Release gate

- Every theorem is classified in `docs/THEOREM_LEDGER.md`.
- Analytic and adversarial tests pass deterministic CI.
- Physical input assumptions are explicit.
- A quantum-information specialist reviews the statements.

### Release

`v1.0-qit-localization`

---

## Paper 1B — Fixed-input and channel-wide recovery

**Working title:** *Fixed-Input Fidelity and Channel-Wide Diamond Recovery in Finite-Dimensional Quantum Channels*

### Core content

- Maximally mixed-input entanglement-fidelity recovery SDP.
- Independent state-specific environment-fidelity diagnostic.
- Unnormalized Choi and input-output ordering conventions.
- Watrous diamond-norm dual SDP.
- Optimal CPTP recovery in diamond norm.
- Closest constant complementary channel in diamond norm.
- KSW convention map and deterministic implementation checks.
- Bény--Oreshkov worst-case fidelity target.
- Adversarial comparison of fixed-input fidelity, worst-case fidelity, and diamond error.

### Current completed results

- 30 optimization tests pass.
- Analytic identity, dephasing, depolarizing, and constant-channel standards pass.
- Optimal dephasing recovery matches the analytic error.
- KSW lower and upper margins pass on the deterministic sweep.
- Solver status and feasibility residuals are archived.

### Release gate

- `docs/NORM_CONVENTIONS.md` and `docs/DIAMOND_NORM_CERTIFICATE_POLICY.md` are independently reviewed.
- Fixed-input and diamond results remain distinctly labeled.
- The Bény--Oreshkov minimax is either implemented or explicitly separated as future work.
- SCS certificate behavior and residual policy are reviewed.
- Platform-complete lock and artifact manifest are archived.
- A QIT specialist reviews the composed-Choi expression and dual constraints.

### Release

`v1.1-qit-recovery`

---

## Paper 2 — HRS/Bianchi remnant capacity or underdetermination

**Working title:** *Information-Capacity Constraints in a Single-Asymptotic-Region Black-to-White-Hole Remnant Scenario*

### Core content

- Han–Rovelli–Soltani effective geometry and validity domain.
- Bianchi et al. remnant life cycle.
- Horizon, bounce, and transition parameters.
- Candidate time slices and observer algebras.
- Source-provenance table separating supplied, free, added, and missing inputs.
- Finite-dimension, finite-Hamiltonian, or sector bounds under explicit assumptions.
- Geometry-only channel-underdetermination proposition.
- Diamond evaluation only for explicitly declared channel families.

### Admissible outcomes

- model-specific capacity bound;
- conditional recovery proposition;
- excluded parameter region;
- microscopic completion;
- rigorous underdetermination theorem.

### Release gate

- HRS formulas and asymptotics pass regression tests.
- No interior-volume-to-capacity substitution is made without derivation.
- Hawking radiation, tunnelling probability, Hamiltonian, sector, and channel assumptions are explicit.
- The optimizer is not described as deriving a channel from geometry.
- A gravity/domain expert reviews the geometry and parameter interpretation.

### Release

`v2.0-remnant`

---

## Paper 3 — JT-bath reconstruction benchmark

**Working title:** *Recovery and Reconstruction Diagnostics in an Evaporating JT-Gravity Bath Model*

### Core content

- One specified JT-plus-bath setup.
- Declared diary, code subspace, and bath radiation algebra.
- Generalized entropy and QES/island transition.
- Entanglement-wedge reconstruction assumptions and error.
- Finite-dimensional surrogate channel.
- Comparison of entropy transitions, complementary decoupling, fixed-input fidelity, and diamond recovery.

### Release gate

- The exact gravitational setup and boundary conditions are fixed.
- Reconstruction theorem assumptions are mapped into repository conventions.
- The surrogate is labeled as a benchmark, not a numerical JT solution.
- Generalized entropy is not labeled an explicit decoder.
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

This replaces Paper 4A only when the full phenomenology gate passes.

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
- Finite state-space, energy, and symmetry constraints.
- Fixed-input fidelity versus worst-case fidelity versus channel-wide diamond error.
- Comparison of abstract channels, HRS/Bianchi remnants, and JT-bath reconstruction.
- Conditions under which observational claims become meaningful.

### Release gate

- Papers 1A, 1B, and 2 are technically stable.
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
| `v1.0-qit-localization` | Paper 1A theorem reproducibility release |
| `v1.1-qit-recovery` | Paper 1B fixed-input and diamond certificate release |
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
