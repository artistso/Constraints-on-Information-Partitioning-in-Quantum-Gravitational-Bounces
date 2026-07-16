# Theorem and Certificate Ledger

This ledger separates proved identities, repository-derived lemmas, imported theorems, recovery certificates, numerical diagnostics, and blocked physical claims.

## Status classes

- **PROVED-HERE:** complete derivation is contained in the repository/manuscript.
- **IMPORTED:** a primary-source theorem whose assumptions and conventions are mapped.
- **NUMERICALLY-CERTIFIED:** convex optimization passed declared solver-status and feasibility requirements.
- **BENCHMARKED:** numerically or analytically checked but not promoted to a theorem or certificate.
- **TARGET:** scientifically meaningful but not yet established or implemented.
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

## L3 — Charge-sector and superselection correlation bound

Let

\[
\mathcal H_B=\bigoplus_q\mathcal H_q,
\qquad
\rho_B=\bigoplus_qp_q\rho_q,
\qquad
d_q=\dim\mathcal H_q.
\]

Then

\[
S(B)=H(p)+\sum_qp_qS(\rho_q)
\leq
H(p)+\sum_qp_q\log_2d_q.
\]

Therefore

\[
I(R:B)
\leq
2\min\left\{S(R),H(p)+\sum_qp_q\log_2d_q\right\},
\]

with the corresponding radiation lower bound for pure \(RAB\).

**Status:** PROVED-HERE for finite direct-sum sectors.  
**Evidence:** entropy decomposition, `src/qgbounce/symmetry.py`, regression tests, and deterministic sweeps.  
**Limit:** the symmetry, sector dimensions, block-diagonality, and sector probabilities must be physically supplied. If the distribution is unconstrained, the maximum reduces to the total-dimension bound.

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

## T3 — Bény--Oreshkov worst-case approximate-correctability duality

For channels \(\mathcal N,\mathcal M\) and declared complementary channels,

\[
\max_{\mathcal R}
F_{\mathrm{wc}}(\mathcal R\mathcal N,\mathcal M)
=
\max_{\mathcal R'}
F_{\mathrm{wc}}(\widehat{\mathcal N},\mathcal R'\widehat{\mathcal M}).
\]

For \(\mathcal M=\operatorname{id}\), the dual target is a constant complementary channel.

**Status:** IMPORTED and convention-mapped.  
**Primary source:** `BenyOreshkov2009`.  
**Repository mapping:** `docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`.

Missing executable work:

- worst-case input optimization;
- declared code/subsystem/algebra convention;
- certified low-dimensional validation;
- comparison with C1 and D1.

C1 and D1 do not implement T3.

## T4 — KSW channel-wide information–disturbance bound

In repository Schrödinger-picture notation, let

\[
\delta_{\mathrm{rec}}
=
\inf_{\mathcal R}
\|\mathcal R\circ\mathcal N-\operatorname{id}\|_\diamond
\]

and

\[
\delta_{\mathrm{env}}
=
\|\mathcal N^c-\mathcal C_\sigma\|_\diamond
\]

for the constant channel paired with the chosen dilation. The KSW bound maps to

\[
\frac14\delta_{\mathrm{rec}}^2
\leq
\delta_{\mathrm{env}}
\leq
2\sqrt{\delta_{\mathrm{rec}}}.
\]

**Status:** IMPORTED and convention-mapped.  
**Primary source:** `KretschmannEtAl2006`.  
**Repository mapping:** `docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`.

Missing executable work:

- diamond-norm SDP or certified bound;
- optimization over the constant environment state where required;
- identity, erasure, and depolarizing regression cases;
- energy-constrained extension.

No current Choi-state distance implements T4.

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

## G2 — Geometry-only channel underdetermination

If a geometric descriptor supplies no rule selecting quantum state spaces and a microscopic channel, information localization and recovery are not identifiable from that descriptor alone.

**Status:** PROVED-HERE as a model-identifiability proposition.  
**Evidence:** `docs/HRS_BIANCHI_UNDERDETERMINATION.md` and explicit one-port isometries with incompatible radiation recovery.  
**Scope:** the proposition diagnoses missing model structure; it does not assert that a microscopic completion is impossible.

## T5 — HRS/Bianchi remnant capacity or recoverability theorem

**Status:** BLOCKED unless additional microscopic assumptions are declared.

Missing:

- remnant Hamiltonian, sector structure, or effective dimension;
- microscopic channel;
- radiation algebra and time cut;
- environmental decoupling or recovery condition.

Near-term admissible outputs are L1–L3 parameterized constraints, excluded regions, or G2 underdetermination.

## T6 — JT-bath reconstruction benchmark

**Status:** SPECIFICATION FIXED; executable result remains TARGET.

`models/JT_BATH_SETUP_V1.md` now declares the diary/reference systems, bath radiation region, code-subspace requirements, generalized-entropy audit, and finite-dimensional surrogate controls.

Still required:

- transcription of one complete published JT-bath calculation;
- parameter and convention reproduction;
- declared reconstruction theorem and error;
- finite-dimensional surrogate compared with recovery certification.

No JT result transfers to the remnant model without a complete assumption map.

## Adversarial test requirement

Every proposed scalar recovery proxy must be tested against channels exhibiting at least one of:

- equal \(I(R:A)\) but different optimal recovery fidelity;
- equal classical Holevo information but different coherent information;
- equal output entropy but different environmental leakage;
- equal remnant dimension but different recoverability.

A claim failing an adversarial comparison is downgraded or rejected in `docs/VALIDITY_LEDGER.md`.
