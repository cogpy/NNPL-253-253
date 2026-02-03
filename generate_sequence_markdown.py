#!/usr/bin/env python3
"""
Generate markdown files for each of the 36 pattern sequences.
Each sequence file aggregates problem-solution pairs and provides insights into
how the sequence relates to its category and the pattern language as a whole.
"""

import json
import os
import re
from pathlib import Path
from typing import Dict, List, Any


def load_json_file(filepath: str) -> Dict:
    """Load a JSON file and return its contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_pattern_markdown(pattern_num: int) -> Dict[str, str]:
    """Load and parse a pattern markdown file."""
    filepath = f"/home/runner/work/skipl-253/skipl-253/markdown/apl/apl{pattern_num:03d}.md"
    
    if not os.path.exists(filepath):
        return {
            'title': f'Pattern {pattern_num}',
            'problem': 'Pattern details not available.',
            'solution': 'Pattern details not available.'
        }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'^# Pattern: (\d+) - (.+)$', content, re.MULTILINE)
    title = title_match.group(2) if title_match else f'Pattern {pattern_num}'
    
    # Extract problem section
    problem_match = re.search(r'## Problem:\s*\n\s*\*\*(.+?)\*\*', content, re.DOTALL)
    problem = problem_match.group(1).strip() if problem_match else 'Problem not specified.'
    
    # Extract solution section
    solution_match = re.search(r'## Solution:\s*\n\s*\*\*(.+?)\*\*', content, re.DOTALL)
    solution = solution_match.group(1).strip() if solution_match else 'Solution not specified.'
    
    return {
        'number': pattern_num,
        'title': title,
        'problem': problem,
        'solution': solution
    }


def get_category_description(category: str) -> Dict[str, str]:
    """Get description and context for each category."""
    descriptions = {
        'Towns': {
            'scale': 'Regional to neighborhood scale (Patterns 1-94)',
            'focus': 'Large-scale urban planning, regional development, community structure, and public spaces',
            'purpose': 'These patterns establish the fundamental structure of human settlements from regions down to neighborhoods, ensuring balanced distribution of population, preservation of natural systems, and creation of identifiable communities.',
            'role': 'Towns patterns form the foundation of the pattern language, creating the overall framework within which buildings and construction details must fit.'
        },
        'Buildings': {
            'scale': 'Building complex to room scale (Patterns 95-204)',
            'focus': 'Building arrangement, spatial organization, room configuration, and indoor-outdoor transitions',
            'purpose': 'These patterns guide the design of individual buildings and building groups, creating spaces that support human activities, facilitate social interaction, and connect meaningfully with their surroundings.',
            'role': 'Buildings patterns bridge between the large-scale structure established by Towns patterns and the detailed construction specified by Construction patterns.'
        },
        'Construction': {
            'scale': 'Structural system to detail scale (Patterns 205-253)',
            'focus': 'Structural systems, materials, construction methods, and architectural details',
            'purpose': 'These patterns specify the physical construction and material details that bring buildings to life, ensuring structural integrity while creating beauty and human comfort.',
            'role': 'Construction patterns complete the pattern language by providing the detailed specifications needed to actually build the spaces envisioned in Towns and Buildings patterns.'
        }
    }
    return descriptions.get(category, {
        'scale': 'Not specified',
        'focus': 'Not specified',
        'purpose': 'Not specified',
        'role': 'Not specified'
    })


def generate_sequence_markdown(sequence: Dict[str, Any], patterns_data: List[Dict]) -> str:
    """Generate markdown content for a single sequence."""
    seq_id = sequence['id']
    heading = sequence['heading']
    description = sequence['description']
    category = sequence['category']
    pattern_nums = sequence['patterns']
    emergent = sequence['emergent_phenomena']
    
    # Load pattern details
    patterns = [load_pattern_markdown(num) for num in pattern_nums]
    
    # Get category context
    cat_info = get_category_description(category)
    
    # Build markdown content
    md = f"""# Sequence {seq_id}: {heading}

## Metadata

- **Category**: {category}
- **Scale**: {cat_info['scale']}
- **Patterns**: {', '.join([str(n) for n in pattern_nums])}
- **Pattern Count**: {len(pattern_nums)}

## Overview

{description}

## Emergent Phenomena

{emergent}

This emergent property arises from the synergistic interaction of the patterns in this sequence. While each pattern addresses specific problems, their combination creates a higher-order quality that transcends individual pattern effects.

## The Algorithm: Flow and Sequence

