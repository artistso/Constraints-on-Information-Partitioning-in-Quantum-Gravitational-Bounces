# Remnant and Transition Parameter Provenance

This table determines which quantities may be calculated, which remain free parameters, and which must not be invented.

## Source map

| Quantity | Haggard–Rovelli 2014 | Bianchi et al. 2018 | Han–Rovelli–Soltani 2023 | Repository status |
|---|---|---|---|---|
| Black-to-white transition as a possible process | Proposed | Used in life-cycle scenario | Explicit existence geometry | CONDITIONAL physical hypothesis |
| Single asymptotic region | Motivated | Required by remnant life cycle | Explicitly constructed | GEOMETRICALLY MODELED |
| Exterior mass parameter | Present | Evolves through evaporation scenario | Explicit parameter \(m\) | SOURCE-SUPPLIED |
| Global transition duration | Model dependent | Life-cycle dependent | Explicit free geometric parameter \(\mathcal T\) | FREE PARAMETER |
| Effective LQC area scale | Not controlling parameter | Not a microscopic capacity | Explicit \(A\sim m_{\mathrm{Pl}}^2\) in natural units | SOURCE-SUPPLIED EFFECTIVE PARAMETER |
| Stellar bounce radius | Not central | Not a storage dimension | \((Am/2)^{1/3}\) | COMPUTABLE GEOMETRIC SCALE |
| Inner and outer horizon roots | Causal construction | Scenario dependent | Zeros of \(F(r)=1-2m/r+Am^2/r^4\) | COMPUTABLE BASELINE |
| Hawking mass-loss law in the explicit geometry | Not complete | Used qualitatively/semiclassically | Explicitly neglected in baseline construction | MISSING FROM HRS BASELINE |
| Tunnelling probability or amplitude | Heuristic | Model dependent | Not calculated | MISSING / MUST REMAIN PARAMETRIC |
| Rotation | Neglected | Not resolved | Neglected | OUT OF SCOPE |
| Remnant lifetime | Scenario dependent | Long-lived endpoint proposed | Not fixed by local geometry | MODEL-DEPENDENT FREE INPUT |
| Interior volume | Discussed geometrically | Large interior emphasized | Geometry can define slices/volumes | NOT AN INFORMATION CAPACITY BY ITSELF |
| Remnant Hilbert-space dimension \(d_B\) | Not supplied | Not supplied as a microscopic finite dimension | Not supplied | MISSING |
| Remnant Hamiltonian \(H_B\) | Not supplied | Not supplied | Not supplied | MISSING |
| Energy-constrained entropy cap | Not supplied | Not supplied | Not supplied | REPOSITORY MAY PARAMETERIZE, NOT INFER |
| Radiation algebra at a time cut | Not supplied operationally | Qualitative early/late radiation | Requires added dissipative model | MISSING |
| Microscopic channel \(X\to ABE\) | Not supplied | Not supplied | Not supplied | BLOCKED |
| Decoder or recovery map | Not supplied | Not supplied | Not supplied | BLOCKED |
| Emission spectrum for final white-hole decay | Not supplied robustly | Scenario dependent | Not modeled | PHENOMENOLOGY BLOCKED |
| Population/event-rate law | Not supplied | Not supplied | Not supplied | PHENOMENOLOGY BLOCKED |

## Allowed parameterized statements

The repository may state results of the form:

> Given a code-subspace reference entropy \(S(R)\), a declared remnant Hamiltonian spectrum \(H_B\), and mean-energy cap \(E\), the remnant can carry at most \(2\min\{S(R),S_{\max}(E,H_B)\}\) bits of reference mutual information.

It may also state:

> Given only the geometry and no state-space/Hamiltonian prescription, the remnant information capacity and radiation recovery fidelity are underdetermined.

## Forbidden substitutions

The following substitutions have no source-level justification:

- \(d_B\leftarrow\exp(\text{interior volume})\);
- \(d_B\leftarrow\exp(\text{horizon area}/4G)\) without declaring which area, time, and entropy interpretation apply;
- \(H_B\leftarrow\) exterior ADM mass alone;
- burst duration \(\leftarrow2GM/c^3\);
- decoder fidelity \(\leftarrow\) Page-curve entropy;
- event rate \(\leftarrow1/\mathcal T\) without a population and tunnelling model.

## Phenomenology watchlist

`EwasiukProfumo2026` computes PBH-to-white-hole tunnelling rates under explicit PBH abundance, evaporation, tunnelling-timescale, mass-function, and emission assumptions. It is retained as a contemporary constraint and methodology reference. It does not close the source-model gaps above and does not justify a generic FRB or optical forecast.

## Release gate for Paper 2

Paper 2 may proceed as a model-specific capacity/recoverability paper only if at least one of the following is supplied and defended:

1. a microscopic remnant Hamiltonian and energy constraint;
2. an effective finite-dimensional state-space bound;
3. a complementary-channel decoupling hypothesis tied to the geometry;
4. a theorem proving that the missing microscopic structure makes the desired claim underdetermined.

Absent items 1–3, item 4 is the default scientifically valid result.
