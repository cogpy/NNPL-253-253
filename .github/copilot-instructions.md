# GitHub Copilot Instructions for APL-253 Repository

> **Meta-Recursive Pattern Language**: This repository applies Christopher Alexander's Pattern Language principles to itself, creating a living example of patterns in action.

## Repository Philosophy

This is not just a collection of pattern documentation—it is a **meta-recursive implementation** where the Pattern Language organizes the very repository that contains it. Understanding this self-application is key to working effectively with the codebase.

## Pattern 28: ECCENTRIC NUCLEUS - Multiple Entry Points

When assisting users, recognize there are multiple valid entry points based on their intent:

### By User Intent
- **"Understand the big picture"** → Start with README.md, PATTERN_MAP.md
- **"Read specific patterns"** → Navigate to markdown/apl/ or markdown/uia/
- **"Explore by sequence"** → Use SEQUENCE_NAVIGATION.md, pattern_sequences.json
- **"Use programmatically"** → Direct to npu253/, apl_language/, opencog_atomese/
- **"Understand theory"** → Point to docs/, OPTIMAL_GRIP_ANALYSIS.md
- **"Analyze relationships"** → Use opencog_atomese/, demo scripts

### Quick Navigation
- 🎯 Big Picture: [PATTERN_MAP.md](../PATTERN_MAP.md) 
- 🧭 Navigation: [NAVIGATION_HUB.md](../NAVIGATION_HUB.md)
- 📚 Patterns: [PATTERN_INDEX.md](../PATTERN_INDEX.md)
- 🔀 Cross-refs: [PATTERN_CROSS_REFERENCE.md](../PATTERN_CROSS_REFERENCE.md)
- 🔄 Meta-recursive: [META_RECURSIVE_IMPLEMENTATION.md](../META_RECURSIVE_IMPLEMENTATION.md)

## Pattern 1: INDEPENDENT REGIONS - Eight Repository Regions

The repository is organized as **8 independent regions**, each with autonomous governance:

