import numpy as np
import pytest

from qgbounce.channels import (
    dephasing_channel,
    depolarizing_channel,
    identity_channel,
)
from qgbounce.diamond import (
    certify_ksw_diamond_tradeoff,
    channel_diamond_distance,
    closest_constant_channel_diamond_distance,
    complementary_kraus,
    diamond_norm_from_choi,
    identity_choi,
    optimal_recovery_diamond_error,
    unnormalized_channel_choi,
)

pytestmark = pytest.mark.optimization


def _assert_certificate_feasible(certificate, atol=2e-7):
    assert certificate.solver_status == "optimal"
    assert certificate.minimum_plus_eigenvalue >= -atol
    assert certificate.minimum_minus_eigenvalue >= -atol
    assert certificate.partial_trace_upper_residual <= atol


def test_identity_map_has_unit_diamond_norm():
    certificate = diamond_norm_from_choi(identity_choi(2), 2, 2)
    _assert_certificate_feasible(certificate)
    assert np.isclose(certificate.diamond_norm, 1.0, atol=2e-7)


def test_identical_channels_have_zero_diamond_distance():
    channel = dephasing_channel(0.23)
    certificate = channel_diamond_distance(channel, channel)
    _assert_certificate_feasible(certificate)
    assert certificate.diamond_norm <= 2e-7


@pytest.mark.parametrize("probability", [0.1, 0.25, 0.5, 0.9])
def test_dephasing_distance_from_identity_is_two_p(probability):
    certificate = channel_diamond_distance(
        dephasing_channel(probability),
        identity_channel(2),
    )
    _assert_certificate_feasible(certificate)
    assert np.isclose(
        certificate.diamond_norm,
        2.0 * probability,
        atol=2e-6,
    )


@pytest.mark.parametrize("probability", [0.1, 0.4, 1.0])
def test_depolarizing_distance_from_identity(probability):
    certificate = channel_diamond_distance(
        depolarizing_channel(probability),
        identity_channel(2),
    )
    _assert_certificate_feasible(certificate)
    assert np.isclose(
        certificate.diamond_norm,
        1.5 * probability,
        atol=2e-6,
    )


def test_identity_is_distance_three_halves_from_closest_constant_qubit_channel():
    certificate = closest_constant_channel_diamond_distance(identity_channel(2))
    _assert_certificate_feasible(certificate)
    assert certificate.constant_state_trace_residual <= 2e-8
    assert certificate.minimum_constant_state_eigenvalue >= -2e-8
    assert np.allclose(certificate.constant_state, np.eye(2) / 2.0, atol=2e-6)
    assert np.isclose(certificate.diamond_distance, 1.5, atol=2e-6)


@pytest.mark.parametrize(
    ("probability", "expected"),
    [(0.0, 0.0), (0.1, 0.2), (0.4, 0.8), (0.6, 0.8), (0.9, 0.2), (1.0, 0.0)],
)
def test_optimal_dephasing_recovery_has_analytic_diamond_error(
    probability,
    expected,
):
    certificate = optimal_recovery_diamond_error(dephasing_channel(probability))
    _assert_certificate_feasible(certificate)
    assert certificate.recovery_trace_preservation_residual <= 2e-7
    assert certificate.minimum_recovery_choi_eigenvalue >= -2e-7
    assert np.isclose(certificate.diamond_error, expected, atol=3e-6)


def test_complementary_kraus_reproduces_complementary_choi_dimensions():
    channel = depolarizing_channel(0.3)
    complement = complementary_kraus(channel)
    original_input = channel[0].shape[1]
    environment_dim = len(channel)
    assert complement[0].shape == (environment_dim, original_input)
    choi = unnormalized_channel_choi(complement)
    assert choi.shape == (
        original_input * environment_dim,
        original_input * environment_dim,
    )


@pytest.mark.parametrize("probability", [0.0, 0.1, 0.25, 0.5])
def test_ksw_tradeoff_holds_for_dephasing(probability):
    certificate = certify_ksw_diamond_tradeoff(
        dephasing_channel(probability)
    )
    _assert_certificate_feasible(certificate.recovery, atol=5e-7)
    _assert_certificate_feasible(certificate.environment, atol=5e-7)
    assert certificate.lower_margin >= -3e-6
    assert certificate.upper_margin >= -3e-6
