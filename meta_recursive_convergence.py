#!/usr/bin/env python3
"""
Meta-Recursive Convergence: Apply the Pattern Language to Itself

This module implements the iterative application of patterns to the pattern language
repository structure to ensure convergence to optimal grip on the fitness function.

The hierarchical structure follows base-6:
- Level 0: 1 meta-pattern (6^0 = 1)
- Level 1: 6 dimensions (6^1 = 6)
- Level 2: 36 sequences (6^2 = 36)
- Level 3: 216 core patterns (6^3 = 216)
- Total: 1 + 6 + 36 + 216 = 253

Fitness function measures:
1. Multi-scale perception clarity
2. Relationship richness
3. Contextual relevance
4. Gestalt perception
5. Interactive navigation
6. Self-similarity across scales
"""

import json
import os
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FitnessMetrics:
    """Metrics for evaluating optimal grip on pattern language structure."""
    multi_scale_clarity: float  # 0-1: How clear is structure at each scale?
    relationship_richness: float  # 0-1: How well are connections represented?
    contextual_relevance: float  # 0-1: Can users find patterns by context?
    gestalt_perception: float  # 0-1: Are wholes perceivable?
    interactive_navigation: float  # 0-1: Can users navigate fluidly?
    self_similarity: float  # 0-1: Do patterns apply to themselves?
    
    @property
    def overall_fitness(self) -> float:
        """Weighted average of all metrics."""
        weights = {
            'multi_scale_clarity': 0.20,
            'relationship_richness': 0.20,
            'contextual_relevance': 0.15,
            'gestalt_perception': 0.15,
            'interactive_navigation': 0.15,
            'self_similarity': 0.15,
        }
        return (
            self.multi_scale_clarity * weights['multi_scale_clarity'] +
            self.relationship_richness * weights['relationship_richness'] +
            self.contextual_relevance * weights['contextual_relevance'] +
            self.gestalt_perception * weights['gestalt_perception'] +
            self.interactive_navigation * weights['interactive_navigation'] +
            self.self_similarity * weights['self_similarity']
        )


