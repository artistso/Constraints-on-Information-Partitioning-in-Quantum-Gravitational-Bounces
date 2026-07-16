# Validity Ledger

This ledger records which claims are retained, rejected, conditional, unresolved, or gated. It controls proposal and manuscript language together with `docs/CANONICAL_CLAIMS.md`.

## Status codes

- **VALID:** derivable under the stated assumptions.
- **CONDITIONAL:** valid only in a specified model or with additional assumptions.
- **REJECTED:** false as stated or contradicted by a counterexample.
- **UNRESOLVED:** meaningful but not established.
- **GATED:** use is blocked until predefined evidence requirements pass.

---

## Quantum-information claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| QIT-01 | For a pure bipartite state \(AB\), \(S(A)=S(B)\). | VALID | Schmidt decomposition. |
| QIT-02 | For a pure input \(X\) mapped to \(AB\), \(S(A)=S(B)=S(X)\). | REJECTED | A pure input has zero entropy while reduced outputs may be mixed. |
| QIT-03 | Mutual information between the consumed input and an output is directly defined after the channel. | REJECTED | Retain a purifier \(R\) and evaluate \(I(R:A)\) or \(I(R:B)\). |
| QIT-04 | For pure \(RAB\), \(I(R:A)+I(R:B)=2S(R)\). | VALID | Exact identity; analytic, extremal, and Haar-random tests pass. |
| QIT-05 | Unitarity forces \(I(R:A)=I(R:B)=S(R)\). | REJECTED | One-port isometries are counterexamples. |
| QIT-06 | A biased information partition is impossible for an isometric channel. | REJECTED | Maximally biased localization is compatible with exact isometry. |
| QIT-07 | Approximate recovery is related to decoupling from the complementary output. | VALID | The exact statement must specify input/code, metric, recovery task, and constants. |
| QIT-08 | A finite remnant dimension bounds its reference mutual information. | VALID | \(I(R:B)\leq2\min\{S(R),\log_2d_B\}\), with the corresponding radiation lower bound for pure \(RAB\). |
| QIT-09 | A finite-dimensional remnant bound alone guarantees high-fidelity radiation recovery. | REJECTED | A correlation bound supplies neither a decoder nor an operational fidelity bound. |
| QIT-10 | Mutual information, coherent information, classical accessibility, output entropy, and recovery fidelity are interchangeable. | REJECTED | Erasure, dephasing, and adversarial pairs separate these diagnostics. |
| QIT-11 | A declared finite Hamiltonian and mean-energy cap bound remnant correlation storage. | VALID | Gibbs maximization gives \(S_{\max}(E,H_B)\). |
| QIT-12 | Exterior mass, interior volume, area, or lifetime determines \(H_B\), \(d_B\), or information capacity. | REJECTED | State-space and Hamiltonian prescriptions are independent physical inputs. |
| QIT-13 | Maximally mixed-input optimal recovery is an SDP over a CPTP recovery Choi matrix. | VALID | Implemented and validated against analytic erasure and dephasing optima. |
| QIT-14 | Agreement of fixed-input recovery and complementary-state calculations proves a channel-wide worst-case theorem. | REJECTED | The comparison is fixed-input only. |
| QIT-15 | The identity decoder is globally optimal for every amplitude-damping parameter. | UNRESOLVED | The recovery SDP certifies sampled instances; no universal analytic statement is claimed. |
| QIT-16 | Symmetry, conserved charge, and superselection strengthen the current resource bounds. | UNRESOLVED | Next theorem-development target. |
| QIT-17 | A channel-wide or energy-constrained diamond-norm information–disturbance bound is implemented. | REJECTED | No diamond norm is currently computed. |
| QIT-18 | A Page curve or island entropy calculation proves operational recovery of the complete input from arbitrary radiation. | REJECTED | Entropy of a declared region is not a decoder and does not characterize arbitrary subdivisions. |
| QIT-19 | A solar-mass black hole requires approximately \(10^{77}\) quantum gates to decode. | REJECTED | The order \(10^{77}\) is associated with entropy scale, not a universal decoding gate count; complexity statements require a defined task and model. |
| QIT-20 | Quantum Darwinism is the established mechanism explaining Hawking thermality and information recovery. | REJECTED | It is not required by the channel analysis and has not been established as the black-hole recovery mechanism. |
| QIT-21 | Global preservation guarantees practical reconstruction by an asymptotic observer. | REJECTED | Recovery depends on accessible algebra, channel knowledge, error criterion, and computational resources. |

