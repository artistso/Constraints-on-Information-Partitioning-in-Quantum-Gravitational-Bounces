# Concept Proposal v0.4

## Constraints on Information Localization and Recoverability in Quantum-Gravitational Bounce Models

**Project type:** Foundational quantum information, effective quantum gravity, and feasibility-gated phenomenology  
**Proposed duration:** 36 months  
**Budget status:** To be developed for a named host institution and funding call; no unsupported amount is assigned in this concept document.

---

## 1. Executive rationale

Black-to-white-hole transitions, nonsingular interiors, and long-lived remnants raise a legitimate operational question: after a proposed quantum-gravitational transition, which observer-accessible algebra permits recovery of information about the initial quantum state?

Generic unitary or isometric evolution preserves the complete quantum state but does not determine how correlations are localized among radiation, retained degrees of freedom, and inaccessible sectors. The corrected research question is therefore:

> Which explicit physical assumptions constrain information localization and support a quantified recovery statement in a specified gravitational model?

The project has four layers:

1. exact channel identities, counterexamples, and adversarial tests;
2. finite-resource bounds and scoped recovery certification;
3. explicit geometric and holographic model embeddings;
4. observational work only after a complete forward signal model passes a predefined gate.

This architecture ensures that the mathematical deliverables remain valid even if a proposed transition or remnant scenario is incomplete, underdetermined, or physically disfavored.

Public language is controlled by `docs/CANONICAL_CLAIMS.md`, `docs/VALIDITY_LEDGER.md`, `docs/THEOREM_LEDGER.md`, and `docs/NORM_CONVENTIONS.md`.

---

## 2. Established mathematical foundation

### 2.1 Reference-assisted formulation

Let \(X\) be the input and let \(R\) purify its initial state. A bipartite isometric output is represented by

\[
V:\mathcal H_X\longrightarrow\mathcal H_A\otimes\mathcal H_B,
\]

where \(A\) is a declared accessible sector and \(B\) is a declared retained sector. For the resulting pure state \(ho_{RAB}\),

\[
I(R:A)+I(R:B)=2S(R).
\]

This identity conserves total reference correlations but does not imply

\[
I(R:A)=I(R:B)=S(R).
\]

For example,

\[
|\psi\rangle_X\mapsto|\psi\rangle_A|0\rangle_B
\]

is a maximally asymmetric isometry. Exact isometry therefore does not determine equal localization.

### 2.2 Finite retained dimension

If \(\dim B=d_B\), then

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\}.
\]

For pure \(RAB\),

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

This is a correlation-storage bound. It does not construct a decoder or imply high recovery fidelity.

### 2.3 Finite Hamiltonian and energy cap

Suppose the retained sector has a declared finite-dimensional Hamiltonian \(H_B\) and satisfies

\[
\operatorname{Tr}(H_B\rho_B)\leq E.
\]

Let \(S_{\max}(E,H_B)\) be the maximum entropy allowed by the constraint, obtained from the Gibbs variational principle. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\},
\]

and

\[
I(R:A)\geq\max\{0,2S(R)-2S_{\max}(E,H_B)\}.
\]

The Hamiltonian and energy cap must be supplied by the physical model. They are not inferred from exterior mass, interior volume, area, or lifetime.

### 2.4 Scoped recovery certification

For a declared finite-dimensional channel \(\mathcal N\), the executable program solves

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N)
\]

for the maximally mixed input using a semidefinite program over the recovery Choi matrix. A second optimization compares the complementary Choi state with a constant environment state.

The repository records:

- solver status;
- objective value;
- trace-preservation residual;
- minimum Choi eigenvalue;
- environment-state feasibility residuals;
- cross-formulation gap.

The recovery-side program is validated against analytic erasure and dephasing standards. The current result is a fixed-input numerical certificate, not a channel-wide worst-case or diamond-norm theorem.

---

## 3. Selected physical tracks

### 3.1 Han--Rovelli--Soltani geometric scaffold

The principal non-holographic geometry is the Han--Rovelli--Soltani single-asymptotic-region effective transition. In natural units, the implemented source-level formulas include

\[
a(T)=\left(\frac{9mT^2+Am}{2}\right)^{1/3}
\]

and

\[
F(r)=1-\frac{2m}{r}+\frac{Am^2}{r^4}.
\]

For \(m^2\gg A\), the positive roots satisfy

\[
r_+\simeq2m,
\qquad
r_-\simeq\left(\frac{Am}{2}\right)^{1/3}.
\]

The repository verifies the source equations, bounce symmetry, horizon roots, and large-mass limits. The geometry supplies causal and metric structure. It does not supply a microscopic quantum state space, transition channel, tunnelling probability, Hawking-radiation model, spectrum, or decoder.

### 3.2 White-hole remnant endpoint

The Bianchi--Christodoulou--D'Ambrosio--Haggard--Rovelli scenario is retained as the first remnant-capacity case study. The initial analysis is parametric because the source model does not provide:

- a remnant Hilbert-space dimension;
- a microscopic Hamiltonian;
- a complete radiation algebra at a specified time cut;
- a complete unitary or CPTP channel;
- an operational recovery map.

