#!/usr/bin/env python3
"""
Analyze repository structure through the lens of Pattern Language
to identify opportunities for pattern application.
"""

import json
import os
from pathlib import Path
from collections import defaultdict

def load_patterns():
    """Load pattern sequences and metadata"""
    with open('pattern_sequences.json') as f:
        seq_data = json.load(f)
    with open('pattern_language_generated.json') as f:
        pattern_data = json.load(f)
    return seq_data, pattern_data

def analyze_repo_structure():
    """Analyze current repository structure"""
    structure = {
        'root_files': [],
        'directories': defaultdict(list),
        'documentation': [],
        'code_files': [],
        'data_files': []
    }
    
    root_path = Path('.')
    
    # Analyze root level
    for item in root_path.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            structure['root_files'].append(item.name)
            if item.suffix == '.md':
                structure['documentation'].append(item.name)
            elif item.suffix == '.py':
                structure['code_files'].append(item.name)
            elif item.suffix == '.json':
                structure['data_files'].append(item.name)
    
    # Analyze directories
    for item in root_path.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            dir_contents = list(item.iterdir())
            structure['directories'][item.name] = [
                f.name for f in dir_contents if not f.name.startswith('.')
            ]
    
    return structure

def map_patterns_to_repo(structure, seq_data):
    """Map APL patterns to repository elements"""
    mappings = []
    
    sequences = seq_data['sequences']
    
    # Pattern 1: INDEPENDENT REGIONS -> Top-level domains
    mappings.append({
        'pattern_id': 1,
        'pattern_name': 'INDEPENDENT REGIONS',
        'application': 'Repository autonomous domains',
        'current_state': list(structure['directories'].keys()),
        'recommendation': 'Ensure each domain (apl, uia, markdown, opencog_atomese, npu253, docs) is self-contained'
    })
    
    # Pattern 8: MOSAIC OF SUBCULTURES -> Pattern collections
    mappings.append({
        'pattern_id': 8,
        'pattern_name': 'MOSAIC OF SUBCULTURES',
        'application': 'Diverse pattern collections',
        'current_state': 'APL, UIA, Archetypal, OpenCog representations',
        'recommendation': 'Maintain diversity while ensuring coherence through cross-references'
    })
    
    # Pattern 28: ECCENTRIC NUCLEUS -> Main entry points
    mappings.append({
        'pattern_id': 28,
        'pattern_name': 'ECCENTRIC NUCLEUS',
        'application': 'Repository navigation centers',
        'current_state': ['README.md', 'QUICK_REFERENCE.md'],
        'recommendation': 'Create pattern-based index system with multiple entry points'
    })
    
    # Pattern 52: NETWORK OF PATHS -> Navigation structure
    mappings.append({
        'pattern_id': 52,
        'pattern_name': 'NETWORK OF PATHS AND CARS',
        'application': 'Documentation navigation',
        'current_state': 'Multiple README files, documentation',
        'recommendation': 'Create clear navigation paths through sequences'
    })
    
    # Pattern 95: BUILDING COMPLEX -> Code organization
    mappings.append({
        'pattern_id': 95,
        'pattern_name': 'BUILDING COMPLEX',
        'application': 'Module organization',
        'current_state': 'Python scripts, JSON data, documentation separate',
        'recommendation': 'Group related functionality into cohesive modules'
    })
    
    return mappings

def generate_pattern_application_plan():
    """Generate concrete plan for applying patterns"""
    seq_data, pattern_data = load_patterns()
    structure = analyze_repo_structure()
    mappings = map_patterns_to_repo(structure, seq_data)
    
    print("=" * 70)
    print("PATTERN LANGUAGE APPLICATION ANALYSIS")
    print("=" * 70)
    print()
    
    print("CURRENT REPOSITORY STRUCTURE:")
    print(f"  Root files: {len(structure['root_files'])}")
    print(f"  Directories: {len(structure['directories'])}")
    print(f"  Documentation files: {len(structure['documentation'])}")
    print(f"  Python files: {len(structure['code_files'])}")
    print(f"  JSON data files: {len(structure['data_files'])}")
    print()
    
    print("KEY DIRECTORIES:")
    for dirname in sorted(structure['directories'].keys()):
        file_count = len(structure['directories'][dirname])
        print(f"  {dirname}/: {file_count} files")
    print()
    
    print("PATTERN APPLICATIONS:")
    print()
    for mapping in mappings:
        print(f"Pattern {mapping['pattern_id']}: {mapping['pattern_name']}")
        print(f"  Application: {mapping['application']}")
        print(f"  Current: {mapping['current_state']}")
        print(f"  Recommendation: {mapping['recommendation']}")
        print()
    
    # Generate specific action items
    print("=" * 70)
    print("CONCRETE ACTION ITEMS")
    print("=" * 70)
    print()
    
    actions = [
        {
            'sequence': 1,
            'pattern': 1,
            'action': 'Create PATTERN_MAP.md documenting repository regions',
            'rationale': 'Establishes autonomous domains with clear boundaries'
        },
        {
            'sequence': 3,
            'pattern': 8,
            'action': 'Create cross-reference index linking APL, UIA, Archetypal patterns',
            'rationale': 'Supports mosaic of diverse pattern representations'
        },
        {
            'sequence': 7,
            'pattern': 28,
            'action': 'Create NAVIGATION_HUB.md with multiple entry points',
            'rationale': 'Provides eccentric nucleus for exploration'
        },
        {
            'sequence': 10,
            'pattern': 52,
            'action': 'Implement sequence-based navigation files',
            'rationale': 'Creates network of paths through pattern space'
        },
        {
            'sequence': 16,
            'pattern': 95,
            'action': 'Group related scripts into modules/',
            'rationale': 'Forms coherent building complexes'
        },
        {
            'sequence': 20,
            'pattern': 132,
            'action': 'Create hierarchical directory structure with clear gradients',
            'rationale': 'Establishes privacy gradient from general to specific'
        }
    ]
    
    for i, action in enumerate(actions, 1):
        print(f"{i}. Sequence {action['sequence']}, Pattern {action['pattern']}")
        print(f"   ACTION: {action['action']}")
        print(f"   RATIONALE: {action['rationale']}")
        print()
    
    return mappings, actions

if __name__ == '__main__':
    mappings, actions = generate_pattern_application_plan()
    
    # Save results
    with open('pattern_application_analysis.json', 'w') as f:
        json.dump({
            'mappings': mappings,
            'actions': actions
        }, f, indent=2)
    
    print("Analysis saved to pattern_application_analysis.json")