---

## Numerical results

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| NUM-01 | The recovery Choi SDP reproduces analytic erasure and dephasing optima. | VALID | Pinned CVXPY/Clarabel CI passed all nine optimization tests; recovery status is `optimal`. |
| NUM-02 | Recovery Choi matrices satisfy CPTP feasibility within declared tolerances. | VALID | Maximum trace-preservation residual in the generated sweep is \(3.33	imes10^{-16}\); minimum reported eigenvalue is \(-6.02	imes10^{-13}\). |
| NUM-03 | The environment-fidelity optimization is an independent numerical diagnostic. | CONDITIONAL | Maximum cross-formulation gap in the sweep is \(8.40	imes10^{-5}\), below the \(1.5	imes10^{-4}\) diagnostic tolerance. Some rank-deficient points returned `optimal_inaccurate`, so this side is not called a certificate. |
| NUM-04 | A solver-reported `optimal_inaccurate` status is theorem-grade evidence. | REJECTED | It may be retained as a documented diagnostic only. |
| NUM-05 | A cross-formulation gap is the conic solver's primal–dual gap. | REJECTED | It compares two physical formulations; it is not an internal solver duality gap. |

---

## Holography and gravity claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| GR-01 | Page-curve behavior can arise in controlled evaporating holographic models through QES/islands. | CONDITIONAL | Applies only to specified models, bath couplings, regions, and approximations. |
| GR-02 | A Page curve proves uniform information distribution across all outputs. | REJECTED | It constrains a declared radiation region, not arbitrary subchannels. |
| GR-03 | Boundary unitarity implies every reduced bulk output channel is isometric. | REJECTED | Reduced channels may be non-isometric after tracing inaccessible degrees. |
| GR-04 | AdS/CFT applies directly to an asymptotically flat loop-inspired transition. | REJECTED | A duality map is required; JT gravity is a separate benchmark. |
| GR-05 | Black-to-white transition and white-hole remnant scenarios exist in the literature. | VALID | Physical realization remains model dependent. |
| GR-06 | A causal diagram or metric alone determines a microscopic channel. | REJECTED | State spaces, dynamics, couplings, and observer algebras are additionally required. |
| GR-07 | The HRS effective geometry supplies explicit large-scale metric functions, bounce radius, and horizon roots. | CONDITIONAL | Valid within its assumptions and \(G=c=1\); regression tests reproduce the formulas and limits. |
| GR-08 | The HRS geometry supplies Hawking evaporation, tunnelling probability, a remnant Hamiltonian, or decoder. | REJECTED | These are absent from the construction. |
| GR-09 | Interior volume automatically measures remnant information capacity. | REJECTED | No volume-to-Hilbert-space map is supplied. |
| GR-10 | A recoverability theorem follows from HRS/Bianchi without added microscopic inputs. | GATED | Current admissible result is a parameterized bound or underdetermination theorem. |
| GR-11 | Conditional reconstruction can be studied in a specified JT-bath code subspace. | CONDITIONAL | Requires a declared setup, radiation algebra, theorem, and error. |
| GR-12 | LQG or LQC has established that all physical black holes undergo a bounce driven by universal repulsive quantum pressure. | REJECTED | Bounce behavior is model dependent; symmetry-reduced or effective results do not establish a universal full-theory prediction. |
| GR-13 | Quantum gravity has reached consensus that collapse must produce a white-hole burst. | REJECTED | This is a family of proposed scenarios, not an established consensus. |
| GR-14 | Singularity resolution, transition geometry, remnant dynamics, and holographic islands are one common theory. | REJECTED | They are distinct frameworks with different assumptions and observables. |

---

