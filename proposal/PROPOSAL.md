# Concept Proposal v0.1

## Constraints on Information Localization and Recoverability in Quantum-Gravitational Bounce Models

**Project type:** Foundational quantum information, quantum gravity, and feasibility-gated phenomenology  
**Proposed duration:** 36 months  
**Budget status:** To be developed for a named host institution and funding call; no unsupported amount is assigned in this concept document.

---

## 1. Executive rationale

Black-to-white-hole transitions, nonsingular interiors, and long-lived remnants appear in several speculative approaches to quantum gravity. These models raise a legitimate information-theoretic question: after the transition, which external or retained subsystem permits recovery of the initial quantum state?

Earlier formulations attempted to answer this question with a universal “no-filtering theorem,” asserting that unitarity forces equal mutual information between the input and every output subsystem. That assertion is false for generic isometric channels. The present proposal begins from the correct quantum-information structure and asks a narrower, publishable question:

> Which additional physical assumptions constrain the localization and recoverability of quantum information in specified gravitational bounce models?

The project is deliberately layered. The first layer establishes model-independent channel identities, counterexamples, and recovery criteria. The second embeds those criteria into explicitly defined gravitational or holographic models. The third develops observational forecasts only for models that provide a complete forward signal model. This architecture prevents a speculative gravitational hypothesis from contaminating the mathematical and observational deliverables.

---

## 2. Corrected theoretical starting point

### 2.1 Channel definition

Let \(X\) denote the quantum system entering a transition and let \(R\) be a reference system that purifies its initial state. A complete transition is represented by an isometry

\[
V:\mathcal H_X\longrightarrow \mathcal H_A\otimes\mathcal H_B,
\]

where \(A\) and \(B\) may represent, for example, asymptotic radiation and retained interior or remnant degrees of freedom. Applying \(V\) to \(X\) gives a pure state \(\rho_{RAB}\).

For any pure tripartite state \(RAB\),

\[
I(R:A)+I(R:B)=2S(R).
\]

This follows from \(S(RA)=S(B)\) and \(S(RB)=S(A)\). It states that total correlations with the reference are conserved across the two outputs. It does **not** imply

\[
I(R:A)=I(R:B)=S(R).
\]

Indeed, the isometry \(V|\psi\rangle_X=|\psi\rangle_A|0\rangle_B\) gives \(I(R:A)=2S(R)\) and \(I(R:B)=0\). Strongly biased localization is therefore compatible with exact unitarity.

### 2.2 The actual research gap

The generic channel problem is solved only at the kinematic level: unitarity preserves information globally but permits substantial variation in where that information is recoverable. Gravity may introduce additional constraints through:

- causal accessibility of output algebras;
- energy, charge, and symmetry conservation;
- semiclassical locality and effective field theory;
- code-subspace structure in holography;
- entanglement-wedge reconstruction;
- restrictions on remnant state spaces;
- boundary conditions and asymptotic completeness;
- finite-dimensional or energy-constrained channel capacities.

The central problem is to identify which combinations of these assumptions produce nontrivial lower or upper bounds on recoverability from the radiation sector.

### 2.3 Scope of claims

The project will distinguish four kinds of result:

1. **Identity:** true for every channel or pure state under stated mathematical conditions.
2. **Conditional theorem:** true only when explicit physical assumptions are imposed.
3. **Counterexample:** a channel or geometry demonstrating that a proposed universal statement is false.
4. **Model constraint:** a result applying to one defined bounce geometry, boundary condition, or emission prescription.

No claim will be promoted across these categories without proof.

---

## 3. Research objectives

### Objective 1 — Classify information localization in bipartite output channels

Develop a rigorous taxonomy for channels \(X\rightarrow AB\), using a purifying reference \(R\). The analysis will quantify:

- mutual information \(I(R:A)\) and \(I(R:B)\);
- coherent information and quantum capacity bounds;
- conditional mutual information;
- entanglement fidelity and approximate recoverability;
- trace-distance and purified-distance decoupling criteria;
- explicit recovery maps;
- effects of conserved quantities and superselection sectors.

The aim is not to prove equal partitioning. It is to determine the feasible region of information-localization measures and identify assumptions that shrink that region.

**Primary deliverable:** A theorem-and-counterexample paper with reproducible symbolic and numerical checks.

### Objective 2 — Derive conditional recoverability bounds

Formulate propositions of the following type:

> If the global transition is isometric, the radiation algebra satisfies specified accessibility and reconstruction assumptions, the retained sector obeys a stated dimensional or energy constraint, and the final state satisfies a defined decoupling condition, then the input is approximately recoverable from radiation with an explicit error bound.

Candidate tools include one-shot decoupling, Fawzi–Renner-type recoverability bounds, operator-algebra quantum error correction, complementary recovery, and energy-constrained channel norms.