"""
    
    # Add the sequence flow
    md += f"This sequence represents a coherent design algorithm that unfolds across {len(patterns)} pattern"
    md += "s" if len(patterns) != 1 else ""
    md += ":\n\n"
    
    for i, pattern in enumerate(patterns, 1):
        md += f"{i}. **Pattern {pattern['number']}: {pattern['title']}**\n"
        md += f"   - Addresses: {pattern['problem'][:200]}{'...' if len(pattern['problem']) > 200 else ''}\n\n"
    
    md += f"""
The sequence flows from {patterns[0]['title'].lower() if patterns else 'start'} to {patterns[-1]['title'].lower() if patterns else 'end'}, with each pattern building upon and refining the previous ones. This progressive refinement ensures that larger structural decisions inform and constrain smaller detailed decisions, maintaining coherence across scales.

## Aggregated Problem-Solution Pairs

"""
    
    # Aggregate problems and solutions
    md += f"### Collective Problem Statement\n\n"
    md += f"This sequence addresses a family of related problems:\n\n"
    
    for i, pattern in enumerate(patterns, 1):
        md += f"{i}. **{pattern['title']}**: {pattern['problem']}\n\n"
    
    md += f"### Integrated Solution Strategy\n\n"
    md += f"The sequence provides an integrated approach through these solutions:\n\n"
    
    for i, pattern in enumerate(patterns, 1):
        md += f"{i}. **{pattern['title']}**: {pattern['solution']}\n\n"
    
    # Add category relationship
    md += f"""
## Relationship to {category} Category

### Category Context

**Focus**: {cat_info['focus']}

**Purpose**: {cat_info['purpose']}

**Role in Pattern Language**: {cat_info['role']}

### Sequence's Role in Category

"""
    
    if category == 'Towns':
        md += f"This sequence contributes to the {category} category by establishing patterns at the {cat_info['scale']} level. "
        if seq_id <= 7:
            md += "As an early sequence in this category, it helps define the fundamental structure and organization of settlements."
        elif seq_id <= 12:
            md += "As a mid-level sequence, it develops specific aspects of urban life and infrastructure."
        else:
            md += "As a later sequence in this category, it addresses the transformation and refinement of community institutions."
    elif category == 'Buildings':
        md += f"This sequence operates at the {cat_info['scale']} level within the {category} category. "
        if seq_id <= 20:
            md += "It focuses on the arrangement and positioning of buildings and their outdoor spaces."
        elif seq_id <= 26:
            md += "It addresses the internal organization and refinement of building spaces."
        else:
            md += "It deals with detailed spatial and structural refinements that complete the building design."
    else:  # Construction
        md += f"This sequence works at the {cat_info['scale']} level within the {category} category. "
        if seq_id <= 31:
            md += "It establishes the structural framework and primary building systems."
        else:
            md += "It specifies the detailed elements and finishes that complete the construction."
    
    md += f"""

The sequence includes {len(patterns)} pattern{"s" if len(patterns) != 1 else ""}, representing {"a focused intervention" if len(patterns) <= 3 else "a moderate-scale transformation" if len(patterns) <= 7 else "a comprehensive design process"} within this scale range.

"""
    
    # Add pattern language integration
    md += f"""
## Integration with Pattern Language

### Horizontal Relationships (Within Category)

This sequence works alongside other {category} sequences to create a complete picture at this scale:

"""
    
    # Describe relationships to other sequences in same category
    if category == 'Towns':
        sequences_in_category = list(range(1, 16))
    elif category == 'Buildings':
        sequences_in_category = list(range(16, 29))
    else:  # Construction
        sequences_in_category = list(range(29, 37))
    
    position = sequences_in_category.index(seq_id) + 1
    total = len(sequences_in_category)
    
    md += f"- **Position**: {position} of {total} sequences in {category} category\n"
    md += f"- **Scope**: {'Foundational' if position <= total/3 else 'Developmental' if position <= 2*total/3 else 'Refinement'} patterns\n"
    md += f"- **Coordination**: Works with other {category} sequences to ensure comprehensive coverage of this scale\n\n"
    
    md += f"""
### Vertical Relationships (Across Categories)

"""
    
    if category == 'Towns':
        md += """This sequence establishes constraints and context for Buildings patterns:
- Sets spatial boundaries and site conditions
- Defines community context and social requirements
- Establishes circulation and access frameworks

The patterns in this sequence must be considered before detailed building design begins, as they establish the essential context within which buildings will exist.
"""
    elif category == 'Buildings':
        md += """This sequence bridges between Towns and Construction:
- **From Towns**: Inherits site conditions, community context, and spatial constraints
- **To Construction**: Provides spatial requirements, structural implications, and material needs

