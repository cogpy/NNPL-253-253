# Pattern - Structured Data Files

> **Processed Pattern Data**: Structured intermediate format for pattern processing

## Overview

This directory contains **253 processed pattern data files** - an intermediate format between source HTML and final outputs. These files store extracted and structured pattern data for various processing pipelines.

## Contents

- **253 pattern files**: Numbered pattern data files
- **Structured format**: Consistent internal structure
- **Processing intermediate**: Between source and output
- **Machine-readable**: For automated processing

## Purpose

### Intermediate Processing Layer

```
Source HTML (apl/, uia/)
↓ extraction
Pattern Data Files (this directory)
↓ transformation
Final Outputs (markdown/, JSON, opencog_atomese/, etc.)
```

### Use Cases

1. **Pattern Extraction**: Store parsed HTML data
2. **Schema Generation**: Source for JSON schemas
3. **Markdown Generation**: Input for markdown conversion
4. **Analysis**: Pattern structure analysis
5. **Validation**: Verify extraction correctness

## File Naming

Files in this directory use various naming schemes:
- Pattern ID numbers (e.g., `12610010`, `12610020`)
- Direct pattern references
- Structured identifiers

**Note**: File count (254) exceeds 253 patterns due to:
- Multiple format versions
- Processing metadata
- Backup/working files

## Relationship to Other Regions

### Source Data

**Inputs** (what generates these files):
- `../apl/*.html` - Original Alexander patterns
- `../uia/*.html` - Original UIA patterns
- Extraction scripts at repository root

### Output Targets

**Outputs** (what uses these files):
- `../markdown/apl/*.md` - Readable pattern docs
- `../markdown/uia/*.md` - UIA pattern docs
- `pattern_language_generated.json` - Schema
- `category_*.json` - Category schemas
- OpenCog Atomese representations

## Processing Scripts

### Generate Pattern Data

From repository root:

```bash
# Extract patterns from HTML
python3 extract_all_patterns.py

# Analyze pattern structure
python3 analyze_pattern_sections.py

# Generate schemas from pattern data
python3 generate_pattern_schema.py
```

### Use Pattern Data

```bash
# Convert to markdown
python3 complete_markdown_patterns.py

# Generate JSON schemas
python3 populate_pattern_json.py

# Create OpenCog representations
python3 generate_opencog_atomese.py
```

## Data Structure

Pattern data files typically contain:
- **Pattern ID**: Unique identifier
- **Title**: Pattern name
- **Category**: Towns, Buildings, or Construction
- **Problem**: Problem statement
- **Solution**: Solution description
- **Context**: Usage context
- **References**: Related patterns

## Not for Direct Use

### Use Derived Outputs Instead

For most purposes, **don't use this directory directly**:

❌ Reading patterns → Use `../markdown/apl/*.md`
❌ Programmatic access → Use `npu253/` or `opencog_atomese/`
❌ Search/browse → Use pattern index or navigation hub
❌ Analysis → Use JSON schemas or pattern API

✅ Only use for pattern processing pipelines and extraction debugging

## Integration with Repository

### Pattern 4: Agricultural Valleys

This directory is **hillside** - derived content:
- Generated from valleys (`../apl/`, `../uia/`)
- Can be regenerated if needed
- Not original source data

### Pattern 3: City-Country Fingers

Processing intermediate:
- Bridges rural (source HTML) and urban (documentation)
- Part of transformation pipeline
- 2 levels from both source and output

## Regeneration

These files can be regenerated from source:

```bash
# From repository root
python3 extract_all_patterns.py   # Re-extract from HTML
python3 analyze_pattern_sections.py  # Re-analyze structure
```

**Safe to delete and regenerate** - not original source data.

## Quality & Completeness

✅ **All patterns processed**
✅ **Structured format**
✅ **Machine-readable**
✅ **Regenerable from source**
⚠️ **Not for human consumption** (use markdown instead)

## Navigation

### For Pattern Access

**Don't start here** - use these instead:
- **Readable patterns**: [../markdown/apl/](../markdown/apl/)
- **Pattern index**: [../PATTERN_INDEX.md](../PATTERN_INDEX.md)
- **Navigation hub**: [../NAVIGATION_HUB.md](../NAVIGATION_HUB.md)

### For Development

- **Source valleys**: [../apl/](../apl/), [../uia/](../uia/)
- **Processing scripts**: Repository root (Python scripts)
- **Output formats**: [../markdown/](../markdown/), JSON files, [../opencog_atomese/](../opencog_atomese/)

## Contributing

### When to Edit

❌ Never edit pattern data files directly
✅ Edit source HTML in `../apl/` or `../uia/`
✅ Edit extraction/processing scripts
✅ Regenerate pattern data from source

### Adding Processing

To add new pattern processing:
1. Read from source valleys (`../apl/`, `../uia/`)
2. Process as needed
3. Write to appropriate output (markdown, JSON, etc.)
4. Optional: Store intermediate data here
5. Document in processing script

## Related Documentation

- **Source Data**: [../apl/README.md](../apl/README.md), [../uia/README.md](../uia/README.md)
- **Output Formats**: [../markdown/apl/README.md](../markdown/apl/README.md)
- **Processing Guide**: [../IMPLEMENTATION_GUIDE.md](../IMPLEMENTATION_GUIDE.md)

## Town Classification

In the **Country Towns** pattern:

**This directory is NOT a self-sustaining town** because:
- ❌ No unique industry (just intermediate processing)
- ❌ Not independently valuable (use outputs instead)
- ⚠️ No README until now (documentation gap filled)

**This is a "warehouse district"** - storage for intermediate goods, not a destination.

## Recommendations

### For Users

- **Skip this directory** - use markdown, JSON, or APIs instead
- Navigate to readable/usable formats
- Only inspect for debugging extraction issues

### For Developers

- **Use as processing intermediate** when needed
- Regenerate from source when in doubt
- Document extraction logic in scripts
- Keep processing pipelines clean

### For Maintainers

- Periodically regenerate from source
- Verify file count matches expectations
- Clean up any redundant intermediate files
- Keep synchronized with source valleys

---

*This directory exists to support pattern processing pipelines. For human-readable patterns, see [../markdown/apl/](../markdown/apl/). For programmatic access, see [../npu253/](../npu253/) or [../opencog_atomese/](../opencog_atomese/).*

---

**Pattern Navigation**:
- [Main README](../README.md)
- [Readable Patterns](../markdown/apl/)
- [Pattern Index](../PATTERN_INDEX.md)
- [Source Valley](../apl/)