Every theorem will include:

- a complete list of assumptions;
- a proof or machine-checkable derivation where practical;
- a saturating example or counterexample;
- a statement of whether the result is kinematic, holographic, or model-specific.

**Primary deliverable:** A conditional recoverability theorem suitable for a quantum-information or quantum-gravity journal.

### Objective 3 — Evaluate selected gravitational model classes

The project will not treat “a bounce” as a single universal process. Two or three model classes will be selected according to literature maturity and calculational tractability, potentially including:

- black-to-white-hole tunneling geometries;
- effective loop-quantum-gravity-inspired nonsingular interiors;
- white-hole remnant models;
- low-dimensional holographic evaporation models used strictly as controlled toy systems.

For each model, the analysis will specify:

1. spacetime asymptotics and causal diagram;
2. Hilbert-space or algebraic subsystem definitions;
3. whether a boundary dual exists;
4. the treatment of Hawking radiation and backreaction;
5. the status of remnants or baby-universe sectors;
6. the lifetime and transition law;
7. the domain in which semiclassical reasoning is trusted;
8. the observable or reconstructable quantity being calculated.

AdS/CFT will not be invoked as a generic proof mechanism for asymptotically flat loop-inspired models. Holographic results will be clearly labeled as conditional benchmarks within models where the dual description is defined.

**Primary deliverable:** One model-specific analysis establishing either a recoverability bound, a counterexample, or a precise obstruction.

### Objective 4 — Build a feasibility-gated phenomenology program

Observational work is scientifically independent of the information-localization theorem. It will proceed only after selecting a model with an explicit forward prescription for:

- transition or decay rate as a function of mass and model parameters;
- emitted energy and spectrum;
- intrinsic duration and time profile;
- cosmological source distribution;
- propagation and attenuation;
- detector response and selection effects.

The Schwarzschild light-crossing time

\[
2GM/c^3
\]

will be used only for dimensional checks. It will not be equated with a detectable burst duration without a model-derived mechanism connecting the two.

Potential channels include optical, ultraviolet, gamma-ray, radio, astrometric, or gravitational signatures. A channel enters the analysis only if the model predicts a measurable observable and the forecast survives order-of-magnitude verification.

**Stage-gate deliverable:** A phenomenology feasibility memorandum. A search paper is authorized only if the model passes the gate defined in Section 5.4.

### Objective 5 — Establish reproducibility and publication infrastructure

All central claims will be linked to one of:

- an analytic derivation;
- a symbolic notebook;
- a numerical notebook with unit tests;
- a cited primary source;
- a documented model assumption.

The repository will maintain a validity ledger, dimension-check tests, parameter provenance, manuscript source, and release checklist.

---

## 4. Methodology

### 4.1 Quantum-channel analysis

The first work package will construct parameterized channel families and compute the localization vector

\[
\mathcal L(V,\rho_{RX})=
\bigl(I(R:A), I(R:B), I_c(R\rangle A), I_c(R\rangle B), F_A, F_B\bigr),
\]

where \(F_A\) and \(F_B\) are optimal entanglement-recovery fidelities. Canonical examples will include:

- identity-to-one-port channels;
- erasure channels and complementary channels;
- random isometries;
- symmetry-constrained channels;
- channels with finite remnant dimension;
- approximate cloning and secret-sharing constructions;
- channels induced by tracing inaccessible environments.

The resulting feasible regions will separate conservation of global information from local reconstructability.

### 4.2 Recoverability and decoupling

Approximate recovery from \(A\) is equivalent, under appropriate purification conditions, to approximate decoupling of \(R\) from the complementary sector \(B\). The project will express this relation using operational distances and recovery errors rather than informal statements that information has “escaped.” Bounds will be reported with norm choice, dimensional dependence, and energy assumptions explicit.

### 4.3 Holographic benchmark

In controlled holographic evaporation models, the project will compare:

- entropy of radiation regions;
- entanglement-wedge transitions;
- reconstruction of a specified code subspace;
- state dependence and approximation error;
- partition of the radiation into operationally accessible subregions.

The Page curve constrains the fine-grained entropy of a selected radiation region. It does not by itself imply uniform distribution across every output channel. The analysis will therefore calculate recoverability for defined boundary regions rather than infer it from purity alone.

### 4.4 Bounce-model case studies

Each selected model will receive a structured “model card” containing equations, assumptions, parameter ranges, and unresolved consistency issues. The channel map will be derived only to the level justified by the model. Where the microscopic map is unavailable, the output will be a bound on admissible channels rather than a fabricated process matrix.

### 4.5 Phenomenology gate

A proposed observational analysis must satisfy all of the following before data mining begins:

