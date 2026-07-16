# Charge, Symmetry, and Superselection Resource Bounds

## Scope

This document adds a finite-dimensional resource bound for a retained system whose Hilbert space decomposes into orthogonal charge sectors. The sector structure, dimensions, and charge probabilities must be supplied by the physical model. They are not inferred from a spacetime metric.

## Direct-sum model

Assume

\[
\mathcal H_B=\bigoplus_q\mathcal H_q,
\qquad
\dim\mathcal H_q=d_q,
\]

and a superselection-compatible state

\[
\rho_B=\bigoplus_q p_q\rho_q,
\qquad
\sum_q p_q=1.
\]

The entropy of a block-diagonal state is

\[
S(B)=H(p)+\sum_q p_q S(\rho_q),
\]

so

\[
S(B)\leq
H(p)+\sum_qp_q\log_2d_q
=:S_{\mathrm{sector}}.
\]

For any joint state on \(RB\),

\[
I(R:B)\leq2\min\{S(R),S(B)\},
\]

therefore

\[
I(R:B)\leq
2\min\{S(R),S_{\mathrm{sector}}\}.
\]

For pure \(RAB\),

\[
I(R:A)\geq
\max\{0,2S(R)-2S_{\mathrm{sector}}\}.
\]

## Interpretation

The storage resource has two parts:

1. classical uncertainty in the sector label, \(H(p)\);
2. quantum entropy available within each sector, bounded by \(\log_2d_q\).

A fixed known charge sector removes the classical term and reduces the cap to \(\log_2d_q\).

When the charge probabilities are unconstrained and may be chosen to maximize entropy, the maximizing distribution is

\[
p_q=\frac{d_q}{\sum_jd_j},
\]

and the cap becomes

\[
S_{\mathrm{sector}}=\log_2\sum_qd_q.
\]

Thus an unconstrained direct-sum decomposition gives no stronger bound than the total Hilbert-space dimension. Additional force comes only from a physically supplied sector restriction or charge distribution.

## What this result does not establish

- It does not determine the relevant conserved charge in a bounce geometry.
- It does not derive sector dimensions from area, volume, mass, or lifetime.
- It does not prove that the retained state is block diagonal unless a superselection rule or dephasing mechanism is specified.
- It does not construct a radiation decoder.
- It does not replace worst-case or diamond-norm recovery analysis.

## Implementation

- `src/qgbounce/symmetry.py`
- `tests/test_symmetry.py`
- `scripts/run_symmetry_stress_tests.py`

The deterministic runner uses two sectors of dimensions one and four to show how sector probability changes the retained entropy cap, remnant mutual-information cap, and radiation mutual-information lower bound.

## Admission rule for a gravitational model

A model may use this bound only after documenting:

1. the charge or symmetry group;
2. the physical reason for block diagonality;
3. all allowed sectors;
4. sector degeneracies or dimensions;
5. the sector distribution or a valid constraint on it;
6. whether the observer can access the sector label;
7. the time slice and retained algebra to which the bound applies.
