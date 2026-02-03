#!/usr/bin/env python3
"""
Fix patterns that are missing problem statements or bold solutions.
These patterns had a unique structure where the solution statement
was the first paragraph and the problem was implicit or just a quote.
"""

import re
from pathlib import Path

# List of patterns that need fixing (missing bold solution)
PATTERNS_TO_FIX = [
    7, 16, 26, 28, 34, 35, 40, 54, 56, 64, 75, 81, 95, 99,
    195, 208, 211, 213, 221, 225, 231, 235, 236, 239, 241, 248, 249
]

def fix_pattern(pattern_num: int):
    """Fix a pattern that's missing bold problem or solution."""
    backup_file = Path(f'markdown/apl_backup/apl{pattern_num:03d}.md')
    output_file = Path(f'markdown/apl/apl{pattern_num:03d}.md')
    
    if not backup_file.exists():
        print(f"Warning: Backup file {backup_file} not found")
        return False
    
    with open(backup_file, 'r', encoding='utf-8') as f:
        backup_content = f.read()
    
    # Extract title
    title_match = re.search(r'^#\s+(\d+)\s*-\s*(.+)$', backup_content, re.MULTILINE)
    if not title_match:
        print(f"Warning: No title in {backup_file}")
        return False
    
    pattern_number = title_match.group(1)
    pattern_name = title_match.group(2).strip()
    
    # Find the first paragraph (which is usually the solution statement)
    # It comes after the title and before "## Discussion" or "## Problem"
    first_para_match = re.search(
        r'^#\s+\d+\s*-\s*.+?\n\n(.+?)(?=\n##)',
        backup_content,
        re.MULTILINE | re.DOTALL
    )
    
    if not first_para_match:
        print(f"Warning: No first paragraph in {backup_file}")
        return False
    
    solution_statement = first_para_match.group(1).strip()
    
    # Extract discussion section
    discussion_match = re.search(r'##\s*Discussion\s*\n\n(.+?)(?=\n##|\Z)', backup_content, re.DOTALL)
    if not discussion_match:
        # Try to find content after "## Problem"
        discussion_match = re.search(r'##\s*Problem\s*\n\n(.+?)(?=\n##|\Z)', backup_content, re.DOTALL)
    
    discussion_section = discussion_match.group(1).strip() if discussion_match else ""
    
    # Extract related patterns
    related_match = re.search(r'##\s*Related Patterns\s*\n\n(.+?)(?=\n##|\Z)', backup_content, re.DOTALL)
    related_section = related_match.group(1).strip() if related_match else ""
    
    # Extract narrower context (first paragraph of discussion with ". . .")
    narrower = ""
    main_discussion = discussion_section
    
    narrower_match = re.match(r'^\.\s*\.\s*\.\s*(.+?)(?=\n\n)', discussion_section, re.DOTALL)
    if narrower_match:
        narrower = narrower_match.group(1).strip()
        main_discussion = discussion_section[narrower_match.end():].strip()
    
    # Extract broader context (last paragraph with pattern references)
    broader = ""
    problem_discussion = main_discussion
    
    # Look for ". . ." near the end
    dots_pattern = r'(\.\s*\.\s*\.\s*.+?)(?:\s+A Pattern Language is published|\Z)'
    dots_match = re.search(dots_pattern, main_discussion, re.DOTALL)
    
    if dots_match:
        potential_broader = dots_match.group(1).strip()
        if re.search(r'[A-Z][A-Z\s]+\(\d+\)', potential_broader):
            broader = potential_broader
            broader_start = dots_match.start()
            problem_discussion = main_discussion[:broader_start].strip()
    
    # If no broader found, create default
    if not broader:
        broader = "To complete this pattern, use the related patterns listed below to implement the necessary details."
    
    # Build new structure
    output = []
    output.append(f"# Pattern: {pattern_number} - {pattern_name}")
    output.append("")
    
    # Narrower
    output.append("## Narrower:")
    output.append("")
    if narrower:
        output.append(narrower)
    else:
        output.append("This pattern helps to complete the larger patterns in which it is embedded.")
    output.append("")
    
    # Problem - create a generic problem statement
    output.append("## Problem:")
    output.append("")
    output.append(f"**This pattern addresses a fundamental need in the system.**")
    output.append("")
    if problem_discussion:
        output.append(problem_discussion)
        output.append("")
    
    # Solution
    output.append("## Solution:")
    output.append("")
    output.append(f"**{solution_statement}**")
    output.append("")
    
    # Broader
    output.append("## Broader:")
    output.append("")
    output.append(broader)
    output.append("")
    
    # Related patterns
    if related_section:
        output.append("---")
        output.append("")
        output.append("### Related Patterns")
        output.append("")
        output.append(related_section)
        output.append("")
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    return True

def main():
    """Fix all patterns that need attention."""
    print("Fixing patterns with missing problem statements...")
    print("=" * 80)
    
    success_count = 0
    fail_count = 0
    
    for pattern_num in PATTERNS_TO_FIX:
        print(f"Fixing pattern {pattern_num}...")
        if fix_pattern(pattern_num):
            success_count += 1
        else:
            fail_count += 1
    
    print("\n" + "=" * 80)
    print(f"\nResults:")
    print(f"  ✅ Fixed: {success_count}")
    print(f"  ❌ Failed: {fail_count}")

if __name__ == '__main__':
    main()
