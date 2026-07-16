"""Low-dimensional diamond-norm and KSW information--disturbance SDPs.

The implementation uses the dual semidefinite program for the completely
bounded trace norm of a Hermiticity-preserving map. Choi matrices are
unnormalized and ordered as ``input tensor output`` throughout this module.

The routines are intended for transparent finite-dimensional certification.
They do not address energy-constrained infinite-dimensional channels.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from .channels import channel_choi_state, compose_channels, validate_kraus
from .optimization import _cvxpy, _solver_options

Array = np.ndarray


def unnormalized_channel_choi(kraus: Iterable[Array]) -> Array:
    """Return ``J(N)`` ordered as input tensor output."""
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, _ = validate_kraus(operators)
    return input_dim * channel_choi_state(operators)


def identity_choi(dim: int) -> Array:
    """Return the unnormalized Choi matrix of the identity channel."""
    if dim <= 0:
        raise ValueError("dim must be positive")
    omega = np.zeros(dim * dim, dtype=np.complex128)
    for index in range(dim):
        omega[index * dim + index] = 1.0
    return np.outer(omega, omega.conj())


def complementary_kraus(kraus: Iterable[Array]) -> tuple[Array, ...]:
    """Return Kraus operators for the complementary channel.

    If the original Kraus operators are ``K_e: X -> A``, the complementary
    channel has one Kraus operator ``L_a: X -> E`` for each output basis state
    ``a``, with ``(L_a)_{e,x}=(K_e)_{a,x}``.
    """
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, output_dim = validate_kraus(operators)
    environment_dim = len(operators)
    complement: list[Array] = []
    for output_index in range(output_dim):
        operator = np.zeros(
            (environment_dim, input_dim),
            dtype=np.complex128,
        )
        for environment_index, source in enumerate(operators):
            operator[environment_index, :] = source[output_index, :]
        complement.append(operator)
    result = tuple(complement)
    validate_kraus(result)
    return result


def constant_channel_kraus(state: Array, input_dim: int) -> tuple[Array, ...]:
    """Return Kraus operators for ``rho -> Tr(rho) state``."""
    state = np.asarray(state, dtype=np.complex128)
    if state.ndim != 2 or state.shape[0] != state.shape[1]:
        raise ValueError("state must be square")
    if input_dim <= 0:
        raise ValueError("input_dim must be positive")
    state = 0.5 * (state + state.conj().T)
    if not np.isclose(np.trace(state), 1.0, atol=1e-10):
        raise ValueError("state must have unit trace")
    eigenvalues, eigenvectors = np.linalg.eigh(state)
    if eigenvalues.min() < -1e-10:
        raise ValueError("state must be positive semidefinite")
    operators: list[Array] = []
    for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors.T, strict=True):
        if eigenvalue <= 1e-14:
            continue
        for basis_index in range(input_dim):
            operator = np.zeros(
                (state.shape[0], input_dim),
                dtype=np.complex128,
            )
            operator[:, basis_index] = np.sqrt(eigenvalue) * eigenvector
            operators.append(operator)
    result = tuple(operators)
    validate_kraus(result)
    return result


def _validate_choi_shape(
    choi: Array,
    input_dim: int,
    output_dim: int,
) -> Array:
    matrix = np.asarray(choi, dtype=np.complex128)
    expected = input_dim * output_dim
    if matrix.shape != (expected, expected):
        raise ValueError("choi has incompatible dimensions")
    if not np.allclose(matrix, matrix.conj().T, atol=1e-10):
        raise ValueError("choi must be Hermitian")
    return 0.5 * (matrix + matrix.conj().T)


def _partial_trace_output_expression(matrix, input_dim: int, output_dim: int):
    cp = _cvxpy()
    return cp.bmat(
        [
            [
                sum(
                    matrix[
                        row * output_dim + output_index,
                        column * output_dim + output_index,
                    ]
                    for output_index in range(output_dim)
                )
                for column in range(input_dim)
            ]
            for row in range(input_dim)
        ]
    )


def _partial_trace_output_numeric(
    matrix: Array,
    input_dim: int,
    output_dim: int,
) -> Array:
    reduced = np.zeros((input_dim, input_dim), dtype=np.complex128)
    for row in range(input_dim):
        for column in range(input_dim):
            reduced[row, column] = sum(
                matrix[
                    row * output_dim + output_index,
                    column * output_dim + output_index,
                ]
                for output_index in range(output_dim)
            )
    return reduced


def _solver_metadata(problem) -> tuple[str, str, float | None, int | None]:
    stats = problem.solver_stats
    return (
        str(problem.status),
        str(stats.solver_name),
        None if stats.solve_time is None else float(stats.solve_time),
        None if stats.num_iters is None else int(stats.num_iters),
    )


@dataclass(frozen=True)
class DiamondNormCertificate:
    """Dual-SDP certificate for one Hermiticity-preserving map."""

    diamond_norm: float
    solver_status: str
    solver_name: str
    solve_time_s: float | None
    iterations: int | None
    dual_matrix: Array
    minimum_plus_eigenvalue: float
    minimum_minus_eigenvalue: float
    partial_trace_upper_residual: float


@dataclass(frozen=True)
class ClosestConstantDiamondCertificate:
    """Certificate for distance to the closest constant-output channel."""

    diamond_distance: float
    solver_status: str
    solver_name: str
    solve_time_s: float | None
    iterations: int | None
    constant_state: Array
    dual_matrix: Array
    constant_state_trace_residual: float
    minimum_constant_state_eigenvalue: float
    minimum_plus_eigenvalue: float
    minimum_minus_eigenvalue: float
    partial_trace_upper_residual: float


@dataclass(frozen=True)
class OptimalRecoveryDiamondCertificate:
    """Certificate for optimal channel-wide recovery in diamond norm."""

    diamond_error: float
    solver_status: str
    solver_name: str
    solve_time_s: float | None
    iterations: int | None
    recovery_choi: Array
    dual_matrix: Array
    recovery_trace_preservation_residual: float
    minimum_recovery_choi_eigenvalue: float
    minimum_plus_eigenvalue: float
    minimum_minus_eigenvalue: float
    partial_trace_upper_residual: float


@dataclass(frozen=True)
class KSWDiamondCertificate:
    """Numerical evaluation of both sides of the KSW tradeoff."""

    recovery: OptimalRecoveryDiamondCertificate
    environment: ClosestConstantDiamondCertificate
    lower_margin: float
    upper_margin: float


def diamond_norm_from_choi(
    choi: Array,
    input_dim: int,
    output_dim: int,
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> DiamondNormCertificate:
    """Compute the diamond norm from an unnormalized Hermitian Choi matrix."""
    cp = _cvxpy()
    matrix = _validate_choi_shape(choi, input_dim, output_dim)
    joint_dim = input_dim * output_dim
    dual_matrix = cp.Variable((joint_dim, joint_dim), hermitian=True)
    bound = cp.Variable(nonneg=True)
    partial = _partial_trace_output_expression(
        dual_matrix,
        input_dim,
        output_dim,
    )
    constraints = [
        dual_matrix - matrix >> 0,
        dual_matrix + matrix >> 0,
        partial << bound * np.eye(input_dim),
    ]
    problem = cp.Problem(cp.Minimize(bound), constraints)
    value = problem.solve(
        solver=solver,
        verbose=verbose,
        **_solver_options(solver),
    )
    if problem.status not in {cp.OPTIMAL, cp.OPTIMAL_INACCURATE}:
        raise RuntimeError(f"diamond-norm SDP failed with status {problem.status}")
    if dual_matrix.value is None or value is None:
        raise RuntimeError("diamond-norm SDP returned no solution")

    dual = np.asarray(dual_matrix.value, dtype=np.complex128)
    dual = 0.5 * (dual + dual.conj().T)
    partial_numeric = _partial_trace_output_numeric(
        dual,
        input_dim,
        output_dim,
    )
    status, solver_name, solve_time, iterations = _solver_metadata(problem)
    return DiamondNormCertificate(
        diamond_norm=float(max(0.0, np.real(value))),
        solver_status=status,
        solver_name=solver_name,
        solve_time_s=solve_time,
        iterations=iterations,
        dual_matrix=dual,
        minimum_plus_eigenvalue=float(np.linalg.eigvalsh(dual + matrix).min()),
        minimum_minus_eigenvalue=float(np.linalg.eigvalsh(dual - matrix).min()),
        partial_trace_upper_residual=float(
            max(
                0.0,
                np.linalg.eigvalsh(
                    partial_numeric - float(np.real(value)) * np.eye(input_dim)
                ).max(),
            )
        ),
    )


def channel_diamond_distance(
    first: Iterable[Array],
    second: Iterable[Array],
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> DiamondNormCertificate:
    """Compute ``||first-second||_diamond`` for channels of equal dimensions."""
    first_ops = tuple(np.asarray(k, dtype=np.complex128) for k in first)
    second_ops = tuple(np.asarray(k, dtype=np.complex128) for k in second)
    first_dims = validate_kraus(first_ops)
    second_dims = validate_kraus(second_ops)
    if first_dims != second_dims:
        raise ValueError("channels must have equal input and output dimensions")
    input_dim, output_dim = first_dims
    difference = unnormalized_channel_choi(first_ops) - unnormalized_channel_choi(
        second_ops
    )
    return diamond_norm_from_choi(
        difference,
        input_dim,
        output_dim,
        solver=solver,
        verbose=verbose,
    )


def closest_constant_channel_diamond_distance(
    kraus: Iterable[Array],
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> ClosestConstantDiamondCertificate:
    """Compute ``inf_sigma ||N-C_sigma||_diamond`` exactly by one SDP."""
    cp = _cvxpy()
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, output_dim = validate_kraus(operators)
    channel_choi = unnormalized_channel_choi(operators)
    joint_dim = input_dim * output_dim

    state = cp.Variable((output_dim, output_dim), hermitian=True)
    dual_matrix = cp.Variable((joint_dim, joint_dim), hermitian=True)
    bound = cp.Variable(nonneg=True)
    difference = channel_choi - cp.kron(np.eye(input_dim), state)
    partial = _partial_trace_output_expression(
        dual_matrix,
        input_dim,
        output_dim,
    )
    constraints = [
        state >> 0,
        cp.trace(state) == 1.0,
        dual_matrix - difference >> 0,
        dual_matrix + difference >> 0,
        partial << bound * np.eye(input_dim),
    ]
    problem = cp.Problem(cp.Minimize(bound), constraints)
    value = problem.solve(
        solver=solver,
        verbose=verbose,
        **_solver_options(solver),
    )
    if problem.status not in {cp.OPTIMAL, cp.OPTIMAL_INACCURATE}:
        raise RuntimeError(
            f"constant-channel diamond SDP failed with status {problem.status}"
        )
    if state.value is None or dual_matrix.value is None or value is None:
        raise RuntimeError("constant-channel diamond SDP returned no solution")

    sigma = np.asarray(state.value, dtype=np.complex128)
    sigma = 0.5 * (sigma + sigma.conj().T)
    dual = np.asarray(dual_matrix.value, dtype=np.complex128)
    dual = 0.5 * (dual + dual.conj().T)
    difference_numeric = channel_choi - np.kron(np.eye(input_dim), sigma)
    partial_numeric = _partial_trace_output_numeric(
        dual,
        input_dim,
        output_dim,
    )
    status, solver_name, solve_time, iterations = _solver_metadata(problem)
    return ClosestConstantDiamondCertificate(
        diamond_distance=float(max(0.0, np.real(value))),
        solver_status=status,
        solver_name=solver_name,
        solve_time_s=solve_time,
        iterations=iterations,
        constant_state=sigma,
        dual_matrix=dual,
        constant_state_trace_residual=float(abs(np.trace(sigma) - 1.0)),
        minimum_constant_state_eigenvalue=float(np.linalg.eigvalsh(sigma).min()),
        minimum_plus_eigenvalue=float(
            np.linalg.eigvalsh(dual + difference_numeric).min()
        ),
        minimum_minus_eigenvalue=float(
            np.linalg.eigvalsh(dual - difference_numeric).min()
        ),
        partial_trace_upper_residual=float(
            max(
                0.0,
                np.linalg.eigvalsh(
                    partial_numeric - float(np.real(value)) * np.eye(input_dim)
                ).max(),
            )
        ),
    )


def _composed_choi_expression(
    channel_choi: Array,
    recovery_choi,
    input_dim: int,
    intermediate_dim: int,
    output_dim: int,
):
    cp = _cvxpy()
    rows = []
    for input_row in range(input_dim):
        for output_row in range(output_dim):
            row = []
            for input_column in range(input_dim):
                for output_column in range(output_dim):
                    entry = sum(
                        channel_choi[
                            input_row * intermediate_dim + middle_row,
                            input_column * intermediate_dim + middle_column,
                        ]
                        * recovery_choi[
                            middle_row * output_dim + output_row,
                            middle_column * output_dim + output_column,
                        ]
                        for middle_row in range(intermediate_dim)
                        for middle_column in range(intermediate_dim)
                    )
                    row.append(entry)
            rows.append(row)
    expression = cp.bmat(rows)
    return 0.5 * (expression + expression.H)


def optimal_recovery_diamond_error(
    kraus: Iterable[Array],
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> OptimalRecoveryDiamondCertificate:
    """Compute ``inf_R ||R o N-id||_diamond`` over all CPTP recoveries."""
    cp = _cvxpy()
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    input_dim, intermediate_dim = validate_kraus(operators)
    output_dim = input_dim
    channel_choi = unnormalized_channel_choi(operators)

    recovery_size = intermediate_dim * output_dim
    recovery_choi = cp.Variable(
        (recovery_size, recovery_size),
        hermitian=True,
    )
    joint_dim = input_dim * output_dim
    dual_matrix = cp.Variable((joint_dim, joint_dim), hermitian=True)
    bound = cp.Variable(nonneg=True)

    composed = _composed_choi_expression(
        channel_choi,
        recovery_choi,
        input_dim,
        intermediate_dim,
        output_dim,
    )
    difference = composed - identity_choi(input_dim)
    partial = _partial_trace_output_expression(
        dual_matrix,
        input_dim,
        output_dim,
    )

    constraints = [recovery_choi >> 0]
    for row in range(intermediate_dim):
        for column in range(intermediate_dim):
            constraints.append(
                sum(
                    recovery_choi[
                        row * output_dim + output_index,
                        column * output_dim + output_index,
                    ]
                    for output_index in range(output_dim)
                )
                == (1.0 if row == column else 0.0)
            )
    constraints.extend(
        [
            dual_matrix - difference >> 0,
            dual_matrix + difference >> 0,
            partial << bound * np.eye(input_dim),
        ]
    )
    problem = cp.Problem(cp.Minimize(bound), constraints)
    value = problem.solve(
        solver=solver,
        verbose=verbose,
        **_solver_options(solver),
    )
    if problem.status not in {cp.OPTIMAL, cp.OPTIMAL_INACCURATE}:
        raise RuntimeError(
            f"optimal-recovery diamond SDP failed with status {problem.status}"
        )
    if recovery_choi.value is None or dual_matrix.value is None or value is None:
        raise RuntimeError("optimal-recovery diamond SDP returned no solution")

    recovery = np.asarray(recovery_choi.value, dtype=np.complex128)
    recovery = 0.5 * (recovery + recovery.conj().T)
    dual = np.asarray(dual_matrix.value, dtype=np.complex128)
    dual = 0.5 * (dual + dual.conj().T)

    composed_numeric = np.zeros(
        (joint_dim, joint_dim),
        dtype=np.complex128,
    )
    for input_row in range(input_dim):
        for output_row in range(output_dim):
            for input_column in range(input_dim):
                for output_column in range(output_dim):
                    composed_numeric[
                        input_row * output_dim + output_row,
                        input_column * output_dim + output_column,
                    ] = sum(
                        channel_choi[
                            input_row * intermediate_dim + middle_row,
                            input_column * intermediate_dim + middle_column,
                        ]
                        * recovery[
                            middle_row * output_dim + output_row,
                            middle_column * output_dim + output_column,
                        ]
                        for middle_row in range(intermediate_dim)
                        for middle_column in range(intermediate_dim)
                    )
    difference_numeric = 0.5 * (
        composed_numeric
        + composed_numeric.conj().T
        - 2.0 * identity_choi(input_dim)
    )
    partial_numeric = _partial_trace_output_numeric(
        dual,
        input_dim,
        output_dim,
    )
    recovery_partial = _partial_trace_output_numeric(
        recovery,
        intermediate_dim,
        output_dim,
    )
    status, solver_name, solve_time, iterations = _solver_metadata(problem)
    return OptimalRecoveryDiamondCertificate(
        diamond_error=float(max(0.0, np.real(value))),
        solver_status=status,
        solver_name=solver_name,
        solve_time_s=solve_time,
        iterations=iterations,
        recovery_choi=recovery,
        dual_matrix=dual,
        recovery_trace_preservation_residual=float(
            np.linalg.norm(
                recovery_partial - np.eye(intermediate_dim),
                ord="fro",
            )
        ),
        minimum_recovery_choi_eigenvalue=float(
            np.linalg.eigvalsh(recovery).min()
        ),
        minimum_plus_eigenvalue=float(
            np.linalg.eigvalsh(dual + difference_numeric).min()
        ),
        minimum_minus_eigenvalue=float(
            np.linalg.eigvalsh(dual - difference_numeric).min()
        ),
        partial_trace_upper_residual=float(
            max(
                0.0,
                np.linalg.eigvalsh(
                    partial_numeric - float(np.real(value)) * np.eye(input_dim)
                ).max(),
            )
        ),
    )


def certify_ksw_diamond_tradeoff(
    kraus: Iterable[Array],
    *,
    solver: str = "CLARABEL",
    verbose: bool = False,
) -> KSWDiamondCertificate:
    """Evaluate optimal recovery and complementary leakage in diamond norm."""
    operators = tuple(np.asarray(k, dtype=np.complex128) for k in kraus)
    recovery = optimal_recovery_diamond_error(
        operators,
        solver=solver,
        verbose=verbose,
    )
    environment = closest_constant_channel_diamond_distance(
        complementary_kraus(operators),
        solver=solver,
        verbose=verbose,
    )
    lower_margin = environment.diamond_distance - 0.25 * recovery.diamond_error**2
    upper_margin = 2.0 * np.sqrt(recovery.diamond_error) - environment.diamond_distance
    return KSWDiamondCertificate(
        recovery=recovery,
        environment=environment,
        lower_margin=float(lower_margin),
        upper_margin=float(upper_margin),
    )
