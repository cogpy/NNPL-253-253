# APL Pattern Language - Quick Reference Card

## Loading the System

```apl
⍝ Load all modules
)LOAD patterns queries transformations relationships data_loader demo

⍝ Initialize and load data
LoadAllPatternData

⍝ Run demos
RunAllDemos
```

## Basic Operations

| Operation | APL Code | Example |
|-----------|----------|---------|
| Get pattern by ID | `GetPatternByID id` | `GetPatternByID 1` |
| Get all pattern IDs | `GetAllPatternIDs` | `⍳253` |
| Get pattern count | `GetPatternCount` | `253` |
| Print pattern | `PrintPattern pattern` | `PrintPattern GetPatternByID 1` |

## Categories

| Operation | APL Code | Result |
|-----------|----------|--------|
| Get Towns patterns | `GetTownPatterns` | `1..94` |
| Get Buildings patterns | `GetBuildingPatterns` | `95..204` |
| Get Construction patterns | `GetConstructionPatterns` | `205..253` |
| Get pattern category | `GetPatternCategory id` | `'Towns'` etc. |
| Count category | `CountPatternsInCategory cat` | count |

## Queries

| Operation | APL Code | Example |
|-----------|----------|---------|
| Search by name | `SearchPatternsByName text` | `SearchPatternsByName 'Sacred'` |
| Search by keyword | `SearchPatternsByKeyword word` | `SearchPatternsByKeyword 'light'` |
| Get high-rated | `GetHighRatedPatterns` | 2-star patterns |
| Complex query | `QueryPatternsComplex cat ast key` | Multi-filter |
| Compare patterns | `ComparePatterns id1 id2` | Similarity 0-100 |
| Find similar | `FindSimilarPatterns id thresh` | Similar patterns |

## Domain Transformations

| Operation | APL Code | Domains |
|-----------|----------|---------|
| Transform to physical | `TransformToPhysical pattern` | Spatial/material |
| Transform to social | `TransformToSocial pattern` | Organizational |
| Transform to conceptual | `TransformToConceptual pattern` | Knowledge/theory |
| Transform to individual | `TransformToIndividual pattern` | Consciousness |
| Apply all domains | `ApplyAllDomains pattern` | All 4 domains |
| Show domains | `ShowDomainInfo` | Domain info |

## Relationships

| Operation | APL Code | Returns |
|-----------|----------|---------|
| Add preceding | `AddPrecedingPattern id pre` | Success flag |
| Add following | `AddFollowingPattern id fol` | Success flag |
| Add related | `AddRelatedPattern id rel` | Success flag |
| Get preceding | `GetPrecedingPatterns id` | ID array |
| Get following | `GetFollowingPatterns id` | ID array |
| Get related | `GetRelatedPatterns id` | ID array |
| Get all connected | `GetAllConnectedPatterns id` | ID array |
| Count connections | `GetTotalConnections id` | Count |
| Find path | `FindPathBetweenPatterns start end` | Path array |
| Get distance | `GetPatternDistance start end` | Hop count |
| Print relationships | `PrintRelationships id` | Formatted |

## Sequences

| Operation | APL Code | Returns |
|-----------|----------|---------|
| Store sequence | `StoreSequence id patterns` | Success flag |
| Get sequence | `GetPatternSequence id` | ID array |
| Get sequence count | `GetSequenceCount` | `36` |

## Statistics

| Operation | APL Code | Returns |
|-----------|----------|---------|
| Show category counts | `ShowCategoryCounts` | Formatted |
| Show query stats | `ShowQueryStats` | Formatted |
| Show relationship stats | `ShowRelationshipStats` | Formatted |
| Most connected | `GetMostConnectedPatterns n` | Top n IDs |
| Least connected | `GetLeastConnectedPatterns n` | Bottom n IDs |

## Array Operations

| Operation | APL Code | Example |
|-----------|----------|---------|
| Generate IDs | `⍳n` | `⍳253` |
| Filter | `mask/data` | `(ids≤94)/ids` |
| Sum | `+/array` | `+/⍳10` → `55` |
| Count | `≢array` | `≢⍳10` → `10` |
| Take | `n↑array` | `5↑⍳10` → `1 2 3 4 5` |
| Drop | `n↓array` | `5↓⍳10` → `6 7 8 9 10` |
| Sort ascending | `array[⍋array]` | Sort indices |
| Sort descending | `array[⍒array]` | Sort indices |
| Unique | `∪array` | Remove duplicates |
| Membership | `elem∊array` | Boolean |
| Intersection | `a∩b` | Set intersection |
| Union | `∪a,b` | Set union |
| Difference | `a~b` | Set difference |
| Each (map) | `func¨array` | Apply to each |

## APL Symbols Quick Reference

