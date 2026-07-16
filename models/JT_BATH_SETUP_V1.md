# JT-Bath Benchmark Setup v1

## Role

This setup fixes the first controlled holographic benchmark. It is not a black-to-white-hole bounce model and is not used to infer properties of the HRS/Bianchi track.

## Selected system

- A two-dimensional Jackiw--Teitelboim gravitating region.
- Quantum matter coupled to a non-gravitating bath.
- A finite diary/code subsystem inserted into the gravitating region.
- A reference system `R` purifying the diary.
- A declared bath radiation region `A(t)` collected up to time `t`.
- The complement `B(t)` containing the remaining gravitating region and uncollected bath degrees of freedom.

Primary source families: `Penington2019`, `AlmheiriEtAl2019Bulk`, and `AlmheiriEtAl2019Replica`.

## Entropy calculation

The gravitational calculation must specify candidate quantum extremal surfaces and evaluate

\[
S_{\mathrm{gen}}(X)
=
\frac{\operatorname{Area}(\partial X)}{4G_N}
+S_{\mathrm{bulk}}(X),
\]

with the two-dimensional dilaton term replacing geometric area where appropriate. The radiation entropy is obtained from the minimum generalized-entropy saddle under the declared model assumptions.

The repository will not treat this entropy calculation as an explicit decoder.

## Code and observer definition

The benchmark must record:

- diary dimension `d_X`;
- code-subspace dimension and energy range;
- diary insertion time and state ensemble;
- bath coupling and boundary conditions;
- radiation interval or algebra `A(t)`;
- candidate island and quantum extremal surface;
- approximation regime in `G_N`, matter central charge, and backreaction;
- reconstruction theorem and declared error.

## Information-theoretic quantities

For a finite-dimensional surrogate calibrated to the entropy balance, calculate:

\[
I(R:A(t)),
\qquad
I(R:B(t)),
\qquad
I_c(R\rangle A(t)),
\]

plus:

- complementary-output decoupling;
- fixed-input optimal recovery fidelity;
- worst-case recovery only after the Bény--Oreshkov implementation exists;
- diamond-norm recovery only after the KSW implementation exists;
- dependence on code-subspace dimension.

## Stage 1 — entropy and subsystem audit

1. Reproduce one published pre-Page and post-Page generalized-entropy comparison.
2. Record every parameter and convention.
3. Verify which radiation region is being assigned an island.
4. Identify the code-subspace statement actually supported by the source.
5. Prohibit extrapolation to arbitrary bath subregions.

## Stage 2 — finite-dimensional surrogate

Construct an explicitly labeled surrogate channel whose dimensions follow a declared entropy balance. The surrogate may test recovery machinery, but it is not called a numerical simulation of JT gravity.

Required controls:

- pre-Page channel with substantial complementary leakage;
- post-Page channel with declared environmental decoupling;
- equal-entropy adversarial channels with different decoder fidelity;
- code-subspace sweep;
- comparison between fixed-input and worst-case diagnostics.

## Stage 3 — reconstruction statement

A benchmark result may be promoted only after it states:

- the operator or algebra reconstructed;
- the radiation region used;
- the code subspace;
- the approximation error;
- whether reconstruction is existential or constructive;
- whether the result is state dependent;
- which theorem connects entanglement-wedge inclusion to recovery.

## Nonclaims

This setup does not establish that:

- every evaporating black hole has the same island structure;
- all outgoing radiation subregions contain the diary;
- a Page curve is a decoder;
- JT gravity is dynamically equivalent to an asymptotically flat remnant;
- holographic reconstruction determines the HRS/Bianchi channel.

## Acceptance gate

The setup is ready for executable implementation when one source calculation has been transcribed with complete parameters and independently checked. Until then, it is a controlled specification document.
