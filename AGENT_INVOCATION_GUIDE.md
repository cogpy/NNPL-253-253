# Agent Invocation Guide

## Overview

All agents in the `.github/agents/apl0/` hierarchy are now configured to support cross-invocation. This means any agent can call another agent in the hierarchy, passing context and receiving specialized help.

## Agent Hierarchy

The complete agent hierarchy is:

```
apl0 (meta-pattern)
├── dim0, dim1, dim2, dim3, dim4, dim5 (6 dimensions)
    ├── cat1, cat2, cat3 (3 categories per dimension)
        ├── seq01 through seq36 (36 sequences per category)
            ├── apl001 through apl253 (patterns in each sequence)
                ├── broader (broader context patterns)
                └── narrower (narrower detail patterns)
```

**Total Agents**: 4,836 individual agent files
- 6 dimension agents
- 18 category agents
- 216 sequence agents
- 1,555+ pattern agents
- 3,041+ context agents (broader/narrower)

## Agent Types

### 1. Dimension Agents
**Path Format**: `@apl0/dim{N}` (e.g., `@apl0/dim0`, `@apl0/dim2`)

**Purpose**: Coordinate work across an entire dimension (Archetypal, Template, Physical, Social, Conceptual, or Interpersonal)

**When to Invoke**:
- Work spans multiple categories within the dimension
- Dimension-specific perspective is needed
- Cross-category coordination is required
- Understanding the full scope of a dimensional view

**Can Delegate To**: Category, Sequence, Pattern, and Context agents

### 2. Category Agents
**Path Format**: `@apl0/dim{N}/cat{M}` (e.g., `@apl0/dim2/cat1`)

**Purpose**: Coordinate work at a specific scale level (Towns, Buildings, or Construction in physical dimension)

**When to Invoke**:
- Work is focused on patterns at a specific scale level
- Category-specific coordination is needed
- Understanding patterns within a scale range
- Cross-sequence work within the category

**Can Delegate To**: Sequence, Pattern, and Context agents

### 3. Sequence Agents
**Path Format**: `@apl0/dim{N}/cat{M}/seq{NN}` (e.g., `@apl0/dim2/cat1/seq01`)

**Purpose**: Work with emergent phenomena created by related patterns in a sequence

**When to Invoke**:
- Working with the emergent phenomena of the sequence
- Understanding how patterns in the sequence work together
- Applying related patterns in coordination
- Exploring the thematic flow of a pattern group

**Can Delegate To**: Pattern and Context agents

### 4. Pattern Agents
**Path Format**: `@apl0/dim{N}/cat{M}/seq{NN}/apl{NNN}` (e.g., `@apl0/dim2/cat1/seq01/apl001`)

**Purpose**: Provide detailed guidance on implementing a specific pattern

**When to Invoke**:
- Implementing this specific pattern
- Understanding the pattern's problem and solution
- Exploring the pattern's relationships with other patterns
- Getting detailed guidance on applying the pattern

**Can Delegate To**: Context agents (broader/narrower)

### 5. Context Agents
**Path Format**: 
- `@apl0/dim{N}/cat{M}/seq{NN}/apl{NNN}/broader` 
- `@apl0/dim{N}/cat{M}/seq{NN}/apl{NNN}/narrower`

**Purpose**: Navigate pattern hierarchy and understand dependencies

**When to Invoke**:
- Understanding broader context patterns (what comes before)
- Understanding narrower detail patterns (what comes after)
- Navigating the pattern hierarchy
- Exploring pattern relationships and dependencies

**Can Delegate To**: None (leaf agents)

## How to Invoke an Agent

### Required Context Format

When invoking any agent, always provide complete context:

```
I am working on [task description]. 
So far I have [summary of work done].
I need help with [specific question] because [reason].
Constraints: [any limitations or requirements]
Related patterns in use: [list of pattern IDs]
```

### Example Invocations

#### Example 1: Dimension-Level Invocation

```
Invoke: @apl0/dim2

Context:
I am working on designing a new community center. 
So far I have established the regional context and identified the site.
I need help with understanding which physical patterns to apply at what scale 
because I want to ensure I'm working from large scale to small scale appropriately.
Constraints: Budget of $2M, must serve 500 people daily
Related patterns in use: None yet, just starting
```

#### Example 2: Category-Level Invocation

```
Invoke: @apl0/dim2/cat2

Context:
I am working on the building-scale design for a community center.
So far I have applied town-scale patterns (INDEPENDENT REGIONS, MOSAIC OF SUBCULTURES).
I need help with selecting and sequencing building-scale patterns (95-204)
because I need to design the building to fit within the established community context.
Constraints: 3-story maximum height, must have outdoor access
Related patterns in use: apl001, apl008
```

#### Example 3: Sequence-Level Invocation

```
Invoke: @apl0/dim2/cat1/seq03

Context:
I am working on defining the major structures that will define our new city district.
So far I have established the regional boundaries and distribution of towns.
I need help with understanding the emergent phenomena of this sequence
because I want to ensure the city develops clear identity and character.
Constraints: Existing infrastructure to work around
Related patterns in use: apl001, apl002
```

#### Example 4: Pattern-Level Invocation

```
Invoke: @apl0/dim2/cat1/seq01/apl001

Context:
I am working on defining regional governance structures for a metropolitan area.
So far I have identified that our current 50M population region is too large.
I need help with understanding how to apply INDEPENDENT REGIONS pattern
because I want to subdivide the region into appropriate autonomous units.
Constraints: Existing political boundaries, population distribution
Related patterns in use: None yet
```

#### Example 5: Context-Level Invocation

