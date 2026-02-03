#!/usr/bin/env python3
"""
Validate that all APL patterns have the required structure:
1. Title: # Pattern: [number] - [NAME]
2. ## Narrower: Introductory paragraph
3. ## Problem: Bold summary + details
4. ## Solution: Bold solution statement
5. ## Broader: Concluding paragraph
"""

import re
from pathlib import Path
from typing import List, Dict

def validate_pattern_structure(filepath: Path) -> Dict[str, bool]:
    """Validate that a pattern file has all required sections."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        'file': filepath.name,
        'has_pattern_title': False,
        'has_narrower_header': False,
        'has_problem_header': False,
        'has_problem_bold': False,
        'has_solution_header': False,
        'has_solution_bold': False,
        'has_broader_header': False,
        'all_valid': False
    }
    
    # Check title format: # Pattern: [number] - [NAME]
    if re.search(r'^#\s+Pattern:\s+\d+\s+-\s+.+$', content, re.MULTILINE):
        results['has_pattern_title'] = True
    
    # Check for required headers
    if re.search(r'^##\s+Narrower:', content, re.MULTILINE):
        results['has_narrower_header'] = True
    
    if re.search(r'^##\s+Problem:', content, re.MULTILINE):
        results['has_problem_header'] = True
    
    if re.search(r'^##\s+Solution:', content, re.MULTILINE):
        results['has_solution_header'] = True
    
    if re.search(r'^##\s+Broader:', content, re.MULTILINE):
        results['has_broader_header'] = True
    
    # Check for bold problem summary after ## Problem:
    problem_section = re.search(r'##\s+Problem:\s*\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    if problem_section:
        # Check if first non-empty line is bold (starts with **)
        first_lines = problem_section.group(1).strip().split('\n', 2)
        if first_lines and first_lines[0].strip().startswith('**'):
            results['has_problem_bold'] = True
    
    # Check for bold solution statement after ## Solution:
    solution_section = re.search(r'##\s+Solution:\s*\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    if solution_section:
        # Check if first non-empty line is bold (starts with **)
        first_lines = solution_section.group(1).strip().split('\n', 2)
        if first_lines and first_lines[0].strip().startswith('**'):
            results['has_solution_bold'] = True
    
    # Check if all validations pass
    results['all_valid'] = all([
        results['has_pattern_title'],
        results['has_narrower_header'],
        results['has_problem_header'],
        results['has_problem_bold'],
        results['has_solution_header'],
        results['has_solution_bold'],
        results['has_broader_header']
    ])
    
    return results

def main():
    """Validate all pattern files."""
    patterns_dir = Path('markdown/apl')
    
    if not patterns_dir.exists():
        print(f"Error: Directory {patterns_dir} not found")
        return
    
    # Find all pattern files (apl001.md through apl253.md)
    pattern_files = sorted(patterns_dir.glob('apl*.md'))
    pattern_files = [f for f in pattern_files if re.match(r'apl\d+\.md', f.name)]
    
    all_results = []
    valid_count = 0
    invalid_count = 0
    
    print("Validating pattern structure...")
    print("=" * 80)
    
    for filepath in pattern_files:
        results = validate_pattern_structure(filepath)
        all_results.append(results)
        
        if results['all_valid']:
            valid_count += 1
        else:
            invalid_count += 1
            # Print details for invalid patterns
            print(f"\n❌ {results['file']} - INVALID:")
            for key, value in results.items():
                if key not in ['file', 'all_valid'] and not value:
                    print(f"   Missing: {key}")
    
    print("\n" + "=" * 80)
    print(f"\nValidation Summary:")
    print(f"  Total patterns: {len(pattern_files)}")
    print(f"  ✅ Valid: {valid_count}")
    print(f"  ❌ Invalid: {invalid_count}")
    
    if invalid_count == 0:
        print("\n🎉 All patterns have the required structure!")
    else:
        print(f"\n⚠️  {invalid_count} patterns need attention.")
    
    return invalid_count == 0

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)
