#!/usr/bin/env python3
"""
Pattern Salience Engine - ML-based Pattern Relevance Scoring

Implements cognitive "optimal grip" through:
- Context-aware salience scoring
- Gestalt pattern detection
- Emergence tracking
- Multi-scale perception

This provides the cognitive enhancement layer described in OPTIMAL_GRIP_ANALYSIS.md Phase 4.
"""

import json
import numpy as np
from typing import List, Dict, Set, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict
import re


@dataclass
class PatternContext:
    """Context for salience computation"""
    focus_patterns: Set[str] = field(default_factory=set)
    current_category: Optional[str] = None
    current_sequence: Optional[str] = None
    keywords: Set[str] = field(default_factory=set)
    domain: Optional[str] = None  # physical, social, conceptual, individual
    scale: Optional[str] = None  # town, building, construction


@dataclass
class SalienceScore:
    """Salience score for a pattern"""
    pattern_id: str
    score: float
    reasons: List[str] = field(default_factory=list)
    
    def __lt__(self, other):
        return self.score < other.score


class PatternSalienceEngine:
    """
    Cognitive salience engine for pattern language
    
    Computes context-aware relevance scores to achieve "optimal grip" on
    the gestalt salience landscape.
    """
    
    def __init__(self, pattern_json_path: str):
        """Initialize salience engine"""
        self.load_patterns(pattern_json_path)
        self.load_categories()
        self._compute_pattern_features()
    
    def load_patterns(self, json_path: str):
        """Load pattern data"""
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        self.patterns = {}
        if 'patterns' in data:
            for pattern in data['patterns']:
                self.patterns[pattern['id']] = pattern
        
        print(f"Loaded {len(self.patterns)} patterns")
    
    def load_categories(self):
        """Load category information"""
        self.category_map = {}
        
        category_files = [
            ('category_towns.json', 'Towns'),
            ('category_buildings.json', 'Buildings'),
            ('category_construction.json', 'Construction')
        ]
        
        for file, cat_name in category_files:
            try:
                with open(file, 'r') as f:
                    cat_data = json.load(f)
                    for pattern in cat_data.get('patterns', []):
                        pattern_id = pattern.get('id', '')
                        if pattern_id:
                            self.category_map[pattern_id] = cat_name
            except FileNotFoundError:
                pass
    
    def _compute_pattern_features(self):
        """Pre-compute pattern features for salience scoring"""
        self.pattern_features = {}
        
        for pattern_id, pattern in self.patterns.items():
            features = {
                'id': pattern_id,
                'number': pattern.get('number', 0),
                'name': pattern.get('name', ''),
                'asterisks': pattern.get('asterisks', 0),  # Importance indicator
                'category': self.category_map.get(pattern_id, 'Unknown'),
                'problem_length': len(pattern.get('problem', '')),
                'solution_length': len(pattern.get('solution', '')),
                'num_preceding': len(pattern.get('preceding_patterns', [])),
                'num_following': len(pattern.get('following_patterns', [])),
                'context_length': len(pattern.get('context', '')),
            }
            
            # Extract keywords from problem and solution
            text = (pattern.get('problem', '') + ' ' + 
                   pattern.get('solution', '') + ' ' +
                   pattern.get('name', '')).lower()
            keywords = set(re.findall(r'\b\w{4,}\b', text))  # Words 4+ chars
            features['keywords'] = keywords
            
            self.pattern_features[pattern_id] = features
        
        # Compute centrality scores
        self._compute_centrality()
    
    def _compute_centrality(self):
        """Compute pattern centrality in the network"""
        # Simple centrality based on connections
        for pattern_id, features in self.pattern_features.items():
            # Patterns with more connections are more central
            centrality = (features['num_preceding'] + features['num_following']) / 10.0
            # Patterns with more asterisks are more important
            centrality += features['asterisks'] * 0.5
            # Earlier patterns tend to be more fundamental
            centrality += (253 - features['number']) / 253.0
            
            features['centrality'] = min(centrality, 5.0)  # Cap at 5.0
    
    def compute_salience(
        self,
        pattern_id: str,
        context: PatternContext
    ) -> SalienceScore:
        """
        Compute salience score for a pattern given context
        
        Higher scores indicate higher relevance in the current context.
        """
        if pattern_id not in self.pattern_features:
            return SalienceScore(pattern_id, 0.0, ["Pattern not found"])
        
        features = self.pattern_features[pattern_id]
        score = 0.0
        reasons = []
        
        # 1. Focus proximity: Is this pattern directly in focus?
        if pattern_id in context.focus_patterns:
            score += 10.0
            reasons.append("In focus set")
        
        # 2. Category match
        if context.current_category and features['category'] == context.current_category:
            score += 5.0
            reasons.append(f"Matches category: {context.current_category}")
        
        # 3. Keyword overlap
        if context.keywords:
            overlap = features['keywords'].intersection(context.keywords)
            keyword_score = len(overlap) * 2.0
            if keyword_score > 0:
                score += keyword_score
                reasons.append(f"Keyword overlap: {len(overlap)} matches")
        
        # 4. Network proximity: Connected to focus patterns?
        pattern = self.patterns[pattern_id]
        for focus_id in context.focus_patterns:
            if focus_id in self.patterns:
                focus_pattern = self.patterns[focus_id]
                # Check if connected
                if pattern['number'] in focus_pattern.get('following_patterns', []):
                    score += 3.0
                    reasons.append(f"Follows focus pattern {focus_id}")
                if pattern['number'] in focus_pattern.get('preceding_patterns', []):
                    score += 2.0
                    reasons.append(f"Precedes focus pattern {focus_id}")
        
        # 5. Centrality: More central patterns get slight boost
        centrality_boost = features['centrality'] * 0.5
        score += centrality_boost
        if centrality_boost > 1.0:
            reasons.append(f"High centrality: {features['centrality']:.2f}")
        
        # 6. Importance (asterisks)
        importance_boost = features['asterisks'] * 1.5
        score += importance_boost
        if importance_boost > 0:
            reasons.append(f"Importance: {features['asterisks']} asterisks")
        
        return SalienceScore(pattern_id, score, reasons)
    
    def rank_patterns_by_salience(
        self,
        context: PatternContext,
        limit: int = 20
    ) -> List[SalienceScore]:
        """
        Rank all patterns by salience in given context
        
        Returns top N patterns most relevant to context.
        """
        scores = []
        for pattern_id in self.patterns.keys():
            salience = self.compute_salience(pattern_id, context)
            if salience.score > 0:
                scores.append(salience)
        
        # Sort by score descending
        scores.sort(reverse=True)
        return scores[:limit]
    
    def detect_gestalt_patterns(
        self,
        pattern_ids: List[str],
        threshold: float = 0.6
    ) -> List[Dict[str, any]]:
        """
        Detect gestalt (emergent) groupings in a set of patterns
        
        Identifies clusters of patterns that form coherent wholes.
        """
        if len(pattern_ids) < 2:
            return []
        
        # Compute similarity matrix
        n = len(pattern_ids)
        similarity = np.zeros((n, n))
        
        for i, pid1 in enumerate(pattern_ids):
            for j, pid2 in enumerate(pattern_ids):
                if i == j:
                    similarity[i, j] = 1.0
                else:
                    similarity[i, j] = self._compute_pattern_similarity(pid1, pid2)
        
        # Find clusters using simple threshold-based grouping
        clusters = []
        visited = set()
        
        for i, pattern_id in enumerate(pattern_ids):
            if pattern_id in visited:
                continue
            
            # Start new cluster
            cluster = [pattern_id]
            visited.add(pattern_id)
            
            # Find similar patterns
            for j, other_id in enumerate(pattern_ids):
                if other_id not in visited and similarity[i, j] >= threshold:
                    cluster.append(other_id)
                    visited.add(other_id)
            
            if len(cluster) > 1:
                clusters.append({
                    'patterns': cluster,
                    'size': len(cluster),
                    'coherence': float(np.mean([similarity[pattern_ids.index(p1), pattern_ids.index(p2)]
                                               for p1 in cluster for p2 in cluster if p1 != p2]))
                })
        
        return sorted(clusters, key=lambda c: c['size'], reverse=True)
    
    def _compute_pattern_similarity(self, pid1: str, pid2: str) -> float:
        """Compute similarity between two patterns"""
        if pid1 not in self.pattern_features or pid2 not in self.pattern_features:
            return 0.0
        
        f1 = self.pattern_features[pid1]
        f2 = self.pattern_features[pid2]
        
        similarity = 0.0
        
        # Same category
        if f1['category'] == f2['category']:
            similarity += 0.3
        
        # Keyword overlap
        common_keywords = f1['keywords'].intersection(f2['keywords'])
        if common_keywords:
            similarity += min(len(common_keywords) / 10.0, 0.4)
        
        # Connected in pattern network
        p1 = self.patterns[pid1]
        p2 = self.patterns[pid2]
        if p2['number'] in p1.get('following_patterns', []) or \
           p2['number'] in p1.get('preceding_patterns', []):
            similarity += 0.3
        
        return min(similarity, 1.0)
    
    def track_emergence(
        self,
        pattern_sequence: List[str]
    ) -> Dict[str, any]:
        """
        Track emergence of higher-level patterns from sequence
        
        Detects when patterns combine to create emergent properties.
        """
        if len(pattern_sequence) < 2:
            return {'emergence_detected': False}
        
        # Analyze sequence properties
        categories = [self.category_map.get(pid, 'Unknown') for pid in pattern_sequence]
        unique_categories = set(categories)
        
        # Compute sequence coherence
        coherences = []
        for i in range(len(pattern_sequence) - 1):
            coherence = self._compute_pattern_similarity(
                pattern_sequence[i],
                pattern_sequence[i + 1]
            )
            coherences.append(coherence)
        
        avg_coherence = np.mean(coherences) if coherences else 0.0
        
        # Detect emergence: high coherence + diverse categories suggests emergence
        emergence_score = avg_coherence
        if len(unique_categories) > 1:
            emergence_score *= 1.5  # Boost for cross-category integration
        
        emergence_detected = emergence_score > 0.5
        
        return {
            'emergence_detected': emergence_detected,
            'emergence_score': float(emergence_score),
            'sequence_coherence': float(avg_coherence),
            'categories_involved': list(unique_categories),
            'sequence_length': len(pattern_sequence),
            'interpretation': self._interpret_emergence(emergence_score, unique_categories)
        }
    
    def _interpret_emergence(self, score: float, categories: Set[str]) -> str:
        """Interpret emergence score"""
        if score < 0.3:
            return "Low emergence: Patterns weakly related"
        elif score < 0.5:
            return "Moderate emergence: Patterns forming loose connections"
        elif score < 0.7:
            return "High emergence: Patterns forming coherent gestalt"
        else:
            cross_cat = " across multiple scales" if len(categories) > 1 else ""
            return f"Very high emergence: Strong synergistic gestalt{cross_cat}"


