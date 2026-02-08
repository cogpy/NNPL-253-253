#!/usr/bin/env python3
"""
Pattern Data Loader - Load all 253 APL patterns from markdown files

This module provides utilities to load pattern data from markdown files
and prepare it for neural network training.
"""

import os
import re
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict


@dataclass
class PatternData:
    """Data structure for a single pattern."""
    id: int
    name: str
    problem: str
    solution: str
    confidence: int  # 0=uncertain, 1=progress, 2=invariant
    category: str  # towns, buildings, construction
    sequence_id: Optional[int] = None
    preceding: List[int] = None
    following: List[int] = None
    
    def __post_init__(self):
        if self.preceding is None:
            self.preceding = []
        if self.following is None:
            self.following = []


class PatternLoader:
    """Load and parse APL pattern data from markdown files."""
    
    def __init__(self, markdown_dir: str = "markdown/apl", sequences_file: str = "pattern_sequences.json"):
        self.markdown_dir = markdown_dir
        self.sequences_file = sequences_file
        self.patterns: Dict[int, PatternData] = {}
        self.sequences: List[Dict] = []
        
    def load_all(self) -> Dict[int, PatternData]:
        """Load all 253 patterns from markdown files."""
        self._load_sequences()
        
        for pattern_id in range(1, 254):
            try:
                pattern = self._load_pattern(pattern_id)
                self.patterns[pattern_id] = pattern
            except Exception as e:
                print(f"Warning: Failed to load pattern {pattern_id}: {e}")
                
        # Add relationship information from sequences
        self._build_relationships()
        
        return self.patterns
    
    def _load_sequences(self):
        """Load sequence information."""
        if os.path.exists(self.sequences_file):
            with open(self.sequences_file, 'r') as f:
                data = json.load(f)
                self.sequences = data.get('sequences', [])
    
    def _load_pattern(self, pattern_id: int) -> PatternData:
        """Load a single pattern from markdown file."""
        filename = os.path.join(self.markdown_dir, f"apl{pattern_id:03d}.md")
        
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Pattern file not found: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract pattern name (from first heading or title)
        name_match = re.search(r'^#\s+(\d+)\.\s+(.+?)$', content, re.MULTILINE)
        if name_match:
            name = name_match.group(2).strip()
        else:
            name = f"Pattern {pattern_id}"
        
        # Extract problem (usually in a section or paragraph)
        problem = self._extract_section(content, ['problem', 'context', '## Problem'])
        if not problem:
            # Fallback: get first substantial paragraph
            paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 50]
            problem = paragraphs[0] if paragraphs else ""
        
        # Extract solution
        solution = self._extract_section(content, ['solution', 'therefore', '## Solution', '## Therefore'])
        if not solution:
            # Fallback: get second substantial paragraph
            paragraphs = [p.strip() for p in content.split('\n\n') if len(p.strip()) > 50]
            solution = paragraphs[1] if len(paragraphs) > 1 else paragraphs[0] if paragraphs else ""
        
        # Determine confidence from asterisks
        confidence = self._extract_confidence(content, name)
        
        # Determine category based on pattern number
        if pattern_id <= 94:
            category = "towns"
        elif pattern_id <= 204:
            category = "buildings"
        else:
            category = "construction"
        
        # Find sequence
        sequence_id = self._find_sequence(pattern_id)
        
        return PatternData(
            id=pattern_id,
            name=name,
            problem=problem[:500],  # Limit length
            solution=solution[:500],  # Limit length
            confidence=confidence,
            category=category,
            sequence_id=sequence_id,
            preceding=[],
            following=[]
        )
    
    def _extract_section(self, content: str, markers: List[str]) -> str:
        """Extract a section of text based on markers."""
        content_lower = content.lower()
        
        for marker in markers:
            marker_lower = marker.lower()
            
            # Try to find section heading
            pattern = rf'#{1,3}\s*{re.escape(marker_lower)}.*?\n\n(.*?)(?:\n#{1,3}\s|\Z)'
            match = re.search(pattern, content_lower, re.DOTALL | re.IGNORECASE)
            if match:
                start = match.start(1)
                # Find the actual text (not lowercased) at this position
                actual_text = content[start:start+2000]
                # Get first paragraph
                paragraphs = [p.strip() for p in actual_text.split('\n\n') if p.strip()]
                if paragraphs:
                    return paragraphs[0]
            
            # Try to find inline marker
            idx = content_lower.find(marker_lower)
            if idx >= 0:
                # Get text after marker
                remaining = content[idx + len(marker):]
                # Skip to next paragraph
                match = re.search(r'\n\n(.+?)(?:\n\n|\Z)', remaining, re.DOTALL)
                if match:
                    return match.group(1).strip()
        
        return ""
    
    def _extract_confidence(self, content: str, name: str) -> int:
        """
        Extract confidence level from pattern name or content.
        0 = no asterisks (tentative)
        1 = one asterisk (probable) 
        2 = two asterisks (invariant)
        """
        # Count asterisks in name
        asterisks = name.count('*')
        return min(asterisks, 2)
    
    def _find_sequence(self, pattern_id: int) -> Optional[int]:
        """Find which sequence this pattern belongs to."""
        for seq in self.sequences:
            if pattern_id in seq.get('patterns', []):
                return seq.get('id')
        return None
    
    def _build_relationships(self):
        """Build preceding/following relationships from sequences."""
        # Group patterns by sequence
        seq_patterns: Dict[int, List[int]] = {}
        for seq in self.sequences:
            seq_id = seq.get('id')
            patterns = seq.get('patterns', [])
            if seq_id and patterns:
                seq_patterns[seq_id] = patterns
        
        # Build relationships within each sequence
        for seq_id, patterns in seq_patterns.items():
            for i, pattern_id in enumerate(patterns):
                if pattern_id in self.patterns:
                    # Add preceding patterns
                    if i > 0:
                        prev_id = patterns[i - 1]
                        if prev_id not in self.patterns[pattern_id].preceding:
                            self.patterns[pattern_id].preceding.append(prev_id)
                    
                    # Add following patterns
                    if i < len(patterns) - 1:
                        next_id = patterns[i + 1]
                        if next_id not in self.patterns[pattern_id].following:
                            self.patterns[pattern_id].following.append(next_id)
    
    def get_patterns_by_sequence(self, sequence_id: int) -> List[PatternData]:
        """Get all patterns in a specific sequence."""
        return [p for p in self.patterns.values() if p.sequence_id == sequence_id]
    
    def get_patterns_by_category(self, category: str) -> List[PatternData]:
        """Get all patterns in a category."""
        return [p for p in self.patterns.values() if p.category == category]
    
    def export_to_json(self, filename: str):
        """Export all patterns to JSON file."""
        data = {
            'meta': {
                'total_patterns': len(self.patterns),
                'source': 'APL markdown files'
            },
            'patterns': {
                pid: asdict(pattern)
                for pid, pattern in self.patterns.items()
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Exported {len(self.patterns)} patterns to {filename}")


def main():
    """Demo: Load all patterns and show statistics."""
    print("=" * 70)
    print("PATTERN LOADER DEMO")
    print("=" * 70)
    
    loader = PatternLoader()
    patterns = loader.load_all()
    
    print(f"\n✓ Loaded {len(patterns)} patterns")
    
    # Statistics by category
    by_category = {}
    for pattern in patterns.values():
        cat = pattern.category
        by_category[cat] = by_category.get(cat, 0) + 1
    
    print("\n=== Patterns by Category ===")
    for cat, count in sorted(by_category.items()):
        print(f"  {cat:15s}: {count:3d} patterns")
    
    # Statistics by confidence
    by_confidence = {}
    for pattern in patterns.values():
        conf = pattern.confidence
        by_confidence[conf] = by_confidence.get(conf, 0) + 1
    
    print("\n=== Patterns by Confidence ===")
    conf_names = {0: "Tentative", 1: "Probable", 2: "Invariant"}
    for conf, count in sorted(by_confidence.items()):
        print(f"  {conf_names.get(conf, 'Unknown'):15s}: {count:3d} patterns")
    
    # Show sample patterns
    print("\n=== Sample Patterns ===")
    for pid in [1, 50, 100, 150, 200, 253]:
        if pid in patterns:
            p = patterns[pid]
            print(f"\nPattern {p.id}: {p.name}")
            print(f"  Category: {p.category}")
            print(f"  Confidence: {p.confidence}")
            print(f"  Sequence: {p.sequence_id}")
            print(f"  Problem: {p.problem[:80]}...")
            print(f"  Solution: {p.solution[:80]}...")
            print(f"  Preceding: {p.preceding}")
            print(f"  Following: {p.following}")
    
    # Export to JSON
    print("\n=== Exporting to JSON ===")
    loader.export_to_json('implementations/all_patterns_data.json')
    
    print("\n✓ Demo complete!")


if __name__ == '__main__':
    main()
