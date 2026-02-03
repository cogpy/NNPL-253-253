# APL Language Implementation

This directory contains the implementation of the Pattern Language using the APL (A Programming Language) array-based programming language.

## Overview

APL is an array-oriented programming language that excels at operations on multi-dimensional data structures. This implementation leverages APL's powerful array operations to efficiently query, transform, and analyze the 253 architectural patterns from Christopher Alexander's "A Pattern Language".

## Features

- **Pattern Representation**: All 253 patterns stored as multi-dimensional arrays
- **Category Organization**: Efficient array-based categorization (Towns, Buildings, Construction)
- **Pattern Sequences**: 36 pattern sequences represented as index arrays
- **Archetypal Patterns**: 102 archetypal patterns with placeholder transformations
- **Query Operations**: Fast array-based pattern queries
- **Domain Transformations**: Apply domain-specific transformations (physical/social/conceptual/individual)
- **Relationship Navigation**: Explore pattern relationships using array indexing

## Files

- `patterns.apl` - Core pattern data structures and operations
- `queries.apl` - Pattern query functions
- `transformations.apl` - Domain transformation operations
- `relationships.apl` - Pattern relationship operations
- `demo.apl` - Demonstration script
- `test.apl` - Test suite

## Usage

### Loading the Module

```apl
)LOAD patterns
```

### Querying Patterns

```apl
⍝ Get pattern by ID
pattern ← GetPatternByID 1

⍝ Get all patterns in Towns category
towns ← GetPatternsByCategory 'Towns'

⍝ Get patterns in sequence 1
seq ← GetPatternSequence 1
```

### Domain Transformations

```apl
⍝ Transform archetypal pattern to social domain
social ← TransformToDomain pattern 'social'

⍝ Apply all domain transformations
all_domains ← ApplyAllDomains pattern
```

### Pattern Relationships

```apl
⍝ Get following patterns
following ← GetFollowingPatterns 1

⍝ Get preceding patterns
preceding ← GetPrecedingPatterns 100
```

## APL Language Basics

APL uses special symbols for operations:

- `⍴` - Shape (dimensions of array)
- `⍳` - Index generator
- `∊` - Member of (set membership)
- `⌿` - Replicate along first axis
- `⍨` - Commute (swap arguments)
- `←` - Assignment
- `⍝` - Comment

## Data Structures

### Pattern Structure

Each pattern is represented as a nested array with the following structure:

```
[pattern_id, name, category, asterisks, context, problem, solution, diagram, connections]
```

### Category Array

Categories are represented as an array mapping pattern IDs to category names:

```
category[pattern_id] = 'Towns' | 'Buildings' | 'Construction'
```

### Sequence Array

Sequences are represented as nested arrays of pattern IDs:

```
sequences[sequence_id] = [pattern_id1, pattern_id2, ...]
```

## Performance

APL's array operations provide excellent performance for pattern queries:

- O(1) lookup by pattern ID
- O(log n) search by name (sorted array)
- O(1) category filtering (boolean indexing)
- O(1) sequence retrieval

## Requirements

This implementation requires an APL interpreter such as:

- Dyalog APL (recommended)
- GNU APL
- NARS2000
- ngn/apl

## Examples

See `demo.apl` for comprehensive examples of all operations.

## Testing

Run the test suite:

```apl
)LOAD test
RunAllTests
```

## License

MIT License - see [LICENSE](../LICENSE) for details.
