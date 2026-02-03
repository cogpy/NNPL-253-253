"""
SkillContext - Execution context for skill workflows

Provides state management, data flow, and scope handling for skill execution.
"""

from enum import Enum
from typing import Any, Dict, Optional, List
from dataclasses import dataclass, field


class ContextScope(Enum):
    """Scope of context variables"""
    GLOBAL = "global"      # Available to all skills in workflow
    SEQUENCE = "sequence"  # Available within a sequence
    LOCAL = "local"        # Available only to current skill


@dataclass
class SkillContext:
    """
    Execution context for skills and workflows.
    
    Manages state, inputs, outputs, and data flow between skills.
    Supports scoped variables for isolation and composition.
    """
    
    # Input data for the workflow
    inputs: Dict[str, Any] = field(default_factory=dict)
    
    # Output data from the workflow
    outputs: Dict[str, Any] = field(default_factory=dict)
    
    # Global variables (shared across all skills)
    global_vars: Dict[str, Any] = field(default_factory=dict)
    
    # Sequence-scoped variables
    sequence_vars: Dict[str, Any] = field(default_factory=dict)
    
    # Local variables (current skill only)
    local_vars: Dict[str, Any] = field(default_factory=dict)
    
    # Execution history
    execution_history: List[Dict[str, Any]] = field(default_factory=list)
    
    # Domain context (physical, social, conceptual, psychic)
    domain: Optional[str] = None
    
    # Metadata about the execution
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def get(self, key: str, default: Any = None, scope: ContextScope = ContextScope.GLOBAL) -> Any:
        """
        Get a variable from the specified scope.
        
        Args:
            key: Variable name
            default: Default value if not found
            scope: Scope to search
            
        Returns:
            Variable value or default
        """
        if scope == ContextScope.LOCAL:
            return self.local_vars.get(key, default)
        elif scope == ContextScope.SEQUENCE:
            return self.sequence_vars.get(key, default)
        else:  # GLOBAL
            return self.global_vars.get(key, default)
    
    def set(self, key: str, value: Any, scope: ContextScope = ContextScope.GLOBAL) -> None:
        """
        Set a variable in the specified scope.
        
        Args:
            key: Variable name
            value: Variable value
            scope: Scope to set in
        """
        if scope == ContextScope.LOCAL:
            self.local_vars[key] = value
        elif scope == ContextScope.SEQUENCE:
            self.sequence_vars[key] = value
        else:  # GLOBAL
            self.global_vars[key] = value
    
    def has(self, key: str, scope: ContextScope = ContextScope.GLOBAL) -> bool:
        """
        Check if a variable exists in the specified scope.
        
        Args:
            key: Variable name
            scope: Scope to check
            
        Returns:
            True if variable exists
        """
        if scope == ContextScope.LOCAL:
            return key in self.local_vars
        elif scope == ContextScope.SEQUENCE:
            return key in self.sequence_vars
        else:  # GLOBAL
            return key in self.global_vars
    
    def clear_local(self) -> None:
        """Clear local scope (call between skills)"""
        self.local_vars.clear()
    
    def clear_sequence(self) -> None:
        """Clear sequence scope (call between sequences)"""
        self.sequence_vars.clear()
        self.local_vars.clear()
    
    def add_history(self, skill_id: str, result: Any) -> None:
        """
        Add an entry to execution history.
        
        Args:
            skill_id: ID of the skill that executed
            result: Result of the execution
        """
        self.execution_history.append({
            "skill_id": skill_id,
            "result": result,
            "timestamp": self._get_timestamp()
        })
    
    def _get_timestamp(self) -> float:
        """Get current timestamp"""
        import time
        return time.time()
    
    def clone(self) -> 'SkillContext':
        """
        Create a deep copy of the context.
        
        Returns:
            New SkillContext with copied data
        """
        import copy
        return SkillContext(
            inputs=copy.deepcopy(self.inputs),
            outputs=copy.deepcopy(self.outputs),
            global_vars=copy.deepcopy(self.global_vars),
            sequence_vars=copy.deepcopy(self.sequence_vars),
            local_vars=copy.deepcopy(self.local_vars),
            execution_history=copy.deepcopy(self.execution_history),
            domain=self.domain,
            metadata=copy.deepcopy(self.metadata)
        )
    
    def __repr__(self) -> str:
        return (f"SkillContext(domain={self.domain}, "
                f"global_vars={len(self.global_vars)}, "
                f"sequence_vars={len(self.sequence_vars)}, "
                f"local_vars={len(self.local_vars)}, "
                f"history={len(self.execution_history)})")
