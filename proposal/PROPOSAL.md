# Concept Proposal v0.5

## Constraints on Information Localization and Recoverability in Quantum-Gravitational Bounce Models

**Project type:** Foundational quantum information, effective quantum gravity, and feasibility-gated phenomenology  
**Proposed duration:** 36 months  
**Budget status:** To be developed for a named host institution and funding call; no unsupported amount is assigned.

---

## 1. Executive rationale

Black-to-white-hole transitions, nonsingular interiors, and long-lived remnants raise an operational question: after a proposed quantum-gravitational transition, which observer-accessible algebra permits recovery of information about the initial quantum state?

Generic unitary or isometric evolution preserves the complete state but does not determine how correlations are localized among radiation, retained degrees of freedom, and inaccessible sectors. The corrected research question is:

> Which explicit physical assumptions constrain information localization and support a quantified recovery statement in a specified gravitational model?

The program has four layers:

1. exact channel identities, counterexamples, and adversarial tests;
2. finite-resource bounds and scoped recovery certification;
3. explicit geometric and holographic model embeddings;
4. observational work only after a complete forward signal model passes a predefined gate.

Public language is controlled by `docs/CANONICAL_CLAIMS.md`, `docs/VALIDITY_LEDGER.md`, `docs/THEOREM_LEDGER.md`, `docs/NORM_CONVENTIONS.md`, and `docs/DIAMOND_NORM_CERTIFICATE_POLICY.md`.

---

## 2. Established mathematical foundation

### 2.1 Reference-assisted formulation

Let \(X\) be the input and let \(R\) purify its initial state. A bipartite isometric output is represented by

\[
V:\mathcal H_X\longrightarrow\mathcal H_A\otimes\mathcal H_B,
\]

where \(A\) is a declared accessible sector and \(B\) is a declared retained sector. For the resulting pure state \(\rho_{RAB}\),

\[
I(R:A)+I(R:B)=2S(R).
\]

This identity permits maximally asymmetric localization. The isometry

\[
V_A|\psi\rangle_X=|\psi\rangle_A|0\rangle_B
\]

gives

\[
I(R:A)=2S(R),
\qquad
I(R:B)=0,
\]

while the reversed one-port isometry produces the opposite localization. Global unitarity therefore does not determine equal partitioning or radiation recovery.

### 2.2 Finite retained dimension

If \(\dim B=d_B\),

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\},
\]

and, for pure \(RAB\),

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

This constrains correlation storage. It does not construct a decoder.

### 2.3 Finite Hamiltonian and energy cap

For a declared finite-dimensional Hamiltonian \(H_B\) satisfying

\[
\operatorname{Tr}(H_B\rho_B)\leq E,
\]

let \(S_{\max}(E,H_B)\) be the Gibbs maximum entropy. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\},
\]

with the corresponding radiation lower bound for pure \(RAB\).

The Hamiltonian and energy cap are physical inputs. Exterior mass, interior volume, area, and lifetime do not determine them without an independent microscopic derivation.

### 2.4 Charge-sector and superselection bound

For

\[
\mathcal H_B=\bigoplus_q\mathcal H_q,
\qquad
\rho_B=\bigoplus_qp_q\rho_q,
\qquad
d_q=\dim\mathcal H_q,
\]

one has

\[
S(B)=H(p)+\sum_qp_qS(\rho_q)
\leq
H(p)+\sum_qp_q\log_2d_q.
\]

Therefore

\[
I(R:B)
\leq
2\min\left\{S(R),H(p)+\sum_qp_q\log_2d_q\right\}.
\]

The symmetry, block-diagonality condition, sector dimensions, and sector distribution must be supplied by the physical model. An unconstrained distribution recovers the ordinary total-dimension bound.

---

## 3. Recovery hierarchy

### 3.1 Fixed-input entanglement-fidelity certificate

For a declared finite-dimensional channel \(\mathcal N\), the repository solves

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N)
\]

for the maximally mixed input. The recovery Choi matrix is constrained to be positive semidefinite and trace preserving. Analytic erasure and dephasing standards, positivity residuals, trace-preservation residuals, and solver status control certificate language.

An independent complementary-state fidelity program is retained as a state-specific diagnostic. It is not a channel-wide norm calculation.

