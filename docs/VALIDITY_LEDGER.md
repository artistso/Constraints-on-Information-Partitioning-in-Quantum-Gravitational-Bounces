# Validity Ledger

This ledger records which claims are retained, rejected, conditional, unresolved, or gated. It controls all proposal and manuscript language.

## Status codes

- **VALID:** derivable under the stated assumptions.
- **CONDITIONAL:** valid only in a specified model or with additional assumptions.
- **REJECTED:** false as stated or contradicted by a counterexample.
- **UNRESOLVED:** meaningful but not yet established.
- **GATED:** use is blocked until predefined evidence requirements pass.

---

## Quantum-information claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| QIT-01 | For a pure bipartite state \(AB\), \(S(A)=S(B)\). | VALID | Standard Schmidt-decomposition consequence. |
| QIT-02 | For a pure input \(X\) mapped to \(AB\), \(S(A)=S(B)=S(X)\). | REJECTED | A pure input has zero entropy while reduced outputs may be mixed. |
| QIT-03 | Mutual information between the consumed input and an output is directly defined after the channel. | REJECTED | Retain a purifier \(R\) and evaluate \(I(R:A)\) or \(I(R:B)\). |
| QIT-04 | For pure \(RAB\), \(I(R:A)+I(R:B)=2S(R)\). | VALID | Exact identity; analytic, extremal, and Haar-random tests pass. |
| QIT-05 | Unitarity forces \(I(R:A)=I(R:B)=S(R)\). | REJECTED | One-port isometries are explicit counterexamples. |
| QIT-06 | A biased information partition is impossible for an isometric channel. | REJECTED | Maximally biased localization is compatible with exact isometry. |
| QIT-07 | Approximate recoverability from \(A\) is related to decoupling of \(R\) from the complement. | VALID | The exact statement must specify input state/code, metric, recovery task, and constants. |
| QIT-08 | A finite remnant dimension bounds its reference mutual information. | VALID | \(I(R:B)\leq2\min\{S(R),\log_2d_B\}\), giving the corresponding radiation lower bound for pure \(RAB\). |
| QIT-09 | A finite-dimensional remnant bound alone guarantees high-fidelity radiation recovery. | REJECTED | A correlation bound supplies neither a decoder nor an operational fidelity bound. |
| QIT-10 | Mutual information, coherent information, classical accessibility, output entropy, and recovery fidelity are interchangeable. | REJECTED | Erasure, dephasing, and adversarial pairs separate these diagnostics. |
| QIT-11 | A declared finite-dimensional Hamiltonian and mean-energy cap bound remnant correlation storage. | VALID | Gibbs maximization gives \(S_{\max}(E,H_B)\); replace \(\log_2d_B\) by that entropy cap. |
| QIT-12 | Exterior mass, interior volume, or remnant lifetime determines \(H_B\), \(d_B\), or information capacity. | REJECTED | A state-space or Hamiltonian prescription is an independent physical input. |
| QIT-13 | The maximally mixed-input optimal recovery problem is an SDP over a CPTP recovery Choi matrix. | VALID | Implemented from the standard linear Choi formulation and tested against analytic channels. |
| QIT-14 | Agreement of the recovery SDP and complementary-state fidelity SDP proves a channel-wide worst-case theorem. | REJECTED | Their present agreement is a fixed-input cross-certificate only. |
| QIT-15 | The amplitude-damping identity decoder is globally optimal. | GATED | The certified recovery SDP must pass CI and independent review before any optimality claim. |
| QIT-16 | Symmetry, conserved charge, and superselection constraints strengthen the current resource bounds. | UNRESOLVED | Next theorem-development target. |
| QIT-17 | A channel-wide or energy-constrained diamond-norm information–disturbance bound has been implemented. | REJECTED | No diamond norm is currently computed; KSW/Bény–Oreshkov remain imported theorem targets. |

---

## Numerical-certificate claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| NUM-01 | The recovery Choi SDP reproduces analytic erasure and dephasing optima. | GATED | Recovery-side values passed; final status awaits the stabilized full optimization CI run. |
| NUM-02 | The independent environment-fidelity SDP matches the recovery optimum within declared tolerance. | GATED | Clarabel exposed boundary-case inaccuracy; the environment problem now uses pinned high-accuracy SCS and must pass CI. |
| NUM-03 | A solver-reported `optimal_inaccurate` status is theorem-grade evidence. | REJECTED | Such a result blocks theorem use unless bounded independently and accepted under a documented tolerance. |
| NUM-04 | A cross-formulation gap is the conic solver's primal–dual gap. | REJECTED | It compares two independently modeled physical formulations; it is not the solver's internal duality gap. |

---

