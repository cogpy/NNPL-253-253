#!/usr/bin/env python3
"""
Generate a list of the 253 UIA patterns with pattern numbers and names.
Pattern numbers are in format 1261{{pattern_num}}0 where pattern_num ranges from 001 to 253.
"""

import os
import re
import json


def extract_pattern_info_from_markdown(filepath):
    """
    Extract pattern number and name from UIA markdown file.
    Expected format: # 12610010 - Independent domains
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
    
    # Parse the first line: # 12610010 - Pattern Name
    match = re.match(r'^#\s+(\d+)\s+-\s+(.+)$', first_line)
    if match:
        pattern_number = match.group(1)
        pattern_name = match.group(2).strip()
        return pattern_number, pattern_name
    
    return None, None


def generate_uia_pattern_list():
    """Generate complete list of 253 UIA patterns with numbers and names."""
    
    markdown_dir = '/home/runner/work/skipl-253/skipl-253/markdown/uia'
    
    patterns = []
    
    # Iterate through all expected pattern numbers (1 to 253)
    for i in range(1, 254):
        # Format: 1261{{pattern_num}}0
        # pattern_num is zero-padded to 3 digits
        pattern_number = f"1261{i:03d}0"
        markdown_file = os.path.join(markdown_dir, f"{pattern_number}.md")
        
        if os.path.exists(markdown_file):
            num, name = extract_pattern_info_from_markdown(markdown_file)
            if num and name:
                patterns.append({
                    'pattern_number': num,
                    'pattern_name': name,
                    'sequence': i
                })
            else:
                print(f"Warning: Could not parse {markdown_file}")
        else:
            print(f"Warning: File not found: {markdown_file}")
    
    return patterns


def main():
    """Main function to generate and display UIA pattern list."""
    
    print("Generating UIA Pattern List...")
    print("=" * 80)
    
    patterns = generate_uia_pattern_list()
    
    print(f"\nFound {len(patterns)} patterns\n")
    
    # Display the list
    print("UIA Pattern List")
    print("=" * 80)
    print(f"{'#':<5} {'Pattern Number':<15} {'Pattern Name'}")
    print("-" * 80)
    
    for pattern in patterns:
        seq = pattern['sequence']
        num = pattern['pattern_number']
        name = pattern['pattern_name']
        print(f"{seq:<5} {num:<15} {name}")
    
    # Save to files
    
    # 1. Save as JSON
    json_output = 'uia_pattern_list.json'
    with open(json_output, 'w', encoding='utf-8') as f:
        json.dump(patterns, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Saved JSON format to: {json_output}")
    
    # 2. Save as text file
    txt_output = 'uia_pattern_list.txt'
    with open(txt_output, 'w', encoding='utf-8') as f:
        f.write("UIA Pattern List - 253 Patterns\n")
        f.write("=" * 80 + "\n")
        f.write(f"{'#':<5} {'Pattern Number':<15} {'Pattern Name'}\n")
        f.write("-" * 80 + "\n")
        for pattern in patterns:
            seq = pattern['sequence']
            num = pattern['pattern_number']
            name = pattern['pattern_name']
            f.write(f"{seq:<5} {num:<15} {name}\n")
    print(f"✓ Saved text format to: {txt_output}")
    
    # 3. Save as markdown
    md_output = 'UIA_PATTERN_LIST.md'
    with open(md_output, 'w', encoding='utf-8') as f:
        f.write("# UIA Pattern List\n\n")
        f.write("Complete list of 253 UIA patterns with pattern numbers and generalized names.\n\n")
        f.write("Pattern numbers follow the format: `1261{{pattern_num}}0` where pattern_num ranges from 001 to 253.\n\n")
        f.write("| # | Pattern Number | Pattern Name |\n")
        f.write("|---|----------------|-------------|\n")
        for pattern in patterns:
            seq = pattern['sequence']
            num = pattern['pattern_number']
            name = pattern['pattern_name']
            f.write(f"| {seq} | {num} | {name} |\n")
    print(f"✓ Saved markdown format to: {md_output}")
    
    print(f"\n✓ Successfully generated list of {len(patterns)} UIA patterns")


if __name__ == '__main__':
    main()
