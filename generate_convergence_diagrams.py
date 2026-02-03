#!/usr/bin/env python3
"""
Visualize the base-6 hierarchical structure and convergence process.
Creates Mermaid diagrams showing the meta-recursive organization.
"""

def generate_base6_hierarchy_diagram():
    """Generate Mermaid diagram of base-6 hierarchy."""
    return """```mermaid
graph TB
    %% Level 0: Meta-pattern
    L0["Level 0: Meta-Pattern<br/>1 = 6^0<br/><b>APL0</b><br/>The Whole Pattern Language"]
    
    %% Level 1: 6 Dimensions
    L1_0["dim0<br/><b>Archetypal</b><br/>Abstract templates"]
    L1_1["dim1<br/><b>Template</b><br/>Generic patterns"]
    L1_2["dim2<br/><b>Physical</b><br/>Spatial/Material"]
    L1_3["dim3<br/><b>Social</b><br/>Organizational"]
    L1_4["dim4<br/><b>Conceptual</b><br/>Knowledge/Theory"]
    L1_5["dim5<br/><b>Individual</b><br/>Consciousness"]
    
    %% Level 2: 36 Sequences (showing structure)
    L2_0["36 Sequences<br/>6×6 = 36<br/>Thematic flows"]
    
    %% Level 3: 216 Core Patterns
    L3_0["216 Core Patterns<br/>6×36 = 216<br/>Individual solutions"]
    
    %% Special Patterns
    L3_S["37 Special Patterns<br/>217-253<br/>Completion patterns"]
    
    %% Connections
    L0 --> L1_0
    L0 --> L1_1
    L0 --> L1_2
    L0 --> L1_3
    L0 --> L1_4
    L0 --> L1_5
    
    L1_0 --> L2_0
    L1_1 --> L2_0
    L1_2 --> L2_0
    L1_3 --> L2_0
    L1_4 --> L2_0
    L1_5 --> L2_0
    
    L2_0 --> L3_0
    L2_0 --> L3_S
    
    %% Styling
    classDef level0 fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px,color:#fff
    classDef level1 fill:#4dabf7,stroke:#1971c2,stroke-width:2px,color:#fff
    classDef level2 fill:#51cf66,stroke:#2f9e44,stroke-width:2px,color:#fff
    classDef level3 fill:#ffd43b,stroke:#f08c00,stroke-width:2px,color:#000
    
    class L0 level0
    class L1_0,L1_1,L1_2,L1_3,L1_4,L1_5 level1
    class L2_0 level2
    class L3_0,L3_S level3
```"""


def generate_convergence_process_diagram():
    """Generate Mermaid diagram showing iterative convergence."""
    return """```mermaid
graph LR
    %% Iterative convergence process
    I0["Initial State<br/>Fitness: ~60%<br/>Basic structure"] 
    I1["Iteration 1<br/>Fitness: ~70%<br/>Multi-representation"]
    I2["Iteration 2<br/>Fitness: ~80%<br/>Knowledge systems"]
    I3["Iteration 3<br/>Fitness: ~90%<br/>Navigation enhanced"]
    I4["Iteration 4<br/>Fitness: ~95%<br/>Meta-recursive awareness"]
    I5["Iteration 5<br/>Fitness: 100%<br/><b>OPTIMAL GRIP</b>"]
    
    %% Process flow
    I0 -->|"Apply Pattern 1<br/>Independent Regions"| I1
    I1 -->|"Apply Pattern 8<br/>Mosaic of Subcultures"| I2
    I2 -->|"Apply Pattern 52<br/>Network of Paths"| I3
    I3 -->|"Apply Pattern 28<br/>Eccentric Nucleus"| I4
    I4 -->|"Apply Pattern 253<br/>Things from Your Life"| I5
    
    %% Feedback loop
    I5 -.->|"Continuous refinement"| I5
    
    %% Styling
    classDef initial fill:#e9ecef,stroke:#adb5bd,stroke-width:2px
    classDef progress fill:#ffe066,stroke:#f08c00,stroke-width:2px
    classDef optimal fill:#51cf66,stroke:#2f9e44,stroke-width:3px,color:#fff
    
    class I0 initial
    class I1,I2,I3,I4 progress
    class I5 optimal
```"""


def generate_fitness_metrics_diagram():
    """Generate Mermaid diagram showing fitness metrics."""
    return """```mermaid
graph TB
    %% Fitness function with metrics
    FF["<b>Fitness Function</b><br/>Overall: 100%"]
    
    M1["Multi-scale Clarity<br/>100%<br/>✓ Clear hierarchy"]
    M2["Relationship Richness<br/>100%<br/>✓ Multiple connections"]
    M3["Contextual Relevance<br/>100%<br/>✓ Easy access"]
    M4["Gestalt Perception<br/>100%<br/>✓ Wholes visible"]
    M5["Interactive Navigation<br/>100%<br/>✓ Fluid exploration"]
    M6["Self-Similarity<br/>100%<br/>✓ Patterns on patterns"]
    
    FF --> M1
    FF --> M2
    FF --> M3
    FF --> M4
    FF --> M5
    FF --> M6
    
    %% Styling
    classDef fitness fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px,color:#fff
    classDef metric fill:#51cf66,stroke:#2f9e44,stroke-width:2px,color:#fff
    
    class FF fitness
    class M1,M2,M3,M4,M5,M6 metric
```"""