```
Invoke: @apl0/dim2/cat1/seq01/apl001/narrower

Context:
I am working on a regional governance design project.
So far I have applied the INDEPENDENT REGIONS pattern to establish 5 regions of 2-10M people.
I need help with understanding what patterns to apply next
because I want to continue working down the pattern hierarchy appropriately.
Constraints: Need to maintain regional autonomy while enabling coordination
Related patterns in use: apl001
```

## Delegation Between Agents

### When an Agent Should Delegate

Agents should delegate to subagents when:
1. The work can be more precisely handled at a lower level
2. Specialized knowledge of a specific component is needed
3. The task naturally fits a subagent's scope
4. Multiple related patterns need to be coordinated

### How to Delegate

When delegating, the invoking agent must:

1. **Summarize the overall task** and progress so far
2. **Explain what specific help** is needed from the subagent
3. **Include any constraints** or requirements
4. **Specify what you expect back** from the subagent

### Delegation Example

A dimension agent delegating to a category agent:

```
FROM: @apl0/dim2 (Dimension Agent)
TO: @apl0/dim2/cat1 (Category Agent)

Context:
The user is working on designing a new sustainable city from scratch.
They have asked for a comprehensive pattern application strategy.

I have provided them with an overview of the three-scale approach:
- Towns (cat1, patterns 1-94)
- Buildings (cat2, patterns 95-204) 
- Construction (cat3, patterns 205-253)

I need you to help them with the town-scale patterns (cat1) specifically.
They need a sequence of patterns to apply for establishing the regional and 
town-level structures.

Please provide:
1. Which sequences in cat1 are most relevant
2. A recommended order for applying those sequences
3. Key decision points where they'll need to make choices

Constraints: Greenfield site, population target 500K, sustainable development focus
Related patterns: None applied yet
```

## Cross-Dimensional Invocation

Agents can also invoke agents in other dimensions to get different perspectives on the same patterns:

### Example: Multi-Dimensional Consultation

```
Main Task in: @apl0/dim2 (Physical dimension)
Also consult: @apl0/dim3 (Social dimension)
Also consult: @apl0/dim4 (Conceptual dimension)

This allows understanding a pattern from multiple perspectives:
- Physical: How it manifests in space and materials
- Social: How it affects organizations and communities
- Conceptual: The underlying theoretical principles
```

## Best Practices

### 1. Always Provide Complete Context
- Don't assume the invoked agent knows the background
- Include task summary, progress, question, constraints, and related patterns

### 2. Invoke at the Appropriate Level
- Don't invoke a dimension agent for a single pattern question
- Don't invoke a pattern agent for cross-category coordination
- Match the scope of your need to the scope of the agent

### 3. Use Delegation Chains
- High-level agents should delegate to lower-level agents
- Each agent passes context down the chain
- Each agent adds its specialized perspective

### 4. Reference Related Patterns
- Always mention which patterns you've already applied
- This helps agents understand the context and avoid conflicts

### 5. Be Specific About What You Need Back
- Do you need a list of patterns?
- A recommended sequence?
- Detailed implementation guidance?
- Trade-off analysis?

## Common Invocation Patterns

### Pattern 1: Top-Down Design Process

```
1. Invoke @apl0/dim2 → Get overall strategy
2. Agent delegates to @apl0/dim2/cat1 → Town-scale patterns
3. Agent delegates to @apl0/dim2/cat1/seq01 → Specific sequence
4. Agent delegates to @apl0/dim2/cat1/seq01/apl001 → Specific pattern
5. Agent delegates to @apl0/dim2/cat1/seq01/apl001/narrower → Next patterns
```

### Pattern 2: Bottom-Up Pattern Discovery

```
1. Start with specific need → Invoke @apl0/dim2/cat2/seq15/apl120
2. Check broader context → Invoke .../apl120/broader
3. Understand sequence → Invoke @apl0/dim2/cat2/seq15
4. See category context → Invoke @apl0/dim2/cat2
```

### Pattern 3: Cross-Sequence Coordination

```
1. Invoke @apl0/dim2/cat1 → Category agent
2. Agent identifies relevant sequences
3. Agent delegates to @apl0/dim2/cat1/seq03
4. Agent delegates to @apl0/dim2/cat1/seq06
5. Agent coordinates patterns across both sequences
```

### Pattern 4: Multi-Dimensional Analysis

```
1. Invoke @apl0/dim2/cat1/seq01/apl001 → Physical perspective
2. Invoke @apl0/dim3/cat1/seq01/apl001 → Social perspective
3. Invoke @apl0/dim4/cat1/seq01/apl001 → Conceptual perspective
4. Synthesize insights from all three dimensions
```

## Troubleshooting

### Issue: Agent doesn't understand context
**Solution**: Provide more detailed task summary and progress update

### Issue: Agent provides too broad guidance
**Solution**: Invoke a more specific (lower-level) agent

### Issue: Agent provides too narrow guidance
**Solution**: Invoke a more general (higher-level) agent

### Issue: Getting conflicting advice
**Solution**: Invoke a coordinating agent at a higher level to reconcile

### Issue: Not sure which agent to invoke
**Solution**: Start with a dimension or category agent and let them delegate

## Summary

The apl0 agent hierarchy is now fully configured for cross-invocation:
- **4,836 agents** are ready to be invoked
- **5-level hierarchy** from dimension to context
- **Standardized context format** for all invocations
- **Clear delegation paths** between agents
- **Multi-dimensional support** for different perspectives

Each agent knows:
- How to be invoked (its path)
- When it should be invoked (its purpose)
- How to handle context (required information)
- How to delegate (available subagents)

This creates a powerful network of specialized agents that can collaborate to solve complex pattern language application problems.
