#!/usr/bin/env python3
"""
Update PHYSICAL_PATTERN_LIST.md with physical pattern names from APL patterns.

The APL (A Pattern Language) patterns ARE the physical/architectural patterns.
This script extracts the APL pattern names and updates the Physical Name column
in the PHYSICAL_PATTERN_LIST.md file.
"""

import json
import re
from pathlib import Path


def load_apl_patterns():
    """Load APL pattern names from pattern_language_generated.json."""
    # Use relative path from script location
    script_dir = Path(__file__).parent
    filepath = script_dir / "pattern_language_generated.json"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    patterns = data.get('patterns', [])
    
    # Create dictionary mapping pattern number to name
    apl_names = {}
    for pattern in patterns:
        if isinstance(pattern, dict):
            num = pattern.get('number', 0)
            name = pattern.get('name', '')
            if num and name:
                apl_names[num] = name
    
    return apl_names


def update_physical_pattern_list(apl_names):
    """Update PHYSICAL_PATTERN_LIST.md with APL pattern names."""
    
    # Use relative path from script location
    script_dir = Path(__file__).parent
    filepath = script_dir / "markdown" / "context" / "physical" / "PHYSICAL_PATTERN_LIST.md"
    
    # Read the current file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines
    lines = content.split('\n')
    
    # Process each line
    updated_lines = []
    for line in lines:
        # Check if this is a data row (starts with | followed by a number)
        match = re.match(r'^\| (\d+) \|', line)
        if match:
            pattern_num = int(match.group(1))
            
            # Get the APL pattern name
            apl_name = apl_names.get(pattern_num, '')
            
            # Count the number of | separators
            num_cols = line.count('|') - 1  # Subtract 1 for leading |
            
            if num_cols == 3:
                # Line has: | # | Pattern Number | Pattern Name |
                # Need to add: Physical Number | Physical Name |
                line = line.rstrip() + f' P{pattern_num:03d} | {apl_name} |'
            elif num_cols == 4:
                # Line has: | # | Pattern Number | Pattern Name | Physical Number |
                # Need to add: Physical Name |
                line = line.rstrip() + f' {apl_name} |'
            elif num_cols >= 5:
                # Line already has all columns, update the last column
                parts = line.rsplit('|', 2)
                if len(parts) >= 2:
                    line = parts[0] + f'| {apl_name} |'
        
        updated_lines.append(line)
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_lines))
    
    print(f"Updated {filepath}")
    print(f"Added {len([n for n in apl_names.values() if n])} physical pattern names")


def main():
    """Main function."""
    print("Loading APL patterns...")
    apl_names = load_apl_patterns()
    print(f"Loaded {len(apl_names)} APL pattern names")
    
    # Show first few
    for i in range(1, 6):
        print(f"  {i}: {apl_names.get(i, 'N/A')}")
    
    print("\nUpdating PHYSICAL_PATTERN_LIST.md...")
    update_physical_pattern_list(apl_names)
    
    print("\nDone!")


if __name__ == "__main__":
    main()
