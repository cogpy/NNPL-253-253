#!/usr/bin/env python3
"""
Test the generated UIA pattern list for correctness.
"""

import json
import os


def test_uia_pattern_list():
    """Test the UIA pattern list generation."""
    
    print("Testing UIA Pattern List Generation")
    print("=" * 80)
    
    # Test 1: Check JSON file exists and is valid
    print("\n1. Testing JSON file...")
    assert os.path.exists('uia_pattern_list.json'), "JSON file not found"
    
    with open('uia_pattern_list.json', 'r', encoding='utf-8') as f:
        patterns = json.load(f)
    
    print(f"   ✓ JSON file exists and is valid")
    print(f"   ✓ Contains {len(patterns)} patterns")
    
    # Test 2: Check we have exactly 253 patterns
    print("\n2. Testing pattern count...")
    assert len(patterns) == 253, f"Expected 253 patterns, got {len(patterns)}"
    print(f"   ✓ Exactly 253 patterns found")
    
    # Test 3: Check pattern number format
    print("\n3. Testing pattern number format (1261{{pattern_num}}0)...")
    errors = []
    for p in patterns:
        seq = p['sequence']
        num = p['pattern_number']
        expected = f'1261{seq:03d}0'
        if num != expected:
            errors.append(f"Pattern {seq}: expected {expected}, got {num}")
    
    if errors:
        print("   ✗ Errors found:")
        for error in errors:
            print(f"     - {error}")
        assert False, "Pattern number format errors"
    else:
        print(f"   ✓ All pattern numbers match expected format")
    
    # Test 4: Check pattern names exist
    print("\n4. Testing pattern names...")
    empty_names = [p['sequence'] for p in patterns if not p['pattern_name'].strip()]
    if empty_names:
        print(f"   ✗ Patterns with empty names: {empty_names}")
        assert False, "Some patterns have empty names"
    else:
        print(f"   ✓ All patterns have names")
    
    # Test 5: Check sequence numbering
    print("\n5. Testing sequence numbering...")
    sequences = [p['sequence'] for p in patterns]
    expected_sequences = list(range(1, 254))
    if sequences != expected_sequences:
        print(f"   ✗ Sequence numbering incorrect")
        assert False, "Sequence numbering is not 1-253"
    else:
        print(f"   ✓ Sequences are correctly numbered 1-253")
    
    # Test 6: Check text file exists
    print("\n6. Testing text file...")
    assert os.path.exists('uia_pattern_list.txt'), "Text file not found"
    with open('uia_pattern_list.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"   ✓ Text file exists with {len(lines)} lines")
    
    # Test 7: Check markdown file exists
    print("\n7. Testing markdown file...")
    assert os.path.exists('UIA_PATTERN_LIST.md'), "Markdown file not found"
    with open('UIA_PATTERN_LIST.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
    # Check for table headers
    assert '| # | Pattern Number | Pattern Name |' in md_content
    print(f"   ✓ Markdown file exists with proper table format")
    
    # Test 8: Verify first and last patterns
    print("\n8. Testing specific patterns...")
    first_pattern = patterns[0]
    assert first_pattern['pattern_number'] == '12610010', "First pattern number incorrect"
    assert first_pattern['pattern_name'] == 'Independent domains', "First pattern name incorrect"
    print(f"   ✓ First pattern: {first_pattern['pattern_number']} - {first_pattern['pattern_name']}")
    
    last_pattern = patterns[-1]
    assert last_pattern['pattern_number'] == '12612530', "Last pattern number incorrect"
    assert last_pattern['pattern_name'] == 'Meaningful symbols of self-transformation', "Last pattern name incorrect"
    print(f"   ✓ Last pattern: {last_pattern['pattern_number']} - {last_pattern['pattern_name']}")
    
    # Success
    print("\n" + "=" * 80)
    print("✓ All tests passed!")
    print("=" * 80)
    return True


if __name__ == '__main__':
    test_uia_pattern_list()
