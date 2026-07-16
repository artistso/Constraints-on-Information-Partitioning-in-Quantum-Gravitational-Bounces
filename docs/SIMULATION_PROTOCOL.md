# Simulation and Stress-Test Protocol v0.1

## Purpose

The first simulation layer tests claims that must be true before any gravitational interpretation is introduced. It then calculates semiclassical physical scales that every proposed bounce phenomenology must distinguish from its model-specific transition and emission scales.

## Simulation A — Information localization under exact isometries

### State and channel

A reference qubit \(R\) purifies an input qubit \(X\) in a maximally entangled state. An isometry maps \(X\) into two output qubits \(A\) and \(B\).

The parameterized family is

\[
V_\theta |0\rangle = |00\rangle,\qquad
V_\theta |1\rangle =
\cos\theta\,|10\rangle+\sin\theta\,|01\rangle.
\]

At \(\theta=0\), all recoverable quantum information is localized in \(A\). At \(\theta=\pi/2\), it is localized in \(B\). Intermediate values provide a continuous stress test.

### Invariant

For the pure output state on \(RAB\),

\[
I(R:A)+I(R:B)=2S(R).
\]

The code asserts this identity numerically. It does not assume equal partitioning.

### Random stress test

Haar-random isometries from one qubit to two qubits are drawn using the complex Ginibre/QR construction. Every sample must satisfy the same sum identity to floating-point tolerance. The resulting point cloud maps the allowed information localization for this fixed input and subsystem dimension.

## Simulation B — Semiclassical gravitational baselines

For a Schwarzschild mass \(M\), the suite evaluates

\[
r_s=\frac{2GM}{c^2},\qquad
t_{\rm cross}=\frac{2GM}{c^3},
\]

\[
T_H=\frac{\hbar c^3}{8\pi GMk_B},
\qquad
\tau_{\rm evap}^{(0)}
=\frac{5120\pi G^2M^3}{\hbar c^4}.
\]

The lifetime is a leading textbook estimate. It omits spin, charge, greybody factors, particle thresholds, backreaction refinements, and quantum-gravity effects.

These quantities are baselines only. A bounce duration, propagation delay, ejecta diffusion time, detector integration time, or event rate requires an independent model and may not be substituted with \(t_{\rm cross}\).

## Reproducibility

```bash
python -m pip install -e ".[test]"
pytest
python scripts/run_stress_tests.py
```

Generated outputs are written below `outputs/` and are intentionally ignored by Git. Figures accepted for publication must be regenerated in a versioned release workflow with parameter provenance and environment metadata.

## Failure policy

A failed assertion blocks the associated claim. Numerical disagreement is recorded in `docs/VALIDITY_LEDGER.md`; it is not repaired by adjusting plot data, random seeds, tolerances, or physical constants without documented justification.
