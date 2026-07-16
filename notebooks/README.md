# Notebook and Simulation Plan

No numerical result enters a manuscript unless it is reproduced by the tested `src/qgbounce` package and then presented transparently in a publication-facing notebook.

## Implemented package layers

### Quantum channels

- `quantum.py` — states, partial traces, entropy, mutual information, explicit and Haar-random isometries.
- `channels.py` — Kraus maps, Stinespring dilations, Choi states, coherent and Holevo information, standard noise channels.
- `recovery.py` — explicit-decoder entanglement and average fidelity, Choi trace and purified distances.
- `decoupling.py` — complementary-state mutual information, product-state distances, Pinsker and Uhlmann diagnostics.
- `optimization.py` — pinned recovery and environment-side fidelity SDPs with residual certificates.

### Resource constraints

- `remnants.py` — finite-dimension mutual-information caps.
- `energy.py` — finite-spectrum Gibbs entropy and mean-energy-constrained correlation bounds.
- `symmetry.py` — finite charge-sector and superselection entropy caps.

### Gravity and geometry

- `gravity.py` — SI Schwarzschild baseline scales.
- `geometry.py` — Han–Rovelli–Soltani natural-unit scale factor, exterior function, bounce radius, and horizon roots.

### Deterministic runners

- `scripts/run_stress_tests.py`
- `scripts/run_channel_stress_tests.py`
- `scripts/run_theorem_stress_tests.py`
- `scripts/run_geometry_stress_tests.py`
- `scripts/run_symmetry_stress_tests.py`

## Publication-facing notebook sequence

1. `01_entropy_identities.ipynb`  
   Pure-state identities, reference-system formulation, and rejected equal-partition claim.

2. `02_isometric_counterexamples.ipynb`  
   One-port encodings, random isometries, feasible localization regions, and secret-sharing examples.

3. `03_open_channels_and_adversarial_pairs.ipynb`  
   Erasure, dephasing, depolarizing, amplitude damping, and channels sharing one diagnostic while differing operationally.

4. `04_certified_recovery.ipynb`  
   Recovery Choi SDP, environment-side fidelity SDP, analytic erasure/dephasing standards, feasibility residuals, solver status, and cross-formulation gap.

5. `05_finite_resource_bounds.ipynb`  
   Finite dimension, Gibbs entropy, energy caps, charge sectors, superselection, and the conditions under which sector data improve the total-dimension cap.

6. `06_imported_recovery_theorems.ipynb`  
   Bény–Oreshkov worst-case fidelity duality, KSW cb/diamond information–disturbance constants, convention mapping, and explicit separation from the fixed-input SDP.

7. `07_hrs_geometry.ipynb`  
   HRS effective bounce, exterior function, horizon roots, large-mass limits, and explicit scope exclusions.

8. `08_remnant_underdetermination.ipynb`  
   HRS/Bianchi parameter provenance, explicit channel non-uniqueness, and the distinction between geometry, state space, Hamiltonian, channel, and decoder.

9. `09_jt_bath_benchmark.ipynb`  
   Created after one published JT setup is transcribed with complete code-subspace, radiation-region, and reconstruction conventions.

10. `10_signal_forward_model.ipynb`  
    Created only after a gravitational model passes the phenomenology gate.

11. `11_injection_recovery.ipynb`  
    Created only after a detector-level signal model is authorized.

## Reproduction

Base suite:

```bash
python -m pip install -e ".[test]"
python scripts/check_claim_language.py
pytest -m "not optimization"
python scripts/run_stress_tests.py
python scripts/run_channel_stress_tests.py
python scripts/run_geometry_stress_tests.py
python scripts/run_symmetry_stress_tests.py
```

Optimization suite:

```bash
python -m pip install -e ".[test,optimization]"
pytest -m optimization
python scripts/run_theorem_stress_tests.py
```

## Engineering requirements

- Fixed random seeds.
- Assertions for positivity, trace preservation, isometry, entropy identities, sector constraints, and geometric roots.
- Exact norm and Choi conventions from `docs/NORM_CONVENTIONS.md`.
- Imported theorem conventions controlled by `docs/APPROXIMATE_RECOVERY_THEOREM_MAP.md`.
- Solver, status, iterations, objective, and residuals stored with every convex certificate.
- No manually entered plot points.
- No baseline decoder described as optimal without proof or certification.
- Geometry outputs never relabeled as channel or detector predictions.
- Top-level optimization pins are committed; a complete platform lock is required before a tagged certificate release.
