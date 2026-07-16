"""Certified low-dimensional recovery optimization with optional CVXPY.

The primal SDP maximizes maximally-mixed-input entanglement fidelity over all
CPTP recovery maps. A second environment-side SDP maximizes fidelity of the
complementary Choi state with a constant-output channel. Their numerical
agreement is an information--disturbance cross-certificate for the declared
input state, not a replacement for a channel-wide worst-case theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from .channels import (
    channel_choi_state,
    complementary_choi_state,
    validate_kraus,
)

Array = np.ndarray


def _cvxpy():
    try:
        import cvxpy as cp
    except ImportError as exc:  # pragma: no cover - exercised in basic install
        raise ImportError(
            "optimization routines require the optional 'optimization' extra: "
            "python -m pip install -e '.[optimization]'"
        ) from exc
    return cp


def recovery_objective_coefficients(kraus: Iterable[Array]) -> Array:
    """Return coefficients linear in the unnormalized recovery Choi matrix.

    If ``J_R`` is ordered as ``input_A tensor output_X``, then

    ``F_e(R o N) = sum(coefficients * J_R)``.
    """
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, channel_output_dim = validate_kraus(operators)
    choi_channel = channel_choi_state(operators)
    coefficients = np.zeros(
        (
            channel_output_dim * input_dim,
            channel_output_dim * input_dim,
        ),
        dtype=np.complex128,
    )
    for a in range(channel_output_dim):
        for b in range(channel_output_dim):
            for x in range(input_dim):
                for y in range(input_dim):
                    coefficients[
                        a * input_dim + x,
                        b * input_dim + y,
                    ] = (
                        choi_channel[
                            x * channel_output_dim + a,
                            y * channel_output_dim + b,
                        ]
                        / input_dim
                    )
    return coefficients


def recovery_choi_to_kraus(
    recovery_choi: Array,
    recovery_input_dim: int,
    recovery_output_dim: int,
    *,
    eigenvalue_cutoff: float = 1e-10,
) -> tuple[Array, ...]:
    """Convert an unnormalized recovery Choi matrix to Kraus operators."""
    recovery_choi = np.asarray(recovery_choi, dtype=np.complex128)
    expected = recovery_input_dim * recovery_output_dim
    if recovery_choi.shape != (expected, expected):
        raise ValueError("recovery_choi has incompatible dimensions")
    hermitian = 0.5 * (recovery_choi + recovery_choi.conj().T)
    eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
    operators: list[Array] = []
    for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors.T, strict=True):
        if eigenvalue <= eigenvalue_cutoff:
            continue
        vector = np.sqrt(eigenvalue) * eigenvector
        operator = vector.reshape(
            recovery_input_dim,
            recovery_output_dim,
        ).T
        operators.append(operator)
    if not operators:
        raise ValueError("recovery Choi matrix has no positive Kraus component")
    return tuple(operators)


def _partial_trace_output_residual(
    choi: Array,
    input_dim: int,
    output_dim: int,
) -> float:
    reduced = np.zeros((input_dim, input_dim), dtype=np.complex128)
    for a in range(input_dim):
        for b in range(input_dim):
            reduced[a, b] = sum(
                choi[a * output_dim + x, b * output_dim + x]
                for x in range(output_dim)
            )
    return float(np.linalg.norm(reduced - np.eye(input_dim), ord="fro"))


@dataclass(frozen=True)
class RecoverySDPCertificate:
    """Numerical certificate for optimal average entanglement recovery."""

    entanglement_fidelity: float
    solver_status: str
    solver_name: str
    solve_time_s: float | None
    iterations: int | None
    recovery_choi: Array
    trace_preservation_residual: float
    minimum_choi_eigenvalue: float


@dataclass(frozen=True)
class EnvironmentFidelityCertificate:
    """Environment-side constant-channel fidelity optimization."""

    root_fidelity: float
    squared_fidelity: float
    solver_status: str
    solver_name: str
    solve_time_s: float | None
    iterations: int | None
    environment_state: Array
    trace_residual: float
    minimum_environment_eigenvalue: float


@dataclass(frozen=True)
class InformationDisturbanceCertificate:
    """Cross-certificate comparing recovery and environment formulations."""

    recovery: RecoverySDPCertificate
    environment: EnvironmentFidelityCertificate
    formulation_gap: float


def optimal_entanglement_recovery(
    kraus: Iterable[Array],
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> RecoverySDPCertificate:
    """Maximize entanglement fidelity over all CPTP recovery channels."""
    cp = _cvxpy()
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, channel_output_dim = validate_kraus(operators)
    recovery_size = channel_output_dim * input_dim
    recovery_choi = cp.Variable(
        (recovery_size, recovery_size),
        hermitian=True,
    )
    constraints = [recovery_choi >> 0]
    for a in range(channel_output_dim):
        for b in range(channel_output_dim):
            traced_entry = sum(
                recovery_choi[
                    a * input_dim + x,
                    b * input_dim + x,
                ]
                for x in range(input_dim)
            )
            constraints.append(traced_entry == (1.0 if a == b else 0.0))

    coefficients = recovery_objective_coefficients(operators)
    objective = cp.Maximize(
        cp.real(cp.sum(cp.multiply(coefficients, recovery_choi)))
    )
    problem = cp.Problem(objective, constraints)
    value = problem.solve(solver=solver, verbose=verbose)
    if problem.status not in {cp.OPTIMAL, cp.OPTIMAL_INACCURATE}:
        raise RuntimeError(f"recovery SDP failed with status {problem.status}")
    if recovery_choi.value is None or value is None:
        raise RuntimeError("recovery SDP returned no solution")

    matrix = np.asarray(recovery_choi.value, dtype=np.complex128)
    matrix = 0.5 * (matrix + matrix.conj().T)
    stats = problem.solver_stats
    return RecoverySDPCertificate(
        entanglement_fidelity=float(np.clip(np.real(value), 0.0, 1.0)),
        solver_status=str(problem.status),
        solver_name=str(stats.solver_name),
        solve_time_s=(
            None if stats.solve_time is None else float(stats.solve_time)
        ),
        iterations=(
            None if stats.num_iters is None else int(stats.num_iters)
        ),
        recovery_choi=matrix,
        trace_preservation_residual=_partial_trace_output_residual(
            matrix,
            channel_output_dim,
            input_dim,
        ),
        minimum_choi_eigenvalue=float(
            np.linalg.eigvalsh(matrix).min(initial=0.0)
        ),
    )


def environment_constant_channel_fidelity(
    kraus: Iterable[Array],
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> EnvironmentFidelityCertificate:
    """Optimize complementary-state fidelity with ``I_R/d tensor sigma_E``.

    The SDP uses the standard block-matrix representation of root fidelity and
    optimizes the constant environment state ``sigma_E``.
    """
    cp = _cvxpy()
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, _ = validate_kraus(operators)
    environment_dim = len(operators)
    rho_reference_environment = complementary_choi_state(operators)
    joint_dim = input_dim * environment_dim

    sigma_environment = cp.Variable(
        (environment_dim, environment_dim),
        hermitian=True,
    )
    cross = cp.Variable((joint_dim, joint_dim), complex=True)
    constant_product = cp.kron(
        np.eye(input_dim, dtype=np.complex128) / input_dim,
        sigma_environment,
    )
    block = cp.bmat(
        [
            [rho_reference_environment, cross],
            [cross.H, constant_product],
        ]
    )
    constraints = [
        sigma_environment >> 0,
        cp.trace(sigma_environment) == 1.0,
        block >> 0,
    ]
    problem = cp.Problem(
        cp.Maximize(cp.real(cp.trace(cross))),
        constraints,
    )
    value = problem.solve(solver=solver, verbose=verbose)
    if problem.status not in {cp.OPTIMAL, cp.OPTIMAL_INACCURATE}:
        raise RuntimeError(
            f"environment fidelity SDP failed with status {problem.status}"
        )
    if sigma_environment.value is None or value is None:
        raise RuntimeError("environment fidelity SDP returned no solution")

    sigma = np.asarray(sigma_environment.value, dtype=np.complex128)
    sigma = 0.5 * (sigma + sigma.conj().T)
    root = float(np.clip(np.real(value), 0.0, 1.0))
    stats = problem.solver_stats
    return EnvironmentFidelityCertificate(
        root_fidelity=root,
        squared_fidelity=root**2,
        solver_status=str(problem.status),
        solver_name=str(stats.solver_name),
        solve_time_s=(
            None if stats.solve_time is None else float(stats.solve_time)
        ),
        iterations=(
            None if stats.num_iters is None else int(stats.num_iters)
        ),
        environment_state=sigma,
        trace_residual=float(abs(np.trace(sigma) - 1.0)),
        minimum_environment_eigenvalue=float(
            np.linalg.eigvalsh(sigma).min(initial=0.0)
        ),
    )


def certify_information_disturbance(
    kraus: Iterable[Array],
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> InformationDisturbanceCertificate:
    """Solve both state-specific recovery and environment fidelity SDPs."""
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    recovery = optimal_entanglement_recovery(
        operators,
        solver=solver,
        verbose=verbose,
    )
    environment = environment_constant_channel_fidelity(
        operators,
        solver=solver,
        verbose=verbose,
    )
    return InformationDisturbanceCertificate(
        recovery=recovery,
        environment=environment,
        formulation_gap=abs(
            recovery.entanglement_fidelity - environment.squared_fidelity
        ),
    )
