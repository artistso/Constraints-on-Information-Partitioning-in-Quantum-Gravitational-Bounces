"""Validation tools for the quantum-gravitational bounce research program."""

from .channels import (
    amplitude_damping_channel,
    coherent_information,
    dephasing_channel,
    depolarizing_channel,
    erasure_channel,
)
from .gravity import baseline_scales
from .quantum import localization_diagnostics
from .recovery import recovery_diagnostics
from .remnants import radiation_information_lower_bound

__all__ = [
    "amplitude_damping_channel",
    "baseline_scales",
    "coherent_information",
    "dephasing_channel",
    "depolarizing_channel",
    "erasure_channel",
    "localization_diagnostics",
    "radiation_information_lower_bound",
    "recovery_diagnostics",
]
