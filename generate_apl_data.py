#!/usr/bin/env python3
"""
Generate APL data initialization from JSON pattern files.
This script reads the pattern JSON files and generates APL code to load the data.
"""

import json
from pathlib import Path
from typing import Dict, List, Any


def escape_apl_string(text: str) -> str:
    """Escape a string for APL."""
    if not text:
        return "''"
    # Replace single quotes with doubled quotes for APL
    text = text.replace("'", "''")
    return f"'{text}'"


def generate_pattern_data_apl() -> str:
    """Generate APL code to initialize pattern data."""
    
    # Load pattern language
    with open('pattern_language_generated.json', 'r', encoding='utf-8') as f:
        pattern_data = json.load(f)
    
    # Load archetypal patterns
    with open('archetypal_patterns.json', 'r', encoding='utf-8') as f:
        archetypal_data = json.load(f)
    
    # Load sequences
    with open('pattern_sequences.json', 'r', encoding='utf-8') as f:
        sequence_data = json.load(f)
    
    apl_code = []
    
    apl_code.append("⍝ data_loader.apl - Pattern Data Initialization")
    apl_code.append("⍝ Generated from JSON pattern files")
    apl_code.append("⍝ Author: APL-253 Project")
    apl_code.append("⍝ License: MIT")
    apl_code.append("")
    apl_code.append("⍝ ============================================================================")
    apl_code.append("⍝ LOAD PATTERN DATA")
    apl_code.append("⍝ ============================================================================")
    apl_code.append("")
    apl_code.append("∇ LoadAllPatternData")
    apl_code.append("  ⍝ Load all pattern data from generated code")
    apl_code.append("  ")
    apl_code.append("  ⍞ ← 'Loading pattern data...',⎕UCS 10")
    apl_code.append("  ")
    apl_code.append("  ⍝ Load main patterns")
    apl_code.append("  LoadMainPatterns")
    apl_code.append("  ")
    apl_code.append("  ⍝ Load sequences")
    apl_code.append("  LoadSequences")
    apl_code.append("  ")
    apl_code.append("  ⍝ Load archetypal patterns")
    apl_code.append("  LoadArchetypalPatterns")
    apl_code.append("  ")
    apl_code.append("  ⍝ Load relationships")
    apl_code.append("  LoadRelationships")
    apl_code.append("  ")
    apl_code.append("  ⍞ ← 'Pattern data loaded successfully!',⎕UCS 10")
    apl_code.append("∇")
    apl_code.append("")
    
    # Generate function to load sample patterns (first 10 for demo)
    apl_code.append("∇ LoadMainPatterns")
    apl_code.append("  ⍝ Load main pattern data")
    apl_code.append("  ⍝ Note: This loads a subset of patterns for demonstration")
    apl_code.append("  ")
    apl_code.append("  ⍞ ← '  Loading main patterns...',⎕UCS 10")
    apl_code.append("  ")
    
    # Load sample patterns (first 10)
    categories = pattern_data.get('categories', [])
    all_patterns = []
    
    # Gather patterns from categories
    if isinstance(categories, list):
        for cat_data in categories:
            if isinstance(cat_data, dict) and 'patterns' in cat_data:
                all_patterns.extend(cat_data['patterns'])
    
    # Also check patterns array directly
    if 'patterns' in pattern_data:
        patterns_list = pattern_data['patterns']
        if isinstance(patterns_list, list):
            all_patterns.extend(patterns_list)
    
    # Load first 10 patterns as examples
    for i, pattern in enumerate(all_patterns[:10], 1):
        if not isinstance(pattern, dict):
            continue
            
        pid = pattern.get('number', i)
        name = pattern.get('name', '')
        category = pattern.get('category', 'Towns')
        asterisks = pattern.get('asterisks', 1)
        context = pattern.get('context', '')[:100]  # Limit length
        problem = pattern.get('problem_summary', '')[:100]
        solution = pattern.get('solution', '')[:100]
        diagram = pattern.get('diagram', '')[:50]
        
        # Get connections
        preceding = pattern.get('preceding_patterns', [])
        following = pattern.get('following_patterns', [])
        connections = preceding + following
        
        # Format as APL vector
        apl_code.append(f"  ⍝ Pattern {pid}: {name}")
        
        # Create pattern data vector
        apl_code.append(f"  pattern ← {pid} {escape_apl_string(name)} {escape_apl_string(category)} {asterisks}")
        apl_code.append(f"  pattern ,← ⊂{escape_apl_string(context)}")
        apl_code.append(f"  pattern ,← ⊂{escape_apl_string(problem)}")
        apl_code.append(f"  pattern ,← ⊂{escape_apl_string(solution)}")
        apl_code.append(f"  pattern ,← ⊂{escape_apl_string(diagram)}")
        
        # Add connections as vector
        if connections:
            conn_str = ' '.join(str(c) for c in connections[:5])  # First 5
            apl_code.append(f"  pattern ,← ⊂({conn_str})")
        else:
            apl_code.append(f"  pattern ,← ⊂⍬")
        
        apl_code.append(f"  dummy ← StorePattern pattern")
        apl_code.append("  ")
    
    apl_code.append("  ⍞ ← '    Loaded sample patterns',⎕UCS 10")
    apl_code.append("∇")
    apl_code.append("")
    
    # Generate function to load sequences
    apl_code.append("∇ LoadSequences")
    apl_code.append("  ⍝ Load pattern sequences")
    apl_code.append("  ")
    apl_code.append("  ⍞ ← '  Loading sequences...',⎕UCS 10")
    apl_code.append("  ")
    
    sequences = sequence_data.get('sequences', [])
    for i, seq in enumerate(sequences[:10], 1):  # First 10 sequences
        seq_id = seq.get('id', i)
        patterns = seq.get('patterns', [])
        
        if patterns:
            pattern_str = ' '.join(str(p) for p in patterns)
            apl_code.append(f"  ⍝ Sequence {seq_id}")
            apl_code.append(f"  dummy ← StoreSequence {seq_id} ({pattern_str})")
    
    apl_code.append("  ")
    apl_code.append("  ⍞ ← '    Loaded sequences',⎕UCS 10")
    apl_code.append("∇")
    apl_code.append("")
    
    # Generate function to load archetypal patterns
    apl_code.append("∇ LoadArchetypalPatterns")
    apl_code.append("  ⍝ Load archetypal patterns")
    apl_code.append("  ")
    apl_code.append("  ⍞ ← '  Loading archetypal patterns...',⎕UCS 10")
    apl_code.append("  ")
    
    arch_patterns = archetypal_data.get('patterns', [])
    for pattern in arch_patterns[:5]:  # First 5 archetypal patterns
        pattern_id = pattern.get('pattern_id', '')
        archetypal = pattern.get('archetypal_pattern', '')
        placeholders = pattern.get('placeholders', [])
        
        if archetypal and pattern_id:
            apl_code.append(f"  ⍝ Archetypal pattern {pattern_id}")
            apl_code.append(f"  archetypal ← {escape_apl_string(archetypal[:150])}")
            
            if placeholders:
                ph_str = ' '.join(escape_apl_string(ph) for ph in placeholders[:3])
                apl_code.append(f"  placeholders ← {ph_str}")
            else:
                apl_code.append(f"  placeholders ← ⍬")
            
            apl_code.append(f"  dummy ← StoreArchetypalPattern {escape_apl_string(pattern_id)} archetypal placeholders")
            apl_code.append("  ")
    
    apl_code.append("  ⍞ ← '    Loaded archetypal patterns',⎕UCS 10")
    apl_code.append("∇")
    apl_code.append("")
    
    # Generate function to load relationships
    apl_code.append("∇ LoadRelationships")
    apl_code.append("  ⍝ Load pattern relationships")
    apl_code.append("  ")
    apl_code.append("  ⍞ ← '  Loading relationships...',⎕UCS 10")
    apl_code.append("  ")
    
    # Sample relationships from first patterns
    for i, pattern in enumerate(all_patterns[:10], 1):
        if not isinstance(pattern, dict):
            continue
            
        pid = pattern.get('number', i)
        following = pattern.get('following_patterns', [])
        
        if following:
            for fid in following[:3]:  # First 3 following patterns
                apl_code.append(f"  dummy ← AddFollowingPattern {pid} {fid}")
    
    apl_code.append("  ")
    apl_code.append("  ⍞ ← '    Loaded relationships',⎕UCS 10")
    apl_code.append("∇")
    apl_code.append("")
    
    apl_code.append("⍞ ← 'Data Loader Module Loaded',⎕UCS 10")
    
    return '\n'.join(apl_code)


def main():
    """Main function."""
    print("Generating APL data initialization code...")
    
    apl_code = generate_pattern_data_apl()
    
    output_path = Path('apl_language/data_loader.apl')
    output_path.write_text(apl_code, encoding='utf-8')
    
    print(f"Generated {output_path}")
    print(f"  Lines: {len(apl_code.splitlines())}")
    print("Done!")


if __name__ == '__main__':
    main()
