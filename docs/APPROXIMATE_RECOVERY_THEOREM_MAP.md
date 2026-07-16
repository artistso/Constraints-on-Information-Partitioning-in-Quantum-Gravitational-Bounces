# Approximate-Recovery Theorem and Convention Map

This document maps the imported Bény--Oreshkov and Kretschmann--Schlingemann--Werner results into the repository's notation and records which corresponding optimizations are executable.

## Repository convention

Let

\[
\mathcal N:X\rightarrow A
\]

be a Schrödinger-picture channel, let

\[
\mathcal N^c:X\rightarrow E
\]

be a complementary channel from one declared Stinespring isometry, and let

\[
\mathcal R:A\rightarrow X
\]

be a recovery channel. A constant environment channel is

\[
\mathcal C_\sigma(\rho)=\operatorname{Tr}(\rho)\sigma_E.
\]

The repository now contains three distinct executable or imported layers:

1. maximally mixed-input entanglement-fidelity recovery;
2. channel-wide diamond-norm recovery and complementary leakage;
3. the imported Bény--Oreshkov worst-case entanglement-fidelity duality, whose minimax implementation remains pending.

---

## Bény--Oreshkov exact worst-case duality

### Source-native statement

Bény and Oreshkov define a worst-case entanglement fidelity between two channels by minimizing the input-dependent entanglement fidelity over all input density operators. For channels \(\mathcal N\) and \(\mathcal M\), and declared complementary channels \(\widehat{\mathcal N}\) and \(\widehat{\mathcal M}\), their Theorem 1 states

\[
\max_{\mathcal R}
F_{\mathrm{wc}}(\mathcal R\mathcal N,\mathcal M)
=
\max_{\mathcal R'}
F_{\mathrm{wc}}(\widehat{\mathcal N},\mathcal R'\widehat{\mathcal M}).
\]

For quantum error correction, \(\mathcal M=\operatorname{id}\), and a complementary channel of the identity is a trace channel. The dual optimization therefore asks how closely the complementary noise channel can be approximated by a constant channel in worst-case fidelity.

### Repository mapping

For the identity target,

\[
\max_{\mathcal R:A\to X}
F_{\mathrm{wc}}
\left(\mathcal R\circ\mathcal N,\operatorname{id}_X\right)
=
\max_{\sigma_E}
F_{\mathrm{wc}}
\left(\mathcal N^c,\mathcal C_\sigma\right).
\]

The paper uses unsquared state fidelity. Because squaring is monotone on \([0,1]\), the equality may equivalently be expressed using squared worst-case fidelity, provided the conversion is applied consistently to both sides.

### Remaining executable work

- minimization over all logical inputs or a declared code;
- subsystem/algebra target conventions where needed;
- certified joint optimization or a valid minimax reduction;
- comparison with the maximally mixed-input and diamond-norm optima;
- low-dimensional analytic regression standards.

Neither the fixed-input fidelity SDP nor the diamond-norm recovery SDP implements the Bény--Oreshkov worst-case fidelity objective.

---

## KSW channel-wide information--disturbance bound

### Source convention

Kretschmann, Schlingemann, and Werner work in the Heisenberg picture and use the completely bounded norm. For a channel \(T_B\), complementary channel \(T_E\), decoding channel \(D\), identity channel \(\operatorname{id}_A\), and a completely depolarizing channel \(S\), their Theorem 3 gives

\[
\frac14
\inf_D
\left\|T_BD-\operatorname{id}_A\right\|_{\mathrm{cb}}^2
\leq
\left\|T_E-S\right\|_{\mathrm{cb}}
\leq
2
\inf_D
\left\|T_BD-\operatorname{id}_A\right\|_{\mathrm{cb}}^{1/2}.
\]

The completely depolarizing channel has one fixed environment state. The bounds are dimension independent.

### Schrödinger-picture repository mapping

The cb norm of a Heisenberg-picture map equals the diamond norm of its Schrödinger adjoint. Define

\[
\delta_{\mathrm{rec}}
=
\inf_{\mathcal R}
\left\|
\mathcal R\circ\mathcal N-\operatorname{id}_X
\right\|_\diamond
\]

and

\[
\delta_{\mathrm{env}}
=
\inf_{\sigma_E}
\left\|
\mathcal N^c-\mathcal C_\sigma
\right\|_\diamond.
\]

The convention-mapped inequality is

\[
\frac14\delta_{\mathrm{rec}}^2
\leq
\delta_{\mathrm{env}}
\leq
2\sqrt{\delta_{\mathrm{rec}}}.
\]

The complementary dilation, constant state optimization, channel composition order, and unhalved diamond-distance convention must be stated explicitly whenever the inequality is used.

### Executable implementation

`src/qgbounce/diamond.py` now computes both quantities in finite dimension:

- \(\delta_{\mathrm{rec}}\) by a joint CPTP-recovery and diamond-dual SDP;
- \(\delta_{\mathrm{env}}\) by a joint constant-state and diamond-dual SDP.

The implementation uses unnormalized Choi matrices in input-output order and the Watrous dual SDP for Hermiticity-preserving maps. Its complete conventions and status policy are in `docs/DIAMOND_NORM_CERTIFICATE_POLICY.md`.

### Validation status

The pinned SCS certificate path passes analytic standards for:

- identity norm;
- identical-channel distance;
- qubit dephasing distance from identity;
- qubit depolarizing distance from identity;
- identity distance from the closest constant qubit channel;
- optimal dephasing recovery;
- KSW lower and upper margins across a deterministic sweep.

The current checkpoint has 30 passing optimization tests. The maximum dephasing analytic errors are below \(2.1\times10^{-8}\), and the minimum computed KSW lower margin is consistent with floating-point zero.

This validates the finite-dimensional implementation and convention mapping. It does not constitute a new proof of the KSW theorem.

### Remaining extensions

- energy-constrained diamond norm;
- infinite-dimensional channels;
- symmetry-restricted channel norms;
- gravitational derivation of the tested channel;
- independent QIT review of the composed-Choi implementation and residual policy.

---

## Relationship between the results

- Bény--Oreshkov gives an exact duality for **worst-case entanglement fidelity**.
- KSW gives dimension-independent inequalities in **cb/diamond norm**.
- The fixed-input SDP gives an optimum for **maximally mixed-input entanglement fidelity**.
- The new diamond SDP gives a finite-dimensional optimum for **channel-wide diamond recovery error**.

These are different operational statements. They may be compared, but not substituted for one another.

## Publication status

| Result | Status |
|---|---|
| Bény--Oreshkov source theorem | Imported and convention-mapped |
| Bény--Oreshkov worst-case fidelity implementation | Not implemented |
| KSW source theorem | Imported and convention-mapped |
| Fixed-input recovery SDP | Implemented and numerically certified within scope |
| Finite-dimensional diamond-norm SDP | Implemented and numerically certified within scope |
| Optimal channel-wide recovery in diamond norm | Implemented and numerically certified on declared benchmarks |
| Closest constant complementary channel in diamond norm | Implemented and numerically certified on declared benchmarks |
| KSW finite-dimensional numerical verification | Implemented and benchmarked |
| Energy-constrained channel-wide extension | Not implemented |

Primary bibliography keys: `BenyOreshkov2009`, `KretschmannEtAl2006`, `Watrous2009`, and `Watrous2012`.