The scientifically admissible model-specific outputs are:

1. a capacity bound under an explicit added state-space assumption;
2. a conditional recovery statement under an explicit decoupling assumption;
3. an excluded parameter region;
4. a theorem of underdetermination identifying the missing physical inputs.

### 3.3 Controlled JT-gravity benchmark

A specified JT-gravity region coupled to quantum matter and a non-gravitating bath is retained as a separate benchmark for:

- generalized entropy and island transitions;
- declared radiation-region algebras;
- finite code-subspace reconstruction;
- complementary decoupling;
- comparison with finite-dimensional recovery certificates.

The entropy of a declared radiation region is not treated as an explicit decoder. Results from this benchmark do not transfer to the non-holographic remnant track without an explicit map of assumptions, algebras, observables, and errors.

---

## 4. Research objectives

### Objective 1 — Complete the information-localization classification

Map feasible values of

\[
\mathcal L=
\bigl(I(R:A),I(R:B),I_c(R\rangle A),I_c(R\rangle B),F_A,F_B\bigr)
\]

for canonical and adversarial channels.

Required examples include:

- one-port isometries;
- erasure and complementary channels;
- dephasing, depolarizing, and amplitude damping;
- random isometries;
- finite-resource retained sectors;
- channels with similar mutual information but different recovery fidelity;
- channels with similar classical accessibility but different coherent information.

**Deliverable:** Paper 1 mathematical core and reproducible package.

### Objective 2 — Establish worst-case approximate recovery under explicit conventions

Advance through three levels:

1. state-specific decoupling and recovery existence;
2. certified maximally mixed-input recovery;
3. worst-case and energy-constrained results only after Bény--Oreshkov and Kretschmann--Schlingemann--Werner statements are reconstructed under repository notation and norm conventions.

Every recovery claim must state:

- input ensemble or code subspace;
- accessible algebra;
- norm and fidelity convention;
- constructive or existential status;
- proof or solver certificate;
- numerical tolerance and failure policy.

**Deliverable:** A conditional theorem or precisely scoped certificate paper.

### Objective 3 — Extend finite-resource bounds

Extend the finite-dimensional and finite-Hamiltonian lemmas to declared:

- conserved charges;
- superselection sectors;
- symmetry-covariant channels;
- energy-constrained capacities and norms.

No resource constraint is inferred from geometry unless the model supplies the relevant operator and state-space structure.

**Deliverable:** A resource-constrained correlation theorem and, where assumptions permit, an operational recovery proposition.

### Objective 4 — Produce a model-specific HRS/Bianchi result

The non-holographic work package will:

- validate the geometric equations and parameter regimes;
- define candidate slices and observer algebras;
- inventory supplied, free, and missing microscopic inputs;
- apply only information bounds supported by declared assumptions;
- determine whether the strongest defensible result is a capacity bound, obstruction, or theorem of underdetermination.

**Deliverable:** Paper 2.

### Objective 5 — Implement one explicit JT-bath benchmark

The holographic work package will:

- select one published JT-bath setup;
- define the code subspace and radiation region;
- reproduce the relevant generalized-entropy transition;
- map the reconstruction theorem and approximation error;
- compare the gravitational criterion with finite-dimensional decoupling and recovery diagnostics.

**Deliverable:** A separate controlled benchmark paper.

### Objective 6 — Maintain a feasibility-gated phenomenology program

No observational data search begins until a selected source model supplies:

- transition or decay rate;
- emitted energy and spectrum;
- intrinsic duration and light curve;
- source population and distance distribution;
- propagation and attenuation;
- detector response and backgrounds;
- a statistical detection or upper-limit plan.

The Schwarzschild time \(2GM/c^3\) is used only as a dimensional baseline. It is not identified with an observed transient duration without a derived source mechanism.

**Deliverable:** A feasibility memorandum; an observational paper only if every mandatory gate passes.

---

## 5. Methodology and reproducibility

### 5.1 Analytic and adversarial validation

Every universal statement is tested against extremal channels and deterministic random ensembles. Single-number diagnostics are challenged using channel pairs with similar scalar values but different operational recovery behavior.

### 5.2 Convex optimization

The recovery SDP uses an unnormalized Choi matrix \(J_{\mathcal R}\) with

\[
J_{\mathcal R}\succeq0,
\qquad
\operatorname{Tr}_{\mathrm{out}}J_{\mathcal R}=I_{\mathrm{in}}.
\]

The optional environment is pinned and tested in CI. Values with unacceptable feasibility residuals or solver status are retained only as diagnostics.

### 5.3 Energy-constrained calculations

For finite spectra, the Gibbs optimizer is solved deterministically and checked against analytic two-level examples, degeneracies, inactive constraints, and parameter sweeps.

### 5.4 Geometry validation

The HRS implementation is restricted to source-level formulas and natural units. No microscopic channel, tunnelling probability, Hawking flux, emission spectrum, or detector signature is inferred from the geometric tests.

### 5.5 Claim-language validation

`scripts/check_claim_language.py` scans the public-facing README, abstract, proposal, and manuscript for known false or overstated formulations. A violation fails CI and blocks claim promotion.

