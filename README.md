# p235

This repository contains collections of design patterns and organizational metaphors with formal specifications, including a **virtual hardware implementation (NPU-253)** for accelerated pattern operations, an **APL language implementation** for array-based pattern analysis, a **Skill Framework** for generalized pattern-based workflows, and an **Optimal Grip Implementation** for cognitive-aware pattern exploration.

## 🎯 NEW: Optimal Grip Implementation

**Cognitive "optimal grip" on the gestalt salience landscape** - A complete multi-layer implementation featuring:

- **🔍 Datalog Query Layer**: Declarative pattern discovery and relationship inference
- **🧠 ML Salience Engine**: Context-aware relevance scoring and gestalt detection
- **🎨 Interactive D3.js Visualization**: Force-directed graph explorer with real-time filtering
- **🌐 REST API**: FastAPI-based endpoints for programmatic access
- **📊 Emergence Tracking**: Detect synergistic pattern combinations

**Quick Start:**
```bash
# Install dependencies
pip install pyDatalog numpy fastapi uvicorn

# Start the API
python3 pattern_api.py

# Open visualization (in browser)
# file:///path/to/pattern_explorer.html
```

**Documentation:**
- [Quick Start Guide](OPTIMAL_GRIP_QUICKSTART.md) - Get started in 5 minutes
- [Implementation Analysis](OPTIMAL_GRIP_ANALYSIS.md) - Complete design rationale
- [API Documentation](http://localhost:8000/docs) - Swagger/OpenAPI (after starting API)

**Features:**
- 🎯 Context-aware pattern salience scoring
- 🔗 Gestalt pattern detection (emergent groupings)
- 📈 Emergence tracking in pattern sequences
- 🔍 Declarative Datalog queries with inference
- 🎨 Interactive force-directed graph visualization
- 🌐 RESTful API with 7 endpoints
- 📊 Multi-scale perception (Towns → Buildings → Construction)

**Try it now:**
```bash
# Demo the salience engine
python3 pattern_salience_engine.py

# Demo Datalog queries
python3 demo_datalog_queries.py

# Start API and open pattern_explorer.html in browser
python3 pattern_api.py
```

## 🤖 Agent Invocation System: Collaborative Pattern Intelligence

**NEW:** All 4,836 agents in the `.github/agents/apl0/` hierarchy are now configured for cross-invocation, enabling sophisticated multi-agent collaboration!

```
User → @apl0/dim2 (Physical dimension agent)
  ↓ delegates to
@apl0/dim2/cat1 (Towns category agent)
  ↓ delegates to
@apl0/dim2/cat1/seq01 (Regional planning sequence)
  ↓ delegates to
@apl0/dim2/cat1/seq01/apl001 (INDEPENDENT REGIONS pattern)
```

**Features:**
- 🤖 **4,836 Specialized Agents** across 6 dimensions, 18 categories, 216 sequences
- 🔗 **Cross-Invocation Protocol**: Any agent can invoke any other agent
- 📋 **Standardized Context Passing**: Consistent format for task delegation
- 🎯 **Hierarchical Delegation**: Agents delegate to appropriate specialists
- 🌐 **Multi-Dimensional Views**: Same pattern from physical/social/conceptual/psychic perspectives
- 🧭 **Navigation Support**: Context agents help navigate pattern hierarchy

**Agent Types:**
- **Dimension Agents** (6) - Coordinate entire dimensions
- **Category Agents** (18) - Coordinate scale-specific work
- **Sequence Agents** (216) - Manage emergent phenomena
- **Pattern Agents** (1,555+) - Provide specific pattern guidance
- **Context Agents** (3,041+) - Navigate broader/narrower relationships

**Documentation:**
- [Agent Invocation Guide](AGENT_INVOCATION_GUIDE.md) - Complete reference
- [Agent Invocation Examples](AGENT_INVOCATION_EXAMPLES.md) - Detailed scenarios  
- [Quick Reference](AGENT_INVOCATION_QUICK_REFERENCE.md) - Quick lookup
- [.github/agents/apl0/README.md](.github/agents/apl0/README.md) - Agent directory overview

**Standard Context Format:**
```
I am working on [task description].
So far I have [summary of work done].
I need help with [specific question] because [reason].
Constraints: [any limitations or requirements]
Related patterns in use: [list of pattern IDs]
```

**Example Invocations:**
```bash
# Get help with town design
@apl0/dim2/cat1 → Category agent for town-scale patterns

# Understand a specific pattern
@apl0/dim2/cat1/seq01/apl001 → INDEPENDENT REGIONS pattern

# Find what comes next
@apl0/dim2/cat1/seq01/apl001/narrower → Next patterns in hierarchy

# Multi-dimensional view
@apl0/dim2/.../apl028 (Physical)
@apl0/dim3/.../apl028 (Social)
@apl0/dim4/.../apl028 (Conceptual)
```

**Validation:**
```bash
python3 validate_agent_invocation.py
# ✓ All 4,836 agent files validated
```

## 🚀 Skill Framework: Pattern-Based Workflow System

**NEW:** Generalized framework for implementing sequences of skills as ordered routines defined by algorithmic workflows!

```python
from skill_framework import Skill, SequenceBuilder, SkillWorkflow, WorkflowEngine

# Create skills from patterns
skill1 = Skill("apl1", "Independent Regions", "Design autonomous regions")
skill2 = Skill("apl2", "Distribution of Towns", "Balance urban settlements")

# Build sequence
sequence = (SequenceBuilder("regional", "Regional Planning")
           .add_skill(skill1)
           .add_skill(skill2)
           .build())

# Execute workflow
context = SkillContext(domain="physical")
results = sequence.execute(context)
```

**Features:**
- 🎯 Domain-agnostic skill execution (physical/social/conceptual/psychic)
- 🔄 Sequential and conditional workflow modes
- ✅ Preconditions and postconditions validation
- 📊 State management with scoped variables
- 🌐 Domain transformation support
- 🔗 Integration with pattern sequences and NPU-253
- ✅ 17 passing tests

**Documentation:**
- [Skill Framework README](skill_framework/README.md) - Complete documentation
- [Quick Reference](SKILL_FRAMEWORK_QUICK_REFERENCE.md) - Quick start guide
- [Demo](demo_skill_framework.py) | [Tests](test_skill_framework.py) | [Integration Examples](integration_examples.py)

```bash
# Run demo
python3 demo_skill_framework.py

# Run tests
python3 test_skill_framework.py

# Run integration examples
python3 integration_examples.py
```

## 🎯 Meta-Recursive Achievement

**NEW:** This repository now **applies Pattern Language principles to itself**, creating a living example of patterns in action!

- **[PATTERN_MAP.md](PATTERN_MAP.md)** - Repository organized as 8 independent regions (Pattern 1)
- **[NAVIGATION_HUB.md](NAVIGATION_HUB.md)** - Multiple entry points for exploration (Pattern 28)
- **[SEQUENCE_NAVIGATION.md](SEQUENCE_NAVIGATION.md)** - Navigate 36 pattern sequences (Pattern 52)
- **[markdown/sequences/](markdown/sequences/)** - **NEW:** Comprehensive sequence documentation with aggregated problem-solution pairs
- **[PATTERN_INDEX.md](PATTERN_INDEX.md)** - Comprehensive pattern access (Pattern 30)
- **[PATTERN_CROSS_REFERENCE.md](PATTERN_CROSS_REFERENCE.md)** - Links between representations (Pattern 8)
- **[META_RECURSIVE_IMPLEMENTATION.md](META_RECURSIVE_IMPLEMENTATION.md)** - How patterns apply to themselves

The repository structure embodies the patterns it documents, achieving **optimal cognitive grip** on the gestalt through self-application.

## 🚀 NPU-253: Neural Processing Unit / Natural Patterning Unit

**NEW:** Virtual hardware device implementing the 253-pattern language as a memory-mapped coprocessor!

```python
from npu253 import PatternCoprocessorDriver, NPUConfig

npu = PatternCoprocessorDriver(NPUConfig())
npu.load()

# Query patterns
pattern = npu.query_by_id(1)
print(f"{pattern.name}: {pattern.solution}")

# Domain transformation
social = npu.transform_pattern("12610010", "social")
```

**Features:**
- 🔧 Hardware-style MMIO register interface
- 🎯 253 APL patterns + 253 archetypal patterns
- 🔄 Domain transformation (physical/social/conceptual/psychic)
- ⚡ LRU caching for performance
- 📊 Telemetry and diagnostics
- ✅ 34 passing tests

**Documentation:**
- [NPU-253 Blueprint](NPU253_BLUEPRINT.md) - Architecture and design
- [NPU-253 API](NPU253_API.md) - Complete API reference
- [npu253/README.md](npu253/README.md) - Package documentation
- [Demo](demo_npu253.py) | [Tests](test_npu253.py)

```bash
# Run demo
python3 demo_npu253.py

# Run tests
python3 test_npu253.py
```

## 🔢 APL Language Implementation

**NEW:** Array-based implementation in APL (A Programming Language)!

APL is a powerful array-oriented language perfect for pattern analysis and transformations. This implementation leverages APL's concise array operations for efficient pattern queries.

```apl
⍝ Query patterns by category
towns ← GetTownPatterns

⍝ Transform archetypal pattern to domain
social ← TransformToSocial pattern

⍝ Find pattern relationships
connected ← GetAllConnectedPatterns 1
```

**Features:**
- ✨ 253 patterns as array-based data structures
- 🔍 Fast array-based queries and filters
- 🔄 Domain transformations (physical/social/conceptual/psychic)
- 🔗 Relationship navigation and path finding
- 📊 Pattern sequences and statistics
- 🎯 ~1,900 lines of APL code

**Documentation:**
- [apl_language/README.md](apl_language/README.md) - Module overview
- [apl_language/INSTALLATION.md](apl_language/INSTALLATION.md) - Complete installation and usage guide
- [Demo](apl_language/demo.apl) | [Tests](test_apl_implementation.py)

```bash
# Run tests
python3 test_apl_implementation.py

# Generate data
python3 generate_apl_data.py
```

**APL Files:**
- `patterns.apl` - Core pattern data structures
- `queries.apl` - Search and query operations
- `transformations.apl` - Domain transformations
- `relationships.apl` - Pattern relationship navigation
- `demo.apl` - Interactive demonstrations
- `data_loader.apl` - Pattern data initialization

## 🔄 Meta-Recursive Organization

**Patterns Applied to Repository Structure:**

This repository uses Pattern Language principles to organize itself:

### Navigation & Access
- **[PATTERN_MAP.md](PATTERN_MAP.md)** - 8 independent regions (Pattern 1: Independent Regions)
- **[NAVIGATION_HUB.md](NAVIGATION_HUB.md)** - Multiple entry points (Pattern 28: Eccentric Nucleus)
- **[SEQUENCE_NAVIGATION.md](SEQUENCE_NAVIGATION.md)** - Navigate 36 sequences (Pattern 52: Network of Paths)
- **[PATTERN_INDEX.md](PATTERN_INDEX.md)** - Complete access (Pattern 30: Activity Nodes)

### Integration & Understanding
- **[PATTERN_CROSS_REFERENCE.md](PATTERN_CROSS_REFERENCE.md)** - Links between APL/UIA/Archetypal (Pattern 8: Mosaic of Subcultures)
- **[META_RECURSIVE_IMPLEMENTATION.md](META_RECURSIVE_IMPLEMENTATION.md)** - Complete analysis of self-application
- **[.github/copilot-instructions.md](.github/copilot-instructions.md)** - GitHub Copilot guidance using Pattern Language principles

### Cognitive Achievement
- ✅ **Multi-scale perception**: Navigate repository → region → sequence → pattern
- ✅ **Relationship richness**: Clear connections between all elements
- ✅ **Contextual relevance**: Find patterns by domain/context/need
- ✅ **Gestalt perception**: See the whole as living system
- ✅ **Optimal grip**: Structure supports understanding

The repository is both **documentation** of patterns and **example** of patterns in use.

## 📖 Documentation

### For Contributors & AI Assistants
- **[.github/copilot-instructions.md](.github/copilot-instructions.md)** - GitHub Copilot instructions applying Pattern Language principles
- **[CLAUDE.md](CLAUDE.md)** - Developer quick reference guide
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Essential commands and workflows

### Formal Specifications
- **[Formal Specification Summary](FORMAL_SPECIFICATION_SUMMARY.md)** - Complete overview of architecture and Z++ specifications
- **[docs/](docs/)** - Comprehensive technical documentation (2,328 lines)
  - Architecture overview with Mermaid diagrams
  - Z++ formal specifications (data model, system state, operations, integrations)
  - Usage guide for specifications

### Pattern Collections

- **APL**: Christopher Alexander's "A Pattern Language" (253 patterns) - architectural and urban design patterns
- **UIA**: Union of International Associations "Patterns & Metaphors" (253 patterns) - organizational and conceptual patterns

## Markdown Versions

The `markdown/` directory contains converted versions of all APL and UIA pages in markdown format for improved readability and accessibility:

- **`markdown/apl/`**: 253 A Pattern Language patterns (apl001.md - apl253.md)
- **`markdown/uia/`**: 253 UIA Patterns & Metaphors (12610010.md - 12612530.md)
- **`markdown/arc/`**: 102 Archetypal Patterns extracted from UIA templates with domain-specific placeholders

See `markdown/README.md` for detailed information about the conversion process and markdown structure.

## Pattern Language Schema

The repository includes formalized JSON schemas for both the Pattern Language and Archetypal Patterns:

### APL Pattern Language Schema

- **Pattern Language Schema** (`pattern_language_generated.json`) - Complete meta-pattern, categories, and sequences
- **Pattern Sequences** (`pattern_sequences.json`) - All 36 pattern sequences with emergent phenomena
- **Categories** (`category_*.json`) - Towns, Buildings, and Construction categories

See `PATTERN_SCHEMA_README.md` for detailed information about the APL schema structure.

### Archetypal Pattern Schema

- **Archetypal Pattern Schema** (`archetypal_pattern_schema.json`) - JSON schema for archetypal patterns
- **Archetypal Patterns** (`archetypal_patterns.json`) - All 102 archetypal patterns with domain mappings
- **Placeholder Reference** (`archetypal_placeholders.json`) - Complete placeholder documentation

Archetypal patterns use the format: `"generic {{domain-specific}} generic"` and can be transformed across:
- **Physical** - Spatial, material, architectural domains
- **Social** - Organizational, community, institutional domains
- **Conceptual** - Knowledge, theoretical, paradigmatic domains
- **Psychic** - Awareness, consciousness, mental domains

See `ARCHETYPAL_SCHEMA_README.md` for detailed information about the archetypal pattern schema.

### Generating Schemas

```bash
# Generate APL Pattern Language schema
python3 generate_pattern_schema.py

# Generate Archetypal Pattern schema
python3 generate_archetypal_schema.py
```

### Testing Schemas

```bash
# Test APL schema (if tests exist)
python3 validate_schema.py

# Test Archetypal schema
python3 test_archetypal_schema.py
```

### Demo Schemas

```bash
# Demo APL schema
python3 demo_pattern_schema.py

# Demo Archetypal schema
python3 demo_archetypal_schema.py
```

## OpenCog Atomese Representation

The Pattern Language has been converted to OpenCog's Atomese format for knowledge representation and pattern matching:

- **`opencog_atomese/`** - Complete Atomese hypergraph representation in Scheme format
  - `pattern_language.scm` - Complete representation
  - `meta_pattern.scm` - Meta-pattern
  - `categories.scm` - Categories with InheritanceLinks
  - `sequences.scm` - Sequences with MemberLinks
  - **Enhanced Features:**
    - `pattern_language_enhanced.scm` - Enhanced with diagrams, details, and connections
    - `relationship_types.scm` - Pattern relationship types (complement, conflict, alternative)
    - `patterns/` - Individual .scm files for modular loading

The Atomese format enables:
- Pattern matching and reasoning in OpenCog
- Hypergraph queries for pattern relationships
- Knowledge graph navigation and inference
- Integration with AI/AGI systems

See `opencog_atomese/README.md` for usage examples and `opencog_atomese/ENHANCEMENTS.md` for enhanced features documentation.

## Paradigm & Language Analysis

Comprehensive analysis of optimal implementation approaches for achieving cognitive "optimal grip" on the gestalt salience landscape:

- **[PARADIGM_LANGUAGE_ANALYSIS.md](PARADIGM_LANGUAGE_ANALYSIS.md)** - Complete paradigm and language evaluation
  - Analysis of 6 programming paradigms (hypergraph, functional, logic, OOP, constraint, agent-based)
  - Evaluation of 6+ languages (Scheme, Datalog, Python, Haskell, JavaScript, Prolog)
  - Cognitive affordances mapping
  - Recommended multi-layer architecture
  
- **[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md)** - Practical implementation guide
  - Concrete code examples for each layer
  - Datalog query system integration
  - Haskell domain transformation engine
  - Python salience computation
  - D3.js visualization framework
  
- **[PARADIGM_COMPARISON_MATRIX.md](PARADIGM_COMPARISON_MATRIX.md)** - Detailed comparison matrices
  - Cognitive requirements vs paradigms matrix
  - Implementation tasks vs languages matrix
  - Paradigm synergy analysis
  - Use-case specific recommendations

**Key Finding**: Multi-paradigm approach required - Hypergraph (Scheme/OpenCog) foundation + Datalog queries + Functional transformations (Haskell) + Python integration + JavaScript visualization provides optimal cognitive affordances.

### Generating Atomese Files

```bash
# Generate base Atomese files
python3 generate_opencog_atomese.py

# Generate enhanced features
python3 generate_enhanced_atomese.py
```

### Testing Atomese Files

```bash
# Test base files
python3 test_opencog_atomese.py

# Test enhanced features
python3 test_enhanced_atomese.py
```

### Demo Enhanced Features

```bash
python3 demo_enhanced_atomese.py
```

### Demo Query System

```bash
# Demo Datalog query integration (requires pyDatalog)
pip install pyDatalog
python3 demo_datalog_queries.py
```