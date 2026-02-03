# APL Pattern Language - Installation and Usage Guide

This guide explains how to install and use the APL Pattern Language implementation.

## Overview

This implementation provides Christopher Alexander's "A Pattern Language" (253 architectural patterns) in the APL array programming language. APL's powerful array operations make it ideal for querying, transforming, and analyzing pattern relationships.

## Installation

### Prerequisites

You need an APL interpreter. Recommended options:

#### Option 1: Dyalog APL (Recommended)

**Download**: https://www.dyalog.com/download-zone.htm

Dyalog APL is the most popular commercial APL implementation with free versions available for non-commercial use.

**Installation**:
- **Windows**: Download and run the installer
- **macOS**: Download the DMG and drag to Applications
- **Linux**: Download and install the appropriate package

#### Option 2: GNU APL (Free/Open Source)

**Installation**:
```bash
# Ubuntu/Debian
sudo apt-get install apl

# macOS with Homebrew
brew install gnu-apl

# Arch Linux
sudo pacman -S gnu-apl
```

#### Option 3: NARS2000 (Free, Windows)

**Download**: http://www.nars2000.org/

Windows-only APL implementation with good Unicode support.

#### Option 4: ngn/apl (JavaScript/Browser)

**Online Demo**: https://ngn.github.io/apl/

No installation required! Run APL in your browser.

### Getting the Code

Clone or download the APL-253 repository:

```bash
git clone https://github.com/o9nn/APL-253.git
cd APL-253/apl_language
```

## Quick Start

### 1. Start APL Interpreter

**Dyalog APL**:
```bash
dyalog
```

**GNU APL**:
```bash
apl
```

**NARS2000**: Launch from Start Menu or desktop icon

### 2. Load the Pattern Language

```apl
)LOAD patterns
)LOAD queries
)LOAD transformations
)LOAD relationships
)LOAD data_loader
)LOAD demo
```

Or load all at once (in some APL implementations):

```apl
)LOAD patterns queries transformations relationships data_loader demo
```

### 3. Initialize and Load Data

```apl
LoadAllPatternData
```

This loads all 253 patterns, 36 sequences, and archetypal patterns.

### 4. Run Demos

```apl
RunAllDemos
```

Or run individual demos:

```apl
DemoBasicOperations
DemoQueryOperations
DemoDomainTransformations
DemoRelationshipOperations
DemoSequenceOperations
DemoAdvancedFeatures
```

## Basic Usage Examples

### Query Patterns by ID

```apl
⍝ Get pattern #1
pattern ← GetPatternByID 1
PrintPattern pattern
```

### Query by Category

```apl
⍝ Get all Towns patterns (1-94)
towns ← GetTownPatterns

⍝ Get all Buildings patterns (95-204)
buildings ← GetBuildingPatterns

⍝ Get all Construction patterns (205-253)
construction ← GetConstructionPatterns
```

### Search Patterns

```apl
⍝ Search by name
ids ← SearchPatternsByName 'Sacred'

⍝ Search by keyword
ids ← SearchPatternsByKeyword 'community'

⍝ Get high-rated patterns (2 asterisks)
important ← GetHighRatedPatterns
```

### Domain Transformations

```apl
⍝ Transform archetypal pattern to different domains
archetypal ← 'Balance between {{domains}} requires autonomy'

⍝ Transform to physical domain
physical ← TransformToPhysical archetypal

⍝ Transform to social domain
social ← TransformToSocial archetypal

⍝ Apply all transformations
all ← ApplyAllDomains archetypal
PrintDomainTransformations all
```

### Navigate Relationships

```apl
⍝ Get patterns that follow from pattern #1
following ← GetFollowingPatterns 1

⍝ Get patterns that precede pattern #50
preceding ← GetPrecedingPatterns 50

⍝ Get all connected patterns
connected ← GetAllConnectedPatterns 10

⍝ Find path between two patterns
path ← FindPathBetweenPatterns 1 50
```