### 5.6 Repository controls

The project maintains:

- canonical-claim, validity, theorem, and norm ledgers;
- model cards and parameter provenance;
- deterministic random seeds;
- Python 3.11/3.12 regression CI;
- a separate pinned optimization CI job;
- generated CSV, figure, JSON, and diagnostic products;
- manuscript and bibliography sources.

---

## 6. Explicit nonclaims

This proposal does not assert that:

- global unitarity determines equal output localization;
- a Page transition supplies an operational decoder;
- a loop-inspired effective model is the consensus prediction of quantum gravity;
- a metric determines information capacity or microscopic dynamics;
- a remnant can or cannot store the input without a state-space assumption;
- a broad primordial-black-hole mass interval produces present-day observable events;
- any named instrument supplies a viable search before the forward-model gate passes;
- analogy provides mathematical or observational evidence.

---

## 7. Work plan

### Year 1 — Quantum-information foundation

- Complete analytic and adversarial channel classification.
- Consolidate fixed-input recovery certificates.
- Reconstruct worst-case information--disturbance conventions and constants.
- Complete charge, symmetry, and superselection extensions.
- Draft Paper 1.

### Year 2 — Geometry and model embedding

- Complete HRS geometry and Bianchi-remnant provenance analysis.
- Determine whether a defensible remnant Hamiltonian, entropy cap, or channel condition exists.
- Produce a model-specific bound or theorem of underdetermination.
- Implement the JT-bath benchmark.
- Draft Papers 2 and 3.

### Year 3 — Feasibility gate and synthesis

- Evaluate whether any selected model supplies a complete signal prescription.
- If the gate passes, conduct injection--recovery and archival analysis.
- If the gate fails, publish the feasibility limit and missing-input result.
- Complete a synthesis manuscript and versioned reproducibility archive.

---

## 8. Deliverables

| ID | Deliverable | Acceptance criterion |
|---|---|---|
| D1 | Canonical claim, validity, theorem, and norm ledgers | Every public claim has a proof, source, certificate, condition, or block |
| D2 | Channel and adversarial test suite | Analytic cases and counterexamples pass deterministic CI |
| D3 | Fixed-input recovery certificates | Solver status and feasibility residuals satisfy declared policy |
| D4 | Worst-case theorem reconstruction | Definitions, constants, code convention, and low-dimensional checks complete |
| D5 | Finite-resource results | Dimension, finite-Hamiltonian, charge, and symmetry assumptions explicit |
| D6 | HRS geometry package | Source equations, roots, limits, and units reproduced |
| D7 | Model cards and provenance | Supplied, free, and missing parameters separated |
| D8 | Paper 1 | Information localization, adversarial examples, and conditional recovery |
| D9 | Paper 2 | HRS/Bianchi capacity bound, obstruction, or underdetermination theorem |
| D10 | JT benchmark paper | Declared code subspace, radiation region, and recovery comparison |
| D11 | Phenomenology memorandum or paper | Released only after the forward-model gate is evaluated |

---

## 9. Risk management

### No strong universal theorem

**Response:** Publish exact identities, counterexamples, finite-resource lemmas, and conditional results.

### No microscopic remnant channel

**Response:** Produce parameterized capacity bounds or a theorem of underdetermination. Do not fabricate channel operators from a causal diagram.

### Numerical conditioning or formulation disagreement

**Response:** Block certificate use, preserve diagnostic artifacts, compare independent formulations, and seek analytic reductions or additional solvers.

### Holographic results do not transfer

**Response:** Maintain JT gravity as a separate benchmark.

### Phenomenology remains incomplete

**Response:** Publish the feasibility limit rather than performing an unsupported search.

---

## 10. Required expertise and resources

A credible team requires:

- quantum channels and approximate quantum error correction;
- convex optimization and numerical certification;
- semiclassical gravity and the selected effective transition geometry;
- holographic reconstruction for the JT benchmark;
- research software and reproducibility;
- astrophysical inference only if the phenomenology gate passes.

The baseline resource model is a principal investigator, one postdoctoral researcher or equivalent effort, modest computation, collaboration travel, and publication costs. No facility construction or custom instrumentation is assumed.

---

## 11. Publication strategy

1. **Paper 1:** information localization, finite-resource bounds, adversarial channels, and scoped recovery certification.
2. **Paper 2:** information-capacity constraints or underdetermination in the HRS/Bianchi remnant track.
3. **Paper 3:** reconstruction and recovery diagnostics in the JT-bath benchmark.
4. **Paper 4:** phenomenology feasibility or observational analysis, only if authorized by the gate.
5. **Synthesis:** consequences and limits of information-recovery claims across gravitational transition models.

No manuscript is labeled theorem-ready until its statement, assumptions, convention mapping, tests, and independent review are complete.

---

## 12. Expected contribution

The project will produce a rigorous hierarchy of what follows from quantum-channel kinematics, finite state-space resources, energy constraints, environmental decoupling, scoped recovery certification, explicit geometry, and additional model assumptions. Where a physical model is incomplete, that incompleteness will be converted into a precise obstruction or theorem of underdetermination rather than an unsupported simulation or forecast.
