"""
Skill - Pattern wrapper with execution semantics

A Skill represents a pattern applied as an actionable unit in a workflow.
Each skill can be executed with context, producing results.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, Callable
from dataclasses import dataclass, field
import time


class SkillStatus(Enum):
    """Status of skill execution"""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class SkillResult:
    """Result of skill execution"""
    status: SkillStatus
    output: Any = None
    error: Optional[str] = None
    duration_ms: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def is_success(self) -> bool:
        """Check if execution was successful"""
        return self.status == SkillStatus.SUCCESS
    
    @property
    def is_failed(self) -> bool:
        """Check if execution failed"""
        return self.status == SkillStatus.FAILED


class Skill:
    """
    A Skill wraps a pattern with execution semantics.
    
    Skills can be:
    - Executed with context
    - Composed into sequences
    - Applied across domains
    - Validated for preconditions
    - Used to produce outputs
    """
    
    def __init__(
        self,
        pattern_id: str,
        name: str,
        description: str,
        execute_fn: Optional[Callable] = None,
        preconditions: Optional[List[Callable]] = None,
        postconditions: Optional[List[Callable]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a skill.
        
        Args:
            pattern_id: ID of the underlying pattern (e.g., "apl1", "12610010")
            name: Human-readable name of the skill
            description: What the skill accomplishes
            execute_fn: Optional execution function
            preconditions: Functions to check before execution
            postconditions: Functions to validate after execution
            metadata: Additional skill metadata
        """
        self.pattern_id = pattern_id
        self.name = name
        self.description = description
        self.execute_fn = execute_fn
        self.preconditions = preconditions or []
        self.postconditions = postconditions or []
        self.metadata = metadata or {}
        
    def check_preconditions(self, context: Any) -> tuple[bool, Optional[str]]:
        """
        Check if preconditions are met.
        
        Args:
            context: Execution context
            
        Returns:
            (success, error_message)
        """
        for i, check in enumerate(self.preconditions):
            try:
                result = check(context)
                if not result:
                    return False, f"Precondition {i} failed"
            except Exception as e:
                return False, f"Precondition {i} raised exception: {e}"
        return True, None
    
    def check_postconditions(self, context: Any, result: Any) -> tuple[bool, Optional[str]]:
        """
        Check if postconditions are met.
        
        Args:
            context: Execution context
            result: Result of execution
            
        Returns:
            (success, error_message)
        """
        for i, check in enumerate(self.postconditions):
            try:
                ok = check(context, result)
                if not ok:
                    return False, f"Postcondition {i} failed"
            except Exception as e:
                return False, f"Postcondition {i} raised exception: {e}"
        return True, None
    
    def execute(self, context: Any) -> SkillResult:
        """
        Execute the skill with given context.
        
        Args:
            context: Execution context containing inputs and state
            
        Returns:
            SkillResult with execution outcome
        """
        start_time = time.time()
        
        # Check preconditions
        precond_ok, precond_error = self.check_preconditions(context)
        if not precond_ok:
            return SkillResult(
                status=SkillStatus.FAILED,
                error=f"Precondition failed: {precond_error}",
                duration_ms=(time.time() - start_time) * 1000
            )
        
        # Execute skill
        try:
            if self.execute_fn:
                output = self.execute_fn(context)
            else:
                # Default behavior: just pass through context
                output = {"pattern_applied": self.pattern_id}
            
            # Check postconditions
            postcond_ok, postcond_error = self.check_postconditions(context, output)
            if not postcond_ok:
                return SkillResult(
                    status=SkillStatus.FAILED,
                    error=f"Postcondition failed: {postcond_error}",
                    output=output,
                    duration_ms=(time.time() - start_time) * 1000
                )
            
            return SkillResult(
                status=SkillStatus.SUCCESS,
                output=output,
                duration_ms=(time.time() - start_time) * 1000,
                metadata={"pattern_id": self.pattern_id}
            )
            
        except Exception as e:
            return SkillResult(
                status=SkillStatus.FAILED,
                error=str(e),
                duration_ms=(time.time() - start_time) * 1000
            )
    
    def __repr__(self) -> str:
        return f"Skill(pattern_id={self.pattern_id}, name={self.name})"
