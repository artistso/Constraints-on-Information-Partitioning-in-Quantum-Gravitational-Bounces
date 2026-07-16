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

# The recovery SDP is required to match analytic optima tightly. The independent
# environment-fidelity formulation is deliberately treated as a numerical
# cross-check: rank-deficient erasure boundary cases can terminate with
# CLARABEL's `optimal_inaccurate` status at approximately 1e-4 objective error.
RECOVERY_ATOL = 2e-6
ENVIRONMENT_DIAGNOSTIC_ATOL = 1.5e-4


@pytest.mark.parametrize("probability", [0.0, 0.25, 0.5, 0.75, 1.0])
def test_erasure_recovery_sdp_and_environment_cross_check(probability):
    certificate = certify_information_disturbance(
        erasure_channel(probability),
        environment_solver="CLARABEL",
    )
    expected = 1.0 - 3.0 * probability / 4.0
    assert np.isclose(
        certificate.recovery.entanglement_fidelity,
        expected,
        atol=RECOVERY_ATOL,
    )
    assert certificate.recovery.solver_status == "optimal"
    assert np.isclose(
        certificate.environment.squared_fidelity,
        expected,
        atol=ENVIRONMENT_DIAGNOSTIC_ATOL,
    )
    assert certificate.environment.solver_status in {
        "optimal",
        "optimal_inaccurate",
    }
    assert certificate.formulation_gap < ENVIRONMENT_DIAGNOSTIC_ATOL
    assert certificate.recovery.trace_preservation_residual < 5e-6
    assert certificate.recovery.minimum_choi_eigenvalue > -5e-6
    assert certificate.environment.trace_residual < 5e-6
    assert certificate.environment.minimum_environment_eigenvalue > -5e-6


@pytest.mark.parametrize("probability", [0.2, 0.5, 0.8])
def test_dephasing_recovery_sdp_and_environment_cross_check(probability):
    certificate = certify_information_disturbance(
        dephasing_channel(probability),
        environment_solver="CLARABEL",
    )
    expected = max(probability, 1.0 - probability)
    assert np.isclose(
        certificate.recovery.entanglement_fidelity,
        expected,
        atol=RECOVERY_ATOL,
    )
    assert certificate.recovery.solver_status == "optimal"
    assert np.isclose(
        certificate.environment.squared_fidelity,
        expected,
        atol=ENVIRONMENT_DIAGNOSTIC_ATOL,
    )
    assert certificate.environment.solver_status in {
        "optimal",
        "optimal_inaccurate",
    }
    assert certificate.formulation_gap < ENVIRONMENT_DIAGNOSTIC_ATOL


def test_optimized_amplitude_damping_is_no_worse_than_identity_decoder():
    gamma = 0.4
    certificate = optimal_entanglement_recovery(
        amplitude_damping_channel(gamma)
    )
    identity_baseline = (1.0 + np.sqrt(1.0 - gamma)) ** 2 / 4.0
    assert certificate.entanglement_fidelity >= identity_baseline - RECOVERY_ATOL
    assert certificate.solver_status == "optimal"
    assert certificate.trace_preservation_residual < 5e-6
    assert certificate.minimum_choi_eigenvalue > -5e-6
