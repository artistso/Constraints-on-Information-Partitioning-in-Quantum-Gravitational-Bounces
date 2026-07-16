# Constraints on Information Localization in Quantum-Gravitational Bounces

> **Research scaffold v0.5 — conditional, falsifiable, and publication-oriented.**
>
> This repository rejects universal equal-partition claims. Generic isometric quantum channels can localize information asymmetrically. The project asks which additional physical assumptions constrain where information is recoverable in black-to-white-hole transitions, remnant models, and controlled holographic benchmarks.

## Project thesis

Let an input system `X`, purified by a reference `R`, evolve through an isometry

\[
V:\mathcal H_X\rightarrow \mathcal H_A\otimes\mathcal H_B.
\]

For the resulting pure state on `RAB`,

\[
I(R:A)+I(R:B)=2S(R).
\]

This identity conserves total reference correlations but does not require equal partitioning. The research problem is:

> Under specified assumptions about causal accessibility, conservation laws, energy, symmetry, semiclassical validity, code-subspace reconstruction, and retained degrees of freedom, when is the infalling quantum state approximately recoverable from a declared asymptotic radiation algebra?

## Controlling scientific documents

Public claims are governed by the following hierarchy:

1. [`docs/CANONICAL_CLAIMS.md`](docs/CANONICAL_CLAIMS.md)
2. [`docs/VALIDITY_LEDGER.md`](docs/VALIDITY_LEDGER.md)
3. [`docs/THEOREM_LEDGER.md`](docs/THEOREM_LEDGER.md)
4. [`docs/NORM_CONVENTIONS.md`](docs/NORM_CONVENTIONS.md)
5. [`docs/DIAMOND_NORM_CERTIFICATE_POLICY.md`](docs/DIAMOND_NORM_CERTIFICATE_POLICY.md)
6. [`docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`](docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md)
7. [`docs/HRS_BIANCHI_UNDERDETERMINATION.md`](docs/HRS_BIANCHI_UNDERDETERMINATION.md)
8. model cards and benchmark specifications in [`models/`](models/)

Older PDFs and narrative summaries are retained only as claim inventories. They are not authoritative research products.

## Executable validation layers

### v0.1 — Kinematics and physical scales

- explicit biased and Haar-random isometries;
- pure-state mutual-information identity;
- Schwarzschild radius, light-crossing time, Hawking temperature, and leading evaporation-time baselines;
- regression protection for rejected numerical scales.

### v0.2 — Open channels and finite remnants

- erasure, dephasing, depolarizing, and amplitude damping;
- Kraus, Stinespring, normalized Choi, coherent-information, and Holevo diagnostics;
- explicit recovery maps, entanglement fidelity, average fidelity, trace distance, and purified distance;
- finite-remnant dimension bounds and adversarial channel comparisons.

### v0.3 — Fixed-input recovery, energy constraints, and geometry

- state-specific environmental decoupling diagnostics;
- pinned CVXPY/Clarabel semidefinite programs for maximally mixed-input recovery;
- independent environment-side fidelity optimization and a cross-formulation gap;
- finite-Hamiltonian Gibbs entropy and energy-constrained correlation bounds;
- Han–Rovelli–Soltani effective geometry, horizon-root, and large-mass asymptotic checks;
- theorem, norm, model, and parameter-provenance ledgers.

### v0.4 — Claim hygiene, theorem mapping, and resource refinement

- canonical claim and external-synthesis policy;
- automated checks blocking known false or overstated formulations from public documents;
- Bény–Oreshkov worst-case recovery theorem mapped into repository fidelity notation;
- KSW cb-norm information–disturbance inequality mapped into Schrödinger-picture diamond norm;
- finite charge-sector and superselection entropy bounds;
- formal geometry-only channel-underdetermination proposition;
- first fixed JT-bath benchmark specification;
- independent review packet.

### v0.5 — Channel-wide diamond recovery and KSW certification

- unnormalized Choi matrices in declared input-output order;
- finite-dimensional diamond norm through the Watrous dual SDP;
- exact optimization of
  \[
  \inf_{\mathcal R}\|\mathcal R\circ\mathcal N-\operatorname{id}\|_\diamond;
  \]
- exact optimization of
  \[
  \inf_{\sigma_E}\|\mathcal N^c-\mathcal C_\sigma\|_\diamond;
  \]
- deterministic KSW lower- and upper-margin checks;
- analytic dephasing, depolarizing, identity, and constant-channel standards;
- a strict SCS certificate path for the current degenerate and rank-deficient cases.

