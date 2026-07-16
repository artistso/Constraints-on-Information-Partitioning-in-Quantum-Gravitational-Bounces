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

### Unnormalized channel Choi matrix

For every diamond-norm calculation,

\[
J(\mathcal N)
=
\sum_{i,j}|i\rangle\langle j|_X\otimes
\mathcal N(|i\rangle\langle j|)_A.
\]

The ordering is `input_X tensor output_A`, and

\[
J(\mathcal N)=d_X\rho_{RA}^{\mathcal N}.
\]

For a trace-preserving channel,

\[
\operatorname{Tr}_AJ(\mathcal N)=I_X.
\]

### Unnormalized recovery Choi matrix

For \(\mathcal R:A\to X\),

\[
J_{\mathcal R}
=
\sum_{a,b}|a\rangle\langle b|\otimes
\mathcal R(|a\rangle\langle b|).
\]

The ordering is `input_A tensor output_X`. Complete positivity and trace preservation are

\[
J_{\mathcal R}\succeq0,
\qquad
\operatorname{Tr}_XJ_{\mathcal R}=I_A.
\]

The fixed-input recovery objective and the channel-wide composed Choi matrix are linear in this unnormalized matrix.

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

## Fixed-input recovery SDP certificate

The recovery optimization is

\[
\max_{\mathcal R\ \mathrm{CPTP}}
F_e(\mathcal R\circ\mathcal N).
\]

The result may be called a **fixed-input numerical certificate** only when:

- the solver status is `optimal`;
- trace preservation and positivity pass declared tolerances;
- analytic benchmark channels agree within the recovery tolerance;
- the optimization conventions match this document.

## Environment-side fidelity diagnostic

The independent state-specific environment formulation is

\[
\max_{\sigma_E}
F\!\left(
\rho_{RE}^{\mathcal N^c},
\frac{I_R}{d}\otimes\sigma_E
\right).
\]

Its difference from the fixed-input recovery optimum is the **cross-formulation gap**. This is not the conic solver's internal primal–dual gap.

Rank-deficient boundary cases may return `optimal_inaccurate`. Such an output is retained only as an **environment diagnostic** under a separately declared tolerance. It is not theorem-grade evidence and does not upgrade the fixed-input result to a channel-wide statement.

## Diamond norm

For a Hermiticity-preserving map \(\Phi\),

\[
\|\Phi\|_\diamond
=
\sup_{\rho_{XR}}
\left\|(\Phi\otimes\operatorname{id}_R)(\rho_{XR})\right\|_1.
\]

An ancilla of dimension \(d_X\) is sufficient in finite dimension.

The repository uses the unhalved channel distance

\[
D_\diamond(\mathcal N,\mathcal M)
=
\|\mathcal N-\mathcal M\|_\diamond,
\]

which lies in \([0,2]\) for channels. No factor of one half is inserted.

## Diamond-norm dual SDP

For unnormalized \(J(\Phi)\) in input-output order, the executable dual is

\[
\begin{aligned}
\text{minimize}\quad & \mu\\
\text{subject to}\quad
& Z-J(\Phi)\succeq0,\\
& Z+J(\Phi)\succeq0,\\
& \operatorname{Tr}_{\mathrm{out}}Z\preceq\mu I_{\mathrm{in}}.
\end{aligned}
\]

The optimum equals \(\|\Phi\|_\diamond\). The detailed implementation and admission policy are fixed in `docs/DIAMOND_NORM_CERTIFICATE_POLICY.md`.

## Optimal channel-wide recovery

For \(\mathcal N:X\to A\),

\[
\delta_{\mathrm{rec}}
=
\inf_{\mathcal R:A\to X\ \mathrm{CPTP}}
\|\mathcal R\circ\mathcal N-\operatorname{id}_X\|_\diamond.
\]

The recovery Choi variable and the diamond dual are solved jointly. This is a channel-wide optimization over all input states and an ancilla. It is not the Bény–Oreshkov worst-case entanglement-fidelity minimax.

## Complementary distance from constant channels

For a declared complement \(\mathcal N^c:X\to E\),

\[
\delta_{\mathrm{env}}
=
\inf_{\sigma_E}
\|\mathcal N^c-\mathcal C_\sigma\|_\diamond,
\]

where

\[
\mathcal C_\sigma(\rho)=\operatorname{Tr}(\rho)\sigma_E
\]

and

\[
J(\mathcal C_\sigma)=I_X\otimes\sigma_E.
\]

The state \(\sigma_E\), dual matrix, and norm upper bound are optimized in one SDP.

## KSW convention

The mapped KSW inequality is

\[
\frac14\delta_{\mathrm{rec}}^2
\leq
\delta_{\mathrm{env}}
\leq
2\sqrt{\delta_{\mathrm{rec}}}.
\]

The imported theorem and the executable numerical verification are distinct evidence objects. A finite sweep validates conventions and code; it is not a new proof of KSW.

## Solver roles

The pinned optional environment contains CVXPY, Clarabel, and SCS.

- **Clarabel:** primary solver for the maximally mixed-input recovery SDP.
- **SCS:** certificate solver for the current diamond-norm layer and the state-specific environment-fidelity diagnostic.

The initial diamond implementation was also tested with Clarabel. At several rank-deficient or degenerate analytic points it returned `optimal_inaccurate` despite accurate objectives and small residuals. The repository retained the strict status policy and selected SCS for the current diamond certificate path.

A platform-complete transitive lock remains required before a tagged certificate release.

## Stored fixed-input optimization data

Every fixed-input result records:

- solver and solver status;
- objective value;
- iterations and solve time where available;
- recovery trace-preservation residual;
- minimum recovery Choi eigenvalue;
- environment-state trace and positivity residuals;
- cross-formulation gap;
- the tolerance class under which the value was accepted.

## Stored diamond-certificate data

Every diamond result records:

- solver and status;
- norm or optimal recovery objective;
- iterations and solve time where available;
- minimum eigenvalues of \(Z+J(\Phi)\) and \(Z-J(\Phi)\);
- residual of \(\operatorname{Tr}_{\mathrm{out}}Z\preceq\mu I\);
- recovery CPTP residuals where applicable;
- constant-state trace and positivity residuals where applicable;
- KSW lower and upper margins where applicable.

## Numerical tolerance policy

- Analytic finite-dimensional identities: default \(10^{-10}\).
- Fixed-input recovery analytic benchmarks: declared in `tests/test_optimal_recovery.py` and require solver status `optimal`.
- State-specific environment diagnostic: a separate, looser tolerance is permitted and must be shown in machine-readable summaries.
- Diamond analytic benchmarks: declared in `tests/test_diamond.py`, use pinned SCS, and require solver status `optimal` plus accepted PSD and partial-trace residuals.

A material feasibility violation, an unaccepted solver status, or an objective outside its analytic tolerance blocks certificate language. Diagnostic results may remain as documented numerical limitations rather than being hidden.

## Blocked norm extensions

The current package does not establish:

- an energy-constrained diamond norm;
- an infinite-dimensional channel norm;
- a symmetry-restricted channel-norm theorem;
- a computational-complexity bound for the optimized recovery;
- a gravitational derivation of the tested channel.