The patterns operate at the critical middle scale where urban context meets physical construction.
"""
    else:  # Construction
        md += """This sequence realizes the intentions established by Towns and Buildings patterns:
- Translates spatial concepts into physical structure
- Specifies materials and construction methods
- Creates the tactile and visual details that inhabitants experience

These patterns complete the pattern language by making abstract spatial ideas into concrete reality.
"""
    
    md += f"""
### Network Effects

The patterns in this sequence don't work in isolation. They create a network of relationships:

1. **Internal Synergy**: Patterns within this sequence reinforce and complete each other
2. **Category Integration**: The sequence contributes to the overall coherence of the {category} category
3. **Cross-Category Bridges**: Patterns connect to patterns in other categories, ensuring consistency across scales
4. **Emergent Properties**: The combination creates qualities that no single pattern could achieve alone

### Usage Guidance

**When to Apply This Sequence**:
"""
    
    # Context-specific guidance
    if category == 'Towns':
        md += f"- During regional planning and urban development\n"
        md += f"- When establishing community structure and character\n"
        md += f"- At the beginning of large-scale design processes\n"
    elif category == 'Buildings':
        md += f"- During building design and site planning\n"
        md += f"- When organizing spaces and circulation\n"
        md += f"- After Towns patterns establish context\n"
    else:  # Construction
        md += f"- During construction documentation and detailing\n"
        md += f"- When specifying materials and methods\n"
        md += f"- After spatial organization is established\n"
    
    md += f"""
**How to Apply**:
1. Review the entire sequence to understand the flow
2. Apply patterns in order, allowing each to inform the next
3. Look for the emergent phenomena to verify successful integration
4. Cross-reference with related sequences in other categories

**Key Success Indicators**:
- The emergent phenomena becomes visible and palpable
- Patterns reinforce rather than contradict each other
- The sequence creates a coherent whole, not just a collection of parts
- Solutions at this scale appropriately constrain and enable solutions at other scales

"""
    
    # Add related sequences
    md += f"""
## Related Sequences

"""
    
    if seq_id > 1 and seq_id < 36:
        md += f"- **Previous Sequence ({seq_id - 1})**: Typically provides broader context or precedes this in design process\n"
        md += f"- **Next Sequence ({seq_id + 1})**: Usually refines or builds upon the foundations laid here\n"
    
    if category == 'Towns' and seq_id == 15:
        md += f"- **Buildings Sequences (16-28)**: Take the urban context established by Towns and develop individual buildings\n"
    elif category == 'Buildings' and seq_id == 16:
        md += f"- **Towns Sequences (1-15)**: Provide the essential context within which these buildings must fit\n"
    elif category == 'Buildings' and seq_id == 28:
        md += f"- **Construction Sequences (29-36)**: Specify how to physically build what Buildings patterns envision\n"
    elif category == 'Construction' and seq_id == 29:
        md += f"- **Buildings Sequences (16-28)**: Define the spatial organization that this sequence must realize structurally\n"
    
    md += f"""
## Pattern Details

For detailed information about each pattern in this sequence:

"""
    
    for pattern in patterns:
        md += f"- [Pattern {pattern['number']}: {pattern['title']}](../apl/apl{pattern['number']:03d}.md)\n"
    
    md += f"""
---

## References

- Alexander, Christopher et al. "A Pattern Language: Towns, Buildings, Construction" (1977)
- Sequence definition from `pattern_sequences.json`
- Individual pattern details from `markdown/apl/` directory

## Navigation

- [Back to Sequence Navigation](../../SEQUENCE_NAVIGATION.md)
- [Pattern Index](../../PATTERN_INDEX.md)
- [Pattern Language Overview](../../README.md)
"""
    
    return md


def main():
    """Main execution function."""
    # Load sequences data
    sequences_file = '/home/runner/work/skipl-253/skipl-253/pattern_sequences.json'
    sequences_data = load_json_file(sequences_file)
    sequences = sequences_data['sequences']
    
    # Create output directory
    output_dir = Path('/home/runner/work/skipl-253/skipl-253/markdown/sequences')
    output_dir.mkdir(exist_ok=True)
    
    print(f"Generating markdown files for {len(sequences)} sequences...")
    
    # Generate markdown for each sequence
    for sequence in sequences:
        seq_id = sequence['id']
        filename = f"seq{seq_id:02d}.md"
        filepath = output_dir / filename
        
        print(f"  Generating {filename}...")
        
        markdown_content = generate_sequence_markdown(sequence, [])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"    ✓ Created {filepath}")
    
    print(f"\n✓ Successfully generated {len(sequences)} sequence markdown files")
    print(f"  Output directory: {output_dir}")


if __name__ == '__main__':
    main()
