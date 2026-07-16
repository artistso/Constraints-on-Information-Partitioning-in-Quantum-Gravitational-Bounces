import numpy as np

from qgbounce.channels import (
    amplitude_damping_channel,
    coherent_information,
    dephasing_channel,
    depolarizing_channel,
    erasure_channel,
    holevo_information,
    validate_kraus,
)


def test_standard_channels_are_trace_preserving():
    for channel in (
        erasure_channel(0.37),
        dephasing_channel(0.37),
        depolarizing_channel(0.37),
        amplitude_damping_channel(0.37),
    ):
        validate_kraus(channel)


def test_qubit_erasure_coherent_information_formula():
    for probability in np.linspace(0.0, 1.0, 11):
        observed = coherent_information(erasure_channel(float(probability)))
        expected = 1.0 - 2.0 * probability
        assert np.isclose(observed, expected, atol=1e-10)


def test_dephasing_preserves_one_classical_z_bit():
    zero = np.array(
        [[1.0, 0.0], [0.0, 0.0]],
        dtype=np.complex128,
    )
    one = np.array(
        [[0.0, 0.0], [0.0, 1.0]],
        dtype=np.complex128,
    )
    for probability in np.linspace(0.0, 1.0, 11):
        chi = holevo_information(
            [0.5, 0.5],
            [zero, one],
            dephasing_channel(float(probability)),
        )
        assert np.isclose(chi, 1.0, atol=1e-10)


def test_amplitude_damping_coherent_information_endpoints():
    assert np.isclose(
        coherent_information(amplitude_damping_channel(0.0)),
        1.0,
        atol=1e-10,
    )
    assert np.isclose(
        coherent_information(amplitude_damping_channel(1.0)),
        -1.0,
        atol=1e-10,
    )
