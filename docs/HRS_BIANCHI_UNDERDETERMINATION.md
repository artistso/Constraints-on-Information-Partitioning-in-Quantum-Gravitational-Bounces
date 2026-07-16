# HRS/Bianchi Information-Channel Underdetermination Result

## Purpose

The Han--Rovelli--Soltani geometry supplies an effective metric and causal scaffold. The Bianchi et al. scenario supplies a proposed remnant life cycle. Neither source specifies the microscopic map from infalling quantum states to radiation and retained degrees of freedom.

This document formalizes what follows from that missing structure.

## Geometric descriptor

Let

\[
\mathfrak G=(g_{\mu\nu},\mathcal B,\tau,\mathcal O)
\]

denote all currently declared geometric data:

- effective metric and parameter domain;
- bounce and horizon structure;
- transition-duration parameters;
- candidate observer regions and time slices.

A quantum information model additionally requires

\[
\mathfrak Q=(\mathcal H_X,\mathcal H_A,\mathcal H_B,\mathcal H_E,
\mathcal N,\mathcal A_{\mathrm{obs}}),
\]

including state spaces, a channel or isometric extension, and an observer algebra.

## Proposition — geometry-only non-identifiability

Suppose a geometric model specifies \(\mathfrak G\) but provides no rule

\[
\Gamma:\mathfrak G\longmapsto\mathfrak Q
\]

that uniquely fixes the state spaces and channel. Then information localization and recovery are not identifiable from \(\mathfrak G\) alone.

### Proof by explicit channel non-uniqueness

Choose a finite logical input \(X\), reference \(R\), and output systems \(A,B\) large enough to contain \(X\). Consider the two exact isometries

\[
V_A|\psi\rangle_X
=|\psi\rangle_A|0\rangle_B,
\]

and

\[
V_B|\psi\rangle_X
=|0\rangle_A|\psi\rangle_B.
\]

Both are compatible with global purity and with the same abstract division into an outgoing sector and a retained sector. Yet for a purified input they give

\[
I(R:A)=2S(R),\quad I(R:B)=0
\]

and

\[
I(R:A)=0,\quad I(R:B)=2S(R),
\]

respectively. Their optimal radiation recovery fidelities are therefore different.

If \(\mathfrak G\) contains no microscopic rule that excludes one map or selects the other, the geometric data cannot determine the information channel. The same argument applies to continuous families of channels between these extremes. \(\square\)

## Corollary — no volume-to-capacity inference

Interior volume, exterior mass, horizon radii, and transition duration cannot by themselves determine

- a Hilbert-space dimension;
- a Hamiltonian spectrum;
- a charge-sector decomposition;
- a channel;
- a decoder fidelity.

Any such inference requires an additional map from geometric quantities to quantum state-space structure.

## Corollary — admissible publication outcomes

Until the missing map is supplied, the HRS/Bianchi track can produce only:

1. source-level geometric validation;
2. conditional information bounds under declared state-space assumptions;
3. excluded regions within a parameterized channel family;
4. a formal statement of underdetermination and the minimal data required to remove it.

A simulated channel chosen only for convenience is a benchmark, not a prediction of the geometry.

## Minimal assumptions that would reduce underdetermination

At least one of the following must be supplied and justified:

- an effective microscopic Hamiltonian and interaction law;
- a path-integral or canonical transition amplitude defining the map;
- an algebraic evolution rule for observables;
- a code-subspace encoding and reconstruction prescription;
- a remnant state-counting law plus a radiation coupling;
- a complementary-channel decoupling condition derived from the gravitational model.

## Falsifiability

This result is overturned for a particular model only when that model supplies enough microscopic structure to select or constrain \(\mathfrak Q\). The burden is constructive: write the channel, Hamiltonian, amplitude, algebraic map, or theorem that removes the non-uniqueness.

## Status

**PROVED-HERE as a model-identifiability proposition.**

The proposition does not say that no microscopic theory exists. It says that the presently selected effective geometry and remnant narrative do not uniquely specify one.
