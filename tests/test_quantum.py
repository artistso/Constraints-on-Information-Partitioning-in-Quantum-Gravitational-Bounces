import numpy as np

from qgbounce.quantum import (
    apply_input_isometry,
    density_matrix,
    haar_random_isometry,
    localization_diagnostics,
    localization_isometry,
    maximally_entangled_pair,
    partial_trace,
    von_neumann_entropy,
)


def test_biased_isometry_extremes():
    phi = maximally_entangled_pair(2)

    state_a = apply_input_isometry(phi, localization_isometry(0.0))
    diag_a = localization_diagnostics(state_a)
    assert np.isclose(diag_a.i_reference_a, 2.0, atol=1e-10)
    assert np.isclose(diag_a.i_reference_b, 0.0, atol=1e-10)

    state_b = apply_input_isometry(phi, localization_isometry(np.pi / 2))
    diag_b = localization_diagnostics(state_b)
    assert np.isclose(diag_b.i_reference_a, 0.0, atol=1e-10)
    assert np.isclose(diag_b.i_reference_b, 2.0, atol=1e-10)


def test_random_isometries_satisfy_sum_identity():
    phi = maximally_entangled_pair(2)
    rng = np.random.default_rng(20260715)
    residuals = []
    for _ in range(100):
        v = haar_random_isometry(4, 2, rng)
        state = apply_input_isometry(phi, v)
        residuals.append(localization_diagnostics(state).identity_residual)
    assert max(abs(x) for x in residuals) < 1e-10


def test_partial_trace_preserves_trace():
    state = np.array([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2.0)
    rho = density_matrix(state)
    rho_a = partial_trace(rho, (2, 2), [0])
    assert np.isclose(np.trace(rho_a), 1.0)
    assert np.isclose(von_neumann_entropy(rho_a), 1.0)
