# Concept Proposal v0.3

## Constraints on Information Localization and Recoverability in Quantum-Gravitational Bounce Models

**Project type:** Foundational quantum information, effective quantum gravity, and feasibility-gated phenomenology  
**Proposed duration:** 36 months  
**Budget status:** To be developed for a named host institution and funding call; no unsupported amount is assigned in this concept document.

---

## 1. Executive rationale

Black-to-white-hole transitions, nonsingular interiors, and long-lived remnants raise a legitimate information-theoretic question: after a proposed quantum-gravitational transition, which observer-accessible subsystem permits recovery of the initial quantum state?

A previous formulation asserted that unitarity forces equal information partitioning between radiation and retained degrees of freedom. Generic isometric channels provide immediate counterexamples. The corrected program asks:

> Which additional physical assumptions constrain information localization and permit a quantified recovery theorem in a specified gravitational model?

The project is divided into four layers:

1. exact channel identities, counterexamples, and adversarial tests;
2. finite-dimension, energy, decoupling, and certified-recovery bounds;
3. explicit geometric and holographic model embeddings;
4. observational work only after a complete forward signal model passes a predefined gate.

This architecture ensures that the mathematical deliverables remain valid even if a proposed bounce or remnant scenario is incomplete or physically disfavored.

---

## 2. Corrected mathematical foundation

### 2.1 Reference-system formulation

Let \(X\) be the input and let \(R\) purify its initial state. A complete bipartite output is represented by

\[
V:\mathcal H_X\longrightarrow\mathcal H_A\otimes\mathcal H_B,
\]

where \(A\) is an accessible radiation sector and \(B\) is a retained sector. For pure \(ho_{RAB}\),

\[
I(R:A)+I(R:B)=2S(R).
\]

This identity conserves total reference correlations but does not imply

\[
I(R:A)=I(R:B)=S(R).
\]

The isometry

\[
|\psi\rangle_X\mapsto|\psi\rangle_A|0\rangle_B
\]

is a maximally biased counterexample.

### 2.2 Finite-remnant correlation lemma

If \(\dim B=d_B\), then

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\}.
\]

For pure \(RAB\),

\[
I(R:A)\geq
\max\{0,2S(R)-2\log_2d_B\}.
\]

This is a valid correlation bound. It does not construct a decoder or imply high recovery fidelity.

### 2.3 Finite-Hamiltonian energy lemma

Suppose the retained sector has a declared finite-dimensional Hamiltonian \(H_B\) and satisfies

\[
\operatorname{Tr}(H_B\rho_B)\leq E.
\]

Let \(S_{\max}(E,H_B)\) be the maximum entropy under the energy constraint, obtained by the Gibbs variational principle. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\},
\]

and

\[
I(R:A)\geq
\max\{0,2S(R)-2S_{\max}(E,H_B)\}.
\]

The Hamiltonian and energy cap must be supplied by the physical model. They are not inferred from exterior mass, interior volume, or lifetime.

### 2.4 Operational recovery

The project distinguishes:

- mutual information;
- coherent information;
- classical Holevo information;
- environmental leakage;
- entanglement fidelity;
- worst-case or channel-wide recovery.

For a declared channel \(\mathcal N\), the executable program evaluates explicit decoders and solves

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N)
\]

through a semidefinite program over the recovery Choi matrix. A second SDP independently optimizes the fidelity of the complementary Choi state to a constant environment channel. Numerical agreement is a fixed-input information–disturbance cross-certificate.

The current certificate concerns the maximally mixed input. It is not yet a worst-case or energy-constrained diamond-norm theorem. Norm and fidelity conventions are fixed in `docs/NORM_CONVENTIONS.md`, and theorem status is controlled by `docs/THEOREM_LEDGER.md`.

---

## 3. Selected physical model tracks

### 3.1 Non-holographic geometric scaffold

The principal geometry is the Han–Rovelli–Soltani single-asymptotic-region transition model. In natural units, its effective stellar scale factor is

\[
a(T)=\left(\frac{9mT^2+Am}{2}\right)^{1/3},
\]

and its exterior function outside the tunnelling region is

\[
F(r)=1-\frac{2m}{r}+\frac{Am^2}{r^4}.
\]

For \(m^2\gg A\),

\[
r_+\simeq2m,
\qquad
r_-\simeq\left(\frac{Am}{2}\right)^{1/3}.
\]

The repository validates these formulas, horizon roots, bounce symmetry, and large-mass limits. The geometry supplies causal and metric structure but not a microscopic quantum channel.

### 3.2 White-hole remnant endpoint

The Bianchi–Christodoulou–D’Ambrosio–Haggard–Rovelli scenario is used as the first remnant-capacity case study. The initial analysis is parametric because the source model does not provide:

- a remnant Hilbert-space dimension;
- a microscopic Hamiltonian;
- a complete radiation algebra at a specified time cut;
- a unitary or CPTP channel;
- a recovery map.

