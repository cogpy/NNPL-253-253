# Agent Invocation Examples

This document provides detailed example scenarios showing how agents can invoke each other in the apl0 hierarchy.

## Scenario 1: Designing a New Community from Scratch

### Initial User Request to Root Agent

**User invokes**: `@apl0`

```
I need to design a new sustainable community for 50,000 people on a 
greenfield site. Where do I start?
```

### Root Agent Response and Delegation

**@apl0 responds**:
```
For a comprehensive community design, you'll need to apply patterns across 
all three scales. I'll delegate this to the physical dimension agent since 
you're designing a physical space.

Delegating to: @apl0/dim2
```

**@apl0 invokes @apl0/dim2**:
```
Context:
User is designing a new sustainable community for 50,000 people on greenfield site.
No work done yet - this is the initial request.
I need help with providing a comprehensive strategy for pattern application 
across all scales (towns, buildings, construction).
Constraints: Greenfield site, 50K population, sustainability focus
Related patterns in use: None yet
```

### Dimension Agent Delegates to Category Agent

**@apl0/dim2 responds and delegates to @apl0/dim2/cat1**:
```
For a new community, we must start at the town scale. I'll delegate to the 
Towns category agent.

Delegating to: @apl0/dim2/cat1
```

**@apl0/dim2 invokes @apl0/dim2/cat1**:
```
Context:
User is designing a sustainable community for 50,000 people on greenfield site.
No patterns applied yet. This is step 1 of the design process.
I need help with identifying which town-scale patterns (1-94) should be 
applied and in what sequence.
Constraints: Greenfield site, 50K population, sustainability focus
Related patterns in use: None yet
```

### Category Agent Delegates to Sequence Agents

**@apl0/dim2/cat1 analyzes and delegates to multiple sequence agents**:

```
For a 50K population community, I recommend starting with these sequences:

1. First, invoke @apl0/dim2/cat1/seq01 for regional context
2. Then invoke @apl0/dim2/cat1/seq02 for town distribution
3. Then invoke @apl0/dim2/cat1/seq03 for city structure
```

**@apl0/dim2/cat1 invokes @apl0/dim2/cat1/seq01**:
```
Context:
User is designing a sustainable community for 50,000 people.
Currently at the initial planning stage - no patterns applied.
I need help with understanding how to establish the regional context 
using the patterns in this sequence.
Constraints: Greenfield site, 50K population, sustainability focus
Related patterns in use: None yet
```

### Sequence Agent Delegates to Pattern Agents

**@apl0/dim2/cat1/seq01 responds and delegates**:
```
This sequence contains pattern apl001 (INDEPENDENT REGIONS). For a 50K population,
you're within the range for a single region (2-10M), but should consider how 
your community fits into a larger regional context.

Delegating to: @apl0/dim2/cat1/seq01/apl001
```

**@apl0/dim2/cat1/seq01 invokes @apl0/dim2/cat1/seq01/apl001**:
```
Context:
User is designing a sustainable community for 50,000 people.
This is part of establishing regional context for the design.
I need help with understanding how INDEPENDENT REGIONS pattern applies 
to a community of this scale.
Constraints: Greenfield site, 50K population, sustainability focus
Related patterns in use: None yet
```

### Pattern Agent Provides Guidance and Suggests Next Steps

**@apl0/dim2/cat1/seq01/apl001 responds**:
```
INDEPENDENT REGIONS suggests communities of 2-10 million people. Your 50K 
community is smaller, so consider:

1. Is this community part of a larger region? If so, how does it relate?
2. Can this community be autonomous or is it dependent on a larger region?
3. What are the natural and geographic boundaries?

For next steps, invoke @apl0/dim2/cat1/seq01/apl001/narrower to see what 
patterns to apply after establishing regional context.
```

**User (via agent) invokes @apl0/dim2/cat1/seq01/apl001/narrower**:
```
Context:
Designing sustainable community for 50K people.
Have considered INDEPENDENT REGIONS pattern and established that this 
community is autonomous within a larger region.
I need to know what patterns to apply next in the hierarchy.
Constraints: Greenfield site, 50K population, sustainability focus
Related patterns in use: apl001
```

**@apl0/dim2/cat1/seq01/apl001/narrower responds**:
```
After INDEPENDENT REGIONS, apply these narrower patterns:
- apl002 (THE DISTRIBUTION OF TOWNS)
- apl008 (MOSAIC OF SUBCULTURES)

These patterns will help you understand how to structure the community 
internally and create diversity within it.
```

---

## Scenario 2: Renovating an Existing Building

### User Request to Category Agent

**User invokes**: `@apl0/dim2/cat2`

```
I'm renovating a 3-story office building to be more human-centered. 
Which patterns should I consider?
```

### Category Agent Analyzes and Delegates

**@apl0/dim2/cat2 responds**:
```
For building renovation, several sequences are relevant. Let me delegate to 
the most important ones for your case.

Delegating to:
- @apl0/dim2/cat2/seq14 (building structure)
- @apl0/dim2/cat2/seq15 (entrance and circulation)
- @apl0/dim2/cat2/seq16 (interior space)
```