def generate_self_application_diagram():
    """Generate Mermaid diagram showing pattern self-application."""
    return """```mermaid
graph TB
    %% Patterns applied to repository structure
    
    subgraph "Repository Structure"
        R["Repository"]
        R1["apl/"]
        R2["uia/"]
        R3["markdown/"]
        R4["pattern/"]
        R5["opencog_atomese/"]
        R6["npu253/"]
        R7["apl_language/"]
        R8["docs/"]
        
        R --> R1 & R2 & R3 & R4 & R5 & R6 & R7 & R8
    end
    
    subgraph "Patterns Applied"
        P1["Pattern 1<br/>Independent Regions<br/>→ 8 autonomous directories"]
        P8["Pattern 8<br/>Mosaic of Subcultures<br/>→ Multiple representations"]
        P28["Pattern 28<br/>Eccentric Nucleus<br/>→ Multiple entry points"]
        P52["Pattern 52<br/>Network of Paths<br/>→ Navigation system"]
        P253["Pattern 253<br/>Things from Your Life<br/>→ Living examples"]
    end
    
    %% Applications
    P1 -.->|"Applied to"| R
    P8 -.->|"Applied to"| R1 & R2 & R3 & R4 & R5
    P28 -.->|"Applied to"| R
    P52 -.->|"Applied to"| R
    P253 -.->|"Applied to"| R
    
    %% Styling
    classDef repo fill:#e9ecef,stroke:#adb5bd,stroke-width:2px
    classDef pattern fill:#4dabf7,stroke:#1971c2,stroke-width:2px,color:#fff
    
    class R,R1,R2,R3,R4,R5,R6,R7,R8 repo
    class P1,P8,P28,P52,P253 pattern
```"""


def generate_six_dimensional_structure():
    """Generate detailed 6-dimensional structure diagram."""
    return """```mermaid
graph TB
    %% Root
    APL0["APL0<br/><b>Meta-Pattern</b><br/>253 Patterns"]
    
    %% 6 Dimensions
    D0["dim0: Archetypal<br/>Abstract with placeholders<br/>{{domains}}, {{elements}}"]
    D1["dim1: Template<br/>Generic patterns<br/>Domain-agnostic"]
    D2["dim2: Physical<br/>Spatial/Architectural<br/>Built environment"]
    D3["dim3: Social<br/>Organizational<br/>Community/Institution"]
    D4["dim4: Conceptual<br/>Knowledge/Theory<br/>Paradigmatic"]
    D5["dim5: Individual<br/>Consciousness<br/>Mental/Psychic"]
    
    %% Categories under dim2 (example)
    D2C1["cat1: Towns<br/>Patterns 1-94<br/>Regional scale"]
    D2C2["cat2: Buildings<br/>Patterns 95-204<br/>Building scale"]
    D2C3["cat3: Construction<br/>Patterns 205-253<br/>Detail scale"]
    
    %% Sequences under cat1 (example)
    D2C1S1["seq01: Regional<br/>Pattern 1"]
    D2C1S2["seq02: Policies<br/>Patterns 2-7"]
    D2C1S3["seq03: Structures<br/>Patterns 8-11"]
    
    %% Patterns under seq02 (example)
    D2C1S2P2["apl002<br/>Distribution of Towns"]
    D2C1S2P3["apl003<br/>City Country Fingers"]
    D2C1S2P7["apl007<br/>The Countryside"]
    
    %% Connections
    APL0 --> D0 & D1 & D2 & D3 & D4 & D5
    D2 --> D2C1 & D2C2 & D2C3
    D2C1 --> D2C1S1 & D2C1S2 & D2C1S3
    D2C1S2 --> D2C1S2P2 & D2C1S2P3 & D2C1S2P7
    
    %% Styling
    classDef meta fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px,color:#fff
    classDef dim fill:#4dabf7,stroke:#1971c2,stroke-width:2px,color:#fff
    classDef cat fill:#51cf66,stroke:#2f9e44,stroke-width:2px,color:#fff
    classDef seq fill:#ffd43b,stroke:#f08c00,stroke-width:2px,color:#000
    classDef pat fill:#e9ecef,stroke:#adb5bd,stroke-width:1px
    
    class APL0 meta
    class D0,D1,D2,D3,D4,D5 dim
    class D2C1,D2C2,D2C3 cat
    class D2C1S1,D2C1S2,D2C1S3 seq
    class D2C1S2P2,D2C1S2P3,D2C1S2P7 pat
```"""


def main():
    """Generate all diagrams."""
    
    print("# Meta-Recursive Structure Visualizations")
    print()
    print("## 1. Base-6 Hierarchical Structure")
    print()
    print(generate_base6_hierarchy_diagram())
    print()
    
    print("## 2. Iterative Convergence Process")
    print()
    print(generate_convergence_process_diagram())
    print()
    
    print("## 3. Fitness Metrics")
    print()
    print(generate_fitness_metrics_diagram())
    print()
    
    print("## 4. Pattern Self-Application")
    print()
    print(generate_self_application_diagram())
    print()
    
    print("## 5. Six-Dimensional Agent Structure")
    print()
    print(generate_six_dimensional_structure())
    print()
    
    print("---")
    print()
    print("**Note**: These diagrams can be viewed using Mermaid Live Editor:")
    print("https://mermaid.live/")
    print()
    print("Or directly in GitHub's markdown renderer.")


if __name__ == "__main__":
    main()
