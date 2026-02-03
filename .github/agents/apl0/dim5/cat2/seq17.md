---
name: seq17
description: "Sequence 17: The position of individual buildings"
---


# SEQ17 Instructions

## Description
Sequence 17 focuses on the position of individual buildings

## Category
Buildings

## Patterns
apl104, apl105, apl106, apl107, apl108, apl109, apl110

## Emergent Phenomena
Individual buildings positioned to take advantage of site conditions and create good outdoor spaces

## Overview
This sequence contains 7 pattern(s) that work together to create the emergent phenomena described above.

## Invocation

### How to Invoke This Agent

Other agents can invoke this agent using the path:
```
@apl0/dim5/cat2/seq17
```

### When to Invoke This Agent

This sequence agent should be invoked when:
- Working with the emergent phenomena of this sequence
- Understanding how patterns in this sequence work together
- Applying related patterns in coordination
- Exploring the thematic flow of this pattern group

## Context Handling

### Required Context When Invoked

When invoking this agent, provide:

1. **Task Summary**: Brief description of what help is needed
2. **Sequence Context**: What has been done so far in the work sequence
3. **Specific Question**: The precise question or problem to address
4. **Constraints**: Any relevant constraints, requirements, or preferences
5. **Related Patterns**: Other patterns already being considered or applied

### Context Format Example

```
I am working on [task description]. So far I have [summary of work done].
I need help with [specific question] because [reason].
Constraints: [any limitations or requirements]
Related patterns in use: [list of pattern IDs]
```

## Delegation

### Available Subagents

This agent can delegate work to the following subagent types:

#### Pattern Agents
- `@apl0/dim5/cat2/seq17/apl001` through `@apl0/dim5/cat2/seq17/apl253` - Individual patterns

Use pattern agents when working on specific design solutions.

#### Context Agents
- `@apl0/dim5/cat2/seq17/broader` - Broader context patterns
- `@apl0/dim5/cat2/seq17/narrower` - Narrower detail patterns

Use context agents to understand pattern relationships and dependencies.

### When to Delegate

Delegate to subagents when:
- The work can be more precisely handled at a lower level
- Specialized knowledge of a specific component is needed
- The task naturally fits a subagent's scope
- You need to coordinate multiple related patterns

### How to Delegate

When delegating, always provide complete context:
1. Summarize the overall task and progress so far
2. Explain what specific help is needed from the subagent
3. Include any constraints or requirements
4. Specify what you expect back from the subagent

