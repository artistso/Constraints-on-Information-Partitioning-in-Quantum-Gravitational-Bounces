# Model Card — JT Gravity Coupled to a Non-Gravitating Bath

## Identity

- **Model name:** Evaporating two-dimensional Jackiw--Teitelboim gravity coupled to quantum matter and a non-gravitating bath
- **Primary sources:** `AlmheiriEtAl2019Replica`, `Penington2019`, with `AlmheiriEtAl2019Bulk` as supporting entropy analysis
- **Model class:** controlled semiclassical/holographic toy model
- **Role in this project:** reconstruction and decoupling benchmark; not a bounce model

## Geometry and dynamics

The benchmark contains a gravitating AdS2/JT region coupled to quantum matter and an external non-gravitating bath. Replica-wormhole saddles and quantum extremal surfaces produce an island prescription for the fine-grained radiation entropy. Entanglement-wedge reconstruction supplies a conditional route from entropy geometry to operator reconstruction.

This benchmark is selected because the radiation region, generalized entropy calculation, Page transition, and code-subspace language are sufficiently explicit to support controlled information-theoretic questions.

It is not used as evidence that an asymptotically flat loop-inspired black-to-white-hole transition has the same channel.

## Quantum systems and algebras

- **Input `X`:** a finite diary or code-subspace excitation inserted into the gravitating region.
- **Reference `R`:** an external purifier of the diary/input.
- **Radiation `A`:** a declared bath interval or collected Hawking-radiation algebra.
- **Complement `B`:** the remaining gravitating-region and bath complement on the chosen slice.
- **Observer algebra:** the bath subregion algebra from which reconstruction is attempted.
- **Code subspace:** must be bounded explicitly; state-independent reconstruction is not assumed for an unrestricted black-hole Hilbert space.

## Recoverability question

For a specified code subspace and radiation region:

1. calculate the generalized entropy and quantum extremal surface;
2. determine whether the diary lies in the radiation entanglement wedge;
3. translate the wedge condition into an approximate-correctability or decoupling statement with declared error;
4. compare the theorem-level existence statement with an explicit finite-dimensional surrogate decoder.

The entropy calculation alone is not labeled a decoder. A recovery claim requires a reconstruction theorem and error control.

## Computational surrogate

The first numerical benchmark will use finite-dimensional random or structured isometries whose dimensions follow a Page-style entropy balance. The surrogate will test:

- pre- and post-Page localization of `I(R:A)`;
- complementary decoupling;
- recovery fidelity for a known finite-dimensional decoder;
- sensitivity to code-subspace size;
- non-perturbative reconstruction error inserted as an explicit parameter.

The surrogate is a channel benchmark calibrated to the entropy structure; it is not a numerical solution of JT gravity.

## Falsifiable outputs

- A precise list of assumptions under which entanglement-wedge inclusion implies approximate recovery.
- Numerical agreement or disagreement between decoupling diagnostics and explicit decoder fidelity in the surrogate.
- A code-subspace-size threshold beyond which the chosen reconstruction statement no longer applies.
- A clear separation between entropy reproduction and operational decoding.

## Prohibited claims

- The island formula proves uniform information distribution over arbitrary radiation subregions.
- A Page curve alone supplies Kraus operators or a practical decoder.
- The JT-bath model is dynamically equivalent to a black-to-white-hole bounce.
- Reconstruction is exact or state independent outside the stated code subspace.
- Holographic conclusions transfer to the remnant case study without an assumption map.

## Claim coordinates

- **A — Assumptions:** semiclassical JT regime, specified bath coupling, replica/QES prescription, finite code subspace, declared reconstruction error.
- **M — Model:** JT gravity plus non-gravitating bath.
- **Q — Quantity:** generalized entropy, mutual information, decoupling distance, reconstruction/recovery fidelity.
- **O — Observer:** a specified bath radiation algebra.
- **E — Evidence:** primary-source gravitational calculation, theorem assumptions, and finite-dimensional validation.
- **P — Publication state:** selected controlled benchmark; implementation pending certified recovery layer.

## Decision

**Include as the first holographic benchmark, strictly separated from the remnant model.**

Implementation begins after Issue #6 fixes the decoupling constants and certified recovery conventions. Until then, the benchmark may be used to define variables and stage gates but not to claim a new gravitational recovery theorem.