1. **Model completeness:** spectrum, duration, energy, rate, and parameter priors are specified.
2. **Dimensional consistency:** every characteristic scale passes automated unit tests.
3. **Detectability:** expected flux or strain overlaps a real instrument response for a non-negligible parameter region.
4. **Background model:** dominant astrophysical contaminants are identified.
5. **Statistical plan:** detection statistic, trials factor, efficiency, and upper-limit method are defined.
6. **Data access:** the required archive or broker stream is available under documented terms.
7. **Null value:** a nondetection yields a meaningful parameter-space constraint.

Failure of any mandatory criterion returns the work package to model development rather than producing an overstated forecast.

---

## 5. Work plan

### Year 1 — Foundations and theorem design

- Complete the validity audit of prior material.
- Formalize the reference-system channel framework.
- Produce analytic counterexamples to universal partition claims.
- Build symbolic notebooks for entropy identities and recovery metrics.
- Select gravitational model classes using explicit inclusion criteria.
- Draft Paper 1: quantum-information framework and conditional theorem candidates.

### Year 2 — Gravitational embedding and model analysis

- Construct model cards and causal/subsystem definitions.
- Analyze one holographic benchmark and one non-holographic bounce model.
- Determine which recoverability statements survive model embedding.
- Release numerical tests and parameter scans.
- Draft Paper 2: model-specific recoverability or obstruction result.

### Year 3 — Phenomenology gate and synthesis

- Complete the signal-model feasibility assessment.
- If the gate passes, perform injection–recovery simulations and an archival or broker-based search.
- If the gate fails, publish the exclusion of the proposed observational strategy and identify the missing theoretical ingredients.
- Integrate the mathematical and gravitational results into a synthesis manuscript.
- Archive a versioned release with reproducibility materials.

---

## 6. Deliverables

| ID | Deliverable | Acceptance criterion |
|---|---|---|
| D1 | Validity ledger | Every inherited claim classified and linked to evidence or rejection |
| D2 | QIT notebook suite | Reproduces all entropy identities and counterexamples |
| D3 | Conditional theorem manuscript | Assumptions, proof, error bound, and saturating example included |
| D4 | Gravitational model cards | Causal structure, subsystem definitions, equations, and limitations explicit |
| D5 | Model-specific paper | Contains a derived bound, counterexample, or obstruction—not analogy |
| D6 | Phenomenology feasibility memo | Pass/fail decision supported by forward modeling and unit tests |
| D7 | Optional search paper | Released only after the feasibility gate passes |
| D8 | Final synthesis | Publication-ready manuscript and archived reproducibility package |

---

## 7. Risk management

### Risk: no nontrivial universal theorem exists

**Response:** This is expected. The project targets conditional theorems and counterexamples, both of which are publishable when the assumptions are physically meaningful.

### Risk: selected bounce models lack a microscopic channel

**Response:** Derive bounds on admissible channels from the available geometry and state explicitly what cannot be calculated. Do not infer microscopic dynamics from a causal diagram alone.

### Risk: holographic conclusions do not transfer to the selected model

**Response:** Maintain holography as a separate benchmark. No transfer is made without an explicit duality argument.

### Risk: phenomenological predictions are too model-dependent or too faint

**Response:** The feasibility gate converts this into a documented negative result rather than an unproductive data search.

### Risk: analogue experiments invite overinterpretation

**Response:** Keep them outside the core milestones. Any later analogue work tests reconstruction protocols or mode-conversion channels only.

---

## 8. Required expertise and resources

A credible team would include:

- quantum information theory and quantum channels;
- semiclassical gravity or holography;
- expertise in the selected loop-inspired or black-to-white-hole model;
- time-domain or high-energy astrophysical inference if the phenomenology gate passes;
- research software and reproducibility support.

The baseline resource model is one principal investigator, one postdoctoral researcher or equivalent research effort, modest computing for symbolic/numerical work, collaboration travel, and publication costs. No facility construction or custom instrumentation is assumed.

---

## 9. Publication strategy

The minimum viable publication sequence is:

1. **Quantum-information foundations:** exact identities, counterexamples, and conditional recoverability bounds.
2. **Gravitational case study:** application to a specified bounce or holographic model.
3. **Phenomenology feasibility or search:** released only after the signal model passes the gate.
4. **Synthesis/review:** information localization across unitary gravitational transition models.

A preprint will not be labeled a theorem paper until the central statement has survived independent technical review, automated checks, and explicit counterexample testing.

---

## 10. Expected contribution

The likely contribution is not evidence that black holes perform selective filtration. It is a rigorous map of what unitarity does and does not imply about information localization, together with model-specific conditions under which radiation recovery can be established or ruled out. That result would clarify the relationship among quantum channels, remnants, Page-curve reasoning, and gravitational reconstruction while creating a defensible route to phenomenology only where the underlying model supports it.
