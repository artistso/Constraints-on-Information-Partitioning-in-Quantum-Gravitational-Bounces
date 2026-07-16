"""Small, dependency-light quantum-information utilities.

The module uses dense NumPy arrays and base-2 logarithms. It is intended for
low-dimensional validation and counterexample construction, not large-scale
many-body simulation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np

Array = np.ndarray


def density_matrix(state: Array) -> Array:
    """Return |psi><psi| after checking and normalizing a state vector."""
    state = np.asarray(state, dtype=np.complex128).reshape(-1)
    norm = np.linalg.norm(state)
    if not np.isfinite(norm) or norm <= 0:
        raise ValueError("state must have a finite, nonzero norm")
    state = state / norm
    return np.outer(state, state.conj())


def partial_trace(rho: Array, dims: Sequence[int], keep: Iterable[int]) -> Array:
    """Trace out every subsystem not listed in ``keep``.

    The returned tensor factors are ordered by ascending retained subsystem
    index.
    """
    dims = tuple(int(d) for d in dims)
    if any(d <= 0 for d in dims):
        raise ValueError("all subsystem dimensions must be positive")
    total_dim = int(np.prod(dims))
    rho = np.asarray(rho, dtype=np.complex128)
    if rho.shape != (total_dim, total_dim):
        raise ValueError(f"rho must have shape {(total_dim, total_dim)}")

    keep_set = set(int(i) for i in keep)
    if any(i < 0 or i >= len(dims) for i in keep_set):
        raise ValueError("keep contains an invalid subsystem index")

    traced = [i for i in range(len(dims)) if i not in keep_set]
    tensor = rho.reshape(*dims, *dims)
    active_dims = list(dims)
    for subsystem in reversed(traced):
        n_active = len(active_dims)
        tensor = np.trace(tensor, axis1=subsystem, axis2=subsystem + n_active)
        active_dims.pop(subsystem)

    kept_dims = [dims[i] for i in sorted(keep_set)]
    out_dim = int(np.prod(kept_dims)) if kept_dims else 1
    return tensor.reshape(out_dim, out_dim)


def von_neumann_entropy(rho: Array, *, base: float = 2.0, atol: float = 1e-12) -> float:
    """Compute ``-Tr(rho log rho)`` after Hermitian symmetrization."""
    rho = np.asarray(rho, dtype=np.complex128)
    if rho.ndim != 2 or rho.shape[0] != rho.shape[1]:
        raise ValueError("rho must be square")
    hermitian = 0.5 * (rho + rho.conj().T)
    evals = np.linalg.eigvalsh(hermitian)
    if evals.min(initial=0.0) < -100 * atol:
        raise ValueError("rho has a significantly negative eigenvalue")
    evals = np.clip(evals.real, 0.0, None)
    trace = evals.sum()
    if not np.isfinite(trace) or trace <= atol:
        raise ValueError("rho must have positive finite trace")
    evals = evals / trace
    nonzero = evals[evals > atol]
    if nonzero.size == 0:
        return 0.0
    logs = np.log(nonzero) / np.log(base)
    return float(-np.sum(nonzero * logs))


def mutual_information(
    rho: Array,
    dims: Sequence[int],
    left: Iterable[int],
    right: Iterable[int],
) -> float:
    """Return quantum mutual information I(left:right) in bits by default."""
    left_set = set(int(i) for i in left)
    right_set = set(int(i) for i in right)
    if left_set & right_set:
        raise ValueError("left and right subsystem sets must be disjoint")
    rho_left = partial_trace(rho, dims, left_set)
    rho_right = partial_trace(rho, dims, right_set)
    rho_joint = partial_trace(rho, dims, left_set | right_set)
    return (
        von_neumann_entropy(rho_left)
        + von_neumann_entropy(rho_right)
        - von_neumann_entropy(rho_joint)
    )


def maximally_entangled_pair(dim: int = 2) -> Array:
    """Return |Phi_d> on reference R and input X."""
    if dim <= 0:
        raise ValueError("dim must be positive")
    state = np.zeros(dim * dim, dtype=np.complex128)
    for i in range(dim):
        state[i * dim + i] = 1.0 / np.sqrt(dim)
    return state


def apply_input_isometry(reference_input_state: Array, isometry: Array) -> Array:
    """Apply I_R tensor V_X->AB to a bipartite R-X state vector."""
    state = np.asarray(reference_input_state, dtype=np.complex128).reshape(-1)
    isometry = np.asarray(isometry, dtype=np.complex128)
    input_dim = isometry.shape[1]
    reference_dim, remainder = divmod(state.size, input_dim)
    if remainder:
        raise ValueError("state size is incompatible with isometry input dimension")
    gram = isometry.conj().T @ isometry
    if not np.allclose(gram, np.eye(input_dim), atol=1e-10):
        raise ValueError("isometry columns are not orthonormal")
    operator = np.kron(np.eye(reference_dim, dtype=np.complex128), isometry)
    return operator @ state


def localization_isometry(theta: float) -> Array:
    """One-qubit encoding interpolating between storage in A and storage in B.

    V|0> = |00>
    V|1> = cos(theta)|10> + sin(theta)|01>
    """
    c = np.cos(theta)
    s = np.sin(theta)
    v = np.zeros((4, 2), dtype=np.complex128)
    v[0, 0] = 1.0
    v[2, 1] = c
    v[1, 1] = s
    return v


def haar_random_isometry(
    output_dim: int,
    input_dim: int,
    rng: np.random.Generator,
) -> Array:
    """Draw an isometry from the complex Ginibre/QR construction."""
    if output_dim < input_dim:
        raise ValueError("output_dim must be at least input_dim")
    z = rng.normal(size=(output_dim, input_dim)) + 1j * rng.normal(
        size=(output_dim, input_dim)
    )
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1.0)
    return q * phases.conj()


@dataclass(frozen=True)
class LocalizationPoint:
    """Information localization diagnostics for a pure RAB state."""

    i_reference_a: float
    i_reference_b: float
    entropy_reference: float
    identity_residual: float


def localization_diagnostics(
    state_rab: Array,
    dims: Sequence[int] = (2, 2, 2),
) -> LocalizationPoint:
    """Evaluate I(R:A), I(R:B), and the exact pure-state sum identity."""
    rho = density_matrix(state_rab)
    i_ra = mutual_information(rho, dims, [0], [1])
    i_rb = mutual_information(rho, dims, [0], [2])
    s_r = von_neumann_entropy(partial_trace(rho, dims, [0]))
    residual = i_ra + i_rb - 2.0 * s_r
    return LocalizationPoint(i_ra, i_rb, s_r, residual)
