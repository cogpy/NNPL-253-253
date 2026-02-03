# APL Pattern Language Examples

This document provides concrete examples of using the APL Pattern Language implementation.

## Table of Contents

1. [Basic Pattern Operations](#basic-pattern-operations)
2. [Query Operations](#query-operations)
3. [Domain Transformations](#domain-transformations)
4. [Relationship Navigation](#relationship-navigation)
5. [Advanced Array Operations](#advanced-array-operations)

## Basic Pattern Operations

### Store and Retrieve a Pattern

```apl
⍝ Initialize the pattern system
InitializePatterns

⍝ Create a pattern record
pattern ← 1 'Independent Regions' 'Towns' 2
pattern ,← ⊂'Wherever possible, work toward independent regions'
pattern ,← ⊂'People need control over their own government'
pattern ,← ⊂'Create regions with natural boundaries'
pattern ,← ⊂'[Diagram: Regional map]'
pattern ,← ⊂(2 7 12 3 4)

⍝ Store the pattern
result ← StorePattern pattern
⍝ Result: 1 (success)

⍝ Retrieve the pattern
retrieved ← GetPatternByID 1
⍝ Result: [1, 'Independent Regions', 'Towns', 2, ...]

⍝ Display pattern
PrintPattern retrieved
⍝ Output:
⍝ Pattern #1: Independent Regions
⍝ Category: Towns | Rating: **
```

### Get Pattern Category

```apl
⍝ Get category of pattern #1
category ← GetPatternCategory 1
⍝ Result: 'Towns'

⍝ Get category of pattern #100
category ← GetPatternCategory 100
⍝ Result: 'Buildings'

⍝ Get category of pattern #250
category ← GetPatternCategory 250
⍝ Result: 'Construction'
```

### Category Counts

```apl
⍝ Show all category counts
ShowCategoryCounts
⍝ Output:
⍝ Pattern Categories:
⍝   Towns: 94
⍝   Buildings: 110
⍝   Construction: 49
⍝   Total: 253
```

## Query Operations

### Get Patterns by Category

```apl
⍝ Get all Towns patterns (1-94)
towns ← GetTownPatterns
⍝ Result: 1 2 3 4 5 6 ... 94

⍝ Count
≢towns
⍝ Result: 94

⍝ Get all Buildings patterns (95-204)
buildings ← GetBuildingPatterns
⍝ Result: 95 96 97 ... 204

⍝ Get all Construction patterns (205-253)
construction ← GetConstructionPatterns
⍝ Result: 205 206 207 ... 253
```

### Search by Name

```apl
⍝ Search for patterns containing "Sacred"
ids ← SearchPatternsByName 'Sacred'
⍝ Result: 24 66 241 (example)

⍝ Search for patterns containing "Street"
ids ← SearchPatternsByName 'Street'
⍝ Result: 49 51 52 100 101 102 (example)
```

### Search by Keyword

```apl
⍝ Search for patterns about "community"
ids ← SearchPatternsByKeyword 'community'
⍝ Result: array of pattern IDs

⍝ Search for patterns about "light"
ids ← SearchPatternsByKeyword 'light'
⍝ Result: array of pattern IDs
```

### Get High-Rated Patterns

```apl
⍝ Get all 2-asterisk patterns (most important)
high_rated ← GetHighRatedPatterns
⍝ Result: array of pattern IDs with 2 asterisks

⍝ Count
≢high_rated
⍝ Result: 94 (example - patterns with ** rating)
```

### Complex Queries

```apl
⍝ Query: High-rated Towns patterns about "region"
⍝ args: category asterisks keyword
result ← QueryPatternsComplex 'Towns' 2 'region'
⍝ Result: array of matching pattern IDs

⍝ Display results
PrintQueryResults result
⍝ Output:
⍝ Found 3 pattern(s):
⍝ 
⍝ Pattern #1: Independent Regions
⍝ Category: Towns | Rating: **
⍝ ...
```

### Pattern Comparison

```apl
⍝ Compare patterns #1 and #2
score ← ComparePatterns 1 2
⍝ Result: 85 (similarity score 0-100)

⍝ Find patterns similar to pattern #1 (threshold 50%)
similar ← FindSimilarPatterns 1 50
⍝ Result: 2 3 4 7 12 (example)
```

## Domain Transformations

### Transform to Different Domains

```apl
⍝ Store an archetypal pattern
archetypal ← 'Balance between {{domains}} will not be achieved'
archetypal ,← ' unless each one is small and autonomous enough'
archetypal ,← ' to be an independent sphere of {{influence-type}}.'

placeholders ← 'domains' 'influence-type'

result ← StoreArchetypalPattern '12610010' archetypal placeholders

⍝ Transform to physical domain
physical ← TransformToPhysical archetypal
⍝ Result: 'Balance between regions/areas will not be achieved
⍝          unless each one is small and autonomous enough
⍝          to be an independent sphere of influence.'

⍝ Transform to social domain
social ← TransformToSocial archetypal
⍝ Result: 'Balance between functional domains/communities will not be achieved
⍝          unless each one is small and autonomous enough
⍝          to be an independent sphere of influence.'

⍝ Transform to conceptual domain
conceptual ← TransformToConceptual archetypal
⍝ Result: 'Balance between knowledge domains will not be achieved
⍝          unless each one is small and autonomous enough
⍝          to be an independent sphere of insight.'

⍝ Transform to individual domain
individual ← TransformToIndividual archetypal
⍝ Result: 'Balance between modes of awareness will not be achieved
⍝          unless each one is small and autonomous enough
⍝          to be an independent sphere of influence.'
```

### Apply All Transformations

```apl
⍝ Apply all domain transformations at once
all_domains ← ApplyAllDomains archetypal
⍝ Result: nested array of (domain, transformed_text) pairs

⍝ Display all transformations
PrintDomainTransformations all_domains
⍝ Output:
⍝ Domain Transformations:
⍝ 
⍝ --- physical ---
⍝ Balance between regions/areas...
⍝ 
⍝ --- social ---
⍝ Balance between functional domains/communities...
⍝ 
⍝ --- conceptual ---
⍝ Balance between knowledge domains...
⍝ 
⍝ --- individual ---
⍝ Balance between modes of awareness...
```

### Transform by ID

```apl
⍝ Transform archetypal pattern by ID to social domain
social ← TransformArchetypalPatternByID '12610010' 'social'
⍝ Result: transformed pattern text
```

### Show Domain Information

```apl
⍝ Display supported domains
ShowDomainInfo
⍝ Output:
⍝ Supported Domains:
⍝   1. physical - Spatial, material, architectural
⍝   2. social - Organizational, community, institutional
⍝   3. conceptual - Knowledge, theoretical, paradigmatic
⍝   4. individual - Awareness, consciousness, mental
```

## Relationship Navigation

### Add Relationships

```apl
⍝ Add following patterns for pattern #1
result ← AddFollowingPattern 1 2
result ← AddFollowingPattern 1 7
result ← AddFollowingPattern 1 12
⍝ Result: 1 (success for each)

⍝ Add preceding patterns for pattern #50
result ← AddPrecedingPattern 50 25
result ← AddPrecedingPattern 50 30
⍝ Result: 1 (success for each)

⍝ Add related patterns
result ← AddRelatedPattern 1 3
result ← AddRelatedPattern 1 4
⍝ Result: 1 (success for each)
```

### Get Relationships

```apl
⍝ Get patterns following pattern #1
following ← GetFollowingPatterns 1
⍝ Result: 2 7 12

⍝ Get patterns preceding pattern #50
preceding ← GetPrecedingPatterns 50
⍝ Result: 25 30

⍝ Get related patterns
related ← GetRelatedPatterns 1
⍝ Result: 3 4

⍝ Get all connected patterns (preceding + following + related)
all ← GetAllConnectedPatterns 1
⍝ Result: 2 3 4 7 12
```

### Count Connections

```apl
⍝ Count preceding patterns
count ← CountPrecedingPatterns 1
⍝ Result: 0

⍝ Count following patterns
count ← CountFollowingPatterns 1
⍝ Result: 3

⍝ Count total connections
count ← GetTotalConnections 1
⍝ Result: 5 (0 + 3 + 2)
```

### Find Most/Least Connected

```apl
⍝ Get 10 most connected patterns
most ← GetMostConnectedPatterns 10
⍝ Result: array of 10 pattern IDs sorted by connection count

⍝ Get 10 least connected patterns
least ← GetLeastConnectedPatterns 10
⍝ Result: array of 10 pattern IDs sorted by connection count (ascending)
```

### Find Paths Between Patterns

```apl
⍝ Find shortest path from pattern #1 to pattern #50
path ← FindPathBetweenPatterns 1 50
⍝ Result: 1 2 15 30 50 (example path)

⍝ Get distance (number of hops)
distance ← GetPatternDistance 1 50
⍝ Result: 4 (number of edges in path)
```

### Display Relationships

```apl
⍝ Print all relationships for pattern #1
PrintRelationships 1
⍝ Output:
⍝ Relationships for Pattern #1:
⍝ Pattern #1: Independent Regions
⍝ Category: Towns | Rating: **
⍝ 
⍝   Preceding patterns (0): (none)
⍝   Following patterns (3): 2 7 12
⍝   Related patterns (2): 3 4
```

## Advanced Array Operations

### Array-Based Filtering

```apl
⍝ Generate first 50 pattern IDs
ids ← 50↑⍳253
⍝ Result: 1 2 3 4 5 ... 50

⍝ Filter to only Towns patterns (≤94)
towns_mask ← ids ≤ 94
towns_ids ← towns_mask/ids
⍝ Result: 1 2 3 4 5 ... 50 (all are Towns)

⍝ Generate IDs 90-110
ids ← 90+⍳21
⍝ Result: 90 91 92 ... 110

⍝ Filter to Towns patterns only
towns_mask ← ids ≤ 94
towns_only ← towns_mask/ids
⍝ Result: 90 91 92 93 94

⍝ Filter to Buildings patterns only
buildings_mask ← (ids≥95)∧(ids≤204)
buildings_only ← buildings_mask/ids
⍝ Result: 95 96 97 ... 110
```

### Batch Operations

```apl
⍝ Get categories for multiple patterns
ids ← 1 50 100 150 200 250
categories ← GetPatternCategory¨ids
⍝ Result: 'Towns' 'Towns' 'Buildings' 'Buildings' 'Buildings' 'Construction'

⍝ Count connections for each pattern
ids ← ⍳10
connections ← GetTotalConnections¨ids
⍝ Result: array of connection counts for patterns 1-10
```

### Sorting by Attributes

```apl
⍝ Sort pattern IDs by connection count (descending)
all_ids ← ⍳253
connections ← GetTotalConnections¨all_ids
sorted_ids ← all_ids[⍒connections]
⍝ Result: pattern IDs sorted by most connected first

⍝ Get top 10 most connected
top10 ← 10↑sorted_ids
⍝ Result: 10 most connected pattern IDs
```

### Set Operations

```apl
⍝ Get Towns patterns
towns ← GetTownPatterns

⍝ Get high-rated patterns
high ← GetHighRatedPatterns

⍝ Find high-rated Towns patterns (intersection)
high_towns ← towns∩high
⍝ Result: pattern IDs that are both Towns and high-rated

⍝ Find patterns that are Towns OR high-rated (union)
union ← ∪towns,high
⍝ Result: unique pattern IDs from both sets

⍝ Find Towns patterns that are NOT high-rated (difference)
low_towns ← towns~high
⍝ Result: Towns patterns with 1 asterisk
```

### Statistical Analysis

```apl
⍝ Count patterns in each category
towns_count ← +/(⍳253)≤94
buildings_count ← +/(⍳253)∊95..204
construction_count ← +/(⍳253)≥205
⍝ Results: 94 110 49

⍝ Calculate percentages
total ← 253
towns_pct ← 100×towns_count÷total
⍝ Result: 37.15

⍝ Average connections per pattern
all_connections ← GetTotalConnections¨⍳253
avg_connections ← (+/all_connections)÷≢all_connections
⍝ Result: average connection count
```

### Pattern Sequences

```apl
⍝ Store a sequence
sequence ← 1 2 7 12 3
result ← StoreSequence 1 sequence
⍝ Result: 1 (success)

⍝ Retrieve sequence
seq ← GetPatternSequence 1
⍝ Result: 1 2 7 12 3

⍝ Get patterns from multiple sequences
seqs ← GetPatternSequence¨1 2 3
⍝ Result: nested array of sequences

⍝ Flatten to unique pattern IDs
unique_ids ← ∪∊seqs
⍝ Result: all unique pattern IDs across sequences 1-3
```

## APL Idioms Used

### Common APL Patterns

```apl
⍝ Identity
x ← ⍳10                    ⍝ Iota: generate 1 2 3 4 5 6 7 8 9 10

⍝ Sum
sum ← +/⍳10                ⍝ Sum: 55

⍝ Average
avg ← (+/⍳10)÷10           ⍝ Average: 5.5

⍝ Maximum
max ← ⌈/3 1 4 1 5          ⍝ Maximum: 5

⍝ Minimum
min ← ⌊/3 1 4 1 5          ⍝ Minimum: 1

⍝ Boolean to indices
mask ← 1 0 1 0 1
indices ← mask/⍳5          ⍝ Result: 1 3 5

⍝ Grade (sort)
sorted ← (⍳5)[⍒3 1 4 1 5]  ⍝ Descending: 5 3 1 2 4
sorted ← (⍳5)[⍋3 1 4 1 5]  ⍝ Ascending: 2 4 1 3 5

⍝ Unique
unique ← ∪1 2 2 3 3 3      ⍝ Result: 1 2 3

⍝ Membership
result ← 3∊1 2 3 4         ⍝ Result: 1 (true)

⍝ Tally (count)
count ← ≢1 2 3 4 5         ⍝ Result: 5

⍝ Each (map)
lengths ← ≢¨(1 2)(3 4 5)(6)  ⍝ Result: 2 3 1
```

### Performance Tips

```apl
⍝ GOOD: Array operation (fast)
sum ← +/⍳1000

⍝ BAD: Explicit loop (slow)
sum ← 0
:For i :In ⍳1000
  sum ← sum + i
:EndFor

⍝ GOOD: Boolean indexing (fast)
evens ← (0=2|⍳100)/⍳100

⍝ BAD: Filtering with loop (slow)
evens ← ⍬
:For i :In ⍳100
  →(0≠2|i)/Skip
  evens ,← i
Skip:
:EndFor
```

## Summary

This APL implementation provides:

- **Efficient array-based operations** on all 253 patterns
- **Fast queries** using APL's built-in array functions
- **Domain transformations** for archetypal patterns
- **Relationship navigation** with path finding
- **Statistical analysis** using array operations
- **Idiomatic APL code** that's concise and expressive

The array-oriented nature of APL makes it particularly well-suited for pattern language operations, enabling complex queries and transformations with minimal code.
