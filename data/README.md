# Data - Storage & Datasets

> **Data Storage**: Future home for datasets, caches, and generated data files

## Overview

This directory is **reserved for future use** as a centralized location for data files, caches, analysis results, and other data artifacts that don't fit in the repository root.

## Purpose

### Future Data Organization

As data accumulates, this directory will house:
- **Analysis results**: Output from analysis scripts
- **Cache files**: Performance optimization caches
- **Generated datasets**: Derived data products
- **Temporary outputs**: Working files from processing
- **Metrics**: Repository metrics and statistics

## Current Status

**Empty** - Data files currently at repository root or in region-specific locations.

## Migration Plan

### When to Move Data Here

Data should migrate here when:
1. Root directory has too many data files (>20)
2. Clear categories of data emerge
3. Data needs organized subdirectories
4. Separation of code and data becomes beneficial

### Candidate Data Files (Future)

Files that might move here:
- `*.json` - Data schemas → `data/schemas/`
- `*_data.json` - Analysis data → `data/analysis/`
- `*_report.txt` - Reports → `data/reports/`
- Cache files → `data/cache/`
- Metrics → `data/metrics/`

## Proposed Structure

```
data/
├── README.md (this file)
├── schemas/       # JSON schemas and structured data
├── analysis/      # Analysis results
├── cache/         # Performance caches
├── reports/       # Generated reports
└── metrics/       # Repository metrics
```

## Why Empty Now?

### Pattern 2: Distribution

Currently, data files at root are manageable:
- ~30 JSON files at root
- Analysis data in specific locations
- Appropriate for current scale
- No overwhelming clutter

**When root data exceeds 30 files**, migrate here.

### Clear Locations

Many data files have better homes:
- **Pattern schemas**: Root (frequently accessed)
- **Interlocking data**: Root (analysis outputs)
- **Navigation data**: Root (reference data)
- **OpenCog data**: `opencog_atomese/` (region-specific)

## When This Becomes a Town

This directory will become a **self-sustaining country town** when:

1. **Population**: 20-100 data files organized in subdirectories
2. **README**: Comprehensive documentation (this file will expand)
3. **Unique Industry**: Data management and artifact storage
4. **Independent Value**: Organized access to generated data

## Current Data Locations

### At Repository Root

Key data files currently at root:

**Schemas**:
- `pattern_language_generated.json`
- `category_towns.json`
- `category_buildings.json`
- `category_construction.json`
- `pattern_sequences.json`
- `archetypal_patterns.json`
- `archetypal_pattern_schema.json`
- `pattern_schema.json`
- `uia_pattern_list.json`

**Analysis Data**:
- `interlocking_analysis_data.json`
- `navigation_analysis_data.json`
- `domain_analysis.json`
- `navigation_gaps.json`
- `pattern_application_analysis.json`

**Reports**:
- `distribution_report.txt`
- `domain_analysis_report.md`

### In Other Regions

**Region-specific data stays with region**:
- `opencog_atomese/*.scm` - Knowledge graphs
- `npu253/` - Runtime data
- `skill_framework/` - Workflow data

## Integration with Repository

### Pattern 6: Country Towns

**Not yet a country town** because:
- ❌ Empty (no population)
- ❌ No unique functionality yet
- ❌ Not independently valuable

**Will become a town** when data migrates and organizes.

### Pattern 4: Agricultural Valleys

**Not a valley** - this will be **hillside**:
- Contains derived/generated data
- Can be regenerated from sources
- Not original/irreplaceable data

**Valleys** remain: `../apl/`, `../uia/`

## Recommendations

### For Now

✅ **Leave empty** - data organization premature
✅ **Keep frequently-accessed data at root**
✅ **Keep region-specific data in regions**
✅ **Wait for natural pressure to organize**

### Future Triggers

Move data here when:
- ⚠️ Root has >30 data files
- ⚠️ Data becomes hard to find
- ⚠️ Clear categories emerge
- ⚠️ Cache management needed

### When Populating

1. Create subdirectories (schemas/, analysis/, etc.)
2. Move appropriate data files
3. Add per-category READMEs
4. Update this README
5. Update scripts to new paths
6. Add to navigation lace

## Design Principles

### Don't Mix Data and Documentation

**Separate**:
- ❌ Mix data JSON with documentation MD at root
- ✅ Keep schemas organized
- ✅ Keep reports separate from data
- ✅ Clear purpose for each location

### Keep Region Data with Region

**Good**:
- ✅ `opencog_atomese/*.scm` stays in opencog_atomese/
- ✅ `npu253/` keeps its own runtime data
- ✅ `skill_framework/` keeps workflow data

**Avoid**:
- ❌ Moving region-specific data to centralized data/
- ❌ Breaking cohesion of self-sustaining towns

## Contributing

### Don't Force Organization

❌ Don't move data here prematurely
❌ Don't centralize region-specific data
✅ Let organization emerge naturally
✅ Move when root becomes crowded

### When Time Comes

1. Propose data organization
2. Categorize data files
3. Update scripts/tools
4. Maintain backward compatibility
5. Document data schemas

## Future Use Cases

When populated, this directory will support:

### For Developers
- Clear data file location
- Organized by purpose
- Easy to find analysis results
- Cached data for performance

### For Users
- Access to generated datasets
- Analysis results
- Metrics and reports
- Clear data provenance

### For Maintainers
- Centralized data management
- Clear regeneration procedures
- Cache management
- Data validation

---

*This directory waits for the day when data organization becomes necessary. Until then, data files live appropriately distributed across the repository.*

**Pattern 2 principle: Create structure when pressure demands it, not before.**

---

**Pattern Navigation**:
- [Main README](../README.md)
- [Distribution Analysis](../DISTRIBUTION_PATTERN.md)
- [Country Towns Analysis](../COUNTRY_TOWNS_ANALYSIS.md)
