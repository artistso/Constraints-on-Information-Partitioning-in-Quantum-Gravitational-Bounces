# Finite-Dimensional Diamond-Norm Certificate Policy

## Scope

This document controls all executable claims involving the diamond norm in the repository. The implementation is finite dimensional, uses dense matrices, and is intended for low-dimensional theorem validation and adversarial channel studies.

It does not implement an energy-constrained diamond norm, an infinite-dimensional channel norm, or a gravitationally derived channel.

## Choi convention

For a linear map

\[
\Phi:\mathcal L(\mathcal H_X)\rightarrow\mathcal L(\mathcal H_A),
\]

the unnormalized Choi matrix is

\[
J(\Phi)
=
\sum_{i,j}|i\rangle\langle j|_X\otimes
\Phi(|i\rangle\langle j|)_A.
\]

The tensor ordering is always

```text
input_X tensor output_A
```

and

\[
\operatorname{Tr}_A J(\mathcal N)=I_X
\]

for a trace-preserving channel.

The normalized Choi state used elsewhere in the package is related by

\[
\rho^{\mathcal N}_{RA}=\frac{1}{d_X}J(\mathcal N).
\]

## Diamond norm

For a Hermiticity-preserving map \(\Phi\),

\[
\|\Phi\|_\diamond
=
\sup_{\rho_{XR}}
\left\|(\Phi\otimes\operatorname{id}_R)(\rho_{XR})\right\|_1,
\]

where an ancilla of dimension \(d_X\) is sufficient in finite dimension.

The executable dual semidefinite program is

\[
\begin{aligned}
\text{minimize}\quad & \mu\\
\text{subject to}\quad
& Z-J(\Phi)\succeq0,\\
& Z+J(\Phi)\succeq0,\\
& \operatorname{Tr}_A Z\preceq \mu I_X.
\end{aligned}
\]

The optimum is \(\|\Phi\|_\diamond\). The implementation follows the finite-dimensional completely bounded trace-norm SDP literature associated with Watrous.

## Channel distance

For channels \(\mathcal N\) and \(\mathcal M\) with equal input and output dimensions,

\[
D_\diamond(\mathcal N,\mathcal M)
=
\|\mathcal N-\mathcal M\|_\diamond.
\]

No factor of one half is inserted. Consequently, channel distances lie in \([0,2]\).

## Optimal channel-wide recovery

For

\[
\mathcal N:X\rightarrow A,
\]

the channel-wide recovery error is

\[
\delta_{\mathrm{rec}}(\mathcal N)
=
\inf_{\mathcal R:A\rightarrow X\ \mathrm{CPTP}}
\left\|
\mathcal R\circ\mathcal N-\operatorname{id}_X
\right\|_\diamond.
\]

The recovery Choi matrix is ordered as

```text
input_A tensor output_X
```

and satisfies

\[
J(\mathcal R)\succeq0,
\qquad
\operatorname{Tr}_XJ(\mathcal R)=I_A.
\]

The composed Choi matrix is built linearly from \(J(\mathcal N)\) and the recovery variable. The recovery and diamond dual constraints are therefore solved in one convex program.

This is a channel-wide norm optimization. It is distinct from the maximally mixed-input entanglement-fidelity program and from the Bény--Oreshkov worst-case fidelity minimax.

## Distance of a complementary channel from constants

For a declared complementary channel

\[
\mathcal N^c:X\rightarrow E,
\]

define

\[
\delta_{\mathrm{env}}(\mathcal N)
=
\inf_{\sigma_E}
\left\|
\mathcal N^c-\mathcal C_{\sigma}
\right\|_\diamond,
\]

where

\[
\mathcal C_\sigma(\rho)=\operatorname{Tr}(\rho)\sigma_E.
\]

The unnormalized Choi matrix of the constant channel is

\[
J(\mathcal C_\sigma)=I_X\otimes\sigma_E.
\]

The state \(\sigma_E\), dual matrix, and norm bound are optimized jointly in one SDP.

## KSW numerical certificate

The imported KSW theorem gives, under the mapped conventions,

\[
\frac14\delta_{\mathrm{rec}}^2
\leq
\delta_{\mathrm{env}}
\leq
2\sqrt{\delta_{\mathrm{rec}}}.
\]

The repository separately establishes:

1. the theorem statement as an imported result;
2. the two finite-dimensional convex optima as numerical certificates;
3. deterministic verification of the KSW inequalities on declared channel families.

A numerical sweep is not a proof of the imported theorem. It is an implementation and convention check.

## Analytic regression standards

The executable layer is tested against:

- \(\|\operatorname{id}\|_\diamond=1\);
- zero distance between identical channels;
- qubit phase-flip distance
  \[
  \|\mathcal Z_p-\operatorname{id}\|_\diamond=2p;
  \]
- qubit depolarizing distance
  \[
  \|\mathcal D_p-\operatorname{id}\|_\diamond=\frac32p;
  \]
- identity-to-closest-constant qubit distance \(3/2\);
- optimal phase-flip recovery error
  \[
  \delta_{\mathrm{rec}}=2\min\{p,1-p\};
  \]
- KSW lower and upper margins across a deterministic dephasing sweep.

## Solver policy

The pinned numerical environment contains CVXPY, Clarabel, and SCS.

For the diamond layer:

- SCS is the certificate solver for the current rank-deficient and degenerate analytic cases;
- `optimal` is required for certificate language;
- `optimal_inaccurate` is retained only as a diagnostic;
- solver substitution requires complete rerunning of analytic standards and residual checks.

The initial Clarabel implementation produced correct analytic values and small feasibility residuals but returned `optimal_inaccurate` at several degenerate points. The repository did not weaken its status policy; it changed the certificate solver to SCS.

## Stored certificate data

Each certificate records:

- solver and status;
- objective value;
- iterations and solve time where available;
- minimum eigenvalues of \(Z+J(\Phi)\) and \(Z-J(\Phi)\);
- the positive-semidefinite upper-bound residual for \(\operatorname{Tr}_{\mathrm{out}}Z\preceq\mu I\);
- recovery trace-preservation and Choi-positivity residuals where applicable;
- constant-state trace and positivity residuals where applicable;
- KSW lower and upper margins where applicable.

## Current certified numerical checkpoint

The deterministic v0.5 sweep reports:

- 30 optimization tests passed;
- maximum dephasing identity-distance analytic error below \(6.3\times10^{-9}\);
- maximum dephasing optimal-recovery analytic error below \(2.1\times10^{-8}\);
- minimum KSW lower margin \(-8.8\times10^{-19}\), consistent with floating-point zero;
- minimum KSW upper margin above \(8.6\times10^{-5}\);
- fully depolarizing qubit distance from identity approximately \(1.5\);
- identity distance from the closest constant qubit channel approximately \(1.5\).

These values apply only to the declared finite-dimensional tests and pinned environment.

## Blocked extensions

The following remain outside the certificate:

- energy-constrained diamond norms;
- infinite-dimensional ancillas or channels;
- symmetry-restricted channel-norm optimization;
- computational-complexity guarantees;
- gravitational derivation of \(\mathcal N\), \(\mathcal N^c\), or \(\mathcal R\);
- operational reconstruction in the JT-bath model before the code and observer algebra are fixed.