### 3.2 Finite-dimensional channel-wide diamond recovery

For \(\mathcal N:X\to A\), the new v0.5 layer solves

\[
\delta_{\mathrm{rec}}
=
\inf_{\mathcal R:A\to X\ \mathrm{CPTP}}
\|\mathcal R\circ\mathcal N-\operatorname{id}_X\|_\diamond.
\]

Using unnormalized Choi matrices in input-output order, the recovery variable and the diamond-norm dual are optimized jointly in one convex program.

For a declared complement \(\mathcal N^c:X\to E\), it also solves

\[
\delta_{\mathrm{env}}
=
\inf_{\sigma_E}
\|\mathcal N^c-\mathcal C_\sigma\|_\diamond,
\]

where

\[
\mathcal C_\sigma(\rho)=\operatorname{Tr}(\rho)\sigma_E.
\]

The constant state, dual matrix, and norm bound are optimized jointly.

### 3.3 KSW implementation and scope

Under the mapped convention,

\[
\frac14\delta_{\mathrm{rec}}^2
\leq
\delta_{\mathrm{env}}
\leq
2\sqrt{\delta_{\mathrm{rec}}}.
\]

The KSW theorem is imported from the primary literature. The repository now computes both finite-dimensional quantities and verifies the inequality on deterministic dephasing families. This validates conventions and implementation; it is not a new proof of the theorem.

The pinned checkpoint reports:

- 30 passing optimization tests;
- dephasing identity-distance analytic error below \(6.3\times10^{-9}\);
- dephasing optimal-recovery analytic error below \(2.1\times10^{-8}\);
- KSW lower margin consistent with floating-point zero;
- positive KSW upper margins across the sweep;
- analytic qubit depolarizing and constant-channel standards reproduced.

### 3.4 Bény--Oreshkov target

The Bény--Oreshkov worst-case entanglement-fidelity duality is imported and convention-mapped, but its fidelity minimax remains unimplemented. It is operationally distinct from both the maximally mixed-input fidelity program and the channel-wide diamond program.

### 3.5 Blocked norm extensions

The current executable results do not establish:

- an energy-constrained diamond norm;
- an infinite-dimensional channel norm;
- a symmetry-restricted norm theorem;
- a computational-complexity guarantee;
- a gravitational derivation of the optimized channel.

Every recovery claim must state the input ensemble or channel scope, accessible algebra, norm and fidelity convention, constructive or existential status, proof or solver certificate, numerical tolerance, and failure policy.

---

## 4. Research objectives

### Objective 1 — Complete the model-independent channel classification

Consolidate the exact reference-assisted identity, extremal counterexamples, finite-resource lemmas, open-channel diagnostics, and adversarial channel pairs into a theorem-and-counterexample manuscript.

**Deliverable:** Paper 1A on information localization and finite-resource constraints.

### Objective 2 — Complete the recovery hierarchy

Maintain the separation among:

- maximally mixed-input entanglement fidelity;
- Bény--Oreshkov worst-case entanglement fidelity;
- channel-wide diamond recovery error;
- complementary leakage in diamond norm.

Implement the remaining Bény--Oreshkov fidelity minimax, compare all recovery metrics on adversarial channels, and obtain independent QIT review.

**Deliverable:** Paper 1B on fixed-input and channel-wide recoverability.

### Objective 3 — Extend resource and norm constraints

Extend the finite-dimensional, finite-Hamiltonian, and sector lemmas to physically declared conserved charges, symmetry-covariant channels, and energy-constrained channel norms.

No resource constraint is inferred from geometry unless the model supplies the relevant operator and state-space structure.

### Objective 4 — Produce a model-specific HRS/Bianchi result

Validate the geometry and parameter regimes, define candidate slices and observer algebras, inventory supplied and missing microscopic inputs, and determine whether the strongest defensible result is a capacity bound, excluded region, microscopic completion, or theorem of underdetermination.

The diamond optimizer may evaluate explicitly declared channel families but cannot select a channel from geometry.

**Deliverable:** Paper 2.

### Objective 5 — Implement one explicit JT-bath benchmark

