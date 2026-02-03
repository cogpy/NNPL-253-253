---
name: apl0-readme
description: "APL0 Agent Directory Overview"
---

# APL0 Agent Directory

This directory contains 4,836 specialized agents organized in a hierarchical structure for working with Christopher Alexander's Pattern Language.

## Structure

```
apl0/
├── dim0/ dim1/ dim2/ dim3/ dim4/ dim5/    (6 dimensions)
    ├── cat1/ cat2/ cat3/                   (3 categories each)
        ├── seq01/ ... seq36/               (36 sequences each)
            ├── apl001/ ... apl253/         (patterns in each sequence)
                ├── broader.md              (broader context patterns)
                └── narrower.md             (narrower detail patterns)
```

## What This Is

Every `.md` file in this directory is a **specialized agent** that:
- Understands its specific domain (dimension, category, sequence, or pattern)
- Can be invoked by other agents for help
- Knows how to delegate to more specialized subagents
- Follows a standard context-passing protocol

## How to Use

### For End Users

Start with the root agent `apl0.md` or jump directly to the appropriate level:

- **Broad project**: Start with dimension agent (e.g., `dim2.md` for physical design)
- **Specific scale**: Start with category agent (e.g., `dim2/cat1.md` for towns)
- **Known sequence**: Start with sequence agent (e.g., `dim2/cat1/seq01.md`)
- **Specific pattern**: Go directly to pattern (e.g., `dim2/cat1/seq01/apl001.md`)

### For Agents Invoking Other Agents

Use the path format:
- `@apl0/dim2` - Dimension agent
- `@apl0/dim2/cat1` - Category agent  
- `@apl0/dim2/cat1/seq01` - Sequence agent
- `@apl0/dim2/cat1/seq01/apl001` - Pattern agent
- `@apl0/dim2/cat1/seq01/apl001/narrower` - Context agent

Always provide context:
```
I am working on [task].
So far I have [progress].
I need help with [question] because [reason].
Constraints: [limitations]
Related patterns: [pattern IDs]
```

## Documentation

See the repository root for complete documentation:

- **AGENT_INVOCATION_GUIDE.md** - Complete reference
- **AGENT_INVOCATION_EXAMPLES.md** - Detailed scenarios
- **AGENT_INVOCATION_QUICK_REFERENCE.md** - Quick lookup

## Agent Files

Every agent file has:

1. **Frontmatter** - Name and description
2. **Core Content** - Agent-specific information
3. **Invocation Section** - How to invoke this agent
4. **Context Handling** - What context to provide
5. **Delegation Section** - Available subagents (if applicable)

## Validation

All 4,836 agent files are validated to ensure proper formatting.

Run from repository root:
```bash
python3 validate_agent_invocation.py
```

## Statistics

- **6** dimensions (archetypal, template, physical, social, conceptual, interpersonal)
- **18** categories (3 per dimension)
- **216** sequences (36 per dimension, organized by category)
- **1,555+** pattern agents
- **3,041+** context agents (broader/narrower)
- **4,836** total agent files

## Dimensions

- **dim0** - Archetypal: Abstract patterns with domain placeholders
- **dim1** - Template: Generic templates for domain variations
- **dim2** - Physical: Spatial, material, architectural patterns
- **dim3** - Social: Organizational, community, institutional patterns
- **dim4** - Conceptual: Knowledge, theoretical, paradigmatic patterns
- **dim5** - Interpersonal: Awareness, consciousness, mental patterns

## Key Features

✓ **Cross-Invocation**: Any agent can invoke any other agent
✓ **Context Passing**: Standardized format for passing context
✓ **Hierarchical Delegation**: Agents delegate to appropriate subagents
✓ **Multi-Dimensional**: Same patterns from different perspectives
✓ **Navigation Support**: Context agents help navigate hierarchy
✓ **Coordination**: Higher-level agents coordinate lower-level work

## Example Usage

### Simple Invocation
```
User → @apl0/dim2/cat1/seq01/apl001
(Get help with Pattern 001)
```

### Delegation Chain
```
User → @apl0/dim2
  ↓ delegates to
@apl0/dim2/cat1
  ↓ delegates to
@apl0/dim2/cat1/seq01
  ↓ delegates to
@apl0/dim2/cat1/seq01/apl001
```

### Cross-Dimensional
```
User → @apl0/dim2/.../apl028 (Physical view)
User → @apl0/dim3/.../apl028 (Social view)
User → @apl0/dim4/.../apl028 (Conceptual view)
```

## Getting Started

1. Read `../../../AGENT_INVOCATION_GUIDE.md` for complete documentation
2. Review `../../../AGENT_INVOCATION_EXAMPLES.md` for scenarios
3. Use `../../../AGENT_INVOCATION_QUICK_REFERENCE.md` for quick lookup
4. Start with `apl0.md` to understand the overall structure
5. Navigate to the appropriate agent for your needs

## Contributing

When modifying agent files:
- Maintain the standard structure
- Keep frontmatter consistent
- Preserve all three sections (Invocation, Context Handling, Delegation)
- Run validation after changes
- Update documentation if adding new capabilities

## Support

For questions about the agent invocation system, see the documentation files in the repository root or examine the example scenarios.
