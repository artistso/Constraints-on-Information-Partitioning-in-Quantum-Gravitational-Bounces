"""State-specific environmental decoupling diagnostics.

The implemented bounds concern the maximally entangled test input and the
normalized complementary Choi state. They are not a channel-wide diamond-norm
information--disturbance theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from .channels import complementary_choi_state, validate_kraus
from .quantum import mutual_information, partial_trace
from .recovery import trace_distance

Array = np.ndarray


def _positive_square_root(matrix: Array, *, atol: float = 1e-12) -> Array:
    matrix = np.asarray(matrix, dtype=np.complex128)
    hermitian = 0.5 * (matrix + matrix.conj().T)
    eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
    if eigenvalues.min(initial=0.0) < -100.0 * atol:
        raise ValueError("matrix is not positive semidefinite")
    eigenvalues = np.clip(eigenvalues.real, 0.0, None)
    return (eigenvectors * np.sqrt(eigenvalues)) @ eigenvectors.conj().T


def root_fidelity(rho: Array, sigma: Array, *, atol: float = 1e-12) -> float:
    """Return ``||sqrt(rho)sqrt(sigma)||_1``.

    This is the root-fidelity convention. Its square is the fidelity convention
    used for entanglement fidelity in the recovery module.
    """
    rho = np.asarray(rho, dtype=np.complex128)
    sigma = np.asarray(sigma, dtype=np.complex128)
    if rho.shape != sigma.shape or rho.ndim != 2 or rho.shape[0] != rho.shape[1]:
        raise ValueError("rho and sigma must be square matrices of equal shape")
    sqrt_rho = _positive_square_root(rho, atol=atol)
    middle = sqrt_rho @ sigma @ sqrt_rho
    sqrt_middle = _positive_square_root(middle, atol=atol)
    value = float(np.real(np.trace(sqrt_middle)))
    return float(np.clip(value, 0.0, 1.0))


def purified_distance(rho: Array, sigma: Array) -> float:
    """Return ``P(rho,sigma)=sqrt(1-f(rho,sigma)^2)``."""
    fidelity_root = root_fidelity(rho, sigma)
    return float(np.sqrt(max(0.0, 1.0 - fidelity_root**2)))


@dataclass(frozen=True)
class DecouplingDiagnostics:
    """Diagnostics for reference/environment decoupling of one Choi input."""

    mutual_information_bits: float
    trace_distance_to_product: float
    purified_distance_to_product: float
    product_root_fidelity: float
    uhlmann_entanglement_fidelity_lower_bound: float
    pinsker_trace_distance_upper_bound: float
    pinsker_residual: float


def decoupling_diagnostics(kraus: Iterable[Array]) -> DecouplingDiagnostics:
    """Compare the complementary Choi state with ``I_R/d tensor rho_E``.

    The Uhlmann value is an existence lower bound for recovery entanglement
    fidelity for the maximally mixed input using the *specific* choice
    ``sigma_E=rho_E``. Optimizing over constant environment states is handled by
    the optional SDP layer.
    """
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, _ = validate_kraus(operators)
    environment_dim = len(operators)
    rho_re = complementary_choi_state(operators)
    rho_e = partial_trace(
        rho_re,
        (input_dim, environment_dim),
        {1},
    )
    product = np.kron(
        np.eye(input_dim, dtype=np.complex128) / input_dim,
        rho_e,
    )
    information = mutual_information(
        rho_re,
        (input_dim, environment_dim),
        {0},
        {1},
    )
    distance = trace_distance(rho_re, product)
    fidelity_root = root_fidelity(rho_re, product)
    purified = float(np.sqrt(max(0.0, 1.0 - fidelity_root**2)))
    pinsker_upper = float(np.sqrt(max(0.0, np.log(2.0) * information / 2.0)))
    return DecouplingDiagnostics(
        mutual_information_bits=information,
        trace_distance_to_product=distance,
        purified_distance_to_product=purified,
        product_root_fidelity=fidelity_root,
        uhlmann_entanglement_fidelity_lower_bound=fidelity_root**2,
        pinsker_trace_distance_upper_bound=pinsker_upper,
        pinsker_residual=distance - pinsker_upper,
    )
