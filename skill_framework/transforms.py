"""
Domain Transformation - Apply skills across different domains

Supports transformation of patterns and skills across:
- Physical domains (spatial, material, architectural)
- Social domains (organizational, community, institutional)  
- Conceptual domains (knowledge, theoretical, paradigmatic)
- Psychic domains (awareness, consciousness, mental)
"""

from enum import Enum
from typing import Dict, Any, Optional, List
import json
from pathlib import Path


class Domain(Enum):
    """Supported domains for pattern transformation"""
    PHYSICAL = "physical"
    SOCIAL = "social"
    CONCEPTUAL = "conceptual"
    PSYCHIC = "psychic"


class DomainTransformer:
    """
    Transforms patterns and skills across domains.
    
    Uses archetypal patterns with placeholder mappings to generate
    domain-specific instantiations of generic patterns.
    """
    
    def __init__(self, archetypal_patterns_path: Optional[str] = None):
        """
        Initialize transformer.
        
        Args:
            archetypal_patterns_path: Path to archetypal_patterns.json
        """
        self.archetypal_patterns = {}
        self.placeholder_mappings = {}
        
        if archetypal_patterns_path:
            self.load_patterns(archetypal_patterns_path)
    
    def load_patterns(self, path: str) -> None:
        """
        Load archetypal patterns from JSON.
        
        Args:
            path: Path to archetypal_patterns.json
        """
        with open(path, 'r') as f:
            data = json.load(f)
            if 'patterns' in data:
                for pattern in data['patterns']:
                    pattern_id = pattern.get('pattern_id')
                    if pattern_id:
                        self.archetypal_patterns[pattern_id] = pattern
    
    def transform_pattern(
        self,
        pattern_id: str,
        target_domain: Domain
    ) -> Optional[Dict[str, Any]]:
        """
        Transform a pattern to a specific domain.
        
        Args:
            pattern_id: ID of the archetypal pattern
            target_domain: Target domain (physical/social/conceptual/psychic)
            
        Returns:
            Transformed pattern dict or None if not found
        """
        pattern = self.archetypal_patterns.get(pattern_id)
        if not pattern:
            return None
        
        domain_str = target_domain.value
        
        # Get domain-specific content if available
        domain_content = pattern.get('domain_specific_content', {})
        transformed_content = domain_content.get(domain_str)
        
        # Get archetypal pattern and apply mappings
        archetypal = pattern.get('archetypal_pattern', '')
        domain_mappings = pattern.get('domain_mappings', {})
        
        # Apply placeholder substitutions
        transformed_text = archetypal
        for placeholder, mappings in domain_mappings.items():
            if domain_str in mappings:
                placeholder_pattern = f"{{{{{placeholder}}}}}"
                transformed_text = transformed_text.replace(
                    placeholder_pattern,
                    mappings[domain_str]
                )
        
        return {
            'pattern_id': pattern_id,
            'name': pattern.get('name', ''),
            'domain': domain_str,
            'archetypal_pattern': archetypal,
            'transformed_pattern': transformed_text,
            'domain_specific_content': transformed_content,
            'original_pattern': pattern
        }
    
    def get_domain_specific_content(
        self,
        pattern_id: str,
        domain: Domain
    ) -> Optional[str]:
        """
        Get domain-specific content for a pattern.
        
        Args:
            pattern_id: ID of the pattern
            domain: Target domain
            
        Returns:
            Domain-specific content text or None
        """
        pattern = self.archetypal_patterns.get(pattern_id)
        if not pattern:
            return None
        
        domain_content = pattern.get('domain_specific_content', {})
        return domain_content.get(domain.value)
    
    def get_available_domains(self, pattern_id: str) -> List[str]:
        """
        Get list of domains with specific content for a pattern.
        
        Args:
            pattern_id: ID of the pattern
            
        Returns:
            List of domain names
        """
        pattern = self.archetypal_patterns.get(pattern_id)
        if not pattern:
            return []
        
        domain_content = pattern.get('domain_specific_content', {})
        return list(domain_content.keys())
    
    def transform_skill_description(
        self,
        description: str,
        source_domain: Domain,
        target_domain: Domain,
        placeholder_mappings: Optional[Dict[str, Dict[str, str]]] = None
    ) -> str:
        """
        Transform a skill description from one domain to another.
        
        Args:
            description: Original skill description
            source_domain: Source domain
            target_domain: Target domain
            placeholder_mappings: Optional custom placeholder mappings
            
        Returns:
            Transformed description
        """
        # This is a simple implementation that could be enhanced
        # with more sophisticated NLP-based transformation
        
        if not placeholder_mappings:
            # Use default mappings from loaded patterns
            placeholder_mappings = self._get_default_mappings()
        
        transformed = description
        for placeholder, mappings in placeholder_mappings.items():
            if source_domain.value in mappings and target_domain.value in mappings:
                source_term = mappings[source_domain.value]
                target_term = mappings[target_domain.value]
                transformed = transformed.replace(source_term, target_term)
        
        return transformed
    
    def _get_default_mappings(self) -> Dict[str, Dict[str, str]]:
        """
        Get default placeholder mappings from loaded patterns.
        
        Returns:
            Dictionary of placeholder mappings
        """
        # Extract common mappings from first pattern
        if not self.archetypal_patterns:
            return {}
        
        first_pattern = next(iter(self.archetypal_patterns.values()))
        return first_pattern.get('domain_mappings', {})
    
    def __repr__(self) -> str:
        return f"DomainTransformer(patterns={len(self.archetypal_patterns)})"
