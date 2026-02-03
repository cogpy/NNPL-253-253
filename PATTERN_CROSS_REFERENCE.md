# Pattern Cross-Reference: Connecting the Mosaic

> **Pattern 8: MOSAIC OF SUBCULTURES** - Linking diverse pattern representations

## Overview

This repository contains multiple representations of the same underlying pattern language. This cross-reference connects them, showing how patterns manifest across different domains and formats.

## The Three Pattern Collections

### 1. APL (Christopher Alexander's A Pattern Language)
**Location**: `apl/`, `markdown/apl/`  
**Count**: 253 patterns  
**Domain**: Physical (architectural and urban design)  
**Format**: HTML (original), Markdown (converted), JSON (structured)  
**Scale**: Regional → Buildings → Construction

### 2. UIA (Union of International Associations)  
**Location**: `uia/`, `markdown/uia/`  
**Count**: 253 patterns  
**Domain**: Multi-domain (physical, social, conceptual, individual)  
**Format**: HTML (original), Markdown (converted)  
**Scale**: Organizational and conceptual structures

### 3. Archetypal Patterns
**Location**: `archetypal_patterns.json`, `markdown/arc/`  
**Count**: 102 unique archetypal templates  
**Domain**: All domains via transformation  
**Format**: JSON with placeholders, Markdown  
**Scale**: Abstract patterns that can be instantiated in any domain

## Cross-Reference Table

### How Patterns Connect

| APL Pattern | UIA Pattern ID | Archetypal Pattern | Relationship |
|-------------|----------------|-------------------|--------------|
| 1: Independent Regions | 12610010 | 12610010 | Source → Archetypal |
| 2: Distribution of Towns | 12610020 | - | APL only (physical domain specific) |
| 8: Mosaic of Subcultures | 12610080 | 12610080 | Source → Archetypal |
| ... | ... | ... | ... |

### Pattern ID Mapping

#### APL to UIA
APL patterns (1-253) are mapped to UIA patterns through subject correspondence:

- **APL 1** (Independent Regions) ← → **UIA 12610010** (Regional autonomy)
- **APL 8** (Mosaic of Subcultures) ← → **UIA 12610080** (Cultural diversity)
- **APL 42** (Industrial Ribbon) ← → **UIA 12610420** (Work integration)

#### UIA to Archetypal  
102 UIA patterns have been extracted as archetypal templates with domain-agnostic placeholders:

- **UIA 12610010** → **Archetypal 12610010** with `{{domains}}` placeholder
- **UIA 12610080** → **Archetypal 12610080** with `{{subcultures}}` placeholder  
- **UIA 12610420** → **Archetypal 12610420** with `{{activities}}` placeholder

## Domain Transformations

### Physical Domain (APL patterns)
Original Christopher Alexander patterns focused on physical space:
- Buildings and architecture
- Urban planning
- Construction details

**Example**: Pattern 42 "Industrial Ribbon"
```
Physical: Factories and workshops along major transport corridors
```

### Social Domain (UIA transformation)
Organizational and community interpretation:
- Community structures
- Institutional organization
- Social systems

**Example**: Pattern 42 transformed
```
Social: Teams and departments organized along communication channels
```

### Conceptual Domain (UIA transformation)
Knowledge and theoretical structures:
- Ideas and concepts
- Paradigms and frameworks
- Theoretical models

**Example**: Pattern 42 transformed
```
Conceptual: Related concepts organized along logical dependencies
```

### Individual Domain (UIA transformation)
Consciousness and awareness patterns:
- Mental structures
- Awareness states
- Cognitive patterns

**Example**: Pattern 42 transformed
```
Individual: Habitual thoughts organized along emotional pathways
```

## Representation Formats

### By Format

