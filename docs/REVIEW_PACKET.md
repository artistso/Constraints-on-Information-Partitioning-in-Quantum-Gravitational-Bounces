# Independent Technical Review Packet

## Review objective

Determine whether Draft PR #1 may be represented as a technically sound research scaffold. This is not a request to endorse a universal bounce, information-return, or observational claim.

## Canonical reading order

1. `docs/CANONICAL_CLAIMS.md`
2. `proposal/ABSTRACT.md`
3. `docs/THEOREM_LEDGER.md`
4. `docs/NORM_CONVENTIONS.md`
5. `docs/DIAMOND_NORM_CERTIFICATE_POLICY.md`
6. `docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`
7. `docs/VALIDITY_LEDGER.md`
8. `docs/HRS_BIANCHI_UNDERDETERMINATION.md`
9. model cards and `models/JT_BATH_SETUP_V1.md`
10. `proposal/PROPOSAL.md`
11. `manuscript/main.tex`

Earlier PDFs are claim inventories and should not control the review.

## Quantum-information review form

For every theorem, lemma, or numerical certificate, record:

| Field | Reviewer entry |
|---|---|
| Statement identifier | |
| Correct as written? | yes / no / conditional |
| Missing assumptions | |
| Norm and fidelity convention | |
| Input ensemble, channel, or code | |
| Constructive or existential | |
| Analytic, imported, or numerical | |
| Counterexample tested | |
| Solver and status policy | |
| Required correction | |

Required checks:

- reference-assisted channel formulation;
- pure-state mutual-information identity;
- finite-dimension proof;
- finite-Hamiltonian Gibbs proof;
- charge-sector entropy decomposition;
- fixed-input recovery Choi objective and tensor order;
- normalized versus unnormalized Choi conversion;
- diamond dual SDP and input-output ordering;
- linear composed-Choi construction for recovery;
- CPTP recovery partial-trace constraints;
- closest constant-channel Choi formula `I_X tensor sigma_E`;
- SCS status and residual policy;
- dephasing, depolarizing, identity, and constant-channel analytic standards;
- KSW cb-to-diamond convention map and constants;
- Bény--Oreshkov worst-case fidelity convention map;
- distinction among fixed-input fidelity, worst-case fidelity, and channel-wide diamond error;
- adversarial examples.

## Diamond-certificate audit

For each generated diamond certificate, verify:

| Field | Reviewer entry |
|---|---|
| Channel and dimensions | |
| Complementary dilation | |
| Recovery or constant-state objective | |
| Solver/status | |
| Objective value | |
| Analytic reference | |
| Minimum eigenvalue of `Z + J` | |
| Minimum eigenvalue of `Z - J` | |
| Partial-trace upper residual | |
| Recovery trace residual | |
| Recovery Choi minimum eigenvalue | |
| Constant-state trace residual | |
| Constant-state minimum eigenvalue | |
| KSW margins | |
| Certificate accepted? | |

Required numerical checkpoint:

- 30 optimization tests pass;
- maximum dephasing identity-distance analytic error is below `6.3e-9`;
- maximum dephasing optimal-recovery analytic error is below `2.1e-8`;
- the minimum KSW lower margin is consistent with floating-point zero;
- every certificate-level solver status is `optimal`.

The reviewer must confirm that sampled KSW checks are described as implementation validation, not as a new proof of the imported theorem.

## Gravity review form

| Field | Reviewer entry |
|---|---|
| Model/source | |
| Equation or claim checked | |
| Source location | |
| Domain of validity | |
| Missing dynamics | |
| Unsupported inference found | |
| Required correction | |

Required checks:

- HRS metric formulas and large-mass limits;
- natural-unit interpretation;
- neglected Hawking radiation, rotation, and microscopic dynamics;
- separation of HRS geometry from the Bianchi remnant endpoint;
- validity of the geometry-only underdetermination proposition;
- absence of volume-to-capacity or lifetime-to-Hilbert-space inference;
- explicit statement that the diamond optimizer evaluates a declared channel and does not derive one from geometry;
- separation from the JT-bath benchmark.

## Holography review form

Required checks:

- one explicit JT-bath setup is identified;
- radiation region and code subspace are declared;
- generalized entropy is not called a decoder;
- entanglement-wedge reconstruction assumptions and errors are stated;
- fixed-input and diamond surrogate diagnostics are labeled as surrogates;
- no result is transferred to the non-holographic track without an assumption map.

## Phenomenology review form

Required checks:

- `2GM/c^3` is used only as a gravitational baseline;
- no generic burst duration is inferred;
- no named instrument is presented as validating a search;
- no rate or sensitivity result appears without emission, population, propagation, response, background, and statistical models;
- analogue gravity is absent from core claims unless a concrete protocol exists.

## Reproducibility commands

```bash
python -m pip install -e ".[test]"
pytest -m "not optimization"
python scripts/check_claim_language.py
python scripts/run_stress_tests.py
python scripts/run_channel_stress_tests.py
python scripts/run_geometry_stress_tests.py
python scripts/run_symmetry_stress_tests.py
```

Optimization layer:

```bash
python -m pip install -e ".[test,optimization]"
pytest -m optimization
python scripts/run_theorem_stress_tests.py
python scripts/run_diamond_stress_tests.py
```

## Acceptance standard

The PR remains a draft until:

- one independent QIT reviewer approves the mathematical and numerical scope;
- one independent gravity reviewer approves the model separation and limitations;
- all critical review comments are resolved;
- every public claim is classified by the canonical language policy;
- all CI jobs pass;
- no blocked result is presented as established;
- the finite-dimensional diamond implementation is not generalized beyond its certificate domain.

## Reviewer-signoff template

```text
Reviewer field:
Name or identifier:
Expertise:
Files reviewed:
Commit SHA:
Major concerns:
Minor corrections:
Claims approved within scope:
Claims rejected or requiring downgrade:
Numerical certificates accepted:
Recommendation: approve scaffold / request changes / reject current scope
Date:
```