Select one published setup, define the code subspace and radiation region, reproduce the relevant generalized-entropy transition, map the reconstruction theorem and approximation error, and compare the gravitational criterion with finite-dimensional decoupling, fixed-input fidelity, and diamond recovery diagnostics.

**Deliverable:** Paper 3.

### Objective 6 — Maintain a feasibility-gated phenomenology program

No observational search begins until a selected source model supplies a transition or decay rate, emitted energy and spectrum, intrinsic duration and light curve, source population, propagation model, detector response, backgrounds, and a statistical detection or upper-limit plan.

The Schwarzschild time \(2GM/c^3\) is used only as a dimensional baseline. It is not identified with an observed transient duration without a derived source mechanism.

**Deliverable:** A feasibility memorandum; an observational paper only when every mandatory gate passes.

---

## 5. Methodology and reproducibility

### 5.1 Analytic and adversarial validation

Every universal statement is tested against extremal channels and deterministic random ensembles. Single-number diagnostics are challenged using channel pairs with similar scalar values but different operational behavior.

### 5.2 Fixed-input convex optimization

The fidelity recovery SDP uses an unnormalized Choi matrix \(J_{\mathcal R}\) with

\[
J_{\mathcal R}\succeq0,
\qquad
\operatorname{Tr}_{\mathrm{out}}J_{\mathcal R}=I_{\mathrm{in}}.
\]

Values with unacceptable feasibility residuals or solver status are retained only as diagnostics.

### 5.3 Diamond-norm convex optimization

For a Hermiticity-preserving map \(\Phi\), the finite-dimensional dual minimizes \(\mu\) subject to

\[
Z\pm J(\Phi)\succeq0,
\qquad
\operatorname{Tr}_{\mathrm{out}}Z\preceq\mu I_{\mathrm{in}}.
\]

The channel distance is unhalved and lies in \([0,2]\). SCS is the current certificate solver. `optimal` status and accepted PSD, partial-trace, trace-preservation, and analytic-objective residuals are required.

### 5.4 Energy and symmetry calculations

For finite spectra, the Gibbs optimizer is solved deterministically and checked against analytic two-level examples, degeneracies, inactive constraints, and parameter sweeps. Sector calculations are checked against fixed-sector, mixed-sector, and unconstrained-distribution limits.

### 5.5 Geometry validation

The HRS implementation is restricted to source-level formulas and natural units. No microscopic channel, tunnelling probability, Hawking flux, emission spectrum, or detector signature is inferred from the geometric tests.

### 5.6 Claim-language validation

`scripts/check_claim_language.py` scans the public-facing README, abstract, proposal, and manuscript for known false or overstated formulations. A violation fails CI and blocks claim promotion.

### 5.7 Repository controls

The project maintains canonical-claim, validity, theorem, norm, and diamond-certificate ledgers; model cards and parameter provenance; deterministic random seeds; Python 3.11/3.12 regression CI; pinned optimization CI; generated data products; and manuscript and bibliography sources.

---

## 6. Explicit nonclaims

This proposal does not assert that:

- global unitarity determines equal output localization;
- an entropy curve supplies an operational decoder;
- a loop-inspired effective model is the consensus prediction of quantum gravity;
- a metric determines information capacity or microscopic dynamics;
- a remnant can or cannot store the input without a state-space assumption;
- a finite-dimensional optimizer derives the HRS/Bianchi channel;
- a diamond certificate automatically extends to energy-constrained or infinite-dimensional systems;
- numerical KSW checks replace the imported theorem;
- a broad primordial-black-hole mass interval produces present-day observable events;
- any named instrument supplies a viable search before the forward-model gate passes;
- analogy provides mathematical or observational evidence.

---

## 7. Work plan

### Year 1 — Quantum-information foundation

- Consolidate exact identities, resource lemmas, and adversarial channel classification.
- Archive fixed-input and finite-dimensional diamond certificates.
- Implement the Bény--Oreshkov worst-case fidelity minimax.
- Compare fixed-input fidelity, worst-case fidelity, and diamond error.
- Complete independent QIT review.
- Draft Papers 1A and 1B.

### Year 2 — Geometry and model embedding

