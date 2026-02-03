---
name: broader
description: "Broader Patterns for apl151"
---


# BROADER Instructions

These patterns provide context and are typically applied before this pattern:

- apl043
- apl044
- apl083
- apl146
- apl148

## Invocation

### How to Invoke This Agent

Other agents can invoke this agent using the path:
```
@apl0/dim5/cat2/seq21/apl151/broader
```

### When to Invoke This Agent

This context agent should be invoked when:
- Understanding broader context patterns (what comes before)
- Understanding narrower detail patterns (what comes after)
- Navigating the pattern hierarchy
- Exploring pattern relationships and dependencies

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

