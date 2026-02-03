#!/usr/bin/env python3
"""
Demo script showing how to use the generated UIA pattern list.
"""

import json


def demo_uia_pattern_list():
    """Demonstrate various ways to use the UIA pattern list."""
    
    print("UIA Pattern List Demo")
    print("=" * 80)
    
    # Load the JSON data
    with open('uia_pattern_list.json', 'r', encoding='utf-8') as f:
        patterns = json.load(f)
    
    print(f"\nLoaded {len(patterns)} UIA patterns\n")
    
    # Example 1: Find a pattern by sequence number
    print("Example 1: Find pattern by sequence number")
    print("-" * 80)
    seq = 42
    pattern = next((p for p in patterns if p['sequence'] == seq), None)
    if pattern:
        print(f"Pattern #{seq}:")
        print(f"  Number: {pattern['pattern_number']}")
        print(f"  Name: {pattern['pattern_name']}")
    
    # Example 2: Find a pattern by pattern number
    print("\nExample 2: Find pattern by pattern number")
    print("-" * 80)
    pattern_num = "12610300"
    pattern = next((p for p in patterns if p['pattern_number'] == pattern_num), None)
    if pattern:
        print(f"Pattern {pattern_num}:")
        print(f"  Sequence: #{pattern['sequence']}")
        print(f"  Name: {pattern['pattern_name']}")
    
    # Example 3: Search patterns by keyword in name
    print("\nExample 3: Search patterns by keyword")
    print("-" * 80)
    keyword = "domain"
    matches = [p for p in patterns if keyword.lower() in p['pattern_name'].lower()]
    print(f"Found {len(matches)} patterns containing '{keyword}':")
    for p in matches[:5]:  # Show first 5
        print(f"  {p['sequence']:3d}. {p['pattern_number']} - {p['pattern_name']}")
    if len(matches) > 5:
        print(f"  ... and {len(matches) - 5} more")
    
    # Example 4: Get patterns in a range
    print("\nExample 4: Get patterns in a range")
    print("-" * 80)
    start, end = 100, 105
    range_patterns = [p for p in patterns if start <= p['sequence'] <= end]
    print(f"Patterns {start}-{end}:")
    for p in range_patterns:
        print(f"  {p['sequence']:3d}. {p['pattern_number']} - {p['pattern_name']}")
    
    # Example 5: Pattern statistics
    print("\nExample 5: Pattern statistics")
    print("-" * 80)
    total = len(patterns)
    avg_name_length = sum(len(p['pattern_name']) for p in patterns) / total
    longest = max(patterns, key=lambda p: len(p['pattern_name']))
    shortest = min(patterns, key=lambda p: len(p['pattern_name']))
    
    print(f"Total patterns: {total}")
    print(f"Average name length: {avg_name_length:.1f} characters")
    print(f"Longest name: '{longest['pattern_name']}' ({len(longest['pattern_name'])} chars)")
    print(f"Shortest name: '{shortest['pattern_name']}' ({len(shortest['pattern_name'])} chars)")
    
    # Example 6: First and last patterns
    print("\nExample 6: First and last patterns")
    print("-" * 80)
    first = patterns[0]
    last = patterns[-1]
    print(f"First pattern: {first['pattern_number']} - {first['pattern_name']}")
    print(f"Last pattern:  {last['pattern_number']} - {last['pattern_name']}")
    
    print("\n" + "=" * 80)
    print("✓ Demo complete!")


if __name__ == '__main__':
    demo_uia_pattern_list()