- Complete HRS geometry and Bianchi-remnant provenance analysis.
- Determine whether a defensible remnant Hamiltonian, sector model, entropy cap, or channel condition exists.
- Produce a model-specific bound, excluded region, microscopic completion, or underdetermination result.
- Implement the source-complete JT-bath benchmark.
- Draft Papers 2 and 3.

### Year 3 — Feasibility gate and synthesis

- Evaluate whether any selected model supplies a complete signal prescription.
- When the gate passes, conduct injection--recovery and archival analysis.
- When the gate fails, publish the feasibility limit and missing-input result.
- Complete a synthesis manuscript and versioned reproducibility archive.

---

## 8. Deliverables

| ID | Deliverable | Acceptance criterion |
|---|---|---|
| D1 | Canonical claim, validity, theorem, norm, and diamond ledgers | Every public claim has a proof, source, certificate, condition, or block |
| D2 | Channel and adversarial test suite | Analytic cases and counterexamples pass deterministic CI |
| D3 | Fixed-input recovery certificates | Solver status and feasibility residuals satisfy policy |
| D4 | Finite-dimensional diamond certificates | Recovery, complement, analytic, and KSW margin checks pass |
| D5 | Worst-case fidelity implementation | Bény--Oreshkov objective, code convention, and low-dimensional checks complete |
| D6 | Finite-resource results | Dimension, Hamiltonian, charge, and symmetry assumptions explicit |
| D7 | HRS geometry package | Source equations, roots, limits, and units reproduced |
| D8 | Model cards and provenance | Supplied, free, and missing parameters separated |
| D9 | Paper 1A | Information localization, adversarial examples, and finite resources |
| D10 | Paper 1B | Fixed-input, worst-case, and diamond recovery hierarchy |
| D11 | Paper 2 | HRS/Bianchi capacity bound, excluded region, completion, or underdetermination theorem |
| D12 | JT benchmark paper | Declared code subspace, radiation region, and recovery comparison |
| D13 | Phenomenology memorandum or paper | Released only after the forward-model gate is evaluated |

---

## 9. Risk management

- **No strong universal gravitational theorem:** publish exact channel identities, counterexamples, finite-resource lemmas, and conditional results.
- **No microscopic remnant channel:** produce parameterized bounds or a theorem of underdetermination.
- **Worst-case fidelity minimax remains difficult:** publish the completed diamond hierarchy while retaining the target transparently.
- **Numerical conditioning:** block certificate use and retain diagnostic artifacts.
- **Holographic results do not transfer:** maintain JT gravity as a separate benchmark.
- **Phenomenology remains incomplete:** publish the feasibility limit rather than performing an unsupported search.

---

## 10. Required expertise and resources

A credible team requires quantum channels and approximate quantum error correction, semidefinite programming and numerical certification, semiclassical gravity and the selected effective geometry, holographic reconstruction for the JT benchmark, research software and reproducibility, and astrophysical inference only when the phenomenology gate passes.

The baseline resource model is a principal investigator, one postdoctoral researcher or equivalent effort, modest computation, collaboration travel, and publication costs. No facility construction or custom instrumentation is assumed.

---

## 11. Publication strategy

1. **Paper 1A:** information localization, finite-resource bounds, and adversarial channels.
2. **Paper 1B:** fixed-input fidelity, channel-wide diamond recovery, KSW implementation, and worst-case fidelity comparison.
3. **Paper 2:** information-capacity constraints, excluded regions, or underdetermination in the HRS/Bianchi track.
4. **Paper 3:** reconstruction and recovery diagnostics in the JT-bath benchmark.
5. **Paper 4:** phenomenology feasibility or observational analysis, only when authorized by the gate.
6. **Synthesis:** consequences and limits of information-recovery claims across gravitational transition models.

No manuscript is labeled theorem-ready until its statement, assumptions, convention mapping, tests, artifacts, and independent review are complete.

---

## 12. Expected contribution

The project will produce a rigorous hierarchy of what follows from quantum-channel kinematics, finite state-space resources, energy and symmetry constraints, fixed-input recovery, channel-wide diamond optimization, effective geometry, and additional model assumptions. Where a physical model is incomplete, that incompleteness will be converted into a precise obstruction or theorem of underdetermination rather than an unsupported simulation or forecast.
