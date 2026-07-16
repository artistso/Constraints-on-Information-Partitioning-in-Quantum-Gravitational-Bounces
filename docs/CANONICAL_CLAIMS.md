# Canonical Claims and Language Policy

This file controls the scientific language used in the README, abstract, proposal, manuscript, presentations, and external synthesis tools. When another document conflicts with this file, the claim must be downgraded or removed until the conflict is resolved through the validity and theorem ledgers.

## Evidence hierarchy

A statement may appear as an established result only when it is supported by one of the following:

1. a proof reproduced in the repository;
2. a primary-source theorem whose assumptions and conventions have been mapped explicitly;
3. a numerical certificate that passes the declared feasibility and solver-status policy;
4. a source-level equation reproduced by deterministic tests;
5. an observation or forecast supported by a complete, provenance-tracked forward model.

Analogies, summaries produced by language models, causal diagrams, and unsourced narrative explanations are not evidence.

## Established model-independent results

### Reference-assisted localization

Let a reference system \(R\) purify an input \(X\), and let

\[
V:\mathcal H_X\rightarrow\mathcal H_A\otimes\mathcal H_B
\]

be an isometry. For pure \(RAB\),

\[
I(R:A)+I(R:B)=2S(R).
\]

This identity permits maximally asymmetric localization. It does not imply equal partitioning.

### Finite retained dimension

If \(\dim B=d_B\), then

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\},
\]

and therefore

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

This is a correlation bound, not a recovery theorem.

### Finite Hamiltonian and energy cap

For a declared finite-dimensional Hamiltonian \(H_B\) and constraint

\[
\operatorname{Tr}(H_B\rho_B)\leq E,
\]

let \(S_{\max}(E,H_B)\) be the Gibbs maximum entropy. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\}.
\]

The Hamiltonian and energy cap must be provided by the physical model. Exterior mass, interior volume, and lifetime do not determine them automatically.

### Charge sectors and superselection

For a declared direct-sum decomposition

\[
\mathcal H_B=\bigoplus_q\mathcal H_q,
\qquad
\rho_B=\bigoplus_qp_q\rho_q,
\]

with \(d_q=\dim\mathcal H_q\),

\[
S(B)\leq H(p)+\sum_qp_q\log_2d_q.
\]

Consequently,

\[
I(R:B)\leq
2\min\left\{S(R),H(p)+\sum_qp_q\log_2d_q\right\}.
\]

This requires a physically supplied sector structure, block-diagonality condition, dimensions, and charge distribution or constraint.

### Fixed-input recovery certification

For a declared finite-dimensional channel \(\mathcal N\), the repository solves

\[
\max_{\mathcal R\ \mathrm{CPTP}}F_e(\mathcal R\circ\mathcal N)
\]

for the maximally mixed input. This is a state-specific entanglement-recovery certificate. It is not a worst-case, channel-wide, or diamond-norm theorem.

### Imported recovery theorems

The Bény--Oreshkov worst-case entanglement-fidelity duality and the KSW cb/diamond information--disturbance inequality are now mapped into repository notation in `docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`.

They are established imported theorems under their stated finite-dimensional assumptions. Their worst-case and diamond-norm optimizations are not yet implemented by the executable package.

## Established model-specific content

### Han--Rovelli--Soltani geometry

Within its stated effective assumptions and natural-unit convention, the repository reproduces the source-level scale factor, exterior function, horizon roots, bounce symmetry, and large-mass limits.

The geometry does not provide a microscopic Hilbert space, remnant Hamiltonian, tunnelling probability, Hawking-radiation channel, or decoder.

### HRS/Bianchi underdetermination

If a geometric descriptor supplies no rule selecting state spaces and a microscopic channel, information localization and recovery are not identifiable from geometry alone. Explicit one-port isometries demonstrate channel non-uniqueness while preserving the same abstract radiation/remnant split.

This does not deny the existence of a microscopic theory. It identifies the additional structure required to specify one.

### Bianchi et al. remnant scenario