### Pattern Sequences

```apl
⍝ Get patterns in sequence 1
seq ← GetPatternSequence 1

⍝ Get total number of sequences
count ← GetSequenceCount
```

## Advanced Usage

### Complex Queries

```apl
⍝ Query with multiple filters
⍝ args: category asterisks keyword
result ← QueryPatternsComplex 'Towns' 2 'region'
PrintQueryResults result
```

### Pattern Similarity

```apl
⍝ Compare two patterns
score ← ComparePatterns 1 2

⍝ Find similar patterns (threshold 50%)
similar ← FindSimilarPatterns 1 50
```

### Array Operations

APL excels at array operations:

```apl
⍝ Get first 10 pattern IDs
ids ← 10↑⍳253

⍝ Filter by category (Towns patterns only)
towns_mask ← ids ≤ 94
towns_ids ← towns_mask/ids

⍝ Count patterns by category
+/(⍳253)≤94        ⍝ Count Towns patterns
+/(⍳253)∊95..204   ⍝ Count Buildings patterns
+/(⍳253)≥205       ⍝ Count Construction patterns
```

### Batch Processing

```apl
⍝ Get all patterns in a category
ids ← GetPatternIDsByCategory 'Towns'

⍝ Get category for each pattern
categories ← GetPatternCategory¨ ids

⍝ Count connections for each pattern
connections ← GetTotalConnections¨ ⍳253

⍝ Sort patterns by connection count
sorted ← {⍵[⍒GetTotalConnections¨⍵]} ⍳253
```

## Statistics and Analysis

```apl
⍝ Show category counts
ShowCategoryCounts

⍝ Show query statistics
ShowQueryStats

⍝ Show relationship statistics
ShowRelationshipStats

⍝ Get most connected patterns
most ← GetMostConnectedPatterns 10

⍝ Get least connected patterns
least ← GetLeastConnectedPatterns 10
```

## APL Symbol Reference

Common symbols used in the implementation:

| Symbol | Name | Description | Example |
|--------|------|-------------|---------|
| `←` | Assignment | Assign value to variable | `x ← 5` |
| `⍝` | Comment | Single-line comment | `⍝ This is a comment` |
| `∇` | Del | Define/end function | `∇ F x` ... `∇` |
| `⍴` | Shape/Reshape | Get or set dimensions | `⍴x` or `3 4⍴⍳12` |
| `⍳` | Index generator | Generate indices | `⍳5` → `1 2 3 4 5` |
| `∊` | Membership | Element in set | `3∊1 2 3` → `1` |
| `⌿` | Replicate | Replicate along axis | `1 0 1/3 4 5` → `3 5` |
| `/` | Reduce/Compress | Reduce with function | `+/1 2 3` → `6` |
| `⍨` | Commute | Swap arguments | `2-⍨5` → `5-2` → `3` |
| `¨` | Each | Apply to each | `⍴¨(1 2)(3 4 5)` |
| `∘` | Compose | Function composition | `(f∘g)x` → `f(g(x))` |
| `⊂` | Enclose | Create nested array | `⊂1 2 3` |
| `⊃` | Disclose | Extract from nested | `⊃(1 2)` → `1 2` |
| `≢` | Tally | Count elements | `≢1 2 3` → `3` |
| `↑` | Take | Take n elements | `3↑1 2 3 4 5` → `1 2 3` |
| `↓` | Drop | Drop n elements | `2↓1 2 3 4 5` → `3 4 5` |
| `⍋` | Grade up | Sort indices ascending | `⍋3 1 2` → `2 3 1` |
| `⍒` | Grade down | Sort indices descending | `⍒3 1 2` → `1 3 2` |
| `∪` | Unique | Remove duplicates | `∪1 2 2 3` → `1 2 3` |
| `∩` | Intersection | Set intersection | `1 2 3∩2 3 4` → `2 3` |
| `∨` | Or | Logical or | `0∨1` → `1` |
| `∧` | And | Logical and | `1∧0` → `0` |
| `~` | Not/Without | Logical not or set difference | `~1 0` → `0 1` |
| `≤` | Less or equal | Comparison | `3≤5` → `1` |
| `≥` | Greater or equal | Comparison | `5≥3` → `1` |
| `≠` | Not equal | Comparison | `3≠5` → `1` |
| `≡` | Match | Exact match | `1 2≡1 2` → `1` |

