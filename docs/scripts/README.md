# Utility and Generator Scripts

> **Pattern 2: Distribution of Towns** - Scripts organized by function

## Overview

This directory contains Python scripts for generation, analysis, transformation, and maintenance of the pattern language system.

## Structure

```
scripts/
├── generators/     # Scripts that generate content (12 files)
├── analyzers/      # Scripts that analyze data (4 files)
├── utilities/      # General utility scripts (8 files)
└── README.md       # This file
```

## Contents by Subdirectory

### generators/ (12 generation scripts)
Scripts that create new content from source data:
- `generate_pattern_schema.py` - Generate pattern schemas
- `generate_archetypal_patterns.py` - Generate archetypal patterns
- `generate_apl_archetypal_variants.py` - Generate APL variants
- `generate_archetypal_schema.py` - Generate archetypal schemas
- `generate_social_pattern_names.py` - Generate social pattern names
- `generate_sequence_markdown.py` - Generate sequence documentation
- `generate_enhanced_atomese.py` - Generate OpenCog Atomese
- `generate_opencog_atomese.py` - Generate Atomese representations
- `generate_lua_sequence_nn.py` - Generate Lua neural network code
- `generate_apl_data.py` - Generate APL data files
- (Additional generators as needed)

### Root Level Scripts (12 utility/analysis scripts)
General-purpose scripts for various operations:

**Analysis Scripts** (4 files):
- `analyze_domains.py` - Analyze domain-specific patterns
- `analyze_pattern_sections.py` - Analyze pattern section structure
- `analyze_variations.py` - Analyze pattern variations
- `apply_patterns_analysis.py` - Apply and analyze patterns

**Completion Scripts** (2 files):
- `complete_markdown_patterns.py` - Complete markdown pattern files
- `complete_template_pattern_list.py` - Complete template patterns

**Extraction/Fix Scripts** (4 files):
- `extract_all_patterns.py` - Extract patterns from source
- `fix_missing_problems.py` - Fix missing problem statements
- `fix_pattern_references.py` - Fix broken pattern references

**Configuration Scripts** (2 files):
- `configure_agent_invocation.py` - Configure agent system
- `create_pattern_index.py` - Create pattern indices

## Usage

### Running Generator Scripts

```bash
cd /home/runner/work/skipl-253/skipl-253

# Generate pattern schemas
python3 docs/scripts/generators/generate_pattern_schema.py

# Generate archetypal patterns
python3 docs/scripts/generators/generate_archetypal_patterns.py

# Generate sequence documentation
python3 docs/scripts/generators/generate_sequence_markdown.py
```

### Running Analysis Scripts

```bash
# Analyze domains
python3 docs/scripts/analyze_domains.py

# Analyze pattern variations
python3 docs/scripts/analyze_variations.py

# Apply pattern analysis
python3 docs/scripts/apply_patterns_analysis.py
```

### Running Utility Scripts

```bash
# Complete markdown patterns
python3 docs/scripts/complete_markdown_patterns.py

# Fix pattern references
python3 docs/scripts/fix_pattern_references.py

# Extract patterns
python3 docs/scripts/extract_all_patterns.py
```

## Script Dependencies

Most scripts depend on:
- **Pattern data** in `../../pattern/data/`
- **Source archives** in `../../apl/` and `../../uia/`
- **Python 3.8+** with standard library
- **Optional**: numpy, pandas for analysis scripts

## Related Content

- `../../pattern/data/` - Data files that scripts process
- `../examples/` - Demo scripts showing usage
- `../tests/` - Test scripts for validation
- `../../markdown/` - Generated markdown pattern files

## Pattern 2 Benefits

Organizing scripts here:
- ✅ Reduces root directory clutter (was 24 files at root)
- ✅ Groups scripts by function
- ✅ Creates clear operational structure
- ✅ Separates generation/maintenance from core system
- ✅ Enables systematic content management
- ✅ Follows "many small scripts, organized logically" principle