def demo_salience_engine():
    """Demonstrate salience engine capabilities"""
    print("="*70)
    print("Pattern Salience Engine - Cognitive Enhancement Demo")
    print("="*70)
    print()
    
    # Initialize engine
    print("1. Initializing salience engine...")
    engine = PatternSalienceEngine('pattern_language_generated.json')
    print()
    
    # Demo 1: Context-aware salience
    print("2. Demo: Context-aware salience scoring")
    context = PatternContext(
        focus_patterns={'apl1', 'apl2'},
        current_category='Towns',
        keywords={'region', 'city', 'urban', 'distribution'}
    )
    
    top_patterns = engine.rank_patterns_by_salience(context, limit=10)
    print(f"   Top 10 patterns for context (focus on apl1, apl2):")
    for i, salience in enumerate(top_patterns[:10], 1):
        pattern = engine.patterns[salience.pattern_id]
        print(f"   {i}. {salience.pattern_id}: {pattern['name']}")
        print(f"      Score: {salience.score:.2f}")
        print(f"      Reasons: {', '.join(salience.reasons[:2])}")
    print()
    
    # Demo 2: Gestalt detection
    print("3. Demo: Gestalt pattern detection")
    pattern_set = ['apl1', 'apl2', 'apl3', 'apl4', 'apl5', 'apl8', 'apl51', 'apl52']
    gestalts = engine.detect_gestalt_patterns(pattern_set, threshold=0.5)
    
    print(f"   Found {len(gestalts)} gestalt clusters:")
    for i, gestalt in enumerate(gestalts, 1):
        print(f"   Cluster {i}: {len(gestalt['patterns'])} patterns")
        print(f"      Patterns: {', '.join(gestalt['patterns'][:5])}")
        print(f"      Coherence: {gestalt['coherence']:.2f}")
    print()
    
    # Demo 3: Emergence tracking
    print("4. Demo: Emergence tracking")
    sequence = ['apl1', 'apl2', 'apl3', 'apl12', 'apl51', 'apl95', 'apl106']
    emergence = engine.track_emergence(sequence)
    
    print(f"   Analyzing sequence: {' → '.join(sequence)}")
    print(f"   Emergence detected: {emergence['emergence_detected']}")
    print(f"   Emergence score: {emergence['emergence_score']:.2f}")
    print(f"   Sequence coherence: {emergence['sequence_coherence']:.2f}")
    print(f"   Categories: {', '.join(emergence['categories_involved'])}")
    print(f"   Interpretation: {emergence['interpretation']}")
    print()
    
    print("="*70)
    print("Demo complete!")
    print("="*70)


if __name__ == '__main__':
    demo_salience_engine()
