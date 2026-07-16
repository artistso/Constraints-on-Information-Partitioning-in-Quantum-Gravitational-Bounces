import numpy as np

from qgbounce.channels import (
    amplitude_damping_channel,
    compose_channels,
    dephasing_channel,
    dephasing_pauli_recovery,
    erasure_channel,
    erasure_recovery,
    identity_channel,
)
from qgbounce.recovery import entanglement_fidelity, recovery_diagnostics


def test_erasure_recovery_entanglement_fidelity():
    for probability in np.linspace(0.0, 1.0, 11):
        diagnostics = recovery_diagnostics(
            erasure_channel(float(probability)),
            erasure_recovery(),
        )
        expected = 1.0 - 3.0 * probability / 4.0
        assert np.isclose(
            diagnostics.entanglement_fidelity,
            expected,
            atol=1e-10,
        )


def test_dephasing_best_fixed_pauli_recovery():
    for probability in np.linspace(0.0, 1.0, 11):
        effective = compose_channels(
            dephasing_pauli_recovery(float(probability)),
            dephasing_channel(float(probability)),
        )
        assert np.isclose(
            entanglement_fidelity(effective),
            max(probability, 1.0 - probability),
            atol=1e-10,
        )


def test_amplitude_damping_identity_recovery_formula():
    for gamma in np.linspace(0.0, 1.0, 11):
        effective = compose_channels(
            identity_channel(),
            amplitude_damping_channel(float(gamma)),
        )
        expected = (1.0 + np.sqrt(1.0 - gamma)) ** 2 / 4.0
        assert np.isclose(
            entanglement_fidelity(effective),
            expected,
            atol=1e-10,
        )


def test_recovery_distances_are_zero_for_identity():
    diagnostics = recovery_diagnostics(
        identity_channel(),
        identity_channel(),
    )
    assert np.isclose(diagnostics.entanglement_fidelity, 1.0)
    assert np.isclose(
        diagnostics.choi_trace_distance,
        0.0,
        atol=1e-12,
    )
    assert np.isclose(
        diagnostics.choi_purified_distance,
        0.0,
        atol=1e-12,
    )