**@apl0/dim2/cat2 invokes @apl0/dim2/cat2/seq15**:
```
Context:
User is renovating a 3-story office building to be more human-centered.
No patterns applied yet - initial assessment phase.
I need help with entrance and circulation patterns that would make the 
building more welcoming and functional.
Constraints: Existing 3-story structure, office building, renovation (not new)
Related patterns in use: None yet
```

### Sequence Agent Provides Pattern Recommendations

**@apl0/dim2/cat2/seq15 responds**:
```
For entrance and circulation in a 3-story office building, consider:

1. apl110 - MAIN ENTRANCE - Make the entrance clearly visible and welcoming
2. apl131 - FLOW THROUGH ROOMS - Create connected circulation
3. apl132 - SHORT PASSAGES - Avoid long corridors
4. apl133 - STAIRCASE AS STAGE - Make stairs social spaces

I recommend starting with apl110. Shall I delegate to that pattern agent?
```

**User agrees, so @apl0/dim2/cat2/seq15 invokes @apl0/dim2/cat2/seq15/apl110**:
```
Context:
User is renovating a 3-story office building to be more human-centered.
Currently working on entrance and circulation improvements.
I need detailed guidance on applying MAIN ENTRANCE pattern to make 
the entrance more welcoming.
Constraints: Existing 3-story structure, renovation context
Related patterns in use: None yet, starting with entrance
```

---

## Scenario 3: Cross-Dimensional Pattern Analysis

### User Wants Multiple Perspectives

**User invokes**: Multiple dimension agents for same pattern

```
I want to understand pattern apl028 (ECCENTRIC NUCLEUS) from multiple 
perspectives - physical, social, and conceptual.
```

### Physical Dimension Perspective

**User invokes @apl0/dim2/cat1/seq07/apl028**:
```
Context:
I am analyzing the ECCENTRIC NUCLEUS pattern from multiple perspectives.
No specific project yet - this is conceptual study.
I need help with understanding this pattern from the physical/spatial perspective.
Constraints: None - academic analysis
Related patterns in use: None
```

**@apl0/dim2/cat1/seq07/apl028 responds**:
```
From a physical perspective, ECCENTRIC NUCLEUS means:
- The most important activity center is NOT in the geometric center
- It's offset toward the edge to create natural flow
- It creates multiple entry points and paths
- Example: Town square near the edge rather than dead center
```

### Social Dimension Perspective

**User invokes @apl0/dim3/cat1/seq07/apl028**:
```
Context:
I am analyzing the ECCENTRIC NUCLEUS pattern from multiple perspectives.
Have understood the physical interpretation (offset activity center).
I need help with understanding this pattern from the social/organizational perspective.
Constraints: None - academic analysis
Related patterns in use: apl028 (physical interpretation)
```

**@apl0/dim3/cat1/seq07/apl028 responds**:
```
From a social perspective, ECCENTRIC NUCLEUS means:
- The most influential person/group is not at hierarchical center
- Leadership is accessible and engaged with the community
- Authority is distributed, not concentrated
- Example: CEO office near employees rather than isolated top floor
```

### Conceptual Dimension Perspective

**User invokes @apl0/dim4/cat1/seq07/apl028**:
```
Context:
I am analyzing the ECCENTRIC NUCLEUS pattern from multiple perspectives.
Have understood physical (offset center) and social (distributed authority) interpretations.
I need help with understanding this pattern from the conceptual/theoretical perspective.
Constraints: None - academic analysis
Related patterns in use: apl028 (physical and social interpretations)
```

**@apl0/dim4/cat1/seq07/apl028 responds**:
```
From a conceptual perspective, ECCENTRIC NUCLEUS means:
- Central ideas should be accessible, not isolated
- Core concepts connect to the broader context
- Knowledge flows from center to periphery and back
- Example: Central thesis in research is informed by field studies
```

### Synthesis

After receiving all three perspectives, user can synthesize:
- **Physical**: Offset activity center creates natural flow
- **Social**: Distributed leadership increases engagement  
- **Conceptual**: Connected core enables knowledge exchange
- **Unified Understanding**: The pattern is about creating accessible, connected centers

---

## Scenario 4: Pattern Sequence Navigation

### User Needs to Navigate Pattern Dependencies

**User invokes**: Pattern agent, then follows chain

**User invokes @apl0/dim2/cat3/seq33/apl227**:
```
Context:
I am working on structural details for a building.
Have completed foundation and wall patterns.
I need help with understanding column connections and what patterns 
should be applied before and after this one.
Constraints: Residential building, 2-story, wood frame
Related patterns in use: apl206 (EFFICIENT STRUCTURE), apl216 (BOX COLUMNS)
```