```
Original Sources (HTML)
  ├── apl/*.htm (253 files)
  └── uia/*.htm (253 files)
       ↓
Markdown Conversions
  ├── markdown/apl/*.md (253 files)
  ├── markdown/uia/*.md (253 files)  
  └── markdown/arc/*.md (102 files)
       ↓
Structured Data (JSON)
  ├── pattern_language_generated.json (APL structure)
  ├── archetypal_patterns.json (102 templates)
  ├── category_*.json (by scale)
  └── pattern_sequences.json (36 sequences)
       ↓
Knowledge Representations
  ├── opencog_atomese/*.scm (hypergraph)
  ├── npu253/*.py (virtual hardware)
  └── apl_language/*.apl (array operations)
```

### Access Methods by Representation

| Format | Use Case | Location | Tool |
|--------|----------|----------|------|
| HTML | Original reference | `apl/`, `uia/` | Web browser |
| Markdown | Reading, documentation | `markdown/` | Any editor |
| JSON | Data processing | `*.json` | Python, jq |
| Scheme | AI/reasoning | `opencog_atomese/` | OpenCog |
| Python | Hardware interface | `npu253/` | Python |
| APL | Array operations | `apl_language/` | Dyalog APL |

## Pattern Relationships

### Within APL
Patterns are connected through:
- **Preceding patterns**: Provide context (broader scale)
- **Following patterns**: Add refinement (narrower scale)
- **Sequences**: Group related patterns
- **Categories**: Organize by scale (Towns/Buildings/Construction)

### Across Collections
Connections between APL and UIA:
- **Subject correspondence**: Same underlying pattern, different domains
- **Structural similarity**: Analogous organization
- **Domain transformation**: Physical ↔ Social ↔ Conceptual ↔ Individual

### Through Archetypes
Archetypal patterns bridge domains:
- **Template**: Generic pattern with placeholders
- **Instantiation**: Fill placeholders for specific domain
- **Transformation**: Convert between domains

## Usage Examples

### Example 1: Find Pattern Across All Representations

**Goal**: Understand "Independent Regions" pattern in all forms

```bash
# Read APL version (physical domain)
cat markdown/apl/apl001.md

# Read UIA version (multi-domain)
cat markdown/uia/12610010.md

# Read archetypal template
python3 -c "
import json
data = json.load(open('archetypal_patterns.json'))
pattern = [p for p in data['patterns'] if p['id'] == '12610010'][0]
print(pattern['archetypal_pattern'])
print(pattern['domain_specific_content']['social'])
"

# Query in OpenCog
# (Query pattern relationships)

# Access via NPU253
python3 -c "
from npu253 import PatternCoprocessorDriver, NPUConfig
npu = PatternCoprocessorDriver(NPUConfig())
npu.load()
pattern = npu.query_by_id(1)
print(f'{pattern.name}: {pattern.solution}')
"
```

### Example 2: Transform Pattern Across Domains

**Goal**: See how Pattern 42 "Industrial Ribbon" transforms

```python
import json

with open('archetypal_patterns.json') as f:
    data = json.load(f)

pattern = [p for p in data['patterns'] if p['id'] == '12610420'][0]

# Physical domain (APL original)
print("Physical:", pattern['domain_specific_content']['physical'])

# Social domain transformation
print("Social:", pattern['domain_specific_content']['social'])

# Conceptual domain transformation  
print("Conceptual:", pattern['domain_specific_content']['conceptual'])

# Individual domain transformation
print("Individual:", pattern['domain_specific_content']['individual'])
```

### Example 3: Navigate Pattern Network

**Goal**: Find all patterns related to Pattern 8

```python
# Using pattern sequences
import json

with open('pattern_sequences.json') as f:
    sequences = json.load(f)

# Find sequences containing pattern 8
for seq in sequences['sequences']:
    if 8 in seq['patterns']:
        print(f"Sequence {seq['id']}: {seq['heading']}")
        print(f"  Related patterns: {seq['patterns']}")
        print(f"  Emergence: {seq['emergent_phenomena']}")
```

## Integration Patterns

### Pattern 52: NETWORK OF PATHS
The cross-reference creates a network where every pattern is reachable through multiple paths:

