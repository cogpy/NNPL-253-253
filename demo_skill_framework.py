#!/usr/bin/env python3
"""
Skill Framework Demo

Demonstrates the generalized pattern-based workflow system with real examples
across different domains.
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from skill_framework import (
    Skill, SkillSequence, SequenceBuilder,
    SkillWorkflow, WorkflowEngine, ExecutionMode,
    SkillContext, ContextScope,
    DomainTransformer, Domain
)


def demo_basic_skills():
    """Demo 1: Basic skill execution"""
    print("=" * 70)
    print("DEMO 1: Basic Skill Execution")
    print("=" * 70)
    
    # Define a simple skill
    def design_region(context):
        """Apply Pattern 1: Independent Regions"""
        region_name = context.get("region_name", "New Region")
        population = context.get("population", 5_000_000)
        
        context.set("region_designed", True)
        context.set("region_details", {
            "name": region_name,
            "population": population,
            "autonomy": "high"
        })
        
        return {
            "success": True,
            "message": f"Designed autonomous region '{region_name}' for {population:,} people"
        }
    
    skill = Skill(
        pattern_id="apl1",
        name="Independent Regions",
        description="Design autonomous regions with 2-10 million people",
        execute_fn=design_region
    )
    
    # Execute the skill
    context = SkillContext(
        inputs={"region_name": "Pacific Northwest", "population": 7_000_000},
        domain="physical"
    )
    
    result = skill.execute(context)
    
    print(f"Skill: {skill.name}")
    print(f"Status: {result.status.value}")
    print(f"Output: {result.output}")
    print(f"Duration: {result.duration_ms:.2f}ms")
    print(f"Region Details: {context.get('region_details')}")
    print()


def demo_skill_sequence():
    """Demo 2: Sequential workflow execution"""
    print("=" * 70)
    print("DEMO 2: Skill Sequence - Regional Planning")
    print("=" * 70)
    
    # Pattern Sequence 2: Regional Policies (Patterns 2-7)
    
    def apply_pattern_2(context):
        """Distribution of Towns - Pattern 2"""
        print("  Applying Pattern 2: Distribution of Towns")
        context.set("towns_distributed", True)
        return {"pattern": 2, "towns_count": 12}
    
    def apply_pattern_3(context):
        """City Country Fingers - Pattern 3"""
        print("  Applying Pattern 3: City Country Fingers")
        context.set("city_fingers_created", True)
        return {"pattern": 3, "green_belts": 8}
    
    def apply_pattern_4(context):
        """Agricultural Valleys - Pattern 4"""
        print("  Applying Pattern 4: Agricultural Valleys")
        context.set("valleys_preserved", True)
        return {"pattern": 4, "agricultural_area_km2": 500}
    
    # Build sequence using fluent API
    sequence = (SequenceBuilder("seq2", "Regional Policies")
               .with_description("Patterns 2-7: Regional planning policies")
               .add_skill(Skill("apl2", "Distribution of Towns", "", execute_fn=apply_pattern_2))
               .add_skill(Skill("apl3", "City Country Fingers", "", execute_fn=apply_pattern_3))
               .add_skill(Skill("apl4", "Agricultural Valleys", "", execute_fn=apply_pattern_4))
               .with_metadata("category", "Towns")
               .with_metadata("emergent_phenomena", "Balanced settlements preserving countryside")
               .build())
    
    print(f"Sequence: {sequence.name}")
    print(f"Description: {sequence.description}")
    print(f"Skills: {len(sequence)}")
    print()
    
    # Execute the sequence
    context = SkillContext(domain="physical")
    results = sequence.execute(context)
    
    print(f"Execution Results:")
    for i, result in enumerate(results):
        print(f"  Step {i+1}: {result.status.value} - {result.output}")
    
    print()
    print(f"Final State:")
    print(f"  Towns Distributed: {context.get('towns_distributed')}")
    print(f"  City Fingers Created: {context.get('city_fingers_created')}")
    print(f"  Valleys Preserved: {context.get('valleys_preserved')}")
    print()


def demo_conditional_workflow():
    """Demo 3: Conditional workflow with branching"""
    print("=" * 70)
    print("DEMO 3: Conditional Workflow - Adaptive Planning")
    print("=" * 70)
    
    def assess_site(context):
        """Assess site conditions"""
        print("  Assessing site conditions...")
        site_type = context.inputs.get("site_type", "urban")
        context.set("site_type", site_type)
        context.set("assessment_complete", True)
        return {"site_type": site_type}
    
    def urban_planning(context):
        """Apply urban planning patterns"""
        print("  Applying urban planning patterns...")
        return {"approach": "urban", "patterns": ["apl8", "apl9", "apl10"]}
    
    def rural_planning(context):
        """Apply rural planning patterns"""
        print("  Applying rural planning patterns...")
        return {"approach": "rural", "patterns": ["apl51", "apl52"]}
    
    def finalize_plan(context):
        """Finalize the plan"""
        print("  Finalizing plan...")
        return {"status": "complete"}
    
    # Create skills
    assess_skill = Skill("assess", "Site Assessment", "", execute_fn=assess_site)
    urban_skill = Skill("urban", "Urban Planning", "", execute_fn=urban_planning)
    rural_skill = Skill("rural", "Rural Planning", "", execute_fn=rural_planning)
    finalize_skill = Skill("finalize", "Finalize Plan", "", execute_fn=finalize_plan)
    
    # Build conditional workflow
    workflow = SkillWorkflow(
        workflow_id="adaptive_planning",
        name="Adaptive Planning Workflow",
        execution_mode=ExecutionMode.CONDITIONAL
    )
    
    # Add steps with conditions and branching
    workflow.add_step("assess", assess_skill, on_success="urban_check")
    
    workflow.add_step(
        "urban_check",
        urban_skill,
        condition=lambda ctx: ctx.get("site_type") == "urban",
        on_success="finalize",
        on_failure="rural_check"
    )
    
    workflow.add_step(
        "rural_check",
        rural_skill,
        condition=lambda ctx: ctx.get("site_type") == "rural",
        on_success="finalize"
    )
    
    workflow.add_step("finalize", finalize_skill)
    
    # Execute with urban site
    print("Scenario 1: Urban Site")
    print("-" * 40)
    context = SkillContext(inputs={"site_type": "urban"})
    engine = WorkflowEngine(verbose=False)
    result = engine.execute(workflow, context)
    print(f"Status: {result['status']}")
    print(f"Steps executed: {len(result['results'])}")
    print()
    
    # Execute with rural site
    print("Scenario 2: Rural Site")
    print("-" * 40)
    context = SkillContext(inputs={"site_type": "rural"})
    result = engine.execute(workflow, context)
    print(f"Status: {result['status']}")
    print(f"Steps executed: {len(result['results'])}")
    print()


def demo_domain_transformation():
    """Demo 4: Domain transformation across physical/social/conceptual/individual"""
    print("=" * 70)
    print("DEMO 4: Domain Transformation")
    print("=" * 70)
    
    # Try to load archetypal patterns
    patterns_path = Path(__file__).parent / "archetypal_patterns.json"
    
    transformer = DomainTransformer()
    
    if not patterns_path.exists():
        print("Note: archetypal_patterns.json not found, using mock data")
        # Add mock pattern
        transformer.archetypal_patterns["12610010"] = {
            "pattern_id": "12610010",
            "name": "Independent Domains",
            "archetypal_pattern": "Balance between {{domains}} will not be achieved unless each one is autonomous.",
            "domain_mappings": {
                "domains": {
                    "physical": "regions/areas",
                    "social": "functional domains/communities",
                    "conceptual": "knowledge domains",
                    "individual": "modes of awareness"
                }
            },
            "domain_specific_content": {
                "physical": "Metropolitan regions will not balance until each is autonomous.",
                "social": "Major networks will not balance until each is autonomous.",
                "conceptual": "Major paradigms will not balance until each is autonomous.",
                "individual": "Major awareness modes will not balance until each is autonomous."
            }
        }
    else:
        try:
            print(f"Loading patterns from {patterns_path}")
            transformer.load_patterns(str(patterns_path))
            print(f"Loaded {len(transformer.archetypal_patterns)} patterns")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading patterns: {e}")
            print("Using mock data instead")
    
    print()
    
    # Transform pattern across domains
    pattern_id = "12610010"
    
    for domain in [Domain.PHYSICAL, Domain.SOCIAL, Domain.CONCEPTUAL, Domain.INDIVIDUAL]:
        print(f"{domain.value.upper()} Domain:")
        print("-" * 40)
        
        transformed = transformer.transform_pattern(pattern_id, domain)
        if transformed:
            print(f"Pattern: {transformed['name']}")
            print(f"Archetypal: {transformed['archetypal_pattern']}")
            print(f"Transformed: {transformed['transformed_pattern']}")
            
            content = transformed.get('domain_specific_content')
            if content:
                print(f"Content: {content[:100]}...")
        else:
            print("Pattern not found")
        
        print()


def demo_complete_workflow():
    """Demo 5: Complete multi-sequence workflow"""
    print("=" * 70)
    print("DEMO 5: Complete Workflow - Building a Community")
    print("=" * 70)
    
    # Sequence 1: Regional Scale (Patterns 1-7)
    def plan_region(context):
        print("  Planning regional structure...")
        return {"region": "planned", "scale": "regional"}
    
    # Sequence 2: City Scale (Patterns 8-15)
    def design_city(context):
        print("  Designing city structures...")
        return {"city": "designed", "scale": "city"}
    
    # Sequence 3: Neighborhood Scale (Patterns 16-27)
    def create_neighborhood(context):
        print("  Creating neighborhood patterns...")
        return {"neighborhood": "created", "scale": "neighborhood"}
    
    # Sequence 4: Building Scale (Patterns 95+)
    def design_buildings(context):
        print("  Designing individual buildings...")
        return {"buildings": "designed", "scale": "building"}
    
    # Create sequences
    regional_seq = (SequenceBuilder("regional", "Regional Planning")
                   .add_skill(Skill("seq1", "Plan Region", "", execute_fn=plan_region))
                   .build())
    
    city_seq = (SequenceBuilder("city", "City Design")
               .add_skill(Skill("seq2", "Design City", "", execute_fn=design_city))
               .build())
    
    neighborhood_seq = (SequenceBuilder("neighborhood", "Neighborhood Creation")
                       .add_skill(Skill("seq3", "Create Neighborhood", "", execute_fn=create_neighborhood))
                       .build())
    
    building_seq = (SequenceBuilder("building", "Building Design")
                   .add_skill(Skill("seq4", "Design Buildings", "", execute_fn=design_buildings))
                   .build())
    
    # Create workflow with all sequences
    workflow = SkillWorkflow(
        workflow_id="complete_community",
        name="Complete Community Development",
        description="From regional planning to building design",
        execution_mode=ExecutionMode.SEQUENTIAL
    )
    
    workflow.add_step("regional", regional_seq)
    workflow.add_step("city", city_seq)
    workflow.add_step("neighborhood", neighborhood_seq)
    workflow.add_step("building", building_seq)
    
    print(f"Workflow: {workflow.name}")
    print(f"Description: {workflow.description}")
    print(f"Steps: {len(workflow.steps)}")
    print()
    
    # Execute workflow
    context = SkillContext(domain="physical")
    engine = WorkflowEngine(verbose=False)
    
    print("Executing workflow...")
    print()
    result = engine.execute(workflow, context)
    
    print()
    print(f"Workflow Status: {result['status']}")
    print(f"Duration: {result['duration_ms']:.2f}ms")
    print(f"Steps Completed: {len(result['results'])}")
    print()
    print("Execution History:")
    for entry in context.execution_history:
        result = entry['result']
        if hasattr(result, 'output'):
            # Single skill result
            print(f"  - {entry['skill_id']}: {result.output}")
        elif isinstance(result, list):
            # Sequence results
            print(f"  - {entry['skill_id']}: {len(result)} steps completed")
        else:
            print(f"  - {entry['skill_id']}: {result}")
    print()


def main():
    """Run all demos"""
    print("\n")
    print("╔═════════════════════════════════════════════════════════════════════╗")
    print("║           SKILL FRAMEWORK DEMONSTRATION                             ║")
    print("║  Generalized Pattern-Based Workflow System for Domain-Agnostic     ║")
    print("║  Application of Pattern Language Principles                         ║")
    print("╚═════════════════════════════════════════════════════════════════════╝")
    print("\n")
    
    demos = [
        ("Basic Skills", demo_basic_skills),
        ("Skill Sequences", demo_skill_sequence),
        ("Conditional Workflows", demo_conditional_workflow),
        ("Domain Transformation", demo_domain_transformation),
        ("Complete Workflow", demo_complete_workflow),
    ]
    
    for i, (name, demo_fn) in enumerate(demos, 1):
        try:
            demo_fn()
        except Exception as e:
            print(f"Error in {name}: {e}")
            import traceback
            traceback.print_exc()
        
        if i < len(demos):
            input("Press Enter to continue to next demo...")
            print("\n" * 2)
    
    print("=" * 70)
    print("All demos completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()