class MetaRecursiveAnalyzer:
    """Analyzes and improves the meta-recursive structure."""
    
    def __init__(self, repo_root: str = "."):
        self.repo_root = Path(repo_root)
        self.pattern_data = None
        self.sequence_data = None
        
    def load_data(self):
        """Load pattern language data."""
        with open(self.repo_root / "pattern_language_generated.json") as f:
            self.pattern_data = json.load(f)
        with open(self.repo_root / "pattern_sequences.json") as f:
            self.sequence_data = json.load(f)
    
    def verify_base6_structure(self) -> Dict[str, Any]:
        """Verify the base-6 hierarchical structure."""
        self.load_data()
        
        # Count actual structure
        num_sequences = len(self.sequence_data['sequences'])
        num_patterns = len(self.pattern_data.get('patterns', []))
        
        # Expected base-6 structure
        expected = {
            'level_0_meta': 1,  # The whole pattern language
            'level_1_dimensions': 6,  # 6 dimensions (already exists in agents)
            'level_2_sequences': 36,  # 6×6 thematic flows
            'level_3_patterns': 210,  # Patterns organized in sequences
            'total': 253  # 1 + 6 + 36 + 210 = 253
        }
        
        actual = {
            'level_0_meta': 1,
            'level_1_dimensions': 6,  # From .github/agents/apl0/
            'level_2_sequences': num_sequences,
            'level_3_patterns': num_patterns,
            'total': num_patterns
        }
        
        verification = {
            'expected': expected,
            'actual': actual,
            'matches': {
                'sequences': num_sequences == expected['level_2_sequences'],
                'total_patterns': num_patterns == expected['total'],
            }
        }
        
        return verification
    
    def calculate_fitness(self) -> FitnessMetrics:
        """Calculate current fitness metrics."""
        self.load_data()
        
        # Analyze multi-scale clarity
        multi_scale = self._assess_multi_scale_clarity()
        
        # Analyze relationship richness  
        relationships = self._assess_relationship_richness()
        
        # Analyze contextual relevance
        context = self._assess_contextual_relevance()
        
        # Analyze gestalt perception
        gestalt = self._assess_gestalt_perception()
        
        # Analyze navigation
        navigation = self._assess_navigation()
        
        # Analyze self-similarity
        self_sim = self._assess_self_similarity()
        
        return FitnessMetrics(
            multi_scale_clarity=multi_scale,
            relationship_richness=relationships,
            contextual_relevance=context,
            gestalt_perception=gestalt,
            interactive_navigation=navigation,
            self_similarity=self_sim
        )
    
    def _assess_multi_scale_clarity(self) -> float:
        """Assess how clearly structure is visible at each scale."""
        checks = []
        
        # Check if meta-pattern is defined
        checks.append(1.0 if 'meta_pattern' in self.pattern_data else 0.0)
        
        # Check if categories are clearly defined
        checks.append(1.0 if len(self.pattern_data['categories']) > 0 else 0.0)
        
        # Check if sequences are organized
        checks.append(1.0 if len(self.sequence_data['sequences']) == 36 else 0.8)
        
        # Check if patterns have clear hierarchy
        has_clear_hierarchy = all(
            'category' in seq for seq in self.sequence_data['sequences']
        )
        checks.append(1.0 if has_clear_hierarchy else 0.5)
        
        return sum(checks) / len(checks)
    
    def _assess_relationship_richness(self) -> float:
        """Assess quality of pattern relationships."""
        checks = []
        
        # Check if sequences define pattern relationships
        seq_has_patterns = all(
            'patterns' in seq and len(seq['patterns']) > 0
            for seq in self.sequence_data['sequences']
        )
        checks.append(1.0 if seq_has_patterns else 0.3)
        
        # Check if emergent phenomena are documented
        has_emergent = all(
            'emergent_phenomena' in seq
            for seq in self.sequence_data['sequences']
        )
        checks.append(1.0 if has_emergent else 0.5)
        
        # Check if cross-references exist
        cross_refs_exist = os.path.exists(
            self.repo_root / "PATTERN_CROSS_REFERENCE.md"
        )
        checks.append(1.0 if cross_refs_exist else 0.0)
        
        # Check if OpenCog hypergraph exists
        atomese_exists = os.path.exists(
            self.repo_root / "opencog_atomese" / "pattern_language.scm"
        )
        checks.append(1.0 if atomese_exists else 0.0)
        
        return sum(checks) / len(checks)
    
    def _assess_contextual_relevance(self) -> float:
        """Assess ability to find patterns by context."""
        checks = []
        
        # Check if pattern index exists
        checks.append(1.0 if os.path.exists(
            self.repo_root / "PATTERN_INDEX.md"
        ) else 0.0)
        
        # Check if navigation hub exists
        checks.append(1.0 if os.path.exists(
            self.repo_root / "NAVIGATION_HUB.md"
        ) else 0.0)
        
        # Check if sequence navigation exists
        checks.append(1.0 if os.path.exists(
            self.repo_root / "SEQUENCE_NAVIGATION.md"
        ) else 0.0)
        
        return sum(checks) / len(checks)
    
    def _assess_gestalt_perception(self) -> float:
        """Assess ability to perceive wholes."""
        checks = []
        
        # Check if sequences create emergent phenomena
        has_emergent = all(
            'emergent_phenomena' in seq and seq['emergent_phenomena']
            for seq in self.sequence_data['sequences']
        )
        checks.append(1.0 if has_emergent else 0.0)
        
        # Check if pattern map exists
        checks.append(1.0 if os.path.exists(
            self.repo_root / "PATTERN_MAP.md"
        ) else 0.0)
        
        # Check if meta-recursive doc exists
        checks.append(1.0 if os.path.exists(
            self.repo_root / "META_RECURSIVE_IMPLEMENTATION.md"
        ) else 0.0)
        
        return sum(checks) / len(checks)
    
    def _assess_navigation(self) -> float:
        """Assess ease of navigation."""
        checks = []
        
        # Check for multiple entry points (Pattern 28)
        entry_points = [
            "README.md",
            "NAVIGATION_HUB.md",
            "PATTERN_INDEX.md",
            "SEQUENCE_NAVIGATION.md"
        ]
        existing = sum(1 for ep in entry_points 
                      if os.path.exists(self.repo_root / ep))
        checks.append(existing / len(entry_points))
        
        # Check for agent hierarchy
        agent_exists = os.path.exists(
            self.repo_root / ".github" / "agents" / "apl0"
        )
        checks.append(1.0 if agent_exists else 0.0)
        
        return sum(checks) / len(checks)
    
    def _assess_self_similarity(self) -> float:
        """Assess how well patterns apply to themselves."""
        checks = []
        
        # Check if repository uses Pattern 1 (Independent Regions)
        regions = ['apl', 'uia', 'markdown', 'pattern', 'opencog_atomese', 
                  'npu253', 'apl_language', 'docs']
        existing_regions = sum(1 for r in regions 
                              if os.path.exists(self.repo_root / r))
        checks.append(existing_regions / len(regions))
        
        # Check if meta-recursive implementation documented
        checks.append(1.0 if os.path.exists(
            self.repo_root / "META_RECURSIVE_IMPLEMENTATION.md"
        ) else 0.0)
        
        return sum(checks) / len(checks)
    
    def generate_improvement_plan(self, metrics: FitnessMetrics) -> List[str]:
        """Generate specific improvements based on fitness metrics."""
        improvements = []
        
        threshold = 0.8  # Target threshold for each metric
        
        if metrics.multi_scale_clarity < threshold:
            improvements.append(
                "Enhance multi-scale clarity: Create clearer visual hierarchy "
                "showing Level 0 (meta) → Level 1 (6 dims) → Level 2 (36 seqs) "
                "→ Level 3 (216+37 patterns)"
            )
        
        if metrics.relationship_richness < threshold:
            improvements.append(
                "Enrich relationships: Add more cross-dimensional links, "
                "complement/conflict/alternative relationships, "
                "and emergent pattern groupings"
            )
        
        if metrics.contextual_relevance < threshold:
            improvements.append(
                "Improve context access: Add domain-specific indexes, "
                "problem-solution mappings, and context-aware search"
            )
        
        if metrics.gestalt_perception < threshold:
            improvements.append(
                "Strengthen gestalt perception: Document more emergent phenomena, "
                "create visualizations of pattern clusters, "
                "highlight synergistic combinations"
            )
        
        if metrics.interactive_navigation < threshold:
            improvements.append(
                "Enhance navigation: Add more entry points (Pattern 28), "
                "create network of paths (Pattern 52), "
                "improve activity nodes (Pattern 30)"
            )
        
        if metrics.self_similarity < threshold:
            improvements.append(
                "Deepen self-similarity: Apply more patterns to repository structure, "
                "document how each pattern manifests in the codebase, "
                "create recursive pattern applications"
            )
        
        return improvements


