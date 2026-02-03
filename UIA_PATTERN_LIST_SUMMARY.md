# UIA Pattern List - Summary

## Overview
This repository now includes a comprehensive list of all 253 UIA (Union of International Associations) patterns with their pattern numbers and generalized names.

## Pattern Number Format
All UIA patterns follow the numbering format: **`1261{{pattern_num}}0`**

Where `{{pattern_num}}` is a zero-padded 3-digit number from 001 to 253.

Examples:
- Pattern 1: `12610010`
- Pattern 30: `12610300`
- Pattern 253: `12612530`

## Files Generated

### 1. Main Output Files
- **`UIA_PATTERN_LIST.md`** (16KB) - Human-readable markdown table with all 253 patterns
- **`uia_pattern_list.json`** (32KB) - Machine-readable JSON with pattern_number, pattern_name, and sequence
- **`uia_pattern_list.txt`** (17KB) - Plain text table format

### 2. Tools
- **`generate_uia_pattern_list.py`** - Script to regenerate the list from source files
- **`test_uia_pattern_list.py`** - Comprehensive test suite to validate the generated files
- **`demo_uia_pattern_list.py`** - Usage examples and demonstrations

## Quick Start

### View the List
```bash
# View in markdown format (best for humans)
cat UIA_PATTERN_LIST.md

# View in JSON format (best for programs)
cat uia_pattern_list.json | python3 -m json.tool | less
```

### Regenerate the List
```bash
python3 generate_uia_pattern_list.py
```

### Run Tests
```bash
python3 test_uia_pattern_list.py
```

### See Usage Examples
```bash
python3 demo_uia_pattern_list.py
```

## Using the JSON Data

```python
import json

# Load the patterns
with open('uia_pattern_list.json', 'r') as f:
    patterns = json.load(f)

# Find a pattern by sequence number
pattern = next(p for p in patterns if p['sequence'] == 42)
print(f"{pattern['pattern_number']} - {pattern['pattern_name']}")

# Search by keyword
keyword = "domain"
matches = [p for p in patterns if keyword.lower() in p['pattern_name'].lower()]
for p in matches:
    print(f"{p['sequence']}. {p['pattern_name']}")
```

## Pattern Statistics
- **Total Patterns**: 253
- **Pattern Number Range**: 12610010 to 12612530
- **Average Name Length**: 40.9 characters
- **Longest Name**: "Congruence between spaces defined by the framework and spaces defined by the processes within it" (96 chars)
- **Shortest Name**: "Interchange" (11 chars)

## Examples

### First 5 Patterns
1. `12610010` - Independent domains
2. `12610020` - Distribution of organization
3. `12610030` - Interpretation of complementary modes of organization
4. `12610040` - Regenerative resource cultivation areas
5. `12610050` - Network of inter-relationships

### Last 5 Patterns
249. `12612490` - Symbols of integration
250. `12612500` - Encouraging emphases
251. `12612510` - Different settings
252. `12612520` - Domains of insight
253. `12612530` - Meaningful symbols of self-transformation

## Notes

- Pattern names are extracted from the markdown files in `markdown/uia/`
- These are generalized pattern names that apply across multiple domains (Physical, Social, Conceptual, Psychic)
- Two patterns contain typos from the original source:
  - Pattern 100: "Arrangement of structures **ot** engender..." (should be "to")
  - Pattern 114: "**Hierachy** of perspectives..." (should be "Hierarchy")
- These typos are preserved as they exist in the original Encyclopedia of World Problems data

## Source
UIA Pattern Language from the Encyclopedia of World Problems & Human Potential
Union of International Associations (UIA) - www.uia.org
