"""
Skill Framework - Generalized Pattern-Based Workflow System

This framework implements sequences of skills as ordered routines defined by
algorithmic workflows, where each step applies a pattern as a skill.

The framework is domain-agnostic and supports application to any domain of inquiry:
- Physical domains (spatial, material, architectural)
- Social domains (organizational, community, institutional)
- Conceptual domains (knowledge, theoretical, paradigmatic)
- Psychic domains (awareness, consciousness, mental)
"""

from .skill import Skill, SkillResult, SkillStatus
from .sequence import SkillSequence, SequenceBuilder
from .workflow import SkillWorkflow, WorkflowEngine, ExecutionMode
from .context import SkillContext, ContextScope
from .transforms import DomainTransformer, Domain

__version__ = "1.0.0"
__all__ = [
    # Core classes
    "Skill",
    "SkillResult",
    "SkillStatus",
    "SkillSequence",
    "SequenceBuilder",
    "SkillWorkflow",
    "WorkflowEngine",
    "ExecutionMode",
    "SkillContext",
    "ContextScope",
    "DomainTransformer",
    "Domain",
]
