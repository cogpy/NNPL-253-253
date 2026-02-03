#!/usr/bin/env python3
"""
Pattern Reader - Rural connection point in urban territory

This script provides programmatic access to the markdown patterns,
creating a bridge between documentation (urban) and code (rural).

Usage:
    python3 pattern_reader.py 3               # Read pattern 3
    python3 pattern_reader.py --search fingers  # Search patterns
    python3 pattern_reader.py --list           # List all patterns
"""

import sys
import re
from pathlib import Path

def get_pattern_path(pattern_num, pattern_type='apl'):
    """Get the path to a pattern file"""
    base_dir = Path(__file__).parent
    if pattern_type == 'apl':
        return base_dir / 'apl' / f'apl{pattern_num:03d}.md'
    else:
        # UIA pattern IDs start at 12610010
        uia_id = 12610000 + (pattern_num * 10)
        return base_dir / 'uia' / f'{uia_id}.md'

def read_pattern(pattern_num, pattern_type='apl'):
    """Read and return pattern content"""
    path = get_pattern_path(pattern_num, pattern_type)
    if not path.exists():
        return f"Pattern {pattern_num} not found at {path}"
    
    return path.read_text()

def extract_title(content):
    """Extract pattern title from markdown"""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else "Unknown"

def list_patterns(pattern_type='apl'):
    """List all available patterns"""
    base_dir = Path(__file__).parent
    pattern_dir = base_dir / pattern_type
    
    patterns = []
    for path in sorted(pattern_dir.glob('*.md')):
        content = path.read_text()
        title = extract_title(content)
        patterns.append((path.stem, title))
    
    return patterns

def search_patterns(query, pattern_type='apl'):
    """Search patterns for a query string"""
    base_dir = Path(__file__).parent
    pattern_dir = base_dir / pattern_type
    
    results = []
    for path in sorted(pattern_dir.glob('*.md')):
        content = path.read_text()
        if query.lower() in content.lower():
            title = extract_title(content)
            results.append((path.stem, title))
    
    return results

def main():
    """Command-line interface"""
    if len(sys.argv) < 2:
        print(__doc__)
        return
    
    arg = sys.argv[1]
    
    if arg == '--list':
        patterns = list_patterns()
        print(f"Found {len(patterns)} APL patterns:\n")
        for name, title in patterns[:10]:  # Show first 10
            print(f"  {name}: {title}")
        if len(patterns) > 10:
            print(f"  ... and {len(patterns) - 10} more")
    
    elif arg == '--search':
        if len(sys.argv) < 3:
            print("Usage: pattern_reader.py --search <query>")
            return
        query = sys.argv[2]
        results = search_patterns(query)
        print(f"Found {len(results)} patterns matching '{query}':\n")
        for name, title in results[:20]:  # Show first 20
            print(f"  {name}: {title}")
    
    elif arg.isdigit():
        pattern_num = int(arg)
        content = read_pattern(pattern_num)
        print(content)
    
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