def main():
    """Main analysis and reporting."""
    analyzer = MetaRecursiveAnalyzer()
    
    print("=" * 70)
    print("META-RECURSIVE CONVERGENCE ANALYSIS")
    print("=" * 70)
    print()
    
    # Verify structure
    print("1. VERIFYING BASE-6 HIERARCHICAL STRUCTURE")
    print("-" * 70)
    verification = analyzer.verify_base6_structure()
    print(f"Expected: {verification['expected']}")
    print(f"Actual:   {verification['actual']}")
    print(f"Matches:  {verification['matches']}")
    print()
    
    # Calculate fitness
    print("2. CALCULATING FITNESS METRICS")
    print("-" * 70)
    metrics = analyzer.calculate_fitness()
    print(f"Multi-scale Clarity:      {metrics.multi_scale_clarity:.2%}")
    print(f"Relationship Richness:    {metrics.relationship_richness:.2%}")
    print(f"Contextual Relevance:     {metrics.contextual_relevance:.2%}")
    print(f"Gestalt Perception:       {metrics.gestalt_perception:.2%}")
    print(f"Interactive Navigation:   {metrics.interactive_navigation:.2%}")
    print(f"Self-Similarity:          {metrics.self_similarity:.2%}")
    print(f"\nOVERALL FITNESS:          {metrics.overall_fitness:.2%}")
    print()
    
    # Generate improvements
    print("3. IMPROVEMENT PLAN")
    print("-" * 70)
    improvements = analyzer.generate_improvement_plan(metrics)
    if improvements:
        for i, improvement in enumerate(improvements, 1):
            print(f"{i}. {improvement}")
    else:
        print("✓ All metrics above threshold - optimal grip achieved!")
    print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Current fitness: {metrics.overall_fitness:.2%}")
    print(f"Target fitness:  80%")
    print(f"Convergence gap: {max(0, 0.80 - metrics.overall_fitness):.2%}")
    print()
    
    if metrics.overall_fitness >= 0.80:
        print("✓ OPTIMAL GRIP ACHIEVED - Meta-recursive convergence complete!")
    else:
        print(f"△ {len(improvements)} improvements needed for optimal grip")
    print()


if __name__ == "__main__":
    main()