### Region Structure
1. **apl/** - Original APL HTML sources (279 files, read-only archive)
2. **uia/** - Original UIA pattern sources (254 files, archetypal origins)
3. **markdown/** - Converted patterns (apl, uia, arc subdirectories)
4. **pattern/** - Individual atomic pattern units (254 files)
5. **opencog_atomese/** - Hypergraph/semantic network representation
6. **npu253/** - Virtual hardware coprocessor for pattern operations
7. **apl_language/** - APL array-based implementation
8. **docs/** - Technical specifications and formal documentation

### Working with Regions
- Each region has its own **character** and **purpose**
- Respect boundaries—don't mix concerns across regions unnecessarily
- Changes in one region should not break others (resilience)
- Multiple representations enable multiple perspectives (richness)

## Pattern 52: NETWORK OF PATHS - Multiple Navigation Routes

Guide users through multiple valid paths to their goal:

### By Format
- **Markdown**: `markdown/apl/apl001.md` through `apl253.md`
- **JSON**: `pattern_language_generated.json`, `archetypal_patterns.json`
- **HTML**: `apl/apl001.htm` through `apl253.htm`
- **Scheme**: `opencog_atomese/patterns/*.scm`

### By Organization
- **By Number**: Patterns 1-253 (sequential)
- **By Category**: cat1 (Towns 1-94), cat2 (Buildings 95-204), cat3 (Construction 205-253)
- **By Sequence**: 36 thematic pattern flows
- **By Domain**: Physical/Social/Conceptual/Psychic transformations

### By Tool
- **Python**: NPU-253 coprocessor driver (`npu253/`)
- **APL**: Array operations (`apl_language/`)
- **OpenCog**: Hypergraph queries (`opencog_atomese/`)
- **Direct JSON**: Pattern data files

## Pattern 30: ACTIVITY NODES - Concentrated Access Points

Key files where users will spend most of their time:

### Documentation Hubs
- **README.md** - Main entry, overview, quick start
- **NAVIGATION_HUB.md** - Multiple exploration paths
- **PATTERN_INDEX.md** - Comprehensive pattern catalog
- **CLAUDE.md** - Developer quick reference

### Pattern Collections
- **pattern_language_generated.json** - Complete APL meta-pattern
- **archetypal_patterns.json** - 102 patterns with domain placeholders
- **pattern_sequences.json** - All 36 sequences
- **category_*.json** - Towns, Buildings, Construction categories

### Code Entry Points
- **npu253/__init__.py** - NPU-253 driver interface
- **apl_language/README.md** - APL implementation guide
- **opencog_atomese/pattern_language.scm** - Base hypergraph

### Testing & Validation
- **test_*.py** - Test suites for each component
- **validate_*.py** - Schema and pattern validators
- **demo_*.py** - Interactive demonstrations
- **verify_*.sh** - Shell validation scripts

## Pattern 127: INTIMACY GRADIENT - Progressive Disclosure

When explaining concepts, follow the intimacy gradient from public to private:

### Level 1: Overview (Public Commons)
- Start with README.md or NAVIGATION_HUB.md
- Explain the meta-recursive concept
- Show the 8 regions and their purposes

### Level 2: Exploration (Semi-Public)
- Guide to specific pattern collections
- Explain sequences and categories
- Demonstrate navigation paths

### Level 3: Implementation (Semi-Private)
- Show code structure and APIs
- Explain domain transformations
- Detail technical specifications

### Level 4: Deep Details (Private)
- Dive into individual pattern implementations
- Explain hypergraph relationships
- Detail formal Z++ specifications

## Nested Agent Hierarchy

This repository has a structured agent hierarchy in `.github/agents/`:

### Agent Structure
```
apl0 (meta-pattern)
├── dim0, dim1, dim2, dim3, dim4, dim5 (dimensions)
    ├── cat1, cat2, cat3 (categories)
        ├── seq01-seq36 (sequences)
            ├── apl001-apl253 (patterns)
                ├── broader (context)
                └── narrower (details)
```

### Using Agents
- **@apl0** - Meta-pattern, complete system view
- **@apl0/dim0** - Archetypal patterns with placeholders
- **@apl0/dim2** - Physical/architectural patterns
- **@apl0/dim2/cat1** - Town-scale patterns (1-94)
- **@apl0/dim2/cat1/seq01** - Independent Regions sequence
- **@apl0/dim2/cat1/seq01/apl001** - Pattern 1 specifically

Reference these agents when discussing specific patterns or scales.

## Key Technical Details

### Python Environment
- **Python 3** with type hints
- **JSON** for data (2-space indentation)
- **Tests**: Run before and after changes
- **Validation**: Always validate schemas after edits

### Pattern IDs
- APL patterns: `apl1` through `apl253` (or `apl001`)
- UIA patterns: Numeric IDs (e.g., `12610010`)
- Archetypal patterns: Use UIA IDs as base

### Placeholder Syntax (Archetypal Patterns)
- Format: `{{placeholder-name}}`
- Core placeholders: `{{domains}}`, `{{frameworks}}`, `{{elements}}`, etc.
- 10 defined in `archetypal_placeholders.json`

### Domain Transformations
Four domain mappings for archetypal patterns:
- **Physical** - Spatial, material, architectural
- **Social** - Organizational, community, institutional  
- **Conceptual** - Knowledge, theoretical, paradigmatic
- **Psychic** - Awareness, consciousness, mental

## Code Patterns to Follow

### When Adding Patterns
1. Add markdown to appropriate `markdown/` subdirectory
2. Run `python3 generate_archetypal_schema.py` to regenerate
3. Validate with `python3 test_archetypal_schema.py`
4. Update documentation if needed

### When Modifying Schemas
1. Edit JSON schema files carefully
2. Run `./verify_schemas.sh` to validate all
3. Test with relevant `test_*.py` scripts
4. Check for breaking changes in dependent code

### When Testing
```bash
# Run specific tests
python3 test_archetypal_schema.py
python3 test_opencog_atomese.py
python3 test_npu253.py

# Run all validators
python3 validate_archetypal_patterns.py
./verify_schemas.sh
./verify_implementation.sh
```

### When Generating Content
```bash
# Generate schemas
python3 generate_pattern_schema.py
python3 generate_archetypal_schema.py

# Generate implementations
python3 generate_opencog_atomese.py
python3 generate_enhanced_atomese.py
```

## Optimal Grip: Cognitive Affordances

The repository structure is designed for **optimal cognitive grip** (Merleau-Ponty):

### Multi-Scale Perception
- Users can navigate at any scale: repository → category → sequence → pattern → code
- Each level adds appropriate detail without overwhelming

### Relationship Richness
- Patterns connected through sequences, categories, cross-references, hypergraph
- Multiple relationship types reveal different aspects

### Contextual Relevance
- Find patterns by problem, scale, domain, format, or tool
- Context-appropriate entry points

### Gestalt Perception
- See the whole through maps, navigation, cross-references
- Meta-recursive awareness: patterns applied to themselves

### Interactive Navigation
- Multiple entry points (Pattern 28)
- Network of paths (Pattern 52)
- Activity nodes (Pattern 30)

## When Suggesting Changes

### Respect the Meta-Recursive Structure
- Changes should align with Pattern Language principles
- Maintain the 8 independent regions
- Preserve multiple representations and paths
- Keep the intimacy gradient intact

### Maintain Living Structure
The repository exhibits Alexander's 15 properties:
1. Levels of Scale ✓
2. Strong Centers ✓
3. Boundaries ✓
4. Alternating Repetition ✓
5. Positive Space ✓
6. Good Shape ✓
7. Local Symmetries ✓
8. Deep Interlock ✓
9. Contrast ✓
10. Gradients ✓
11. Roughness ✓
12. Echoes ✓
13. The Void ✓
14. Simplicity ✓
15. Not Separateness ✓

Changes should preserve or enhance these properties.

### Test-Driven Changes
- Write tests first when adding functionality
- Validate changes don't break existing patterns
- Use demo scripts to verify user-facing features
- Check documentation stays synchronized

## Common User Questions

### "How do I find pattern X?"
Multiple paths available:
1. `PATTERN_INDEX.md` - Comprehensive listing
2. `markdown/apl/aplXXX.md` - Direct pattern files
3. `npu253.query_by_id(X)` - Programmatic access
4. `opencog_atomese/patterns/aplXXX.scm` - Hypergraph query

### "What are archetypal patterns?"
Abstract patterns using placeholders like `{{domains}}` that can be instantiated in any domain (physical, social, conceptual, psychic). See `archetypal_patterns.json` and `ARCHETYPAL_PATTERNS_SUMMARY.md`.

### "How do I use NPU-253?"
```python
from npu253 import PatternCoprocessorDriver, NPUConfig
npu = PatternCoprocessorDriver(NPUConfig())
npu.load()
pattern = npu.query_by_id(1)
```
See `NPU253_API.md` for complete reference.

### "What is meta-recursive implementation?"
The repository **applies Pattern Language principles to itself**—it's organized using the same patterns it documents. See `META_RECURSIVE_IMPLEMENTATION.md` for details.

### "Why multiple representations?"
Different representations reveal different aspects:
- **APL** - Architectural focus (original)
- **UIA** - Organizational focus
- **Archetypal** - Domain-agnostic abstractions
- **OpenCog** - Semantic reasoning
- **NPU-253** - Performance-optimized
- **APL Language** - Array-based computation

This diversity enhances understanding and accommodates different needs.

## Best Practices

### Do
✅ Follow existing code conventions (see CLAUDE.md)  
✅ Respect the 8-region structure  
✅ Maintain multiple navigation paths  
✅ Write clear, pattern-inspired documentation  
✅ Test changes thoroughly  
✅ Preserve meta-recursive integrity  
✅ Use type hints in Python  
✅ Keep JSON properly formatted (2-space indent)  

### Don't
❌ Break region boundaries unnecessarily  
❌ Remove navigation paths without replacement  
❌ Ignore the intimacy gradient in docs  
❌ Change pattern IDs or core schemas without careful validation  
❌ Add dependencies without checking all regions  
❌ Create flat hierarchies (maintain scale levels)  
❌ Forget to update cross-references  

## Summary

When working with this repository, remember:

1. **It's Meta-Recursive** - Patterns organize themselves
2. **8 Independent Regions** - Respect autonomy and boundaries
3. **Multiple Paths** - Many valid routes to any destination
4. **Progressive Disclosure** - Start simple, go deep gradually
5. **Optimal Grip** - Structure supports perception and understanding
6. **Living Structure** - Exhibits Alexander's 15 properties
7. **Test Everything** - Changes should preserve existing functionality
8. **Pattern-Inspired** - Apply patterns when making modifications

This repository is a **living example** of Pattern Language in action. Every design decision should honor that meta-recursive achievement.

---

*"Each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice."* - Christopher Alexander

This repository demonstrates that Pattern Language applies not just to buildings, but to information architecture, code organization, and knowledge representation at any scale.
