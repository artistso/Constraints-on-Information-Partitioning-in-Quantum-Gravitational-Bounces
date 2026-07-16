# Approximate-Recovery Theorem and Convention Map

This document maps the imported Bény--Oreshkov and Kretschmann--Schlingemann--Werner results into the repository's notation. It does not claim that the current fixed-input SDP implements the worst-case or diamond-norm optimizations below.

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

The current executable recovery program optimizes entanglement fidelity only for the maximally mixed input. The theorems below use either worst-case entanglement fidelity or a channel norm.

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

For quantum error correction, \(\mathcal M=\operatorname{id}\), and a complementary channel of the identity is a trace channel. The dual optimization therefore asks how closely the complementary noise channel can be approximated by a constant channel.

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

### What remains to implement

- minimization over all logical inputs or a declared code;
- subsystem/algebra target conventions where needed;
- certified joint optimization or a valid minimax reduction;
- comparison with the current maximally mixed-input SDP;
- low-dimensional analytic regression standards.

The current environment-state SDP is a fixed-input analogue and must not be cited as an implementation of this theorem.

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

and, for the constant channel paired with the chosen dilation,

\[
\delta_{\mathrm{env}}
=
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

The constant state \(\sigma_E\), complementary dilation, and channel composition order must be stated explicitly whenever this inequality is used.

### Implementation gate

Before this result is used as a repository theorem, add:

1. a diamond-norm SDP or independently certified bound;
2. explicit Choi and tensor-order conventions;
3. optimization over the constant environment state where required by the chosen formulation;
4. exact identity, erasure, and depolarizing regression cases;
5. finite numerical tolerances and primal/dual diagnostics;
6. a proof note showing the Heisenberg-to-Schrödinger conversion.

No current Choi-state trace distance is a diamond norm.

---

## Relationship between the imported results

- Bény--Oreshkov gives an exact duality for **worst-case entanglement fidelity**.
- KSW gives dimension-independent inequalities in **cb/diamond norm**.
- The current repository SDP gives an exact finite-dimensional optimum for **maximally mixed-input entanglement fidelity**, subject to numerical solver certification.

These are different operational statements. They may be compared, but not substituted for one another.

## Publication status

| Result | Status |
|---|---|
| Bény--Oreshkov source theorem | Imported and convention-mapped |
| KSW source theorem | Imported and convention-mapped |
| Fixed-input recovery SDP | Implemented and numerically certified within scope |
| Worst-case recovery implementation | Not implemented |
| Diamond-norm information--disturbance implementation | Not implemented |
| Energy-constrained channel-wide extension | Not implemented |

Primary bibliography keys: `BenyOreshkov2009` and `KretschmannEtAl2006`.