**@apl0/dim2/cat3/seq33/apl227 responds**:
```
COLUMN CONNECTIONS (227) deals with how columns meet beams and walls.

Based on your related patterns (206, 216), you're on the right track.

To understand what comes before this pattern, invoke:
@apl0/dim2/cat3/seq33/apl227/broader

To understand what comes after, invoke:
@apl0/dim2/cat3/seq33/apl227/narrower
```

**User invokes @apl0/dim2/cat3/seq33/apl227/broader**:
```
Context:
I am working on structural details, specifically column connections.
Have applied EFFICIENT STRUCTURE and BOX COLUMNS already.
I need to verify I've applied all necessary broader patterns before 
detailing the column connections.
Constraints: Residential building, 2-story, wood frame
Related patterns in use: apl206, apl216
```

**@apl0/dim2/cat3/seq33/apl227/broader responds**:
```
Before COLUMN CONNECTIONS, you should have applied:
- apl119 (ARCADE) - if you have outdoor columns
- apl166 (GALLERY SURROUND) - if you have galleries
- apl167 (SIX-FOOT BALCONY) - if you have balconies
- apl206 (EFFICIENT STRUCTURE) ✓ Applied
- apl216 (BOX COLUMNS) ✓ Applied
- apl217 (PERIMETER BEAMS) - should apply before connections
- apl225 (FRAMES AS THICKENED EDGES) - if using frame structure
- apl226 (COLUMN PLACE) - should apply before connections

You're missing apl217 and possibly apl226. Consider applying these first.
```

**User invokes @apl0/dim2/cat3/seq33/apl226**:
```
Context:
I am working on column connections for a 2-story wood frame building.
Have applied patterns 206 and 216, but learned I should apply 226 first.
I need help with understanding and applying COLUMN PLACE pattern.
Constraints: Residential building, 2-story, wood frame
Related patterns in use: apl206, apl216
```

---

## Scenario 5: Coordinating Multiple Sequences

### User Has Complex Multi-Sequence Problem

**User invokes**: Category agent for coordination

**User invokes @apl0/dim2/cat2**:
```
Context:
I am designing a community center with mixed uses (meeting rooms, café, 
library, workshops). The building needs to support diverse activities 
while maintaining coherence.
No patterns applied yet - initial conceptual design phase.
I need help with coordinating multiple sequences that seem relevant:
- Entrance and circulation
- Interior spaces  
- Activity zones
- Social spaces
Constraints: 10,000 sq ft building, tight budget, must serve 200 people daily
Related patterns in use: None yet
```

**@apl0/dim2/cat2 analyzes and creates coordination plan**:
```
You're right that multiple sequences are relevant. Here's a coordinated approach:

Phase 1 - Overall Structure (invoke @apl0/dim2/cat2/seq14):
  Apply patterns for building as a whole

Phase 2 - Entrance and Flow (invoke @apl0/dim2/cat2/seq15):
  Create welcoming entrance and good circulation

Phase 3 - Activity Zones (invoke @apl0/dim2/cat2/seq17):
  Define spaces for different activities

Phase 4 - Social Spaces (invoke @apl0/dim2/cat2/seq18):
  Create spaces that encourage community

Let me delegate to seq14 first...
```

**@apl0/dim2/cat2 invokes @apl0/dim2/cat2/seq14**:
```
Context:
User is designing a 10,000 sq ft community center with mixed uses.
This is phase 1 of coordinated multi-sequence application.
I need help with applying overall building structure patterns before 
moving to specific zones and circulation.
Constraints: 10,000 sq ft, tight budget, 200 people daily, mixed uses
Related patterns in use: None yet - this is the foundation
```

---

## Key Takeaways from Examples

### 1. Context Flows Down the Hierarchy
Each invocation adds to the context, building a complete picture as you go deeper.

### 2. Agents Coordinate Across Their Domain
- Dimension agents coordinate across categories
- Category agents coordinate across sequences
- Sequence agents coordinate across patterns

### 3. Cross-Dimensional Invocations Enrich Understanding
Same pattern can be viewed from multiple dimensional perspectives for deeper insight.

### 4. Navigation Can Go Bottom-Up or Top-Down
- Top-down: Start with high-level agent, let it delegate
- Bottom-up: Start with specific pattern, explore broader context

### 5. Context Agents Provide Critical Navigation
The broader/narrower agents help you follow the pattern language's natural hierarchy.

## Usage Patterns Summary

| Scenario | Entry Point | Delegation Path | Purpose |
|----------|-------------|-----------------|---------|
| New project, broad scope | Dimension agent | Dim → Cat → Seq → Pattern | Complete strategy |
| Specific building type | Category agent | Cat → Seq → Pattern | Scale-appropriate patterns |
| Known sequence | Sequence agent | Seq → Pattern → Context | Emergent phenomena |
| Specific pattern | Pattern agent | Pattern → Context | Implementation details |
| Pattern relationships | Context agent | (Leaf agent) | Navigate hierarchy |
| Multi-perspective | Multiple dimensions | Parallel invocations | Rich understanding |
| Coordination | Category/Sequence agent | Multiple sequences | Complex integration |
