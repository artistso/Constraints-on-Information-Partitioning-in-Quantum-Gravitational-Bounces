# Norm, Fidelity, Choi, and Optimization Conventions

This document fixes the conventions used by every theorem, regression test, and numerical result. Any result using another convention must provide an explicit conversion.

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

The Fuchs–van de Graaf inequalities are written

\[
1-f(\rho,\sigma)\leq T(\rho,\sigma)\leq P(\rho,\sigma).
\]

## Entanglement fidelity

For a channel \(\mathcal N:X\to X'\) with equal input and output dimension \(d\), evaluated on the maximally mixed input,

\[
F_e(\mathcal N)
=
\langle\Phi_d|
(\operatorname{id}\otimes\mathcal N)(\Phi_d)
|\Phi_d\rangle,
\]

where

\[
|\Phi_d\rangle=
\frac{1}{\sqrt d}\sum_{i=1}^d|i\rangle|i\rangle.
\]

For Kraus operators \(K_i\),

\[
F_e(\mathcal N)=\frac1{d^2}\sum_i|\operatorname{Tr}K_i|^2.
\]

The Haar-average pure-state fidelity is

\[
F_{\mathrm{avg}}=\frac{dF_e+1}{d+1}.
\]

## Choi conventions

### Normalized channel Choi state

For \(\mathcal N:X\to A\),

\[
\rho_{RA}^{\mathcal N}
=(\operatorname{id}_R\otimes\mathcal N)(\Phi_{RX}),
\]

with normalized \(\Phi\). Thus \(\operatorname{Tr}\rho_{RA}^{\mathcal N}=1\).

### Unnormalized recovery Choi matrix

For \(\mathcal R:A\to X\),

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

The recovery objective in `src/qgbounce/optimization.py` is linear in this unnormalized matrix.

## Environmental decoupling

For the normalized complementary Choi state \(\rho_{RE}\), the default product comparator is

\[
\frac{I_R}{d}\otimes\rho_E.
\]

The state-specific decoupling module reports:

- \(I(R:E)\);
- trace distance to the product;
- purified distance to the product;
- a Uhlmann existence lower bound on maximally mixed-input recovery fidelity.

Quantum Pinsker is used in the base-two convention:

\[
T\!\left(\rho_{RE},\rho_R\otimes\rho_E\right)
\leq
\sqrt{\frac{\ln2}{2}I(R:E)}.
\]

This is state specific. It is not a diamond-norm statement about every input.

## Recovery SDP certificate

The recovery optimization is

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N).
\]

The recovery result may be called a **numerical certificate** only when:

- the solver status is `optimal`;
- trace preservation and positivity pass declared tolerances;
- analytic benchmark channels agree within the recovery tolerance;
- the optimization conventions match this document.

## Environment-side fidelity diagnostic

The independent environment formulation is

\[
\max_{\sigma_E}
F\!\left(
\rho_{RE}^{\mathcal N^c},
\frac{I_R}{d}\otimes\sigma_E
\right).
\]

Its difference from the recovery optimum is the **cross-formulation gap**. This is not the conic solver's internal primal–dual gap.

The current open-source solvers can return `optimal_inaccurate` on rank-deficient erasure boundary cases. Such an output is retained only as an **environment diagnostic** under a separately declared tolerance. It is not theorem-grade evidence and does not upgrade the recovery certificate to a channel-wide information–disturbance theorem.

Every stored optimization result records:

- solver and solver status;
- objective value;
- iterations and solve time where available;
- recovery trace-preservation residual;
- minimum recovery Choi eigenvalue;
- environment-state trace and positivity residuals;
- cross-formulation gap;
- the tolerance class under which the value was accepted.

## Diamond and energy-constrained diamond norms

No diamond norm is currently computed by the executable package. Accordingly:

- no Choi-state distance is labeled a diamond distance;
- no fixed-input recovery result is promoted to a channel-wide worst-case theorem;
- Kretschmann–Schlingemann–Werner and Bény–Oreshkov are imported theorem targets until their assumptions and constants are rederived under these conventions.

An energy-constrained diamond norm additionally requires a declared input Hamiltonian, energy cap, ancillary-system convention, and a certified finite or infinite-dimensional method.

## Solver roles

The pinned optional environment contains CVXPY, Clarabel, and SCS.

- **Clarabel:** primary recovery SDP solver and fast environment diagnostic.
- **SCS:** secondary diagnostic solver retained for comparison; it is not the default certificate path because the rank-deficient fidelity SDP can reach its iteration cap with `optimal_inaccurate` status.

A platform-complete transitive lock remains required before a tagged certificate release.

## Numerical tolerance policy

- Analytic finite-dimensional identities: default \(10^{-10}\).
- Recovery SDP analytic benchmarks: declared in `tests/test_optimal_recovery.py` and required with solver status `optimal`.
- Environment diagnostic: a separate, looser tolerance is permitted and must be shown on plots and in machine-readable summaries.

A material feasibility violation, an unaccepted solver status, or a recovery objective outside its analytic tolerance blocks theorem-level use. An environment diagnostic may remain in the repository as a documented numerical limitation rather than being hidden.