## Phenomenology claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| PH-01 | \(2GM/c^3\) is the Schwarzschild light-crossing baseline. | VALID | Dimensional gravitational scale. |
| PH-02 | For \(M=10^{12}\,\mathrm{kg}\), \(2GM/c^3\approx10^{-5}\,\mathrm{s}\). | REJECTED | The value is approximately \(4.95	imes10^{-24}\,\mathrm{s}\). |
| PH-03 | The light-crossing time is automatically an observed burst duration. | REJECTED | A source, propagation, and detector model must connect the scales. |
| PH-04 | Named instruments constrain a generic bounce. | REJECTED | Instrument claims require a concrete signal and population model. |
| PH-05 | Existing broker infrastructure may be preferable to an independent pipeline. | CONDITIONAL | Only if a validated signal overlaps the broker's cadence and products. |
| PH-06 | A generic white-hole search improves limits by one or two orders of magnitude. | REJECTED | No validated efficiency, background, signal, or population calculation supports it. |
| PH-07 | Observational work proceeds only after the feasibility gate. | GATED | The HRS/Bianchi track lacks a complete forward model. |
| PH-08 | A model-dependent PBH-to-white-hole rate calculation establishes a generic transient explanation. | REJECTED | Conclusions depend on PBH abundance, tunnelling, mass-function, and emission assumptions. |
| PH-09 | Primordial black holes across \(10^{11}\)–\(10^{13}\,\mathrm{kg}\) are generically expected to transition in the present epoch. | REJECTED | Present-epoch rates require a declared lifetime law, initial mass function, evaporation history, abundance, and transition model. |
| PH-10 | Rubin, ULTRASAT, CTA, or Gaia constitutes a dedicated validated white-hole search program. | REJECTED | A general survey capability is not evidence of a validated source-specific search. |
| PH-11 | A general transient survey capability authorizes a multi-messenger forecast. | REJECTED | The source-to-detector chain must be complete and unit tested. |

---

## Analogue-gravity claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| AG-01 | Analogue horizons can benchmark mode conversion or reconstruction. | CONDITIONAL | Specify Hamiltonian, channel, modes, and task. |
| AG-02 | A BEC horizon directly tests Planck-scale bounce dynamics. | REJECTED | It does not reproduce gravitational microscopic dynamics. |
| AG-03 | Analogue tomography may support a later methods paper. | GATED | Requires a mature protocol and experimental collaborator. |

---

## Communication and analogy claims

| ID | Claim | Status | Correction or evidence requirement |
|---|---|---|---|
| COM-01 | Paper folding can illustrate the breakdown of a classical description at extreme curvature. | CONDITIONAL | It must be labeled an analogy and not a derivation of a bounce. |
| COM-02 | Shredded-paper reconstruction can illustrate the distinction between preservation and operational decoding. | CONDITIONAL | Access, channel knowledge, accuracy, and computational complexity must be stated. |
| COM-03 | Ink dispersing in water can illustrate scrambling across a larger system. | CONDITIONAL | Radiation, retained degrees, and environment must remain separate sectors. |
| COM-04 | An intuitive analogy establishes scientific consensus. | REJECTED | Analogies communicate a model; they do not validate it. |

---

## Required terminology

| Term | Required usage |
|---|---|
| LQG | Loop quantum gravity |
| LQC | Loop quantum cosmology |
| Information after a channel | Correlations with an explicit purifying reference |
| Information escaped | A declared recovery task succeeds from a specified algebra within quantified error |
| Bounce model | Named equations, boundary conditions, and validity domain |
| Recovery certificate | `optimal` solver status plus accepted feasibility and analytic-benchmark residuals |
| Environment diagnostic | Independent calculation that may include `optimal_inaccurate` values under a declared diagnostic tolerance |
| Detection forecast | Source population, response, efficiency, backgrounds, and statistics |
| Analogy | Communication aid with no evidentiary status |

---

## Validation status

Completed:

1. pure-state identities, biased isometries, and random checks;
2. open-channel and adversarial diagnostics;
3. finite-dimension and finite-Hamiltonian bounds;
4. state-specific decoupling diagnostics;
5. pinned recovery SDP tests and generated optimization artifacts;
6. Schwarzschild regression tests;
7. HRS geometry, horizon, and asymptotic tests;
8. norm, theorem, model, publication, provenance, and canonical-claim ledgers;
9. automated public-language validation.

Next gates:

1. independent QIT review of the recovery objective and convention mapping;
2. worst-case Bény–Oreshkov and KSW theorem reconstruction;
3. charge and symmetry constraints;
4. formal HRS/Bianchi underdetermination theorem;
5. exact JT-bath setup and code subspace;
6. continued phenomenology block until a complete signal model exists.
