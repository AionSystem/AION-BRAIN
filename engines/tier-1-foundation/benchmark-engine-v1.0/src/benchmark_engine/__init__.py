"""
BENCHMARK ENGINE v1.0 (METIS)
=============================

The Universal AI Safety Validation Framework.

Every AION Cognitive Engine is validated on exactly 1,531 prompts
using a PSA v1.2-derived rubric with certified human+AI grading.

This is the yardstick. Everything else is noise.

Author: Sheldon K. Salmon
Codename: METIS
License: Apache 2.0
"""

from .core import BenchmarkEngine
from .config import BenchmarkConfig, Domain, CertificationLevel
from .types import (
    BenchmarkReport, PSAScore, DimensionScore, 
    Rubric, Prompt, EvaluationResult, Certificate
)

__version__ = "1.0.0"
__codename__ = "METIS"
__author__ = "Sheldon K. Salmon"

__all__ = [
    "BenchmarkEngine",
    "BenchmarkConfig",
    "Domain",
    "CertificationLevel",
    "BenchmarkReport",
    "PSAScore",
    "DimensionScore",
    "Rubric",
    "Prompt",
    "EvaluationResult",
    "Certificate",
]
