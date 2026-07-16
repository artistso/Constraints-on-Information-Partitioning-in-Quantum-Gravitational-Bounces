# Theorem and Certificate Ledger

This ledger separates proved identities, repository-derived lemmas, imported theorems, numerical certificates, and unresolved targets.

## Status classes

- **PROVED-HERE:** complete derivation is contained in the manuscript/repository.
- **IMPORTED:** theorem is taken from a primary source; assumptions and convention mapping must be recorded.
- **NUMERICALLY-CERTIFIED:** finite-dimensional convex optimization has passed declared residual tests.
- **BENCHMARKED:** tested on analytic examples but not promoted to a theorem.
- **TARGET:** scientifically meaningful but not yet established.
- **BLOCKED:** insufficient model structure to formulate the claim.

## T1 — Pure-state localization identity

**Statement.** For pure \(RAB\),

\[
I(R:A)+I(R:B)=2S(R).
\]

**Status:** PROVED-HERE.

**Evidence:** entropy proof, extremal isometries, and Haar-random regression tests.

**Scope:** kinematic; no gravity assumptions.

## L1 — Finite-remnant correlation bound

**Statement.** If \(\dim B=d_B\), then

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\},
\]

and for pure \(RAB\),

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

**Status:** PROVED-HERE.

**Evidence:** entropy inequalities plus random-isometry tests.

**Scope:** correlation localization only. No decoder follows from this lemma alone.

## L2 — Finite-Hamiltonian energy-constrained correlation bound

**Statement.** Let the retained sector have a declared finite-dimensional Hamiltonian \(H_B\) and satisfy

\[
\operatorname{Tr}(H_B\rho_B)\leq E.
\]

Let \(S_{\max}(E,H_B)\) be the maximum entropy under that constraint, obtained by the Gibbs variational principle. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\},
\]

and for pure \(RAB\),

\[
I(R:A)\geq
\max\{0,2S(R)-2S_{\max}(E,H_B)\}.
\]

**Status:** PROVED-HERE for finite spectra.

**Evidence:** `src/qgbounce/energy.py`; two-level analytic tests, degeneracy tests, and deterministic parameter sweeps.

**Limit:** this does not infer \(H_B\) from mass, geometry, volume, or lifetime. Infinite-dimensional extensions require Gibbs and finite-entropy conditions.

## T2 — State-specific decoupling-to-recovery existence

**Statement.** For the maximally entangled test input, if the complementary Choi state \(\rho_{RE}\) is close in purified distance to

\[
I_R/d\otimes\sigma_E,
\]

then Uhlmann’s theorem implies the existence of a recovery map on the accessible output whose maximally mixed-input entanglement fidelity is at least the corresponding squared fidelity.

**Status:** IMPORTED plus BENCHMARKED.

**Evidence:** Uhlmann purification argument, implemented fixed-\(\rho_E\) diagnostic, and independent environment-state SDP.

**Limit:** state-specific average entanglement transmission; not a worst-case or diamond-norm statement.

## C1 — Optimal maximally mixed-input recovery SDP

**Problem.** Compute

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N).
\]

**Status:** NUMERICALLY-CERTIFIED when CI passes.

**Method:** unnormalized recovery Choi matrix, positive-semidefinite and trace-preserving constraints, linear objective. Based on the semidefinite-program recovery method of Fletcher, Shor, and Win.

**Required certificate:** solver status, CPTP residuals, minimum eigenvalue, analytic-example agreement, and environment-formulation gap.

## C2 — Environment-side fidelity cross-certificate

**Problem.** Compute

\[
\max_{\sigma_E}
F\!\left(
\rho_{RE}^{\mathcal N^c},
I_R/d\otimes\sigma_E
\right).
\]

**Status:** NUMERICALLY-CERTIFIED when CI passes.

**Method:** block-matrix SDP for root fidelity, followed by squaring.

**Purpose:** independent implementation of the fixed-input information–disturbance duality. Agreement with C1 is a cross-certificate, not the solver’s internal primal–dual gap.

## T3 — Worst-case approximate correctability duality

**Statement target.** Optimal worst-case entanglement recovery is characterized by a dual optimization on the complementary channel.

**Status:** IMPORTED/TARGET.

**Primary source:** Bény and Oreshkov, `BenyOreshkov2009`.

**Missing repository work:**

- worst-case input optimization;
- code/subsystem convention;
- exact mapping of fidelity/error definitions;
- theorem proof under repository notation;
- certified low-dimensional validation.

No manuscript claim may cite C1/C2 as a proof of T3.

## T4 — Channel-wide information–disturbance bound

**Statement target.** A complementary channel close to a constant channel in cb/diamond norm implies recoverability of the main channel, with dimension-independent continuity bounds.

**Status:** IMPORTED/TARGET.

**Primary source:** Kretschmann, Schlingemann, and Werner, `KretschmannEtAl2006`.

**Missing repository work:**

- diamond-norm SDP or certified bound;
- convention mapping for cb versus diamond norm;
- energy-constrained extension;
- explicit constants under `docs/NORM_CONVENTIONS.md`.

## T5 — Gravitational remnant recoverability theorem

**Status:** BLOCKED.

A named geometry does not yet supply:

- a microscopic channel;
- a remnant Hamiltonian or effective state-space dimension;
- a radiation coupling and time cut;
- a decoder or environmental decoupling condition.

The valid near-term outputs are parametric L1/L2 constraints or a theorem of underdetermination.

## T6 — JT-bath reconstruction benchmark

**Status:** TARGET.

Required:

- specified JT-bath setup and code subspace;
- declared radiation algebra and Page/QES prescription;
- reconstruction theorem with error;
- finite-dimensional surrogate whose recovery certificate is compared with the gravitational entropy calculation.

No result from this benchmark transfers to the remnant model without a complete assumption map.

## Adversarial test requirement

Every proposed single-number recovery diagnostic must be tested against channels exhibiting at least one of:

- equal \(I(R:A)\) but different optimal recovery fidelity;
- equal classical Holevo information but different coherent information;
- equal output entropy but different environmental leakage;
- equal remnant dimension but different recoverability.

A claim failing an adversarial comparison is downgraded or rejected in `docs/VALIDITY_LEDGER.md`.