## Reproduction

Base validation:

```bash
python -m pip install -e ".[test]"
python scripts/check_claim_language.py
pytest -m "not optimization"
python scripts/run_stress_tests.py
python scripts/run_channel_stress_tests.py
python scripts/run_geometry_stress_tests.py
python scripts/run_symmetry_stress_tests.py
```

Pinned optimization validation:

```bash
python -m pip install -e ".[test,optimization]"
pytest -m optimization
python scripts/run_theorem_stress_tests.py
python scripts/run_diamond_stress_tests.py
```

The optimization extra pins CVXPY, Clarabel, and SCS. A platform-complete transitive lock remains a release gate before a tagged numerical-certificate archive.

## Current mathematical findings

### Finite dimension

For pure `RAB` with retained dimension `d_B`,

\[
I(R:B)\leq2\min\{S(R),\log_2d_B\},
\]

hence

\[
I(R:A)\geq\max\{0,2S(R)-2\log_2d_B\}.
\]

### Finite Hamiltonian and energy cap

For a declared finite-dimensional retained Hamiltonian `H_B` and

\[
\operatorname{Tr}(H_B\rho_B)\leq E,
\]

let \(S_{\max}(E,H_B)\) be the Gibbs maximum entropy. Then

\[
I(R:B)\leq2\min\{S(R),S_{\max}(E,H_B)\},
\]

and

\[
I(R:A)\geq\max\{0,2S(R)-2S_{\max}(E,H_B)\}.
\]

### Charge sectors and superselection

For

\[
\mathcal H_B=\bigoplus_q\mathcal H_q,
\qquad
\rho_B=\bigoplus_qp_q\rho_q,
\]

with \(d_q=\dim\mathcal H_q\),

\[
S(B)\leq H(p)+\sum_qp_q\log_2d_q,
\]

and therefore

\[
I(R:B)\leq
2\min\left\{S(R),H(p)+\sum_qp_q\log_2d_q\right\}.
\]

The sector structure and distribution are physical inputs. An unconstrained distribution reduces to the ordinary total-dimension cap.

These results constrain correlation storage. None supplies a decoder by itself.

## Recovery layers

### Maximally mixed-input fidelity

The fixed-input SDP evaluates

\[
\max_{\mathcal R\ \mathrm{CPTP}}F_e(\mathcal R\circ\mathcal N)
\]

for the maximally mixed input. It records solver status, CPTP residuals, positivity residuals, and an independent state-specific environment-fidelity diagnostic.

### Channel-wide diamond recovery

For a declared finite-dimensional channel,

\[
\delta_{\mathrm{rec}}
=
\inf_{\mathcal R\ \mathrm{CPTP}}
\|\mathcal R\circ\mathcal N-\operatorname{id}\|_\diamond
\]

is solved by a joint recovery-Choi and diamond-dual SDP.

For a declared complementary channel,

\[
\delta_{\mathrm{env}}
=
\inf_{\sigma_E}
\|\mathcal N^c-\mathcal C_\sigma\|_\diamond
\]

is solved by jointly optimizing the constant state and diamond dual.

The mapped KSW inequality is

\[
\frac14\delta_{\mathrm{rec}}^2
\leq
\delta_{\mathrm{env}}
\leq
2\sqrt{\delta_{\mathrm{rec}}}.
\]

The source theorem remains imported. The executable sweep verifies the implementation and convention map on declared finite-dimensional channel families.

### Numerical checkpoint

The pinned workflow currently reports:

| Diagnostic | Result |
|---|---:|
| Optimization tests | 30 passed |
| Dephasing identity-distance analytic error | \(<6.3\times10^{-9}\) |
| Dephasing optimal-recovery analytic error | \(<2.1\times10^{-8}\) |
| Minimum KSW lower margin | \(-8.8\times10^{-19}\) |
| Minimum KSW upper margin | \(>8.6\times10^{-5}\) |
| Fully depolarizing qubit distance from identity | approximately \(1.5\) |
| Identity distance from closest constant qubit channel | approximately \(1.5\) |

The tiny negative lower margin is consistent with floating-point zero. Every certificate uses solver status `optimal` and declared PSD, trace, and partial-trace residual tests.

### Remaining recovery target

The Bény–Oreshkov worst-case entanglement-fidelity minimax is still not executable. It is distinct from both the fixed-input fidelity SDP and the channel-wide diamond optimization.

Energy-constrained and infinite-dimensional diamond norms also remain outside the current certificate.

## Selected physical tracks

### Non-holographic track

