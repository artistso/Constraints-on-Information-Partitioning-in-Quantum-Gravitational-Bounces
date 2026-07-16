# Norm, Fidelity, Choi, and Optimization Conventions

This document fixes the conventions used by every theorem, regression test, and numerical certificate. A result using another convention must provide an explicit conversion.

## Logarithms and entropy

All entropies and mutual informations use base-two logarithms and are measured in bits:

\[
S(\rho)=-\operatorname{Tr}(\rho\log_2\rho).
\]

## Trace norm and trace distance

For an operator \(X\),

\[
\|X\|_1=\operatorname{Tr}\sqrt{X^\dagger X}.
\]

For density operators,

\[
T(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
\]

No quantity called “trace distance” in this repository omits the factor of one half.

## Fidelity

The **root fidelity** is

\[
f(\rho,\sigma)=\left\|\sqrt\rho\sqrt\sigma\right\|_1.
\]

The **squared fidelity** is

\[
F(\rho,\sigma)=f(\rho,\sigma)^2.
\]

For a pure target \(|\psi\rangle\),

\[
F(\rho,|\psi\rangle)=\langle\psi|\rho|\psi\rangle.
\]

The purified distance is

\[
P(\rho,\sigma)=\sqrt{1-F(\rho,\sigma)}.
\]

The Fuchs–van de Graaf inequalities are therefore written

\[
1-f(\rho,\sigma)\leq T(\rho,\sigma)\leq P(\rho,\sigma).
\]

## Entanglement fidelity

For a channel \(\mathcal N:X\to X'\) with \(\dim X=\dim X'=d\), evaluated on the maximally mixed input, the entanglement fidelity is the squared overlap

\[
F_e(\mathcal N)
=
\langle\Phi_d|
(\operatorname{id}\otimes\mathcal N)(\Phi_d)
|\Phi_d\rangle,
\]

where

\[
|\Phi_d\rangle=rac1{\sqrt d}\sum_{i=1}^d|i\rangle|i\rangle.
\]

For Kraus operators \(K_i\),

\[
F_e(\mathcal N)=\frac1{d^2}\sum_i|\operatorname{Tr}K_i|^2.
\]

The corresponding Haar-average pure-state fidelity is

\[
F_{\mathrm{avg}}=rac{dF_e+1}{d+1}.
\]

## Choi conventions

### Normalized channel Choi state

For \(\mathcal N:X\to A\),

\[
\rho_{RA}^{\mathcal N}
=(\operatorname{id}_R\otimes\mathcal N)(\Phi_{RX}),
\]

with normalized \(\Phi\). Thus \(\operatorname{Tr}\rho_{RA}^{\mathcal N}=1\).

### Unnormalized optimization Choi matrix

For a recovery \(\mathcal R:A\to X\),

\[
J_{\mathcal R}
=
\sum_{a,b}|a\rangle\langle b|\otimes
\mathcal R(|a\rangle\langle b|).
\]

The tensor ordering is `input_A tensor output_X`. Complete positivity and trace preservation are

\[
J_{\mathcal R}\succeq0,
\qquad
\operatorname{Tr}_XJ_{\mathcal R}=I_A.
\]

The SDP objective in `src/qgbounce/optimization.py` is linear in this unnormalized matrix.

## Environmental decoupling

For the normalized complementary Choi state \(\rho_{RE}\), the default product comparator is

\[
\frac{I_R}{d}\otimes\rho_E.
\]

The state-specific decoupling module reports:

- \(I(R:E)\);
- trace distance to the product;
- purified distance to the product;
- the Uhlmann existence lower bound on maximally mixed-input recovery fidelity.

Quantum Pinsker is used in the base-two convention:

\[
T\!\left(\rho_{RE},\rho_R\otimes\rho_E\right)
\leq
\sqrt{\frac{\ln2}{2}I(R:E)}.
\]

This is a state-specific inequality. It is not a diamond-norm statement about all possible inputs.

## Certified recovery SDP

The primal optimization is

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N).
\]

The environment-side cross-certificate optimizes

\[
\max_{\sigma_E}
F\!\left(
\rho_{RE}^{\mathcal N^c},
\frac{I_R}{d}\otimes\sigma_E
\right).
\]

The implementation compares these two independently modeled quantities for the same maximally mixed input. Their numerical difference is called the **formulation gap**. It is not the internal primal–dual gap reported by a conic solver.

Every numerical certificate records:

- solver and solver status;
- objective value;
- trace-preservation residual;
- minimum Choi eigenvalue;
- environment-state trace and positivity residuals;
- recovery/environment formulation gap.

## Diamond and energy-constrained diamond norms

No diamond norm is currently computed by the executable package. Accordingly:

- no Choi-state distance is labeled a diamond distance;
- no state-specific recovery result is promoted to a channel-wide worst-case theorem;
- the Kretschmann–Schlingemann–Werner and Bény–Oreshkov results are cited as theorem targets until their constants are rederived under these conventions.

An energy-constrained diamond norm will require a declared input Hamiltonian, energy cap, ancillary system convention, and finite approximation or certified infinite-dimensional method.

## Numerical tolerance policy

Analytic finite-dimensional identities use a default acceptance scale of \(10^{-10}\). Conic optimization tests use looser tolerances declared in the individual test because solver canonicalization and complex-to-real conversion introduce additional numerical error.

A solver status of `optimal_inaccurate`, a material positivity violation, or a formulation gap above the declared tolerance blocks theorem-level use of the result.
