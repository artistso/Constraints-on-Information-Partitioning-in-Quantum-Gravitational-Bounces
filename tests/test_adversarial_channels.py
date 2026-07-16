import numpy as np

from qgbounce.channels import (
    channel_choi_state,
    channel_information,
    coherent_information,
    dephasing_channel,
    erasure_channel,
    holevo_information,
    identity_channel,
)
from qgbounce.quantum import mutual_information


def reference_output_mutual_information(kraus) -> float:
    output_dim, input_dim = kraus[0].shape
    choi = channel_choi_state(kraus)
    return mutual_information(
        choi,
        (input_dim, output_dim),
        {0},
        {1},
    )


def test_equal_mutual_information_can_hide_different_optimal_recovery():
    erasure = erasure_channel(0.5)
    dephasing = dephasing_channel(0.5)

    assert np.isclose(
        reference_output_mutual_information(erasure),
        reference_output_mutual_information(dephasing),
        atol=1e-10,
    )

    # Analytic optima for maximally mixed-input entanglement fidelity:
    # erasure: 1 - 3p/4; phase flip: max(p, 1-p).
    erasure_optimum = 1.0 - 3.0 * 0.5 / 4.0
    dephasing_optimum = 0.5
    assert erasure_optimum - dephasing_optimum > 0.1


def test_identical_classical_accessibility_can_hide_quantum_difference():
    zero = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=np.complex128)
    one = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=np.complex128)
    ensemble_probabilities = [0.5, 0.5]
    ensemble_states = [zero, one]

    identity = identity_channel()
    fully_dephased = dephasing_channel(0.5)
    assert np.isclose(
        holevo_information(
            ensemble_probabilities,
            ensemble_states,
            identity,
        ),
        1.0,
        atol=1e-10,
    )
    assert np.isclose(
        holevo_information(
            ensemble_probabilities,
            ensemble_states,
            fully_dephased,
        ),
        1.0,
        atol=1e-10,
    )
    assert np.isclose(coherent_information(identity), 1.0, atol=1e-10)
    assert np.isclose(
        coherent_information(fully_dephased),
        0.0,
        atol=1e-10,
    )


def test_equal_output_entropy_can_hide_environmental_leakage():
    identity = channel_information(identity_channel())
    fully_dephased = channel_information(dephasing_channel(0.5))
    assert np.isclose(identity.output_entropy, 1.0, atol=1e-10)
    assert np.isclose(fully_dephased.output_entropy, 1.0, atol=1e-10)
    assert np.isclose(identity.exchange_entropy, 0.0, atol=1e-10)
    assert np.isclose(fully_dephased.exchange_entropy, 1.0, atol=1e-10)