The scenario is retained as a model-dependent endpoint and information-capacity case study. Until a state-space or Hamiltonian prescription is supplied, valid outputs are parameterized bounds or a theorem of underdetermination.

### JT gravity plus bath

This is a separate controlled holographic benchmark for generalized entropy, islands, code-subspace reconstruction, and recovery diagnostics. `models/JT_BATH_SETUP_V1.md` fixes the first benchmark specification, but executable gravitational reproduction and an operational decoder remain pending.

Its conclusions do not transfer automatically to an asymptotically flat loop-inspired remnant model.

## Conditional or unresolved targets

The following may be presented only as objectives or implementation targets:

- executable worst-case Bény--Oreshkov optimization;
- executable KSW diamond-norm certification;
- energy-constrained diamond-norm extensions;
- gravitationally derived charge sectors or symmetry data;
- a microscopic HRS/Bianchi transition channel;
- a model-derived remnant Hamiltonian or effective Hilbert-space dimension;
- an operational JT-bath decoder with a declared code subspace and error;
- any detector-level bounce or remnant forecast.

## Prohibited claims

The following statements are false, unsupported, or materially overstated and must not appear as project conclusions:

1. Unitarity forces equal information partitioning between radiation and a remnant.
2. Monogamy of entanglement forbids a biased output partition.
3. A Page curve or island calculation proves that every initial degree of freedom is operationally recoverable from arbitrary outgoing radiation.
4. Boundary unitarity makes every reduced bulk channel isometric.
5. LQG or LQC has established that all physical black holes bounce because of a universal repulsive quantum pressure.
6. A black-to-white-hole geometry by itself defines a quantum channel, information capacity, radiation spectrum, burst duration, or tunnelling probability.
7. Interior volume is automatically equivalent to Hilbert-space dimension or entropy capacity.
8. Primordial black holes in a broad mass range are generically expected to burst in the present epoch.
9. A named survey or observatory supplies a viable white-hole search before a source, population, propagation, and detector model is complete.
10. The Page curve and generalized entropy provide an explicit practical decoder.
11. A solar-mass black hole requires approximately \(10^{77}\) quantum gates to decode. That number is an entropy-scale order of magnitude, not a universal decoding-complexity result.
12. Quantum Darwinism is the established explanation for Hawking thermality or black-hole information recovery.
13. The project has proved a universal no-go or no-filtering theorem.
14. The project has produced observational constraints before the phenomenology gate passes.

## Analogy policy

The paper-folding, shredded-paper, and ink-in-water analogies may be used only as communication aids.

A permitted formulation is:

> Some quantum-gravity models replace the classical singular regime with a bounce or extension. Information may then be scrambled among radiation, retained degrees of freedom, and inaccessible sectors. Global unitarity constrains the complete system but does not determine which subsystem supports operational recovery.

The analogies must not be used to assert that:

- singularity resolution is universal or experimentally established;
- a bounce necessarily produces an observable burst;
- all information must emerge in one output sector;
- recoverability follows from global preservation;
- a specific model is the consensus of quantum gravity.

## External synthesis policy

NotebookLM and other summarization systems must be grounded primarily in:

1. `docs/CANONICAL_CLAIMS.md`;
2. `docs/VALIDITY_LEDGER.md`;
3. `docs/THEOREM_LEDGER.md`;
4. `docs/NORM_CONVENTIONS.md`;
5. `docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`;
6. `docs/HRS_BIANCHI_UNDERDETERMINATION.md`;
7. the model cards and `models/JT_BATH_SETUP_V1.md`;
8. `proposal/ABSTRACT.md` and `proposal/PROPOSAL.md`.

Older PDFs and narrative drafts are claim inventories only. They must not be treated as authoritative sources.

## Publication-language check

Before release, every abstract-level sentence must be classifiable as one of:

- **proved here**;
- **imported under explicit assumptions**;
- **numerically certified within declared scope**;
- **source-level model content**;
- **conditional objective**;
- **blocked or unresolved**.

Any sentence that cannot be classified is removed or rewritten.