```
Entry Point → Format → Domain → Pattern
     ↓          ↓        ↓        ↓
  By Number  HTML     Physical  APL 1
  By Name    Markdown  Social   UIA
  By Theme   JSON     Conceptual Archetypal
  By Domain  Scheme   Individual    Instance
```

### Pattern 31: PROMENADE  
Create pleasant walks through the pattern space:

1. **Architectural Tour**: APL 1 → 8 → 28 → 52 → 95 → 253
2. **Organizational Tour**: UIA patterns in social domain
3. **Conceptual Tour**: Archetypal patterns in conceptual domain
4. **Cross-domain Tour**: Same pattern across all four domains

### Pattern 106: POSITIVE OUTDOOR SPACE
Each representation creates a "positive space" - well-defined and purposeful:

- **APL**: Physical architectural knowledge
- **UIA**: Multi-domain organizational knowledge
- **Archetypal**: Abstract transformable patterns
- **OpenCog**: Reasoning and inference space
- **NPU253**: High-performance access space
- **APL Language**: Computational transformation space

## Finding Patterns

### By Number
- **APL patterns**: Use pattern number (1-253)
- **UIA patterns**: Use pattern ID (12610010-12612530)
- **Archetypal**: Use source UIA ID

### By Name/Topic
1. Search markdown files: `grep -r "pattern name" markdown/`
2. Search JSON: `jq '.patterns[] | select(.name | contains("keyword"))' pattern_language_generated.json`
3. Use PATTERN_INDEX.md for comprehensive list

### By Domain
- **Physical only**: `apl/` directory
- **All domains**: `archetypal_patterns.json`
- **Social domain**: Filter archetypal patterns with `domain_specific_content.social`

### By Representation
- **For reading**: Markdown in `markdown/`
- **For processing**: JSON files
- **For reasoning**: OpenCog Atomese
- **For performance**: NPU253
- **For computation**: APL language

## Mosaic Properties

### Pattern 8: MOSAIC OF SUBCULTURES Applied

The pattern collections form a mosaic where:
1. **Diversity**: Different formats serve different needs
2. **Coherence**: All represent the same underlying patterns
3. **Autonomy**: Each collection complete in itself
4. **Connection**: Cross-references maintain unity
5. **Accessibility**: Multiple entry points for different users

### Emergent Properties

From the combination of representations:
- **Robustness**: Loss of one format doesn't lose knowledge
- **Flexibility**: Choose appropriate format for task
- **Completeness**: Physical + Social + Conceptual + Individual = Whole
- **Navigability**: Multiple paths to every pattern
- **Comprehensibility**: Different cognitive styles accommodated

## Maintenance

### Keeping Cross-References Current

When adding or modifying patterns:
1. Update JSON schemas
2. Regenerate indexes
3. Check cross-references
4. Validate transformations
5. Test access methods

### Validation Scripts
```bash
# Verify all patterns exist
python3 validate_schema.py
python3 validate_archetypal_patterns.py

# Test access methods
python3 demo_pattern_schema.py
python3 demo_archetypal_schema.py
python3 demo_opencog_atomese.py
python3 demo_npu253.py
```

## Conclusion

This cross-reference implements **Pattern 8: MOSAIC OF SUBCULTURES** at the repository level:
- Multiple pattern collections (subcultures)
- Each with distinct character (APL/UIA/Archetypal)
- Connected through cross-references (paths between subcultures)
- Serving different needs (diverse uses)
- Forming coherent whole (unified pattern language)

The diversity of representations achieves **optimal grip** by providing:
- Physical patterns for spatial understanding
- Social patterns for organizational insight
- Conceptual patterns for theoretical clarity
- Individual patterns for personal growth
- Multiple formats for different cognitive preferences

Navigate between them freely to gain the deepest understanding of the pattern language as a living whole.

---

*"The variety of different cultures which can flourish side by side in a region creates a rich and natural cultural fabric." - Pattern 8*
