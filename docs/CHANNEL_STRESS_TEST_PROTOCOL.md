# Open-Channel and Finite-Remnant Stress-Test Protocol

## Purpose

This protocol extends the pure-isometry checks into operationally distinct forms of information loss, noise, and recovery. It is designed to prevent three quantities from being conflated:

1. correlation with a purifying reference;
2. coherent quantum transmission;
3. fidelity of an explicit decoder.

The calculations are finite dimensional and exact up to floating-point error. They are quantum-information benchmarks, not gravitational dynamics.

## Channel convention

A channel is represented by Kraus operators

\[
\mathcal N(\rho)=\sum_i K_i\rho K_i^\dagger,
\qquad
\sum_i K_i^\dagger K_i=I.
\]

The normalized Choi state is obtained by applying the channel to one half of a maximally entangled state. Coherent information is evaluated for the maximally mixed input:

\[
I_c(R\rangle A)=S(A)-S(RA).
\]

For a recovered channel with equal input and output dimensions, the maximally mixed-input entanglement fidelity is

\[
F_e=\frac{1}{d^2}\sum_i|\operatorname{Tr}K_i|^2.
\]

The Haar-average pure-state fidelity is

\[
F_{\mathrm{avg}}=\frac{dF_e+1}{d+1}.
\]

## Experiment 1 — Erasure

The qubit erasure channel transmits the state with probability \(1-p\) and maps it to an orthogonal flag with probability \(p\). The explicit recovery decodes the transmitted sector and replaces the erasure flag by the maximally mixed state.

Regression targets:

\[
I_c=1-2p,
\]

\[
F_e=1-\frac{3p}{4},
\qquad
F_{\mathrm{avg}}=1-\frac{p}{2}.
\]

Interpretation: coherent information reaches zero at \(p=1/2\), but a state-estimation or replacement fidelity remains nonzero. Zero coherent information, nonzero mutual information, and nonzero average fidelity are not equivalent statements.

## Experiment 2 — Dephasing

The phase-flip channel is

\[
\mathcal Z_p(\rho)=(1-p)\rho+pZ\rho Z.
\]

The equiprobable computational-basis ensemble retains one full classical bit for every \(p\), while quantum coherent information reaches zero at \(p=1/2\). A known channel with \(p>1/2\) is better followed by a fixed \(Z\) correction; the best fixed-Pauli entanglement fidelity is

\[
F_e^{\mathrm{Pauli}}=\max(p,1-p).
\]

Interpretation: a channel can preserve a complete classical basis while destroying superposition coherence.

## Experiment 3 — Amplitude damping

The amplitude-damping Kraus operators are

\[
K_0=|0\rangle\!\langle0|+\sqrt{1-\gamma}|1\rangle\!\langle1|,
\qquad
K_1=\sqrt{\gamma}|0\rangle\!\langle1|.
\]

For identity recovery, the entanglement fidelity is

\[
F_e=\frac{(1+\sqrt{1-\gamma})^2}{4}.
\]

Interpretation: excitation-energy loss and loss of recoverable quantum information are related but are not the same observable. The present result is a baseline decoder, not a proof of globally optimal recovery over all CPTP maps.

## Experiment 4 — Finite remnant dimension

For a pure state on \(RAB\),

\[
I(R:A)+I(R:B)=2S(R).
\]

The remnant dimension implies

\[
I(R:B)\leq 2\min\{S(R),\log_2 d_B\},
\]

and therefore

\[
I(R:A)\geq
\max\left\{0,2S(R)-2\log_2d_B\right\}.
\]

This is a valid dimension-only correlation bound. It is not, by itself, a decoder construction or a lower bound on entanglement fidelity. An operational recovery theorem requires an additional decoupling, complementary-channel, code, or approximate-correctability hypothesis.

The numerical experiment samples Haar-random isometries

\[
V:\mathcal H_X\rightarrow\mathcal H_A\otimes\mathcal H_B
\]

for fixed input and radiation dimensions and remnant dimensions \(d_B\in\{1,2,4\}\). Every sample must satisfy both the pure-state sum identity and the remnant information cap.

## Generated products

Running

```bash
python scripts/run_channel_stress_tests.py
```

produces:

- `erasure_recovery.csv` and `erasure_recovery.png`;
- `dephasing_classical_quantum.csv` and `dephasing_classical_quantum.png`;
- `amplitude_damping.csv` and `amplitude_damping.png`;
- `finite_remnant_points.csv` and `finite_remnant_regions.png`;
- `finite_remnant_bound.png`;
- `summary.json`.

## Acceptance criteria

- Every Kraus family passes trace-preservation checks.
- The erasure coherent-information and recovery-fidelity formulas agree to less than \(10^{-10}\).
- Dephasing preserves one computational-basis Holevo bit to less than \(10^{-10}\).
- Random pure-state sum-identity residuals remain below \(10^{-10}\) bits.
- No sample violates the finite-remnant information cap by more than \(10^{-10}\) bits.
- Any claim about optimal recovery must be identified as analytic, numerically optimized, or only a named baseline decoder.

## Scope boundary

No result in this protocol identifies \(A\) with actual Hawking radiation or \(B\) with a physical white-hole remnant. That translation requires a completed gravitational model card specifying geometry, dynamics, algebras, state space, asymptotics, and accessibility.