The valid output is therefore one of:

1. a capacity bound under an explicit added state-space assumption;
2. a conditional recovery theorem under an explicit decoupling assumption;
3. a no-go region;
4. a rigorous underdetermination result.

### 3.3 Controlled holographic benchmark

A JT-gravity region coupled to quantum matter and a non-gravitating bath is retained as a separate reconstruction benchmark. It permits controlled study of:

- Page transitions;
- generalized entropy and islands;
- radiation-region algebras;
- code-subspace reconstruction;
- complementary decoupling and recovery error.

No JT/island conclusion is transferred to the non-holographic remnant model without an explicit map of assumptions, algebras, observables, and approximation errors.

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
- dephasing and amplitude damping;
- random isometries;
- finite-remnant channels;
- channels with equal mutual information but different recovery fidelity;
- channels with equal classical accessibility but different coherent information.

**Deliverable:** Paper 1 theorem-and-counterexample core and reproducible package.

### Objective 2 — Establish certified approximate recovery

Develop three levels of result:

1. state-specific decoupling and Uhlmann recovery existence;
2. certified maximally mixed-input recovery through SDP;
3. worst-case and energy-constrained recovery only after Bény–Oreshkov and Kretschmann–Schlingemann–Werner conventions and constants are independently rederived.

Every recovery claim must state:

- input ensemble or code;
- accessible algebra;
- norm and fidelity convention;
- whether the result is constructive or existential;
- solver or proof certificate;
- failure tolerance.

**Deliverable:** conditional recoverability theorem or precisely scoped certificate paper.

### Objective 3 — Extend capacity bounds beyond finite dimension

Use a declared Hamiltonian and energy cap to replace a bare dimension bound by a Gibbs entropy cap. Subsequent extensions will examine:

- conserved charge;
- superselection sectors;
- symmetry-covariant channels;
- energy-constrained capacities and norms.

**Deliverable:** finite-Hamiltonian lemma and, if assumptions permit, an energy-constrained recovery proposition.

### Objective 4 — Embed the results into the selected geometries

For the HRS/Bianchi track:

- validate the geometry and parameter regimes;
- define candidate slices, radiation algebras, and retained sectors;
- inventory missing state-space and coupling inputs;
- apply only those information bounds supported by declared assumptions.

For the JT-bath track:

- select one explicit setup;
- define the code subspace and radiation region;
- compare entropy transitions with decoupling and certified recovery in a finite-dimensional surrogate.

**Deliverable:** Paper 2 model-specific bound, obstruction, or underdetermination result; separate JT benchmark paper.

### Objective 5 — Maintain a feasibility-gated phenomenology program

No data search begins until the selected model supplies:

- transition or decay rate;
- emitted energy and spectrum;
- intrinsic duration and light curve;
- population and distance distribution;
- propagation and attenuation;
- detector response and backgrounds;
- a statistical detection or upper-limit plan.

The Schwarzschild time \(2GM/c^3\) remains a dimensional baseline and is never equated with an observed burst duration without a derived source mechanism.

**Deliverable:** feasibility memorandum; observational paper only if the gate passes.

---

## 5. Methodology and reproducibility

### 5.1 Analytic and adversarial validation

Every universal statement must survive explicit extremal channels and automated random tests. Similar values of one information measure will be paired with different recovery behavior to expose insufficient diagnostics.

### 5.2 Convex optimization

The recovery SDP uses an unnormalized Choi matrix \(J_{\mathcal R}\) with

\[
J_{\mathcal R}\succeq0,
\qquad
\operatorname{Tr}_{\mathrm{out}}J_{\mathcal R}=I_{\mathrm{in}}.
\]

The pinned optimization environment uses CVXPY and Clarabel. Certificates record solver status, trace-preservation residual, positivity residual, and recovery/environment formulation gap. Analytic erasure and dephasing cases serve as regression standards.

### 5.3 Energy-constrained calculations

For finite spectra, the Gibbs optimizer is solved by deterministic bisection in inverse temperature and checked against analytic two-level results, degeneracies, inactive constraints, and parameter sweeps.

### 5.4 Geometry validation

The HRS implementation is restricted to source-level formulas and natural units. Tests verify:

- time symmetry and minimum bounce radius;
- positive horizon roots;
- \(F(r_\pm)=0\);
- \(r_+\to2m\);
- \(r_-\to(Am/2)^{1/3}\).

No channel, tunnelling probability, Hawking flux, or emission spectrum is inferred from these tests.

### 5.5 Repository controls

The project maintains:

- validity, theorem, and norm ledgers;
- model cards and parameter provenance;
- deterministic random seeds;
- Python 3.11/3.12 regression CI;
- a separate pinned optimization CI job;
- generated CSV, figure, and JSON products;
- manuscript and bibliography sources.

