"""
SIMPLEXITY v2.0 - Eight Modules
================================

The 8-module framework for complexity management.
"""

from .abstraction import AbstractionLevel, AbstractionModule
from .emergence import EmergenceType, EmergenceModule
from .decomposition import DecompositionStrategy, DecompositionModule
from .simplification import SimplificationLevel, SimplificationModule
from .dynamics import DynamicsModule
from .calibration import CognitiveProfile, CalibrationModule
from .transfer import TransferModule
from .mvc import MVCModule

__all__ = [
    "AbstractionLevel",
    "AbstractionModule",
    "EmergenceType",
    "EmergenceModule",
    "DecompositionStrategy",
    "DecompositionModule",
    "SimplificationLevel",
    "SimplificationModule",
    "DynamicsModule",
    "CognitiveProfile",
    "CalibrationModule",
    "TransferModule",
    "MVCModule",
]
