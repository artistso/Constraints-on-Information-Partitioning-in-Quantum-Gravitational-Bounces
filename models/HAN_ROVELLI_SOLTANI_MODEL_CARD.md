# Model Card — Han–Rovelli–Soltani Single-Asymptotic-Region Geometry

## Identity

- **Model name:** Singular-free black-to-white-hole transition geometry in one asymptotic region
- **Primary source:** `HanRovelliSoltani2023`
- **Model class:** effective loop-inspired geometry with an Oppenheimer–Snyder/LQC interior and a local horizon-tunnelling region
- **Role:** principal geometric scaffold for the non-holographic track

## Source-level content

The source constructs an explicit Lorentzian metric for a black-to-white-hole transition in the same asymptotic region. It separates three physical regions:

- stellar collapse and bounce;
- the interior/exterior effective geometry;
- a local horizon-tunnelling region.

Outside the tunnelling region, the effective pressureless-star scale factor in natural units is

\[
a(T)=\left(\frac{9mT^2+Am}{2}\right)^{1/3},
\]

and the static exterior function is

\[
F(r)=1-\frac{2m}{r}+\frac{Am^2}{r^4}.
\]

For \(m^2\gg A\), the positive roots satisfy

\[
r_+\simeq2m,
\qquad
r_-\simeq\left(\frac{Am}{2}\right)^{1/3}.
\]

The large-scale geometry is described by the mass and a global transition-duration parameter. Local parameters characterize the tunnelling region.

## Explicit source limitations

The source:

- neglects Hawking radiation in the constructed geometry;
- neglects rotation;
- treats quantum effects through effective local violations of Einstein’s equations rather than a full quantum state analysis;
- does not calculate the tunnelling probability;
- describes the interpolating tunnelling geometry as a proof of geometric existence, not as a literal physical trajectory;
- does not provide a Hilbert space, Hamiltonian, microscopic unitary, Kraus operators, or radiation decoder.

These limitations are controlling assumptions, not footnotes.

## Implemented geometric baseline

`src/qgbounce/geometry.py` implements only the source-level large-scale formulas:

- `hrs_scale_factor`;
- `hrs_bounce_radius`;
- `hrs_exterior_function`;
- positive real horizon roots;
- asymptotic consistency checks.

`scripts/run_geometry_stress_tests.py` generates:

- mass-dependent bounce, inner-horizon, and outer-horizon radii;
- residuals of \(F(r_\pm)=0\);
- convergence to the large-mass asymptotic formulas;
- the symmetric effective stellar bounce.

The implementation uses \(G=c=1\). It does not infer SI event durations or observable signals.

## Quantum-information translation

- **Input `X`:** a declared finite code subspace of infalling matter/microstate degrees of freedom.
- **Reference `R`:** external purifier.
- **Radiation `A`:** requires a time cut and a radiation model not supplied by the static geometric baseline.
- **Retained sector `B`:** interior/remnant algebra on the declared slice.
- **Environment `E`:** unresolved quantum geometry, omitted dissipation, or any degrees traced from the effective treatment.

The metric determines causal and geometric structure. It does not determine the channel

\[
X\longrightarrow A\otimes B\otimes E.
\]

## First admissible calculations

1. Verify geometric equations, horizon roots, and limiting regimes.
2. Use the geometry to define candidate slices and observer algebras.
3. Preserve transition duration as a free global parameter unless a quantum calculation supplies a distribution.
4. Add Hawking/backreaction phenomenologically only in a separate, explicitly sourced extension.
5. Apply finite-dimension or energy-constrained information bounds only after a remnant state-space or Hamiltonian assumption is declared.

## Prohibited inferences

- The bounce radius is a Hilbert-space dimension.
- Interior volume is automatically information capacity.
- Transition duration is fixed by \(2GM/c^3\).
- The effective metric defines a unitary channel.
- Horizon roots determine a radiation spectrum.
- The existence geometry validates a particular tunnelling probability.

## Claim coordinates

- **A:** spherical symmetry, pressureless homogeneous star, effective LQC correction, neglected rotation/dissipation, local tunnelling violation, declared parameter regime.
- **M:** Han–Rovelli–Soltani effective geometry.
- **Q:** metric functions, horizon radii, causal accessibility; information quantities only after extra channel assumptions.
- **O:** specified asymptotic observer and time cut.
- **E:** source equations, analytic root checks, deterministic numerical validation.
- **P:** geometry baseline validated; channel mapping unresolved.

## Decision

**Include as the geometric scaffold, not as a microscopic information model.**

The next valid output is a parameter-provenance and underdetermination analysis connecting this geometry to the Bianchi et al. remnant scenario. A quantum-channel simulation remains blocked until the missing state-space and coupling inputs are supplied.
