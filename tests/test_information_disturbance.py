import numpy as np

from qgbounce.channels import erasure_channel, identity_channel
from qgbounce.decoupling import decoupling_diagnostics


def test_identity_channel_environment_is_decoupled():
    diagnostics = decoupling_diagnostics(identity_channel())
    assert np.isclose(diagnostics.mutual_information_bits, 0.0, atol=1e-12)
    assert np.isclose(diagnostics.trace_distance_to_product, 0.0, atol=1e-12)
    assert np.isclose(diagnostics.purified_distance_to_product, 0.0, atol=1e-12)
    assert np.isclose(
        diagnostics.uhlmann_entanglement_fidelity_lower_bound,
        1.0,
        atol=1e-12,
    )


def test_quantum_pinsker_bound_for_erasure_family():
    for probability in np.linspace(0.0, 1.0, 21):
        diagnostics = decoupling_diagnostics(
            erasure_channel(float(probability))
        )
        assert diagnostics.pinsker_residual <= 1e-10


def test_complete_erasure_environment_is_not_decoupled():
    diagnostics = decoupling_diagnostics(erasure_channel(1.0))
    assert diagnostics.mutual_information_bits > 1.9
    assert diagnostics.trace_distance_to_product > 0.5
    assert diagnostics.uhlmann_entanglement_fidelity_lower_bound < 0.5
