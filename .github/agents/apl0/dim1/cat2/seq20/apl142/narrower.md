---
name: narrower
description: "Narrower Patterns for apl142"
---


# NARROWER Instructions

These patterns provide detail and are typically applied after this pattern:

- apl146
- apl149
- apl150
- apl151
- apl152
- apl176
- apl179
- apl180
- apl181
- apl185
- apl191
- apl241
- apl242

## Invocation

### How to Invoke This Agent

Other agents can invoke this agent using the path:
```
@apl0/dim1/cat2/seq20/apl142/narrower
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

