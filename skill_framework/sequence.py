"""
SkillSequence - Ordered collection of skills

Represents an ordered sequence of skills that form a coherent routine or workflow step.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field
from .skill import Skill, SkillResult
from .context import SkillContext


@dataclass
class SkillSequence:
    """
    An ordered sequence of skills forming a routine.
    
    Corresponds to pattern sequences in the Pattern Language (e.g., 36 sequences).
    Each sequence represents a coherent set of patterns applied in order.
    """
    
    sequence_id: str
    name: str
    description: str
    skills: List[Skill] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_skill(self, skill: Skill) -> 'SkillSequence':
        """
        Add a skill to the sequence.
        
        Args:
            skill: Skill to add
            
        Returns:
            Self for chaining
        """
        self.skills.append(skill)
        return self
    
    def execute(self, context: SkillContext) -> List[SkillResult]:
        """
        Execute all skills in sequence.
        
        Args:
            context: Execution context
            
        Returns:
            List of SkillResults, one per skill
        """
        results = []
        
        for skill in self.skills:
            result = skill.execute(context)
            results.append(result)
            context.add_history(skill.pattern_id, result)
            
            # Stop on failure if not configured to continue
            if result.is_failed and not self.metadata.get("continue_on_error", False):
                break
            
            # Clear local scope between skills
            context.clear_local()
        
        return results
    
    def __len__(self) -> int:
        """Return number of skills in sequence"""
        return len(self.skills)
    
    def __repr__(self) -> str:
        return f"SkillSequence(id={self.sequence_id}, name={self.name}, skills={len(self.skills)})"


class SequenceBuilder:
    """
    Fluent interface for building skill sequences.
    
    Example:
        sequence = (SequenceBuilder("seq1", "My Sequence")
                   .with_description("A test sequence")
                   .add_skill(skill1)
                   .add_skill(skill2)
                   .build())
    """
    
    def __init__(self, sequence_id: str, name: str):
        """
        Initialize builder.
        
        Args:
            sequence_id: Unique identifier for the sequence
            name: Human-readable name
        """
        self._sequence_id = sequence_id
        self._name = name
        self._description = ""
        self._skills: List[Skill] = []
        self._metadata: Dict[str, Any] = {}
    
    def with_description(self, description: str) -> 'SequenceBuilder':
        """
        Set sequence description.
        
        Args:
            description: Description text
            
        Returns:
            Self for chaining
        """
        self._description = description
        return self
    
    def add_skill(self, skill: Skill) -> 'SequenceBuilder':
        """
        Add a skill to the sequence.
        
        Args:
            skill: Skill to add
            
        Returns:
            Self for chaining
        """
        self._skills.append(skill)
        return self
    
    def add_skills(self, skills: List[Skill]) -> 'SequenceBuilder':
        """
        Add multiple skills to the sequence.
        
        Args:
            skills: List of skills to add
            
        Returns:
            Self for chaining
        """
        self._skills.extend(skills)
        return self
    
    def with_metadata(self, key: str, value: Any) -> 'SequenceBuilder':
        """
        Add metadata to the sequence.
        
        Args:
            key: Metadata key
            value: Metadata value
            
        Returns:
            Self for chaining
        """
        self._metadata[key] = value
        return self
    
    def continue_on_error(self, enabled: bool = True) -> 'SequenceBuilder':
        """
        Configure whether to continue execution on skill failure.
        
        Args:
            enabled: If True, continue even on skill failures
            
        Returns:
            Self for chaining
        """
        self._metadata["continue_on_error"] = enabled
        return self
    
    def build(self) -> SkillSequence:
        """
        Build the SkillSequence.
        
        Returns:
            Constructed SkillSequence
        """
        return SkillSequence(
            sequence_id=self._sequence_id,
            name=self._name,
            description=self._description,
            skills=self._skills.copy(),
            metadata=self._metadata.copy()
        )
