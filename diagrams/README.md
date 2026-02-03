# Pattern Language Diagrams

This directory contains Mermaid (`.mmd`) diagrams visualizing the Pattern Language architecture and relationships.

## Diagrams Overview

| Diagram | Description |
|---------|-------------|
| `pattern-language-hierarchy.mmd` | Overall hierarchy showing the three main categories (Towns, Buildings, Construction) |
| `pattern-sequences.mmd` | The 36 pattern sequences and their flow from Towns through Construction |
| `domain-transformations.mmd` | How archetypal patterns transform across four domains (Physical, Social, Conceptual, Individual) |
| `architecture-layers.mmd` | System architecture showing Presentation, Integration, Processing, and Foundation layers |
| `pattern-relationships.mmd` | Types of relationships between patterns (hierarchy, sequence, dependency, emergence) |
| `placeholder-system.mmd` | The 10 core placeholders and how they map to domain-specific terms |
| `data-flow.mmd` | Data pipeline from source files through generators to output formats |
| `cognitive-affordances.mmd` | Mind map of cognitive affordances for "optimal grip" on pattern language |

## Viewing Diagrams

### GitHub
GitHub renders Mermaid diagrams natively in markdown files. Wrap the content in:
```markdown
```mermaid
<diagram content>
```
```

### VS Code
Install the "Markdown Preview Mermaid Support" extension.

### Mermaid Live Editor
Paste diagram content into: https://mermaid.live/

### Command Line
Use `mmdc` (Mermaid CLI) to generate images:
```bash
npx @mermaid-js/mermaid-cli mmdc -i diagram.mmd -o diagram.svg
```

## Color Legend

| Color | Domain/Category |
|-------|-----------------|
| Purple (#805ad5) | Archetypal/Meta patterns |
| Blue (#4299e1) | Towns / Physical domain |
| Green (#48bb78) | Buildings / Social domain |
| Orange (#ed8936) | Construction / Conceptual domain |
| Pink (#ed64a6) | Individual domain |
| Gray (#718096) | Data/Sources |

## Pattern Categories

- **Towns (1-94)**: Regional and urban planning patterns
- **Buildings (95-204)**: Building design and room arrangement patterns
- **Construction (205-253)**: Construction details and finishing patterns
