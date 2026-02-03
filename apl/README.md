# APL - A Pattern Language (Original HTML Source)

> **Urban finger embedded in rural territory** - Documentation within raw HTML data

## Overview

This directory contains the original HTML files scraped from Christopher Alexander's "A Pattern Language" website. These are the **raw source patterns** - the "countryside" that feeds the entire pattern language system.

## Structure

- **253 Pattern HTML files** (`apl1.htm` - `apl253.htm`)
- **Navigation HTML files** (Buildings, Towns, Construction, etc.)
- **Supporting HTML assets** (images, stylesheets in subdirectories)

## The Rural Character

This is a **rural finger** in the City-Country interlocking:
- **High density code/data**: Raw HTML files
- **Working productive land**: Source material for all pattern transformations
- **Minimal processing**: Direct from source with minimal transformation

## Access Points to Urban Areas

### Want readable versions?
→ See **`markdown/apl/`** - 253 processed markdown files (urban)

### Want to understand the structure?
→ See **`PATTERN_INDEX.md`** at root - Navigation guide (urban)

### Want to use patterns programmatically?
→ See **`pattern/`** - JSON data files (rural with docs)

## Why This Directory Exists

From Pattern 3 (City Country Fingers):
> "People need access to both cities and the countryside... the city becomes good for life only when it contains a great density of interactions."

This rural finger provides:
1. **Authenticity**: Original source material unmodified
2. **Grounding**: Connection to the authentic patterns
3. **Reference**: Source of truth for all transformations

## Adjacent Urban Areas (Documentation)

Within **1-2 directory levels**:
- This README (you are here)
- Root documentation at `../` (1 level up)
- Processed patterns at `../markdown/apl/` (1 level up, 1 level down)

## Tools Working This Land

Scripts that process these HTML files:
- `scrape_apl_patterns.py` - Extracts patterns from HTML
- `populate_pattern_json.py` - Converts to JSON
- Pattern transformation scripts in `docs/scripts/`

## Navigation

- **Up to root**: `../` - Main navigation hub
- **To processed markdown**: `../markdown/apl/` - Human-readable versions
- **To pattern data**: `../pattern/` - Structured data
- **To documentation**: `../docs/` - Technical guides
