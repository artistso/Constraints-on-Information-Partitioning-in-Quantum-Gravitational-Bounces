# Theorem and Certificate Ledger

This ledger separates proved identities, repository-derived lemmas, imported theorems, recovery certificates, numerical diagnostics, and blocked physical claims.

## Status classes

- **PROVED-HERE:** complete derivation is contained in the repository/manuscript.
- **IMPORTED:** a primary-source theorem whose assumptions and conventions must be mapped.
- **NUMERICALLY-CERTIFIED:** convex optimization passed declared solver-status and feasibility requirements.
- **BENCHMARKED:** numerically or analytically checked but not promoted to a theorem or certificate.
- **TARGET:** scientifically meaningful but not yet established.
- **BLOCKED:** insufficient model structure to formulate the claim.

## T1 — Pure-state localization identity

For pure \(RAB\),

\[
I(R:A)+I(R:B)=2S(R).
\]

**Status:** PROVED-HERE.  
**Evidence:** entropy proof, extremal isometries, and Haar-random regression tests.  
**Scope:** kinematic; no gravitational assumptions.

## L1 — Finite-remnant correlation bound

If \(\dim B=d_B\),

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\},
\]

and for pure \(RAB\),

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

**Status:** PROVED-HERE.  
**Evidence:** entropy inequalities and random-isometry tests.  
**Scope:** correlation localization; no decoder follows by itself.

## L2 — Finite-Hamiltonian energy-constrained correlation bound

Let the retained sector have a declared finite-dimensional Hamiltonian \(H_B\) and satisfy

\[
\operatorname{Tr}(H_B\rho_B)\leq E.
\]

Let \(S_{\max}(E,H_B)\) be the Gibbs maximum entropy under the constraint. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\},
\]

and for pure \(RAB\),

\[
I(R:A)\geq
\max\{0,2S(R)-2S_{\max}(E,H_B)\}.
\]

**Status:** PROVED-HERE for finite spectra.  
**Evidence:** `src/qgbounce/energy.py`, analytic two-level tests, degeneracy tests, and deterministic sweeps.  
**Limit:** no Hamiltonian is inferred from mass, geometry, volume, or lifetime. Infinite-dimensional extensions require additional Gibbs/entropy conditions.

## T2 — State-specific decoupling-to-recovery existence

For the maximally entangled test input, if the complementary Choi state \(\rho_{RE}\) is close in purified distance to

\[
I_R/d\otimes\sigma_E,
\]

Uhlmann's theorem implies the existence of a recovery on the accessible output with corresponding maximally mixed-input entanglement fidelity.

**Status:** IMPORTED plus BENCHMARKED.  
**Evidence:** Uhlmann purification argument, fixed-\(\rho_E\) diagnostics, and environment-state optimization.  
**Limit:** fixed input; not a worst-case or diamond-norm theorem.

## C1 — Optimal maximally mixed-input recovery SDP

Compute

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N).
\]

**Status:** NUMERICALLY-CERTIFIED only after the pinned optimization CI passes.  
**Method:** unnormalized recovery Choi matrix, PSD and trace-preserving constraints, linear objective, following the SDP method of Fletcher, Shor, and Win.  
**Required evidence:** solver status `optimal`, analytic benchmark agreement, trace-preservation residual, and minimum Choi eigenvalue.

The recovery certificate does not require the independent environment formulation to have theorem-grade solver status. The environment calculation is a cross-check, not part of the primal feasibility certificate.

## D1 — Environment-side fidelity diagnostic

Compute

\[
\max_{\sigma_E}
F\!\left(
\rho_{RE}^{\mathcal N^c},
I_R/d\otimes\sigma_E
\right).
\]

**Status:** BENCHMARKED numerical diagnostic.  
**Method:** block-matrix SDP for root fidelity, followed by squaring.  
**Purpose:** independently test the fixed-input information–disturbance relation and report the cross-formulation gap.

Rank-deficient erasure cases can return `optimal_inaccurate` in the pinned open-source solvers. Such values may be plotted and stored under the declared diagnostic tolerance but are not called numerical certificates. The gap is not a solver primal–dual gap.

## T3 — Worst-case approximate-correctability duality

Optimal worst-case entanglement recovery is characterized by a complementary-channel optimization.

**Status:** IMPORTED/TARGET.  
**Primary source:** `BenyOreshkov2009`.

Missing repository work:

- worst-case input optimization;
- code/subsystem convention;
- exact fidelity/error mapping;
- theorem statement under repository notation;
- certified low-dimensional validation.

C1 and D1 do not prove T3.

## T4 — Channel-wide information–disturbance bound

A complementary channel close to a constant channel in cb/diamond norm implies recoverability of the main channel with dimension-independent continuity bounds.

**Status:** IMPORTED/TARGET.  
**Primary source:** `KretschmannEtAl2006`.

Missing repository work:

- diamond-norm SDP or certified bound;
- cb/diamond convention mapping;
- energy-constrained extension;
- constants under `docs/NORM_CONVENTIONS.md`.

## G1 — HRS geometric baseline

The HRS effective model provides the scale factor

\[
a(T)=\left(\frac{9mT^2+Am}{2}\right)^{1/3}
\]

and exterior function

\[
F(r)=1-\frac{2m}{r}+\frac{Am^2}{r^4}
\]

outside its tunnelling region, with large-mass horizon approximations

\[
r_+\simeq2m,
\qquad
r_-\simeq\left(\frac{Am}{2}\right)^{1/3}.
\]

**Status:** IMPORTED and BENCHMARKED.  
**Evidence:** primary source, root residual tests, bounce symmetry, and asymptotic sweeps.  
**Limit:** no Hawking evaporation, tunnelling probability, state space, Hamiltonian, channel, or decoder is supplied.

## T5 — HRS/Bianchi remnant capacity theorem

**Status:** BLOCKED unless additional microscopic assumptions are declared.

Missing:

- remnant Hamiltonian or effective dimension;
- microscopic channel;
- radiation algebra and time cut;
- environmental decoupling or recovery condition.

Near-term admissible outputs are L1/L2 parameterized constraints or a theorem that the desired capacity/recoverability claim is underdetermined by the geometry.

## T6 — JT-bath reconstruction benchmark

**Status:** TARGET.

Required:

- one fixed JT-bath setup and code subspace;
- radiation algebra and QES prescription;
- reconstruction theorem with error;
- finite-dimensional surrogate compared with recovery certification.

No JT result transfers to the remnant model without a complete assumption map.

## Adversarial test requirement

Every proposed scalar recovery proxy must be tested against channels exhibiting at least one of:

- equal \(I(R:A)\) but different optimal recovery fidelity;
- equal classical Holevo information but different coherent information;
- equal output entropy but different environmental leakage;
- equal remnant dimension but different recoverability.

A claim failing an adversarial comparison is downgraded or rejected in `docs/VALIDITY_LEDGER.md`.
