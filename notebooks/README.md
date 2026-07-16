# Notebook Plan

No numerical result is accepted into the manuscript unless it can be reproduced from this directory.

## Planned notebooks

1. `01_entropy_identities.ipynb`  
   Symbolically verify the pure-state entropy relations and mutual-information sum identity.

2. `02_isometric_counterexamples.ipynb`  
   Construct identity-to-one-port, erasure, complementary, secret-sharing, and random-isometry examples. Plot the feasible region of \(I(R:A)\) and \(I(R:B)\).

3. `03_recovery_decoupling.ipynb`  
   Compare decoupling measures, coherent information, and optimal or bounded recovery fidelities.

4. `04_symmetry_energy_constraints.ipynb`  
   Test candidate conditional bounds under finite dimension, conserved charge, and energy constraints.

5. `05_model_scale_checks.ipynb`  
   Recalculate all gravitational timescales, masses, energies, and unit conversions with automated dimensional checks.

6. `06_signal_forward_model.ipynb`  
   Created only after a selected bounce model provides a complete emission and event-rate prescription.

7. `07_injection_recovery.ipynb`  
   Created only after the phenomenology gate passes.

## Engineering requirements

- Fixed random seeds for stochastic experiments.
- Assertions for entropy identities and trace preservation.
- Unit-aware physical calculations.
- Parameter provenance stored beside each calculation.
- No manually entered plot points.
- Exported figures generated from source notebooks.
- Environment lock file added before the first reproducibility release.
