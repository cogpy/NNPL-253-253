#!/usr/bin/env python3
"""
Validate sequence markdown files.
Ensures all 36 sequence files exist and have the expected structure.
"""

import json
import os
from pathlib import Path


def validate_sequences():
    """Validate sequence markdown files."""
    print("=" * 70)
    print("SEQUENCE MARKDOWN VALIDATION")
    print("=" * 70)
    
    # Load sequences data
    sequences_file = 'pattern_sequences.json'
    with open(sequences_file, 'r', encoding='utf-8') as f:
        sequences_data = json.load(f)
    
    sequences = sequences_data['sequences']
    sequences_dir = Path('markdown/sequences')
    
    print(f"\n=== Checking Sequence Files ===")
    print(f"Expected sequences: {len(sequences)}")
    
    missing_files = []
    invalid_files = []
    valid_files = []
    
    # Check each sequence
    for sequence in sequences:
        seq_id = sequence['id']
        filename = f"seq{seq_id:02d}.md"
        filepath = sequences_dir / filename
        
        # Check if file exists
        if not filepath.exists():
            missing_files.append(filename)
            print(f"✗ {filename} - MISSING")
            continue
        
        # Read file content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Validate structure
        required_sections = [
            "# Sequence",
            "## Metadata",
            "## Overview",
            "## Emergent Phenomena",
            "## The Algorithm: Flow and Sequence",
            "## Aggregated Problem-Solution Pairs",
            "## Relationship to",
            "## Integration with Pattern Language",
            "## Pattern Details"
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)
        
        if missing_sections:
            invalid_files.append({
                'filename': filename,
                'missing_sections': missing_sections
            })
            print(f"✗ {filename} - INVALID (missing sections)")
        else:
            valid_files.append(filename)
            print(f"✓ {filename} - OK")
    
    # Check README
    readme_path = sequences_dir / "README.md"
    if readme_path.exists():
        print(f"✓ README.md - OK")
    else:
        print(f"✗ README.md - MISSING")
    
    # Summary
    print(f"\n=== Validation Summary ===")
    print(f"Total sequences: {len(sequences)}")
    print(f"Valid files: {len(valid_files)}")
    print(f"Missing files: {len(missing_files)}")
    print(f"Invalid files: {len(invalid_files)}")
    
    if missing_files:
        print(f"\nMissing files:")
        for filename in missing_files:
            print(f"  - {filename}")
    
    if invalid_files:
        print(f"\nInvalid files:")
        for item in invalid_files:
            print(f"  - {item['filename']}")
            for section in item['missing_sections']:
                print(f"    Missing: {section}")
    
    # Check file sizes
    print(f"\n=== File Size Check ===")
    total_size = 0
    min_size = float('inf')
    max_size = 0
    
    for seq_id in range(1, 37):
        filename = f"seq{seq_id:02d}.md"
        filepath = sequences_dir / filename
        if filepath.exists():
            size = filepath.stat().st_size
            total_size += size
            min_size = min(min_size, size)
            max_size = max(max_size, size)
    
    avg_size = total_size / 36 if total_size > 0 else 0
    
    print(f"Total size: {total_size:,} bytes")
    print(f"Average size: {avg_size:,.0f} bytes")
    print(f"Min size: {min_size:,} bytes")
    print(f"Max size: {max_size:,} bytes")
    
    # Final result
    print("\n" + "=" * 70)
    if len(valid_files) == 36 and readme_path.exists():
        print("✓ ALL VALIDATIONS PASSED")
        print("=" * 70)
        return True
    else:
        print("✗ VALIDATION FAILED")
        print("=" * 70)
        return False


if __name__ == '__main__':
    success = validate_sequences()
    exit(0 if success else 1)