## Tips for APL Programming

### 1. Think in Arrays

APL is designed for array operations. Instead of loops, think about operating on entire arrays:

```apl
⍝ Python-style loop (not idiomatic APL):
sum ← 0
:For i :In ⍳10
  sum ← sum + i
:EndFor

⍝ APL-style array operation:
sum ← +/⍳10
```

### 2. Use Composition

Combine operations using composition:

```apl
⍝ Get total connections for each pattern
connections ← GetTotalConnections¨ ⍳253

⍝ Sort pattern IDs by connection count (descending)
sorted ← {⍵[⍒GetTotalConnections¨⍵]} ⍳253
```

### 3. Boolean Indexing

Use boolean arrays to filter:

```apl
⍝ Get high-rated patterns
mask ← 2=GetPatternAsterisks¨⍳253
high_rated ← mask/⍳253
```

### 4. Working with Nested Arrays

Use `⊂` (enclose) and `⊃` (disclose) for nested structures:

```apl
⍝ Create nested array
nested ← (1 2)(3 4 5)(6)

⍝ Apply function to each
lengths ← ≢¨nested  ⍝ Result: 2 3 1
```

## Troubleshooting

### Symbol Input

**Problem**: Can't type APL symbols

**Solution**:
- **Dyalog APL**: Use the APL keyboard layout or backtick (`) key prefix
- **GNU APL**: Symbols work automatically in the APL environment
- **Copy-paste**: Copy symbols from the examples above
- **Online**: Use https://tryapl.org for in-browser APL with symbol palette

### Module Not Loading

**Problem**: `FILE NOT FOUND` error

**Solution**: Ensure you're in the `apl_language` directory or provide full path:

```apl
)LOAD /full/path/to/apl_language/patterns
```

### Memory Issues

**Problem**: Out of memory with large datasets

**Solution**: APL is very memory-efficient, but if needed:
- Load data in smaller batches
- Use `⎕EX` to delete unused variables
- Increase workspace size (interpreter-specific)

## Performance Tips

1. **Avoid explicit loops**: Use array operations instead
2. **Vectorize operations**: Apply functions to entire arrays
3. **Use primitive functions**: Built-in APL primitives are highly optimized
4. **Cache results**: Store frequently-used computed values
5. **Profile code**: Use APL profiling tools to find bottlenecks

## Further Resources

### Learning APL
- **Dyalog APL Tutorial**: https://tutorial.dyalog.com/
- **APL Wiki**: https://aplwiki.com/
- **TryAPL**: https://tryapl.org/
- **APLcart**: https://aplcart.info/ (searchable examples)
- **Mastering Dyalog APL** (free book): https://www.dyalog.com/mastering-dyalog-apl.htm

### Pattern Language
- Christopher Alexander, "A Pattern Language" (1977)
- Pattern Language website: http://www.patternlanguage.com/
- Repository documentation: See main README.md

### Community
- **APL Orchard** (chat): https://chat.stackexchange.com/rooms/52405/the-apl-orchard
- **Stack Overflow**: Tag [apl]
- **Reddit**: r/apljk

## Support

For issues with this implementation:
- GitHub Issues: https://github.com/o9nn/APL-253/issues
- See repository documentation in the main README.md

## License

MIT License - see [LICENSE](../LICENSE) for details.

---

**Happy pattern exploring in APL!** 🎯