| Symbol | Name | Usage | Example |
|--------|------|-------|---------|
| `←` | Assignment | `var ← value` | `x ← 5` |
| `⍝` | Comment | `⍝ comment` | `⍝ This is a comment` |
| `∇` | Del | Function def | `∇ F x` ... `∇` |
| `⍴` | Shape | `⍴array` | `⍴3 4 5` → `3` |
| `⍳` | Iota | `⍳n` | `⍳5` → `1 2 3 4 5` |
| `∊` | Member | `x∊array` | `3∊1 2 3` → `1` |
| `/` | Compress/Reduce | `+/` or `mask/` | `+/1 2 3` → `6` |
| `⌿` | Compress first | `mask⌿array` | Filter rows |
| `¨` | Each | `func¨array` | Apply each |
| `⊂` | Enclose | `⊂array` | Make nested |
| `⊃` | Disclose | `⊃nested` | Extract |
| `≢` | Tally | `≢array` | Count |
| `↑` | Take | `n↑array` | First n |
| `↓` | Drop | `n↓array` | Drop n |
| `⍋` | Grade up | `array[⍋array]` | Sort asc |
| `⍒` | Grade down | `array[⍒array]` | Sort desc |
| `∪` | Unique | `∪array` | Remove dups |
| `∩` | Intersection | `a∩b` | Common |
| `~` | Not/Without | `~array` or `a~b` | Negate/diff |
| `∨` | Or | `a∨b` | Logical or |
| `∧` | And | `a∧b` | Logical and |
| `≤` | Less/Equal | `a≤b` | Compare |
| `≥` | Greater/Equal | `a≥b` | Compare |
| `≠` | Not equal | `a≠b` | Compare |
| `≡` | Match | `a≡b` | Exact match |

## Common Patterns

### Filter by Category

```apl
⍝ Get IDs in Towns category
towns ← (⍳253)[((⍳253)≥1)∧((⍳253)≤94)]

⍝ Simpler
towns ← GetTownPatterns
```

### Count by Category

```apl
⍝ Count Towns patterns
+/((⍳253)≤94)

⍝ Count Buildings patterns
+/((⍳253)≥95)∧((⍳253)≤204)

⍝ Count Construction patterns
+/((⍳253)≥205)
```

### Batch Processing

```apl
⍝ Get categories for multiple patterns
ids ← 1 50 100 150 200 250
categories ← GetPatternCategory¨ids

⍝ Get connections for all patterns
connections ← GetTotalConnections¨⍳253

⍝ Sort by connections
sorted ← (⍳253)[⍒connections]
```

### Set Operations on Categories

```apl
⍝ High-rated Towns patterns
towns ← GetTownPatterns
high ← GetHighRatedPatterns
high_towns ← towns∩high

⍝ All important patterns (Towns OR high-rated)
important ← ∪towns,high

⍝ Low-rated Towns patterns
low_towns ← towns~high
```

### Statistical Analysis

```apl
⍝ Average connections per pattern
avg ← (+/GetTotalConnections¨⍳253)÷253

⍝ Most connected pattern
max_id ← ⊃(⍳253)[⍒GetTotalConnections¨⍳253]

⍝ Category distribution
total ← 253
towns_pct ← 100×(+/(⍳253)≤94)÷total
```

## Demo Scripts

| Demo | Command |
|------|---------|
| Basic operations | `DemoBasicOperations` |
| Query operations | `DemoQueryOperations` |
| Domain transformations | `DemoDomainTransformations` |
| Relationship operations | `DemoRelationshipOperations` |
| Sequence operations | `DemoSequenceOperations` |
| Advanced features | `DemoAdvancedFeatures` |
| All demos | `RunAllDemos` |

## Tips

1. **Think in arrays** - Avoid loops, use array operations
2. **Use each (`¨`)** - Apply functions to array elements
3. **Boolean indexing** - Filter with boolean masks
4. **Composition** - Chain operations together
5. **Grade for sorting** - Use `⍋` (ascending) or `⍒` (descending)

## Performance

- **O(1)** - Pattern lookup by ID
- **O(log n)** - Search by name (if sorted)
- **O(1)** - Category filtering
- **O(1)** - Sequence retrieval
- **O(n)** - Full text search
- **O(V+E)** - Path finding (BFS)

## Files

- `patterns.apl` - Core data structures (314 lines)
- `queries.apl` - Search and query (332 lines)
- `transformations.apl` - Domain transforms (302 lines)
- `relationships.apl` - Relationship navigation (407 lines)
- `demo.apl` - Demonstrations (302 lines)
- `data_loader.apl` - Data initialization (226 lines)

**Total: ~1,900 lines of APL code**

## Resources

- Full documentation: `README.md`
- Installation guide: `INSTALLATION.md`
- Examples: `EXAMPLES.md`
- APL Tutorial: https://tutorial.dyalog.com/
- APLcart: https://aplcart.info/

---

**Quick Start**: `LoadAllPatternData` → `RunAllDemos`
