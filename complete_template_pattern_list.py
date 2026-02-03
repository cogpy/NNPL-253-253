#!/usr/bin/env python3
"""
Complete the TEMPLATE_PATTERN_LIST.md with all template numbers (T001-T253).
"""

import json

def complete_template_pattern_list():
    """Generate complete template pattern list with template numbers."""
    
    # Load the UIA pattern data
    with open('uia_pattern_list.json', 'r') as f:
        patterns = json.load(f)
    
    # Build the markdown content
    lines = []
    lines.append("# Template Pattern List")
    lines.append("")
    lines.append("Complete list of 253 Template patterns with pattern numbers and generalized names.")
    lines.append("")
    lines.append("Pattern numbers follow the format: `1261{{pattern_num}}0` where pattern_num ranges from 001 to 253.")
    lines.append("Template Patterns follow the format: `T{{pattern_num}}` where pattern_num ranges from 001 to 253.")
    lines.append("")
    lines.append("| # | Pattern Number | Pattern Name | Template Number | Template Name |")
    lines.append("|---|----------------|-------------|-----------------|---------------|")
    
    # Add each pattern with template number
    for i, pattern in enumerate(patterns, 1):
        pattern_num = pattern['pattern_number']
        pattern_name = pattern['pattern_name']
        template_num = f"T{i:03d}"  # Format as T001, T002, etc.
        
        # Template name is same as pattern name for now (can be customized later)
        template_name = pattern_name
        
        # Format the table row
        line = f"| {i} | {pattern_num} | {pattern_name} | {template_num} | {template_name} |"
        lines.append(line)
    
    # Write the completed file
    output_path = 'markdown/context/template/TEMPLATE_PATTERN_LIST.md'
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    
    print(f"✓ Completed {output_path}")
    print(f"✓ Added template numbers T001-T{len(patterns):03d}")
    print(f"✓ Total patterns: {len(patterns)}")

if __name__ == '__main__':
    complete_template_pattern_list()
