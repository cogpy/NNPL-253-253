# Agent Invocation Quick Reference

## Agent Hierarchy at a Glance

```
apl0 (4,836 agents total)
├── 6 dimensions (dim0-dim5)
│   ├── 3 categories each (cat1-cat3) = 18 total
│   │   ├── 36 sequences each (seq01-seq36) = 216 total  
│   │   │   ├── patterns (apl001-apl253) = 1,555+ total
│   │   │   │   ├── broader = context agent
│   │   │   │   └── narrower = context agent
```

## Agent Path Format

| Agent Type | Path Format | Example |
|-----------|-------------|---------|
| Root | `@apl0` | `@apl0` |
| Dimension | `@apl0/dim{N}` | `@apl0/dim2` |
| Category | `@apl0/dim{N}/cat{M}` | `@apl0/dim2/cat1` |
| Sequence | `@apl0/dim{N}/cat{M}/seq{NN}` | `@apl0/dim2/cat1/seq01` |
| Pattern | `@apl0/dim{N}/cat{M}/seq{NN}/apl{NNN}` | `@apl0/dim2/cat1/seq01/apl001` |
| Context | `@apl0/.../apl{NNN}/broader` or `.../narrower` | `@apl0/dim2/cat1/seq01/apl001/narrower` |

## Standard Context Format

```
I am working on [task description].
So far I have [summary of work done].
I need help with [specific question] because [reason].
Constraints: [any limitations or requirements]
Related patterns in use: [list of pattern IDs]
```

## Dimensions

| Code | Name | Focus |
|------|------|-------|
| dim0 | Archetypal | Abstract patterns with placeholders |
| dim1 | Template | Generic template patterns |
| dim2 | Physical | Spatial, material, architectural |
| dim3 | Social | Organizational, community, institutional |
| dim4 | Conceptual | Knowledge, theoretical, paradigmatic |
| dim5 | Interpersonal | Awareness, consciousness, mental |

## Categories (Physical Dimension)

| Code | Name | Pattern Range | Scale |
|------|------|---------------|-------|
| cat1 | Towns | 1-94 | Large-scale |
| cat2 | Buildings | 95-204 | Medium-scale |
| cat3 | Construction | 205-253 | Small-scale |

## When to Invoke Each Type

### Dimension Agent
- Work spans multiple categories
- Need dimension-specific perspective
- Cross-category coordination required

### Category Agent  
- Work focused on specific scale
- Category-specific coordination needed
- Cross-sequence work within category

### Sequence Agent
- Working with emergent phenomena
- Understanding pattern synergies
- Applying related patterns together

### Pattern Agent
- Implementing specific pattern
- Understanding problem/solution
- Exploring pattern relationships

### Context Agent
- Navigating pattern hierarchy
- Understanding dependencies
- Finding next/previous patterns

## Delegation Chain Examples

### Top-Down (Full Design)
```
@apl0 
  → @apl0/dim2
    → @apl0/dim2/cat1
      → @apl0/dim2/cat1/seq01
        → @apl0/dim2/cat1/seq01/apl001
          → @apl0/dim2/cat1/seq01/apl001/narrower
```

### Bottom-Up (Pattern Discovery)
```
@apl0/dim2/cat2/seq15/apl120
  → @apl0/dim2/cat2/seq15/apl120/broader (what comes before?)
    → @apl0/dim2/cat2/seq15 (sequence context)
      → @apl0/dim2/cat2 (category context)
```

### Cross-Dimensional
```
@apl0/dim2/cat1/seq01/apl001 (Physical)
@apl0/dim3/cat1/seq01/apl001 (Social)
@apl0/dim4/cat1/seq01/apl001 (Conceptual)
```

## Common Invocation Patterns

| Need | Invoke | Then |
|------|--------|------|
| Start new project | Dimension agent | Let it delegate down |
| Renovate building | Category agent (cat2) | Follow sequence recommendations |
| Understand pattern | Pattern agent | Check broader/narrower |
| Find next pattern | Context agent (narrower) | Get list of following patterns |
| Find prerequisites | Context agent (broader) | Get list of prerequisite patterns |
| Multi-perspective | Multiple dimension agents | Compare interpretations |
| Coordinate sequences | Category agent | Get coordination strategy |

## Agent Capabilities

| Agent Type | Can Delegate To | Leaf Agent? |
|-----------|-----------------|-------------|
| Dimension | Category, Sequence, Pattern, Context | No |
| Category | Sequence, Pattern, Context | No |
| Sequence | Pattern, Context | No |
| Pattern | Context | No |
| Context | None | Yes |

## Validation

Run validation script:
```bash
python3 validate_agent_invocation.py
```

Expected result: All 4,836 files validated ✓

## Documentation Files

| File | Purpose |
|------|---------|
| `AGENT_INVOCATION_GUIDE.md` | Complete reference guide |
| `AGENT_INVOCATION_EXAMPLES.md` | Detailed scenarios and examples |
| `AGENT_INVOCATION_QUICK_REFERENCE.md` | This file - quick lookup |
| `configure_agent_invocation.py` | Script that configured all agents |
| `validate_agent_invocation.py` | Validation script |

## Statistics

- **Total Agents**: 4,836
- **Updated**: 4,683 agents (some already had sections)
- **Validation**: 4,836/4,836 passing ✓
- **Lines Added**: ~250,000+ lines of invocation sections
- **Dimensions**: 6
- **Categories**: 18 (3 per dimension)
- **Sequences**: 216 (36 per dimension)
- **Patterns**: 1,555+
- **Context Agents**: 3,041+

## Remember

✓ Always provide complete context when invoking
✓ Match agent level to scope of need  
✓ Follow delegation chains for complex tasks
✓ Use context agents to navigate hierarchy
✓ Consider cross-dimensional perspectives
✓ Coordinate sequences through category agents
✓ Start broad, delegate down as needed

## Quick Examples

### Example 1: "I need to design a new town"
```
Invoke: @apl0/dim2/cat1
Context: New town design, 50K people, greenfield site
```

### Example 2: "How do I apply pattern 120?"
```
Invoke: @apl0/dim2/cat2/seq15/apl120
Context: Building renovation, need implementation details
```

### Example 3: "What comes after pattern 001?"
```
Invoke: @apl0/dim2/cat1/seq01/apl001/narrower
Context: Applied INDEPENDENT REGIONS, need next steps
```

### Example 4: "Multi-perspective on pattern 028"
```
Invoke: @apl0/dim2/cat1/seq07/apl028 (Physical)
Invoke: @apl0/dim3/cat1/seq07/apl028 (Social)
Invoke: @apl0/dim4/cat1/seq07/apl028 (Conceptual)
Context: Academic analysis, want all perspectives
```

### Example 5: "Coordinate multiple sequences"
```
Invoke: @apl0/dim2/cat2
Context: Mixed-use building, need to coordinate entrance, 
         interior, and social space sequences
```
