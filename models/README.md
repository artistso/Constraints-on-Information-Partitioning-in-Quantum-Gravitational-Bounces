# Selected Model Tracks

The project now separates geometric, remnant, and holographic questions so that no result is transferred across incompatible models.

## Track A — Non-holographic transition and remnant constraints

### Geometric scaffold

**Han–Rovelli–Soltani 2023** (`HanRovelliSoltani2023`) is the principal explicit geometry. It supplies a singularity-free Lorentzian black-to-white transition in one asymptotic region, an effective Oppenheimer–Snyder/LQC stellar bounce, an exterior metric, horizon structure, and a free global transition duration.

Implemented artifacts:

- `models/HAN_ROVELLI_SOLTANI_MODEL_CARD.md`;
- `src/qgbounce/geometry.py`;
- `tests/test_geometry.py`;
- `scripts/run_geometry_stress_tests.py`.

The geometry is a causal and metric scaffold. It does not supply a quantum channel or information capacity.

### Remnant endpoint

**Bianchi et al. 2018** (`BianchiEtAl2018`) remains the primary remnant-life-cycle scenario, with **Haggard–Rovelli 2014** (`HaggardRovelli2014`) retained as historical/supporting tunnelling structure.

The remnant track uses:

- `models/BIANCHI_REMNANT_MODEL_CARD.md`;
- `models/REMNANT_PARAMETER_PROVENANCE.md`;
- finite-dimension and finite-Hamiltonian entropy bounds.

It is treated as a parametric capacity/underdetermination problem, not as a completed microscopic channel.

## Track B — Controlled holographic benchmark

**Selected benchmark:** two-dimensional Jackiw–Teitelboim gravity coupled to quantum matter and a non-gravitating bath, using replica-wormhole/island calculations (`AlmheiriEtAl2019Replica`) and entanglement-wedge reconstruction (`Penington2019`).

This track provides a controlled setting for Page transitions, radiation entropy, code subspaces, and reconstruction criteria. It is not identified with a loop-inspired transition or an asymptotically flat white-hole remnant.

Artifact:

- `models/JT_BATH_BENCHMARK_CARD.md`.

## Separation rule

No statement proved in the JT-bath benchmark is transferred to the HRS/Bianchi track unless an explicit map of assumptions, observables, algebras, and approximation errors is supplied.

Likewise, geometric quantities such as horizon radii, interior volume, or transition duration are not converted into Hilbert-space dimensions, Hamiltonians, or decoder fidelities without an independent physical derivation.

## Immediate deliverables

1. Validate the HRS large-scale geometry and limiting regimes.
2. Complete the remnant source/provenance inventory.
3. Apply finite-dimension or finite-Hamiltonian bounds only to declared state-space assumptions.
4. Add certified recovery and environment-side optimization.
5. Produce a reconstruction/decoupling benchmark for the JT-bath track after norm conventions are fixed.
6. Stop with an underdetermination theorem whenever a microscopic channel is not specified.