- **Geometry:** Han–Rovelli–Soltani single-asymptotic-region transition.
- **Remnant endpoint:** Bianchi et al. white-hole remnant scenario.
- **Established conclusion:** geometry alone does not identify a unique quantum channel when no geometry-to-channel rule is supplied.
- **Valid next outputs:** parameterized information-capacity constraints, excluded regions, or a microscopic completion that removes the underdetermination.

The geometry does not determine a Hilbert-space dimension, Hamiltonian, charge sectors, microscopic channel, radiation spectrum, or decoder. The new optimizer can evaluate a declared channel; it cannot derive one from the metric.

### Controlled holographic benchmark

- **Model:** JT gravity coupled to quantum matter and a non-gravitating bath.
- **Specification:** [`models/JT_BATH_SETUP_V1.md`](models/JT_BATH_SETUP_V1.md).
- **Research output:** source-complete generalized-entropy reproduction followed by reconstruction and decoupling calibration in a declared code subspace.

No JT or island conclusion is transferred to the non-holographic remnant track without an explicit assumption map.

## Repository map

| Path | Purpose |
|---|---|
| [`proposal/ABSTRACT.md`](proposal/ABSTRACT.md) | Canonical formal abstract |
| [`proposal/PROPOSAL.md`](proposal/PROPOSAL.md) | Corrected concept proposal and work packages |
| [`docs/CANONICAL_CLAIMS.md`](docs/CANONICAL_CLAIMS.md) | Allowed, conditional, blocked, and prohibited public claims |
| [`docs/VALIDITY_LEDGER.md`](docs/VALIDITY_LEDGER.md) | Accepted, rejected, conditional, and unresolved claims |
| [`docs/THEOREM_LEDGER.md`](docs/THEOREM_LEDGER.md) | Proof, imported-theorem, and numerical-certificate status |
| [`docs/NORM_CONVENTIONS.md`](docs/NORM_CONVENTIONS.md) | Entropy, fidelity, Choi, norm, and SDP conventions |
| [`docs/DIAMOND_NORM_CERTIFICATE_POLICY.md`](docs/DIAMOND_NORM_CERTIFICATE_POLICY.md) | Finite-dimensional diamond SDP and certificate rules |
| [`docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`](docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md) | Bény–Oreshkov and KSW convention map |
| [`docs/SYMMETRY_RESOURCE_BOUNDS.md`](docs/SYMMETRY_RESOURCE_BOUNDS.md) | Charge-sector and superselection lemma |
| [`docs/HRS_BIANCHI_UNDERDETERMINATION.md`](docs/HRS_BIANCHI_UNDERDETERMINATION.md) | Geometry-only channel non-identifiability proposition |
| [`docs/REVIEW_PACKET.md`](docs/REVIEW_PACKET.md) | Independent QIT and gravity review protocol |
| [`models/`](models/) | HRS, Bianchi-remnant, and JT-bath model specifications |
| [`src/qgbounce/`](src/qgbounce/) | Tested quantum-information, recovery, energy, symmetry, geometry, and gravity utilities |
| [`scripts/`](scripts/) | Simulations, certificates, and claim-language validation |
| [`tests/`](tests/) | Regression, adversarial, symmetry, geometry, fidelity, and diamond tests |
| [`manuscript/main.tex`](manuscript/main.tex) | LaTeX manuscript scaffold |
| [`references/references.bib`](references/references.bib) | Primary-source bibliography |
| [`notebooks/README.md`](notebooks/README.md) | Publication-facing notebook roadmap |
| [`data/README.md`](data/README.md) | Data provenance and phenomenology gate |

## Scientific guardrails

1. Reference systems are explicit.
2. Kinematics, dynamics, geometry, and state-space assumptions are separated.
3. Correlation, coherent transmission, fixed-input fidelity, worst-case fidelity, and diamond recovery are distinct.
4. Fixed-input certificates are not called channel-wide results.
5. Diamond certificates are not called energy-constrained or gravitational results.
6. Imported theorems and executable implementations are distinguished.
7. Holographic claims require a specified dual, region, and code subspace.
8. Geometry is not converted into information capacity without a state-space model.
9. Phenomenology remains blocked until a complete forward model exists.
10. Failed tests and unsupported language block claim promotion.

## Current status

The regression, geometry, symmetry, fixed-input optimization, diamond optimization, and claim-language workflows pass. The project is now in the **worst-case fidelity, gravitational-resource derivation, JT-source transcription, and independent-review phase**. Draft PR #1 remains open pending external QIT and gravity review and source-complete implementation of the next model gates.
