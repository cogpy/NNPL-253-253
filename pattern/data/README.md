# Pattern Data Directory

> **Pattern 2: Distribution of Towns** - Data files distributed to appropriate region

## Overview

This directory contains JSON and data files that represent the core pattern language data structures. By moving these files from the root directory, we achieve better organization and follow Pattern 2's principle of distributing "towns" (file clusters) appropriately.

## Contents

### Pattern Language Data
- `archetypal_patterns.json` - Complete archetypal pattern definitions
- `archetypal_pattern_schema.json` - Schema for archetypal patterns
- `archetypal_placeholders.json` - Placeholder mappings for pattern instantiation
- `pattern_sequences.json` - Sequence definitions and emergent phenomena
- `pattern_schema.json` - Core pattern schema
- `patterns_extracted.json` - Extracted pattern data
- `pattern_language_generated.json` - Generated pattern language

### UIA Pattern Data
- `uia_pattern_list.json` - User Interface Archetype patterns (JSON)
- `uia_pattern_list.txt` - User Interface Archetype patterns (text)

### Analysis Data
- `domain_analysis.json` - Cross-domain pattern analysis
- `pattern_application_analysis.json` - Pattern application metrics

### Backup Files
- `archetypal_patterns.json.backup` - Backup of archetypal patterns

## Usage

These data files are the foundation of the pattern language system. They are:

1. **Read-only source data** - Should not be modified directly (see AGRICULTURAL_VALLEYS.md)
2. **Programmatically accessed** - Used by scripts in `docs/scripts/`
3. **Regenerable** - Can be regenerated from authoritative sources in `apl/` and `uia/`

## Related Directories

- `../categories/` - Category-specific pattern data
- `../../docs/scripts/generators/` - Scripts that generate/process this data
- `../../markdown/` - Human-readable pattern files derived from this data

## Pattern 2 Compliance

By centralizing data files here, we:
- ✅ Reduce root directory overcrowding
- ✅ Group related files logically
- ✅ Create clear home for pattern data
- ✅ Support Pattern 4 (Agricultural Valleys) - protect source data
- ✅ Enable Pattern 5 (Lace of Streets) - clear navigation paths