## Holography and gravity claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| GR-01 | Page-curve behavior can arise in controlled evaporating holographic models through QES/islands. | CONDITIONAL | Applies only to specified models, bath couplings, regions, and approximations. |
| GR-02 | A Page curve proves uniform information distribution across all outputs. | REJECTED | It constrains the entropy of a defined radiation region, not arbitrary subchannels. |
| GR-03 | Boundary unitarity implies every reduced bulk output channel is isometric. | REJECTED | Reduced channels may be non-isometric after tracing inaccessible degrees of freedom. |
| GR-04 | AdS/CFT applies directly to an asymptotically flat loop-inspired transition. | REJECTED | A duality map is required; JT gravity remains a separate benchmark. |
| GR-05 | Black-to-white transition and white-hole remnant scenarios exist in the literature. | VALID | Physical realization and consistency remain model dependent. |
| GR-06 | A causal diagram or metric alone determines a microscopic bounce channel. | REJECTED | State spaces, dynamics, couplings, and observer algebras are additionally required. |
| GR-07 | The HRS effective geometry supplies explicit large-scale metric functions, bounce radius, and horizon roots outside its tunnelling region. | CONDITIONAL | Valid within the source assumptions and \(G=c=1\); regression tests reproduce the formulas and limits. |
| GR-08 | The HRS geometry supplies Hawking evaporation, tunnelling probability, a remnant Hamiltonian, or radiation decoder. | REJECTED | These are explicitly absent or beyond the geometric construction. |
| GR-09 | Interior volume automatically measures remnant information capacity. | REJECTED | No validated volume-to-Hilbert-space map is supplied. |
| GR-10 | A model-specific recoverability theorem can be derived from HRS/Bianchi without additional microscopic inputs. | GATED | Current admissible result is a parameterized bound or underdetermination theorem. |
| GR-11 | Conditional reconstruction can be studied in a specified JT-bath code subspace. | CONDITIONAL | Requires a declared setup, radiation algebra, theorem, and reconstruction error. |

---

## Phenomenology claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| PH-01 | \(2GM/c^3\) is the Schwarzschild light-crossing baseline. | VALID | It is a dimensional gravitational scale. |
| PH-02 | For \(M=10^{12}\,\mathrm{kg}\), \(2GM/c^3\approx10^{-5}\,\mathrm{s}\). | REJECTED | The value is approximately \(4.95	imes10^{-24}\,\mathrm{s}\). |
| PH-03 | The light-crossing time is automatically an observed burst duration. | REJECTED | A source, propagation, and detector model must connect the scales. |
| PH-04 | Named optical, gamma-ray, radio, UV, astrometric, or gravitational instruments constrain a generic bounce. | REJECTED | Instrument claims require a concrete signal and population model. |
| PH-05 | Existing broker infrastructure may be preferable to an independent alert pipeline. | CONDITIONAL | Only if a validated signal overlaps the broker's cadence and products. |
| PH-06 | A generic white-hole search improves limits by one or two orders of magnitude. | REJECTED | No validated efficiency, background, signal, or population calculation supports this. |
| PH-07 | Observational work proceeds only after the feasibility gate. | GATED | The current HRS/Bianchi track has not supplied the required forward model. |
| PH-08 | Recent PBH-to-white-hole rate calculations establish a generic FRB explanation. | REJECTED | Their conclusions are narrow and depend on explicit PBH abundance, tunnelling, mass-function, and emission assumptions. |

---

## Analogue-gravity claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| AG-01 | Analogue horizons can benchmark mode conversion or reconstruction methods. | CONDITIONAL | Specify the Hamiltonian, channel, measured modes, and task. |
| AG-02 | A BEC horizon directly tests Planck-scale bounce dynamics. | REJECTED | It does not reproduce gravitational microscopic dynamics. |
| AG-03 | Analogue process tomography may support a later methods paper. | GATED | Requires a mature protocol and experimental collaborator. |

---

## Terminology corrections

| Term | Required usage |
|---|---|
| LQG | Loop quantum gravity |
| LQC | Loop quantum cosmology |
| “Information in the input” after a channel | Correlations with an explicit purifying reference system |
| “Information escaped” | A declared recovery task succeeds from a specified algebra within quantified error |
| “Bounce model” | A named geometry or dynamics with equations, boundary conditions, and validity domain |
| “Certified recovery” | A proof or convex certificate with solver status and feasibility residuals |
| “Detection forecast” | A detector-level calculation including source population, response, efficiency, backgrounds, and statistics |

---

## Validation status

Completed in the base executable suite:

1. pure-state identities, biased isometries, and random-isometry checks;
2. open-channel and adversarial diagnostics;
3. finite-remnant dimension bounds;
4. finite-Hamiltonian Gibbs entropy bounds;
5. state-specific environmental decoupling diagnostics;
6. Schwarzschild scale regression tests;
7. HRS geometry and horizon/asymptotic tests;
8. norm, theorem, model, and parameter-provenance ledgers.

Active gate:

1. obtain a passing pinned recovery/environment optimization CI run;
2. review the numerical certificate tolerances and solver statuses;
3. reproduce worst-case information–disturbance conventions before claiming a channel-wide theorem;
4. extend to charge and symmetry constraints;
5. convert HRS/Bianchi missing inputs into a formal underdetermination statement;
6. keep phenomenology blocked until a complete signal model exists.
