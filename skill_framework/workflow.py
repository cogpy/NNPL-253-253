"""
SkillWorkflow - Algorithmic workflow execution engine

Implements algorithmic workflows that orchestrate sequences of skills with
support for sequential, conditional, and parallel execution.
"""

from enum import Enum
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
import time

from .skill import Skill, SkillResult, SkillStatus
from .sequence import SkillSequence
from .context import SkillContext


class ExecutionMode(Enum):
    """Workflow execution mode"""
    SEQUENTIAL = "sequential"  # Execute skills one after another
    PARALLEL = "parallel"      # Execute skills concurrently (future)
    CONDITIONAL = "conditional"  # Execute skills based on conditions


@dataclass
class WorkflowStep:
    """A single step in a workflow"""
    step_id: str
    skill_or_sequence: Any  # Skill or SkillSequence
    condition: Optional[Callable[[SkillContext], bool]] = None
    on_success: Optional[str] = None  # Next step ID on success
    on_failure: Optional[str] = None  # Next step ID on failure
    metadata: Dict[str, Any] = field(default_factory=dict)


class SkillWorkflow:
    """
    Algorithmic workflow that orchestrates skill sequences.
    
    Supports:
    - Sequential execution
    - Conditional branching
    - Error handling and recovery
    - Multiple sequences composition
    """
    
    def __init__(
        self,
        workflow_id: str,
        name: str,
        description: str = "",
        execution_mode: ExecutionMode = ExecutionMode.SEQUENTIAL
    ):
        """
        Initialize workflow.
        
        Args:
            workflow_id: Unique identifier
            name: Human-readable name
            description: Workflow description
            execution_mode: How to execute steps
        """
        self.workflow_id = workflow_id
        self.name = name
        self.description = description
        self.execution_mode = execution_mode
        self.steps: Dict[str, WorkflowStep] = {}
        self.start_step: Optional[str] = None
        self.metadata: Dict[str, Any] = {}
    
    def add_step(
        self,
        step_id: str,
        skill_or_sequence: Any,
        condition: Optional[Callable[[SkillContext], bool]] = None,
        on_success: Optional[str] = None,
        on_failure: Optional[str] = None
    ) -> 'SkillWorkflow':
        """
        Add a step to the workflow.
        
        Args:
            step_id: Unique step identifier
            skill_or_sequence: Skill or SkillSequence to execute
            condition: Optional condition to check before execution
            on_success: Next step ID on success (for conditional mode)
            on_failure: Next step ID on failure (for conditional mode)
            
        Returns:
            Self for chaining
        """
        step = WorkflowStep(
            step_id=step_id,
            skill_or_sequence=skill_or_sequence,
            condition=condition,
            on_success=on_success,
            on_failure=on_failure
        )
        self.steps[step_id] = step
        
        # First step becomes start step
        if self.start_step is None:
            self.start_step = step_id
        
        return self
    
    def set_start_step(self, step_id: str) -> 'SkillWorkflow':
        """
        Set the starting step.
        
        Args:
            step_id: ID of step to start with
            
        Returns:
            Self for chaining
        """
        if step_id not in self.steps:
            raise ValueError(f"Step {step_id} not found")
        self.start_step = step_id
        return self
    
    def __repr__(self) -> str:
        return f"SkillWorkflow(id={self.workflow_id}, name={self.name}, steps={len(self.steps)})"


class WorkflowEngine:
    """
    Engine for executing workflows.
    
    Handles execution logic, error recovery, and result collection.
    """
    
    def __init__(self, verbose: bool = False):
        """
        Initialize engine.
        
        Args:
            verbose: Enable verbose logging
        """
        self.verbose = verbose
    
    def execute(self, workflow: SkillWorkflow, context: SkillContext) -> Dict[str, Any]:
        """
        Execute a workflow with given context.
        
        Args:
            workflow: Workflow to execute
            context: Execution context
            
        Returns:
            Dictionary with execution results and metadata
        """
        start_time = time.time()
        
        if workflow.execution_mode == ExecutionMode.SEQUENTIAL:
            results = self._execute_sequential(workflow, context)
        elif workflow.execution_mode == ExecutionMode.CONDITIONAL:
            results = self._execute_conditional(workflow, context)
        else:
            raise NotImplementedError(f"Execution mode {workflow.execution_mode} not implemented")
        
        duration_ms = (time.time() - start_time) * 1000
        
        return {
            "workflow_id": workflow.workflow_id,
            "status": "completed",
            "results": results,
            "duration_ms": duration_ms,
            "context": context
        }
    
    def _execute_sequential(self, workflow: SkillWorkflow, context: SkillContext) -> List[Any]:
        """Execute workflow steps sequentially"""
        results = []
        
        for step_id in sorted(workflow.steps.keys()):
            step = workflow.steps[step_id]
            
            if self.verbose:
                print(f"Executing step: {step_id}")
            
            # Check condition if present
            if step.condition and not step.condition(context):
                if self.verbose:
                    print(f"  Skipping (condition not met)")
                continue
            
            # Execute skill or sequence
            if isinstance(step.skill_or_sequence, Skill):
                result = step.skill_or_sequence.execute(context)
                results.append({"step_id": step_id, "result": result})
                context.add_history(step_id, result)
            elif isinstance(step.skill_or_sequence, SkillSequence):
                seq_results = step.skill_or_sequence.execute(context)
                results.append({"step_id": step_id, "results": seq_results})
            
            # Clear local scope between steps
            context.clear_local()
        
        return results
    
    def _execute_conditional(self, workflow: SkillWorkflow, context: SkillContext) -> List[Any]:
        """Execute workflow with conditional branching"""
        results = []
        current_step_id = workflow.start_step
        
        max_iterations = 1000  # Prevent infinite loops
        iteration = 0
        
        while current_step_id and iteration < max_iterations:
            iteration += 1
            
            step = workflow.steps.get(current_step_id)
            if not step:
                break
            
            if self.verbose:
                print(f"Executing step: {current_step_id}")
            
            # Check condition
            if step.condition and not step.condition(context):
                if self.verbose:
                    print(f"  Skipping (condition not met)")
                # For conditional mode, move to failure branch
                current_step_id = step.on_failure
                continue
            
            # Execute skill or sequence
            success = True
            if isinstance(step.skill_or_sequence, Skill):
                result = step.skill_or_sequence.execute(context)
                results.append({"step_id": current_step_id, "result": result})
                context.add_history(current_step_id, result)
                success = result.is_success
            elif isinstance(step.skill_or_sequence, SkillSequence):
                seq_results = step.skill_or_sequence.execute(context)
                results.append({"step_id": current_step_id, "results": seq_results})
                # Check if all succeeded
                success = all(r.is_success for r in seq_results if isinstance(r, SkillResult))
            
            # Determine next step
            if success and step.on_success:
                current_step_id = step.on_success
            elif not success and step.on_failure:
                current_step_id = step.on_failure
            else:
                # No explicit next step
                break
            
            # Clear local scope
            context.clear_local()
        
        if iteration >= max_iterations:
            raise RuntimeError(f"Workflow exceeded maximum iterations: {max_iterations}")
        
        return results
