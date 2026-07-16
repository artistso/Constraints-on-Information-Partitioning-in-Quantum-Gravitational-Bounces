import numpy as np
import pytest

pytest.importorskip("cvxpy")

from qgbounce.channels import (  # noqa: E402
    amplitude_damping_channel,
    dephasing_channel,
    erasure_channel,
)
from qgbounce.optimization import (  # noqa: E402
    certify_information_disturbance,
    optimal_entanglement_recovery,
)

pytestmark = pytest.mark.optimization


@pytest.mark.parametrize("probability", [0.0, 0.25, 0.5, 0.75, 1.0])
def test_erasure_sdp_matches_analytic_optimum(probability):
    certificate = certify_information_disturbance(
        erasure_channel(probability)
    )
    expected = 1.0 - 3.0 * probability / 4.0
    assert np.isclose(
        certificate.recovery.entanglement_fidelity,
        expected,
        atol=2e-6,
    )
    assert np.isclose(
        certificate.environment.squared_fidelity,
        expected,
        atol=2e-6,
    )
    assert certificate.formulation_gap < 5e-6
    assert certificate.recovery.trace_preservation_residual < 5e-6
    assert certificate.recovery.minimum_choi_eigenvalue > -5e-6


@pytest.mark.parametrize("probability", [0.2, 0.5, 0.8])
def test_dephasing_sdp_matches_analytic_optimum(probability):
    certificate = certify_information_disturbance(
        dephasing_channel(probability)
    )
    expected = max(probability, 1.0 - probability)
    assert np.isclose(
        certificate.recovery.entanglement_fidelity,
        expected,
        atol=2e-6,
    )
    assert np.isclose(
        certificate.environment.squared_fidelity,
        expected,
        atol=2e-6,
    )
    assert certificate.formulation_gap < 5e-6


def test_optimized_amplitude_damping_is_no_worse_than_identity_decoder():
    gamma = 0.4
    certificate = optimal_entanglement_recovery(
        amplitude_damping_channel(gamma)
    )
    identity_baseline = (1.0 + np.sqrt(1.0 - gamma)) ** 2 / 4.0
    assert certificate.entanglement_fidelity >= identity_baseline - 2e-6
    assert certificate.trace_preservation_residual < 5e-6
