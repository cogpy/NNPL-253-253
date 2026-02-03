# APL Patterns in Markdown

> **Urban Documentation**: Readable versions of Christopher Alexander's Pattern Language

## Overview

This directory contains all **253 patterns** from Christopher Alexander's "A Pattern Language" in clean, readable **Markdown format**. These are the "urban" (documentation) counterpart to the "rural" (source data) HTML files in `../../apl/`.

## Contents

- **253 pattern files**: `apl001.md` through `apl253.md`
- **Markdown format**: Clean, readable, searchable
- **Complete information**: Title, category, problem, solution, references
- **Generated content**: Regenerable from source valley

## Pattern Organization

### By Category

**Towns** (Patterns 1-94): Large-scale patterns
```bash
ls apl001.md to apl094.md  # Regional and city planning
```

**Buildings** (Patterns 95-204): Medium-scale patterns
```bash
ls apl095.md to apl204.md  # Building design and layout
```

**Construction** (Patterns 205-253): Small-scale patterns
```bash
ls apl205.md to apl253.md  # Construction details and materials
```

### By Sequence

See [../sequences/README.md](../sequences/README.md) for the 36 pattern sequences that organize these 253 patterns into coherent flows.

## Using These Patterns

### Reading Individual Patterns

```bash
# View a specific pattern
cat apl001.md  # Pattern 1: Independent Regions
cat apl042.md  # Pattern 42: Industrial Ribbon
cat apl106.md  # Pattern 106: Positive Outdoor Space
```

### Searching Patterns

```bash
# Search by keyword
grep -r "courtyard" *.md
grep -r "sunlight" *.md
grep -r "children" *.md

# Find patterns mentioning other patterns
grep -r "Pattern 12" *.md
```

### Pattern Structure

Each markdown file contains:

1. **Title**: Pattern name and number
2. **Category**: Towns, Buildings, or Construction
3. **Problem Statement**: What issue does this pattern address?
4. **Solution**: Core solution description
5. **Implementation**: How to apply the pattern
6. **Related Patterns**: Links to broader/narrower patterns

### Example Pattern Format

```markdown
# Pattern 106: Positive Outdoor Space

**Category**: Buildings

## Problem
Outdoor spaces that are merely "left over" between buildings...

## Solution
Make all outdoor spaces positive...

## Related Patterns
Broader: Pattern 105 - South Facing Outdoors
Narrower: Pattern 107 - Wings of Light
```

## Relationship to Source

### This is the Urban Documentation

**Pattern 3 (City Country Fingers)** principle:
- **Source Valley** (rural): `../../apl/*.html` - Original HTML files
- **Urban Documentation** (this directory): Readable markdown versions
- **Max Distance**: 2 directory levels apart (proper interlocking)

### Regeneration

These files are **generated content** - they can be rebuilt from source:

```bash
# Regenerate all markdown patterns (from repository root)
python3 complete_markdown_patterns.py

# Regenerate specific patterns
python3 extract_all_patterns.py
```

**Never manually edit these files** - edit the source and regenerate.

## Navigation

### Explore Patterns

- **By Number**: `apl001.md` through `apl253.md`
- **By Category**: See organization above
- **By Sequence**: [../sequences/README.md](../sequences/README.md)

### Find Related Content

- **Original Sources**: [../../apl/](../../apl/) - HTML source files
- **Pattern Schemas**: `../../pattern_language_generated.json`
- **Hypergraph**: [../../opencog_atomese/](../../opencog_atomese/)
- **Virtual Hardware**: [../../npu253/](../../npu253/)

### Return to Hub

- [Repository README](../../README.md)
- [Navigation Hub](../../NAVIGATION_HUB.md)
- [Pattern Index](../../PATTERN_INDEX.md)
- [Pattern Map](../../PATTERN_MAP.md)

## Quick Reference

### Find Patterns About...

**Community & Social**:
- Pattern 12: Community of 7000
- Pattern 28: Eccentric Nucleus
- Pattern 37: House Cluster
- Pattern 41: Work Community

**Buildings & Spaces**:
- Pattern 95: Building Complex
- Pattern 106: Positive Outdoor Space
- Pattern 127: Intimacy Gradient
- Pattern 159: Light on Two Sides

**Construction & Details**:
- Pattern 205: Structure Follows Social Spaces
- Pattern 212: Columns at the Corners
- Pattern 227: Column Connection
- Pattern 253: Things from Your Life

### Access by Scale

**Large Scale** (Regional): Patterns 1-30
**Medium Scale** (City/Neighborhood): Patterns 31-94
**Building Scale**: Patterns 95-150
**Room Scale**: Patterns 151-204
**Detail Scale**: Patterns 205-253

## Integration with Repository

### Pattern 2: Distribution

These 253+ files follow logarithmic distribution as "small files" in the repository ecosystem.

### Pattern 3: City-Country Fingers

This directory is an "urban finger" reaching into the documentation region, interlocked with "rural" source data valley.

### Pattern 4: Agricultural Valleys

Content here is **hillside** - generated from valley (`../../apl/`). Can be regenerated if needed.

### Pattern 5: Lace of Country Streets

Multiple navigation paths:
1. Direct file access (apl001.md)
2. Sequence navigation (../sequences/)
3. Pattern Index (../../PATTERN_INDEX.md)
4. Search/grep
5. Schema access (JSON)
6. Programmatic (npu253/, opencog_atomese/)

## Quality & Completeness

✅ **All 253 patterns converted**
✅ **Consistent markdown formatting**
✅ **Searchable text**
✅ **Cross-references preserved**
✅ **Regenerable from source**
✅ **Part of navigation lace**

## Contributing

### Don't Edit Directly

❌ Don't edit markdown files directly
✅ Edit source HTML or conversion scripts
✅ Regenerate markdown from source

### Reporting Issues

If you find errors:
1. Check source file in `../../apl/`
2. Report issue with pattern number
3. Suggest correction
4. Run regeneration after fix

### Adding Features

To enhance pattern markdown:
1. Modify `complete_markdown_patterns.py`
2. Test on subset of patterns
3. Regenerate all patterns
4. Verify formatting

## Related Documentation

- **Pattern Language Book**: See `../../docs/*.pdf`
- **Sequence Documentation**: [../sequences/](../sequences/)
- **Dimensional Views**: [../context/](../context/)
- **Implementation Examples**: [../../implementations/](../../implementations/)

## Town Metaphor

In the **Country Towns** pattern:

**This directory is a "documentation town"** providing:
- ✅ Unique industry: Human-readable pattern access
- ✅ Self-sustaining: Complete with README
- ✅ Independently valuable: Can be used without other regions
- ✅ Connected: Part of navigation lace

---

*"Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem."* - Christopher Alexander

**These 253 markdown files make that wisdom accessible, searchable, and usable.**

---

**Pattern Navigation**:
- [Main README](../../README.md)
- [Pattern Index](../../PATTERN_INDEX.md)
- [Sequences](../sequences/)
- [Source Valley](../../apl/)
