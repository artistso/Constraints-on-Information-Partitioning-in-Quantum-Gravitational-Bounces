# Notebook and Simulation Plan

No numerical result is accepted into the manuscript unless it can be reproduced from this directory or from the tested `src/qgbounce` package.

## Implemented foundation

The executable package now contains two validated layers:

- `src/qgbounce/quantum.py` — density matrices, partial traces, entropy, mutual information, explicit localization isometries, and Haar-random isometries.
- `src/qgbounce/channels.py` — Kraus channels, Stinespring dilations, Choi states, coherent information, Holevo information, erasure, dephasing, depolarizing, and amplitude damping.
- `src/qgbounce/recovery.py` — entanglement fidelity, average state fidelity, Choi trace distance, purified distance, and explicit decoder diagnostics.
- `src/qgbounce/remnants.py` — finite-remnant mutual-information caps, radiation lower bounds, extremal encodings, and random-isometry sampling.
- `src/qgbounce/gravity.py` — unit-explicit Schwarzschild radius, light-crossing time, Hawking temperature, and leading evaporation-time baselines.
- `scripts/run_stress_tests.py` — pure-isometry and gravitational-scale products.
- `scripts/run_channel_stress_tests.py` — open-channel, recovery, and finite-remnant products.
- `tests/` — regression tests for exact identities, channel formulas, recovery metrics, dimensional caps, and physical scales.
- `docs/SIMULATION_PROTOCOL.md` and `docs/CHANNEL_STRESS_TEST_PROTOCOL.md` — equations, scope boundaries, and failure policy.

This package-first approach prevents notebook state, manually edited cells, or hidden execution order from becoming the sole source of a result.

## Planned notebooks

1. `01_entropy_identities.ipynb`  
   Present and symbolically verify the pure-state entropy relations and mutual-information sum identity already enforced by package tests.

2. `02_isometric_counterexamples.ipynb`  
   Visualize the identity-to-one-port family, complementary channels, secret-sharing encodings, and random-isometry information-localization region.

3. `03_recovery_decoupling.ipynb`  
   Convert the implemented erasure, dephasing, amplitude-damping, Choi-distance, and decoder diagnostics into a publication-facing notebook. Add decoupling inequalities only after constants and norm conventions are independently checked.

4. `04_symmetry_energy_constraints.ipynb`  
   Extend the implemented finite-remnant dimension bound to conserved charge, superselection sectors, and energy-constrained state spaces.

5. `05_model_scale_checks.ipynb`  
   Expand the Schwarzschild baselines into unit-aware comparisons with model-specific transition, propagation, and emission scales.

6. `06_signal_forward_model.ipynb`  
   Created only after a selected bounce model provides a complete emission and event-rate prescription.

7. `07_injection_recovery.ipynb`  
   Created only after the phenomenology gate passes.

## Reproduction

```bash
python -m pip install -e ".[test]"
pytest
python scripts/run_stress_tests.py
python scripts/run_channel_stress_tests.py
```

## Engineering requirements

- Fixed random seeds for stochastic experiments.
- Assertions for entropy identities, positivity, isometry, Kraus completeness, and trace preservation.
- Unit-explicit physical calculations.
- Parameter provenance stored beside each calculation.
- No manually entered plot points.
- Exported figures generated from source code.
- Baseline decoders must not be described as optimal unless optimization is proved or independently certified.
- Environment lock file added before the first reproducibility release.
