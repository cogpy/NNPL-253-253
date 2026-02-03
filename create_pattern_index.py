#!/usr/bin/env python3
"""
Generate comprehensive pattern index with multiple access methods.
Applies Pattern 30: ACTIVITY NODES to create access concentrations.
"""

import json

def load_data():
    """Load pattern data"""
    with open('pattern_language_generated.json') as f:
        patterns = json.load(f)
    with open('pattern_sequences.json') as f:
        sequences = json.load(f)
    with open('archetypal_patterns.json') as f:
        archetypal = json.load(f)
    return patterns, sequences, archetypal

def generate_index():
    """Generate comprehensive pattern index"""
    patterns, sequences, archetypal = load_data()
    
    index = []
    
    # Header
    index.append("# Pattern Index: Complete Reference")
    index.append("")
    index.append("> **Pattern 30: ACTIVITY NODES** - Concentrated access to all patterns")
    index.append("")
    index.append("## Quick Access")
    index.append("")
    index.append("### By Number")
    index.append("")
    index.append("| Pattern | Name | Category | Asterisks |")
    index.append("|---------|------|----------|-----------|")
    
    # Meta-pattern
    meta = patterns.get('meta_pattern', {})
    index.append(f"| 0 | [{meta.get('name', 'Pattern Language')}](markdown/apl/APL%20-%20Home.md) | Meta-Pattern | {'*' * meta.get('asterisks', 2)} |")
    
    # Create pattern number lookup from sequences
    pattern_info = {}
    for seq in sequences['sequences']:
        category = seq['category']
        for pnum in seq['patterns']:
            if pnum not in pattern_info:
                pattern_info[pnum] = {'category': category, 'sequences': []}
            pattern_info[pnum]['sequences'].append(seq['id'])
    
    # Generate full index by number
    for i in range(1, 254):
        info = pattern_info.get(i, {'category': 'Unknown', 'sequences': []})
        cat = info['category']
        asterisks = 2 if i <= 94 else (1 if i <= 204 else 0)
        ast_str = '*' * asterisks if asterisks > 0 else ''
        index.append(f"| {i} | [Pattern {i}](markdown/apl/apl{i:03d}.md) | {cat} | {ast_str} |")
    
    index.append("")
    index.append("### By Category")
    index.append("")
    
    # Towns
    index.append("#### Towns (Patterns 1-94) - Large Scale")
    index.append("Patterns governing regional planning, city structure, communities, and local environments.")
    index.append("")
    index.append("**Sequences**: 1-15 covering regions, policies, city structures, communities, housing, work, paths, open land, families, learning, and gathering places.")
    index.append("")
    index.append("[View all Towns patterns](category_towns.json)")
    index.append("")
    
    # Buildings
    index.append("#### Buildings (Patterns 95-204) - Medium Scale")
    index.append("Patterns governing building arrangements, positions, spaces, and room organization.")
    index.append("")
    index.append("**Sequences**: 16-28 covering building complexes, positions, thresholds, circulation, gradients, main rooms, secondary spaces, and wall depth.")
    index.append("")
    index.append("[View all Buildings patterns](category_buildings.json)")
    index.append("")
    
    # Construction
    index.append("#### Construction (Patterns 205-253) - Small Scale")
    index.append("Patterns governing structural systems, building details, surfaces, and completion.")
    index.append("")
    index.append("**Sequences**: 29-36 covering structural layout, frame construction, openings, surfaces, details, and finishing.")
    index.append("")
    index.append("[View all Construction patterns](category_construction.json)")
    index.append("")
    
    # By Sequence
    index.append("### By Sequence")
    index.append("")
    index.append("The 36 sequences organize patterns into coherent flows with emergent phenomena.")
    index.append("")
    
    for seq in sequences['sequences']:
        index.append(f"#### Sequence {seq['id']}: {seq['heading']}")
        index.append(f"**Category**: {seq['category']}  ")
        index.append(f"**Patterns**: {', '.join(map(str, seq['patterns']))}  ")
        index.append(f"**Emergence**: {seq['emergent_phenomena']}")
        index.append("")
    
    # Special indexes
    index.append("## Special Indexes")
    index.append("")
    
    # By importance (asterisks)
    index.append("### By Importance (Asterisk Levels)")
    index.append("")
    index.append("Alexander marked patterns with asterisks to indicate importance:")
    index.append("")
    index.append("#### Two Asterisks (**) - Most Essential")
    index.append("The most fundamental patterns that define the character of the environment.")
    index.append("")
    index.append("*Patterns 1-94 (Towns category) are considered most essential.*")
    index.append("")
    index.append("#### One Asterisk (*) - Very Important")
    index.append("Important patterns that significantly contribute to life and comfort.")
    index.append("")
    index.append("*Patterns 95-204 (Buildings category).*")
    index.append("")
    index.append("#### No Asterisk - Important Details")
    index.append("Detailed patterns that complete and refine the larger patterns.")
    index.append("")
    index.append("*Patterns 205-253 (Construction category).*")
    index.append("")
    
    # Archetypal patterns
    index.append("### Archetypal Patterns")
    index.append("")
    index.append(f"**Total**: {len(archetypal['patterns'])} archetypal patterns with domain transformations")
    index.append("")
    index.append("Archetypal patterns use placeholders like `{{domains}}` that can be transformed across:")
    index.append("- **Physical**: Spatial, material, architectural")
    index.append("- **Social**: Organizational, community, institutional")
    index.append("- **Conceptual**: Knowledge, theoretical, paradigmatic")
    index.append("- **Psychic**: Awareness, consciousness, mental")
    index.append("")
    index.append("[View archetypal patterns](archetypal_patterns.json)")
    index.append("")
    
    # Key patterns
    index.append("## Key Entry Patterns")
    index.append("")
    index.append("These patterns are especially useful as starting points:")
    index.append("")
    
    key_patterns = [
        (1, "Independent Regions", "Start here for understanding regional scale"),
        (8, "Mosaic of Subcultures", "Diversity and cultural identity"),
        (12, "Community of 7000", "Optimal community size"),
        (28, "Eccentric Nucleus", "Off-center centers"),
        (52, "Network of Paths and Cars", "Pedestrian-first circulation"),
        (95, "Building Complex", "Grouping buildings"),
        (106, "Positive Outdoor Space", "Creating outdoor rooms"),
        (127, "Intimacy Gradient", "Privacy progression"),
        (132, "Short Passages", "Minimize corridors"),
        (159, "Light on Two Sides", "Cross ventilation and light"),
        (205, "Structure Follows Social Spaces", "Let form follow life"),
        (253, "Things from Your Life", "Personal connection"),
    ]
    
    for num, name, desc in key_patterns:
        index.append(f"### Pattern {num}: {name}")
        index.append(f"{desc}")
        index.append(f"[Read pattern →](markdown/apl/apl{num:03d}.md)")
        index.append("")
    
    # Navigation
    index.append("## Navigation")
    index.append("")
    index.append("- **[NAVIGATION_HUB.md](NAVIGATION_HUB.md)** - Multiple entry points")
    index.append("- **[SEQUENCE_NAVIGATION.md](SEQUENCE_NAVIGATION.md)** - Navigate by sequence")
    index.append("- **[PATTERN_MAP.md](PATTERN_MAP.md)** - Repository structure")
    index.append("- **[README.md](README.md)** - Main overview")
    index.append("")
    
    # Access methods
    index.append("## Access Methods")
    index.append("")
    index.append("### 1. Direct File Access")
    index.append("```bash")
    index.append("# Read markdown version")
    index.append("cat markdown/apl/apl042.md")
    index.append("")
    index.append("# View in browser")
    index.append("open apl/apl042.htm")
    index.append("```")
    index.append("")
    index.append("### 2. JSON API Access")
    index.append("```python")
    index.append("import json")
    index.append("")
    index.append("# Load all patterns")
    index.append("with open('pattern_language_generated.json') as f:")
    index.append("    patterns = json.load(f)")
    index.append("")
    index.append("# Load sequences")
    index.append("with open('pattern_sequences.json') as f:")
    index.append("    sequences = json.load(f)")
    index.append("```")
    index.append("")
    index.append("### 3. NPU253 Virtual Hardware")
    index.append("```python")
    index.append("from npu253 import PatternCoprocessorDriver, NPUConfig")
    index.append("")
    index.append("npu = PatternCoprocessorDriver(NPUConfig())")
    index.append("npu.load()")
    index.append("pattern = npu.query_by_id(42)")
    index.append("```")
    index.append("")
    index.append("### 4. OpenCog Atomese")
    index.append("```scheme")
    index.append("; Load pattern language")
    index.append("(load \"opencog_atomese/pattern_language.scm\")")
    index.append("")
    index.append("; Query pattern")
    index.append("(cog-execute! (Get (TypedVariable $x (Type 'ConceptNode))")
    index.append("  (Inheritance $x (Concept \"Category-Towns\"))))")
    index.append("```")
    index.append("")
    index.append("### 5. APL Language")
    index.append("```apl")
    index.append("⍝ Load and query patterns")
    index.append(")LOAD apl_language/patterns.apl")
    index.append("towns ← GetTownPatterns")
    index.append("```")
    index.append("")
    
    # Conclusion
    index.append("## Pattern Relationships")
    index.append("")
    index.append("Patterns are interconnected through:")
    index.append("- **Sequences**: Groups of related patterns that flow together")
    index.append("- **Scale**: Patterns at different scales (towns → buildings → construction)")
    index.append("- **Preceding/Following**: Context patterns and refinement patterns")
    index.append("- **Category**: Shared organizational grouping")
    index.append("- **Emergence**: Synergies that arise from pattern combinations")
    index.append("")
    index.append("Use the hypergraph in `opencog_atomese/` to explore these relationships programmatically.")
    index.append("")
    index.append("---")
    index.append("")
    index.append("*This index applies Pattern 30 (Activity Nodes) to create concentrated access points to the pattern language, while Pattern 52 (Network of Paths) ensures multiple routes to each pattern.*")
    
    return '\n'.join(index)

if __name__ == '__main__':
    content = generate_index()
    
    with open('PATTERN_INDEX.md', 'w') as f:
        f.write(content)
    
    print("Pattern index created: PATTERN_INDEX.md")
    print(f"Length: {len(content)} characters")
    print(f"Lines: {len(content.splitlines())}")