A failed identity, solver residual, or model assumption blocks promotion of the associated claim.

---

## 6. Phenomenology gate

An observational work package must satisfy all mandatory criteria:

1. complete source model;
2. dimensional consistency;
3. detector overlap;
4. background population;
5. statistical plan;
6. data access and licensing;
7. meaningful null-result constraint.

Current PBH-to-white-hole rate calculations, including narrow FRB-compatible parameter regions, are retained as model-dependent constraints and methodology references. They do not justify a generic optical, radio, or gamma-ray search.

---

## 7. Work plan

### Year 1 — Quantum-information foundation

- Complete analytic and adversarial channel classification.
- Validate the recovery/environment SDPs.
- Reproduce worst-case information–disturbance conventions and constants.
- Complete finite-Hamiltonian, charge, and symmetry extensions.
- Draft Paper 1.

### Year 2 — Geometry and model embedding

- Complete the HRS geometry and Bianchi-remnant provenance analysis.
- Determine whether a defensible remnant Hamiltonian, entropy cap, or channel condition exists.
- Produce a model-specific bound or underdetermination theorem.
- Implement the JT-bath reconstruction benchmark.
- Draft Papers 2 and 3.

### Year 3 — Phenomenology gate and synthesis

- Evaluate whether any selected model supplies a complete signal prescription.
- If the gate passes, conduct injection–recovery and archival analysis.
- If the gate fails, publish the feasibility limit and missing-input result.
- Complete synthesis manuscript and versioned reproducibility archive.

---

## 8. Deliverables

| ID | Deliverable | Acceptance criterion |
|---|---|---|
| D1 | Validity, theorem, and norm ledgers | Every abstract-level claim has a proof, source, certificate, or blocking condition |
| D2 | Channel and adversarial test suite | Analytic cases and counterexamples pass deterministic CI |
| D3 | Certified recovery package | SDP status, residuals, analytic benchmarks, and cross-formulation gap recorded |
| D4 | Finite-Hamiltonian bound | Gibbs solver reproduces analytic spectra and declared correlation bounds |
| D5 | HRS geometry package | Metric functions, horizons, and asymptotic tests reproduced without channel overreach |
| D6 | Model cards and provenance | Supplied, free, and missing parameters explicitly separated |
| D7 | Paper 1 | Information localization, adversarial examples, and conditional recovery results |
| D8 | Paper 2 | HRS/Bianchi capacity bound, obstruction, or underdetermination theorem |
| D9 | JT benchmark paper | Code-subspace reconstruction and recovery comparison in a controlled model |
| D10 | Phenomenology memo or paper | Released only after the forward-model gate is evaluated |

---

## 9. Risk management

### No strong universal theorem

**Response:** Publish exact identities, counterexamples, finite-resource lemmas, and conditional theorems.

### No microscopic remnant channel

**Response:** Produce parameterized capacity bounds or a rigorous theorem of underdetermination. Do not fabricate Kraus operators from a causal diagram.

### SDP disagreement or poor conditioning

**Response:** Block certificate use, retain diagnostic artifacts, compare independent formulations, and seek a second solver or analytic reduction.

### Holographic results fail to transfer

**Response:** Maintain JT gravity as a separate benchmark with no automatic transfer.

### Phenomenology remains incomplete

**Response:** Publish the feasibility limit rather than performing an unsupported search.

---

## 10. Required expertise and resources

A credible team requires:

- quantum channels and approximate quantum error correction;
- convex optimization and numerical certification;
- semiclassical gravity and the selected black-to-white-hole geometry;
- holographic reconstruction for the JT benchmark;
- research software and reproducibility;
- astrophysical inference only if the phenomenology gate passes.

The baseline resource model is a principal investigator, one postdoctoral researcher or equivalent effort, modest computation, collaboration travel, and publication costs. No facility construction or custom instrumentation is assumed.

---

## 11. Publication strategy

1. **Paper 1:** information localization, finite-resource bounds, adversarial channels, and certified recovery.
2. **Paper 2:** information-capacity constraints or underdetermination in the HRS/Bianchi remnant track.
3. **Paper 3:** reconstruction and recovery diagnostics in the JT-bath benchmark.
4. **Paper 4:** phenomenology feasibility or observational search, only if authorized by the gate.
5. **Synthesis:** consequences and limits of information-recovery claims across gravitational transition models.

No manuscript is labeled theorem-ready until its statement, assumptions, convention mapping, tests, and independent review are complete.

---

## 12. Expected contribution

The project will not claim that black holes perform selective filtration or that a bounce automatically returns information uniformly. Its contribution is a rigorous hierarchy of what follows from unitarity, finite state-space resources, energy constraints, environmental decoupling, certified recovery, explicit geometry, and additional model assumptions. Where the physical model is incomplete, the project will convert that incompleteness into a precise obstruction or underdetermination result rather than an unsupported simulation.
