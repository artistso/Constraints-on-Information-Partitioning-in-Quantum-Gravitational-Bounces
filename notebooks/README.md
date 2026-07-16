# Notebook and Simulation Plan

No numerical result is accepted into the manuscript unless it can be reproduced from this directory or from the tested `src/qgbounce` package.

## Implemented foundation

The first executable layer is now available before notebook conversion:

- `src/qgbounce/quantum.py` — density matrices, partial traces, entropy, mutual information, explicit localization isometries, and Haar-random isometries.
- `src/qgbounce/gravity.py` — unit-explicit Schwarzschild radius, light-crossing time, Hawking temperature, and leading evaporation-time baselines.
- `scripts/run_stress_tests.py` — deterministic CSV and figure generation.
- `tests/` — regression tests for exact information identities, biased-channel counterexamples, trace preservation, mass scalings, and the corrected `2GM/c^3` value.
- `docs/SIMULATION_PROTOCOL.md` — assumptions, equations, scope, and failure policy.

This package-first approach prevents notebook state, manually edited cells, or hidden execution order from becoming the sole source of a result.

## Planned notebooks

1. `01_entropy_identities.ipynb`  
   Present and symbolically verify the pure-state entropy relations and mutual-information sum identity already enforced by the package tests.

2. `02_isometric_counterexamples.ipynb`  
   Visualize the identity-to-one-port family, complementary channels, secret-sharing encodings, and random-isometry information-localization region.

3. `03_recovery_decoupling.ipynb`  
   Compare decoupling measures, coherent information, and optimal or bounded recovery fidelities.

4. `04_symmetry_energy_constraints.ipynb`  
   Test candidate conditional bounds under finite dimension, conserved charge, and energy constraints.

5. `05_model_scale_checks.ipynb`  
   Expand the implemented Schwarzschild baselines into unit-aware comparisons with model-specific transition, propagation, and emission scales.

6. `06_signal_forward_model.ipynb`  
   Created only after a selected bounce model provides a complete emission and event-rate prescription.

7. `07_injection_recovery.ipynb`  
   Created only after the phenomenology gate passes.

## Reproduction

```bash
python -m pip install -e ".[test]"
pytest
python scripts/run_stress_tests.py
```

## Engineering requirements

- Fixed random seeds for stochastic experiments.
- Assertions for entropy identities, positivity, isometry, and trace preservation.
- Unit-explicit physical calculations.
- Parameter provenance stored beside each calculation.
- No manually entered plot points.
- Exported figures generated from source code.
- Environment lock file added before the first reproducibility release.
