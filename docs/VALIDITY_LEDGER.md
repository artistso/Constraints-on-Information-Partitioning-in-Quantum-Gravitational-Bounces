# Validity Ledger

This ledger records which inherited claims are retained, rejected, conditional, or unresolved. It is the controlling document for future drafts.

## Status codes

- **VALID:** derivable under the stated assumptions.
- **CONDITIONAL:** valid only in a specified model or with additional assumptions.
- **REJECTED:** false as stated or contradicted by a counterexample.
- **UNRESOLVED:** meaningful but not yet established.
- **GATED:** work may proceed only after predefined evidence requirements are met.

---

## Quantum-information claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| QIT-01 | For a pure bipartite state \(AB\), \(S(A)=S(B)\). | VALID | Standard consequence of Schmidt decomposition. |
| QIT-02 | For a pure input \(X\) mapped to \(AB\), \(S(A)=S(B)=S(X)\). | REJECTED | The input entropy is zero when \(X\) is pure, while reduced output entropies may be nonzero. |
| QIT-03 | Mutual information between the consumed input and each output is directly defined after the channel. | REJECTED | Introduce a reference \(R\) purifying the input; evaluate \(I(R:A)\) and \(I(R:B)\). |
| QIT-04 | For pure \(RAB\), \(I(R:A)+I(R:B)=2S(R)\). | VALID | Exact entropy identity. |
| QIT-05 | Unitarity forces \(I(R:A)=I(R:B)=S(R)\). | REJECTED | The isometry \(|\psi\rangle_X\mapsto|\psi\rangle_A|0\rangle_B\) is a counterexample. |
| QIT-06 | A biased information partition is impossible for an isometric channel. | REJECTED | Generic isometries permit maximally biased localization. |
| QIT-07 | Approximate recoverability from \(A\) is related to decoupling of \(R\) from \(B\). | VALID | Must specify distance measure, recovery task, and error bound. |
| QIT-08 | Additional symmetry, energy, dimensional, or accessibility constraints may bound localization. | UNRESOLVED | Central theorem-development target. |

---

## Holography and gravity claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| GR-01 | Page-curve behavior can arise in controlled evaporating holographic models through quantum extremal surfaces and islands. | CONDITIONAL | Applies to specified models and couplings, not automatically to every bounce geometry. |
| GR-02 | A Page curve proves uniform information distribution across all output channels. | REJECTED | It constrains the entropy of a defined radiation region, not arbitrary subdivisions or complementary channels. |
| GR-03 | Boundary unitarity implies every reduced bulk output channel is isometric. | REJECTED | Reduced channels may be non-isometric after tracing inaccessible degrees of freedom. |
| GR-04 | AdS/CFT can be applied directly to any asymptotically flat LQG-inspired bounce. | REJECTED | A duality map must be supplied; otherwise holography is a separate benchmark. |
| GR-05 | Black-to-white-hole transition and white-hole remnant models exist in the research literature. | VALID | Their physical realization and consistency remain model-dependent. |
| GR-06 | A universal bounce channel can be inferred from a causal diagram alone. | REJECTED | Microscopic dynamics, subsystem algebras, and state spaces are required. |
| GR-07 | Conditional recoverability bounds may be derived in a specified geometry or code subspace. | UNRESOLVED | Primary gravitational objective. |

---

## Phenomenology claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| PH-01 | \(2GM/c^3\) is the Schwarzschild light-crossing timescale. | VALID | It is a dimensional gravitational timescale. |
| PH-02 | For \(M=10^{12}\,\mathrm{kg}\), \(2GM/c^3\approx10^{-5}\,\mathrm{s}\). | REJECTED | The value is approximately \(4.95\times10^{-24}\,\mathrm{s}\). |
| PH-03 | The light-crossing time is automatically the observed burst duration. | REJECTED | A source model must connect the transition, ejecta, propagation, and detector response. |
| PH-04 | Rubin, gamma-ray, radio, UV, astrometric, or gravitational data may constrain a concrete model. | CONDITIONAL | Requires a forward signal model and sensitivity calculation. |
| PH-05 | Existing broker infrastructure is preferable to building a complete alert pipeline from scratch. | CONDITIONAL | Sensible if the selected signal occupies the broker’s cadence, data products, and selection domain. |
| PH-06 | A generic white-hole optical search improves limits by one or two orders of magnitude. | REJECTED | No validated signal, efficiency, background, or population model supports the forecast. |
| PH-07 | A model-specific observational analysis should proceed after a feasibility gate. | GATED | See `proposal/PROPOSAL.md`, Section 4.5. |

---

## Analogue-gravity claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| AG-01 | Analogue horizons can benchmark mode conversion and channel-reconstruction methods. | CONDITIONAL | The analogue Hamiltonian and measured modes must be specified. |
| AG-02 | A BEC horizon directly tests Planck-scale information flow in gravitational bounces. | REJECTED | It does not reproduce quantum-gravitational microscopic dynamics. |
| AG-03 | Analogue process tomography may be useful as a methods appendix. | GATED | Only after the core QIT protocol is defined and an experimental collaborator confirms feasibility. |

---

## Terminology corrections

| Term | Required usage |
|---|---|
| LQG | Loop quantum gravity |
| LQC | Loop quantum cosmology |
| “Information in the input” after a channel | Correlations with an explicit purifying reference system |
| “Information escaped” | A stated recovery task succeeds from a defined output algebra within a quantified error |
| “Bounce model” | A named geometry or dynamics with equations, boundary conditions, and domain of validity |
| “Detection forecast” | A detector-level calculation including source population, response, efficiency, backgrounds, and statistics |

---

## Immediate validation queue

1. Implement symbolic checks of the pure-state entropy identities.
2. Build explicit biased isometry examples and random-channel tests.
3. Define operational recovery metrics and norm conventions.
4. Select one holographic benchmark and one non-holographic bounce model.
5. Construct model cards before drafting any gravitational theorem.
6. Recalculate every physical scale with automated unit tests.
7. Permit observational work only after the signal-model gate passes.
