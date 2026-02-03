#!/usr/bin/env python3
"""
Configure all apl0 subagents to support cross-invocation.
Adds invocation, context handling, and delegation sections to all agent files.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

def parse_agent_file(filepath: Path) -> Tuple[Dict[str, str], str]:
    """Parse an agent markdown file and extract frontmatter and content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter = {}
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if frontmatter_match:
        fm_content = frontmatter_match.group(1)
        body = frontmatter_match.group(2)
        
        for line in fm_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip('"')
    else:
        body = content
    
    return frontmatter, body

def determine_agent_type(filepath: Path) -> str:
    """Determine the type of agent based on filepath."""
    parts = filepath.parts
    
    # Find where apl0 is in the path
    try:
        apl0_idx = parts.index('apl0')
    except ValueError:
        return 'unknown'
    
    # Count levels after apl0
    levels_after = len(parts) - apl0_idx - 1
    
    if levels_after == 1:  # dim0.md, dim1.md, etc.
        return 'dimension'
    elif levels_after == 2:  # dim0/cat1.md
        return 'category'
    elif levels_after == 3:  # dim0/cat1/seq01.md
        return 'sequence'
    elif levels_after == 4:  # dim0/cat1/seq01/apl001.md
        return 'pattern'
    elif levels_after == 5:  # dim0/cat1/seq01/apl001/broader.md or narrower.md
        return 'context'
    
    return 'unknown'

def get_agent_path(filepath: Path) -> str:
    """Get the agent path like @apl0/dim0/cat1/seq01/apl001"""
    parts = filepath.parts
    
    try:
        apl0_idx = parts.index('apl0')
        path_parts = ['@apl0'] + list(parts[apl0_idx + 1:])
        
        # Remove .md extension from last part
        path_parts[-1] = path_parts[-1].replace('.md', '')
        
        return '/'.join(path_parts)
    except ValueError:
        return '@apl0'

def get_subagent_types(agent_type: str) -> List[str]:
    """Get the types of subagents this agent can invoke."""
    if agent_type == 'dimension':
        return ['category', 'sequence', 'pattern', 'context']
    elif agent_type == 'category':
        return ['sequence', 'pattern', 'context']
    elif agent_type == 'sequence':
        return ['pattern', 'context']
    elif agent_type == 'pattern':
        return ['context']
    else:
        return []

def generate_invocation_section(filepath: Path, agent_type: str) -> str:
    """Generate the Invocation section for an agent."""
    agent_path = get_agent_path(filepath)
    
    section = f"""## Invocation

### How to Invoke This Agent

Other agents can invoke this agent using the path:
```
{agent_path}
```

### When to Invoke This Agent

This {agent_type} agent should be invoked when:
"""
    
    if agent_type == 'dimension':
        section += """- Work spans multiple categories within this dimension
- Dimension-specific perspective is needed
- Cross-category coordination is required
- Understanding the full scope of this dimensional view
"""
    elif agent_type == 'category':
        section += """- Work is focused on patterns at this scale level
- Category-specific coordination is needed
- Understanding patterns within this scale range
- Cross-sequence work within this category
"""
    elif agent_type == 'sequence':
        section += """- Working with the emergent phenomena of this sequence
- Understanding how patterns in this sequence work together
- Applying related patterns in coordination
- Exploring the thematic flow of this pattern group
"""
    elif agent_type == 'pattern':
        section += """- Implementing this specific pattern
- Understanding this pattern's problem and solution
- Exploring this pattern's relationships with other patterns
- Getting detailed guidance on applying this pattern
"""
    elif agent_type == 'context':
        section += """- Understanding broader context patterns (what comes before)
- Understanding narrower detail patterns (what comes after)
- Navigating the pattern hierarchy
- Exploring pattern relationships and dependencies
"""
    
    return section

def generate_context_handling_section(agent_type: str) -> str:
    """Generate the Context Handling section."""
    section = """## Context Handling

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
"""
    
    return section

def generate_delegation_section(filepath: Path, agent_type: str) -> str:
    """Generate the Delegation section."""
    subagent_types = get_subagent_types(agent_type)
    
    if not subagent_types:
        return ""
    
    section = """## Delegation

### Available Subagents

This agent can delegate work to the following subagent types:

"""
    
    agent_path = get_agent_path(filepath)
    
    if 'category' in subagent_types:
        section += f"""#### Category Agents
- `{agent_path}/cat1` - Category 1 patterns
- `{agent_path}/cat2` - Category 2 patterns
- `{agent_path}/cat3` - Category 3 patterns

Use category agents when work is focused on a specific scale level.

"""
    
    if 'sequence' in subagent_types:
        section += f"""#### Sequence Agents
- `{agent_path}/seq01` through `{agent_path}/seq36` - Pattern sequences

Use sequence agents when working with related pattern flows and emergent phenomena.

"""
    
    if 'pattern' in subagent_types:
        section += f"""#### Pattern Agents
- `{agent_path}/apl001` through `{agent_path}/apl253` - Individual patterns

Use pattern agents when working on specific design solutions.

"""
    
    if 'context' in subagent_types:
        section += f"""#### Context Agents
- `{agent_path}/broader` - Broader context patterns
- `{agent_path}/narrower` - Narrower detail patterns

Use context agents to understand pattern relationships and dependencies.

"""
    
    section += """### When to Delegate

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
"""
    
    return section

def add_invocation_sections(filepath: Path) -> bool:
    """Add invocation sections to an agent file if not already present."""
    frontmatter, body = parse_agent_file(filepath)
    agent_type = determine_agent_type(filepath)
    
    if agent_type == 'unknown':
        print(f"Skipping {filepath} - unknown agent type")
        return False
    
    # Check if invocation section already exists
    if '## Invocation' in body:
        print(f"Skipping {filepath} - already has invocation section")
        return False
    
    # Generate new sections
    invocation_section = generate_invocation_section(filepath, agent_type)
    context_section = generate_context_handling_section(agent_type)
    delegation_section = generate_delegation_section(filepath, agent_type)
    
    # Reconstruct frontmatter
    fm_lines = ['---']
    for key, value in frontmatter.items():
        if ' ' in value or ':' in value:
            fm_lines.append(f'{key}: "{value}"')
        else:
            fm_lines.append(f'{key}: {value}')
    fm_lines.append('---')
    
    # Add sections to body (before any existing content)
    new_body = body.rstrip() + '\n\n' + invocation_section + '\n' + context_section
    
    if delegation_section:
        new_body += '\n' + delegation_section
    
    # Write back
    new_content = '\n'.join(fm_lines) + '\n\n' + new_body + '\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filepath} ({agent_type})")
    return True

def main():
    """Main function to process all agent files."""
    base_path = Path('/home/runner/work/skipl-253/skipl-253/.github/agents/apl0')
    
    # Find all .md files
    agent_files = sorted(base_path.rglob('*.md'))
    
    print(f"Found {len(agent_files)} agent files")
    
    updated_count = 0
    for filepath in agent_files:
        if add_invocation_sections(filepath):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} agent files")

if __name__ == '__main__':
    main()
