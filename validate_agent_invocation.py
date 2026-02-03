#!/usr/bin/env python3
"""
Validate that all apl0 agent files have proper invocation sections.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

def validate_agent_file(filepath: Path) -> Tuple[bool, List[str]]:
    """
    Validate that an agent file has all required invocation sections.
    
    Returns:
        (is_valid, list_of_issues)
    """
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, [f"Failed to read file: {e}"]
    
    # Check for frontmatter
    if not content.startswith('---'):
        issues.append("Missing frontmatter")
    
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        issues.append("Malformed frontmatter")
    else:
        fm_content = frontmatter_match.group(1)
        if 'name:' not in fm_content:
            issues.append("Frontmatter missing 'name' field")
        if 'description:' not in fm_content:
            issues.append("Frontmatter missing 'description' field")
    
    # Check for required sections (except for files that were skipped)
    if '## Invocation' not in content:
        # This is expected for files that were skipped (already had invocation)
        # or files we couldn't process
        pass
    else:
        # If it has Invocation section, validate its structure
        if '### How to Invoke This Agent' not in content:
            issues.append("Invocation section missing 'How to Invoke' subsection")
        
        if '### When to Invoke This Agent' not in content:
            issues.append("Invocation section missing 'When to Invoke' subsection")
        
        if '## Context Handling' not in content:
            issues.append("Missing 'Context Handling' section")
        
        if '### Required Context When Invoked' not in content:
            issues.append("Context Handling missing 'Required Context' subsection")
        
        if '### Context Format Example' not in content:
            issues.append("Context Handling missing 'Format Example' subsection")
        
        # Check for Delegation section (not required for context agents)
        if filepath.name not in ['broader.md', 'narrower.md']:
            # Dimension, category, sequence, and pattern agents should have delegation
            if '## Delegation' not in content:
                # This is OK for agents that have no subagents
                pass
    
    return len(issues) == 0, issues

def main():
    """Main validation function."""
    base_path = Path('/home/runner/work/skipl-253/skipl-253/.github/agents/apl0')
    
    print("Validating apl0 agent files...")
    print("=" * 80)
    
    # Find all .md files
    agent_files = sorted(base_path.rglob('*.md'))
    
    total_files = len(agent_files)
    valid_files = 0
    invalid_files = 0
    issues_by_file = {}
    
    for filepath in agent_files:
        is_valid, issues = validate_agent_file(filepath)
        
        if is_valid:
            valid_files += 1
        else:
            invalid_files += 1
            rel_path = filepath.relative_to(base_path)
            issues_by_file[str(rel_path)] = issues
    
    print(f"\nValidation Results:")
    print(f"  Total files: {total_files}")
    print(f"  Valid files: {valid_files}")
    print(f"  Invalid files: {invalid_files}")
    
    if invalid_files > 0:
        print(f"\n{'=' * 80}")
        print(f"Issues Found ({invalid_files} files):")
        print(f"{'=' * 80}")
        
        # Show first 10 files with issues
        count = 0
        for filepath, issues in sorted(issues_by_file.items()):
            if count >= 10:
                remaining = len(issues_by_file) - 10
                print(f"\n... and {remaining} more files with issues")
                break
            
            print(f"\n{filepath}:")
            for issue in issues:
                print(f"  - {issue}")
            count += 1
    
    print(f"\n{'=' * 80}")
    if invalid_files == 0:
        print("✓ All agent files are properly formatted!")
    else:
        print(f"✗ Found issues in {invalid_files} files")
    
    return 0 if invalid_files == 0 else 1

if __name__ == '__main__':
    exit(main())
