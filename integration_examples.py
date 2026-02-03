#!/usr/bin/env python3
"""
Skill Framework Integration Examples

Shows how to integrate the Skill Framework with existing pattern data:
- Pattern sequences from pattern_sequences.json
- Archetypal patterns with domain transformation
- NPU-253 coprocessor integration
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from skill_framework import (
    Skill, SkillSequence, SequenceBuilder,
    SkillWorkflow, WorkflowEngine, ExecutionMode,
    SkillContext, DomainTransformer, Domain
)


def example_1_pattern_sequences():
    """Example 1: Load and execute pattern sequences from JSON"""
    print("=" * 70)
    print("EXAMPLE 1: Pattern Sequences from JSON")
    print("=" * 70)
    
    # Load pattern sequences
    try:
        with open("pattern_sequences.json") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading pattern_sequences.json: {e}")
        return
    
    print(f"Loaded {len(data['sequences'])} pattern sequences")
    print()
    
    # Take first sequence as example
    seq_data = data["sequences"][1]  # Sequence 2: Regional Policies
    
    print(f"Sequence {seq_data['id']}: {seq_data['heading']}")
    print(f"Description: {seq_data['description']}")
    print(f"Category: {seq_data['category']}")
    print(f"Patterns: {seq_data['patterns']}")
    print()
    
    # Create skills from pattern IDs
    skills = []
    for pattern_id in seq_data["patterns"]:
        # In a real implementation, you would load pattern details
        # For demo, create simple skills
        def make_executor(pid):
            def executor(context):
                print(f"    Applying Pattern {pid}")
                context.set(f"pattern_{pid}_applied", True)
                return {"pattern_id": pid, "status": "applied"}
            return executor
        
        skill = Skill(
            pattern_id=f"apl{pattern_id}",
            name=f"Pattern {pattern_id}",
            description=f"Apply pattern {pattern_id}",
            execute_fn=make_executor(pattern_id)
        )
        skills.append(skill)
    
    # Build sequence
    sequence = (SequenceBuilder(str(seq_data["id"]), seq_data["heading"])
               .with_description(seq_data["description"])
               .add_skills(skills)
               .with_metadata("category", seq_data["category"])
               .with_metadata("emergent_phenomena", seq_data["emergent_phenomena"])
               .build())
    
    print(f"Created sequence with {len(sequence)} skills")
    print()
    
    # Execute sequence
    print("Executing sequence...")
    context = SkillContext(domain="physical")
    results = sequence.execute(context)
    
    print()
    print(f"Results: {len(results)} skills executed")
    print(f"Emergent Phenomena: {sequence.metadata['emergent_phenomena']}")
    print()


def example_2_archetypal_transformation():
    """Example 2: Use archetypal patterns with domain transformation"""
    print("=" * 70)
    print("EXAMPLE 2: Archetypal Pattern Transformation")
    print("=" * 70)
    
    # Load archetypal patterns
    patterns_path = Path("archetypal_patterns.json")
    if not patterns_path.exists():
        print("archetypal_patterns.json not found")
        return
    
    transformer = DomainTransformer(str(patterns_path))
    print(f"Loaded {len(transformer.archetypal_patterns)} archetypal patterns")
    print()
    
    # Select a pattern
    pattern_id = "12610010"
    
    # Transform across all domains
    print("Transforming pattern across domains:")
    print()
    
    for domain in [Domain.PHYSICAL, Domain.SOCIAL, Domain.CONCEPTUAL, Domain.PSYCHIC]:
        transformed = transformer.transform_pattern(pattern_id, domain)
        
        if transformed:
            # Create domain-specific skill
            def make_executor(domain_val, content):
                def executor(context):
                    print(f"      Applying in {domain_val} domain")
                    return {"domain": domain_val, "applied": True}
                return executor
            
            content = transformed.get('domain_specific_content', '')
            
            skill = Skill(
                pattern_id=f"{pattern_id}_{domain.value}",
                name=f"{transformed['name']} ({domain.value})",
                description=transformed['transformed_pattern'],
                execute_fn=make_executor(domain.value, content)
            )
            
            print(f"  {domain.value.upper()} Domain:")
            print(f"    Pattern: {skill.name}")
            print(f"    Description: {skill.description[:80]}...")
            
            # Execute skill
            context = SkillContext(domain=domain.value)
            result = skill.execute(context)
            print()
    
    print()


def example_3_multi_scale_workflow():
    """Example 3: Multi-scale workflow from region to building"""
    print("=" * 70)
    print("EXAMPLE 3: Multi-Scale Workflow")
    print("=" * 70)
    
    # Load sequences at different scales
    with open("pattern_sequences.json") as f:
        sequences_data = json.load(f)["sequences"]
    
    print("Building multi-scale workflow:")
    print("  Region → City → Neighborhood → Building")
    print()
    
    # Create representative sequences at each scale
    scales = {
        "regional": (sequences_data[1], "Regional Policies"),
        "city": (sequences_data[2], "Major City Structures"),
        "neighborhood": (sequences_data[3], "Communities and Neighborhoods"),
        "building": (sequences_data[6], "Local Centers")
    }
    
    workflow = SkillWorkflow(
        workflow_id="multi_scale",
        name="Multi-Scale Community Development",
        description="Complete workflow from regional to building scale",
        execution_mode=ExecutionMode.SEQUENTIAL
    )
    
    # Add each scale as a sequence
    for scale_name, (seq_data, display_name) in scales.items():
        # Create simplified skill for demo
        def make_scale_executor(scale, seq_id, heading):
            def executor(context):
                print(f"    {scale.upper()}: {heading}")
                context.set(f"{scale}_complete", True)
                return {"scale": scale, "sequence": seq_id}
            return executor
        
        skill = Skill(
            pattern_id=f"seq_{seq_data['id']}",
            name=display_name,
            description=seq_data['description'],
            execute_fn=make_scale_executor(scale_name, seq_data['id'], seq_data['heading'])
        )
        
        sequence = (SequenceBuilder(scale_name, display_name)
                   .add_skill(skill)
                   .build())
        
        workflow.add_step(scale_name, sequence)
    
    print(f"Created workflow with {len(workflow.steps)} scales")
    print()
    
    # Execute workflow
    print("Executing multi-scale workflow:")
    print()
    context = SkillContext(domain="physical")
    engine = WorkflowEngine(verbose=False)
    result = engine.execute(workflow, context)
    
    print()
    print(f"Status: {result['status']}")
    print(f"Duration: {result['duration_ms']:.2f}ms")
    print()
    
    # Check completion at each scale
    print("Scale Completion:")
    for scale in scales.keys():
        complete = context.get(f"{scale}_complete", False)
        print(f"  {scale.capitalize()}: {'✓' if complete else '✗'}")
    print()


def example_4_conditional_planning():
    """Example 4: Conditional workflow based on context"""
    print("=" * 70)
    print("EXAMPLE 4: Conditional Planning Workflow")
    print("=" * 70)
    
    # Create skills for different scenarios
    def assess_context_fn(context):
        # Assess project requirements
        project_type = context.inputs.get("project_type", "residential")
        scale = context.inputs.get("scale", "neighborhood")
        
        print(f"    Assessing: {project_type} project at {scale} scale")
        
        context.set("project_type", project_type)
        context.set("scale", scale)
        
        return {"assessment": "complete"}
    
    def residential_planning_fn(context):
        print("    Applying residential planning patterns...")
        return {"approach": "residential", "patterns": [37, 38, 39]}
    
    def commercial_planning_fn(context):
        print("    Applying commercial planning patterns...")
        return {"approach": "commercial", "patterns": [41, 42, 43]}
    
    def mixed_use_planning_fn(context):
        print("    Applying mixed-use planning patterns...")
        return {"approach": "mixed-use", "patterns": [37, 41, 44]}
    
    # Create skills
    assess = Skill("assess", "Context Assessment", "", execute_fn=assess_context_fn)
    residential = Skill("residential", "Residential Planning", "", execute_fn=residential_planning_fn)
    commercial = Skill("commercial", "Commercial Planning", "", execute_fn=commercial_planning_fn)
    mixed_use = Skill("mixed_use", "Mixed-Use Planning", "", execute_fn=mixed_use_planning_fn)
    
    # Build conditional workflow
    workflow = SkillWorkflow(
        workflow_id="conditional_planning",
        name="Conditional Planning Workflow",
        execution_mode=ExecutionMode.CONDITIONAL
    )
    
    workflow.add_step("assess", assess, on_success="residential_check")
    
    workflow.add_step(
        "residential_check",
        residential,
        condition=lambda ctx: ctx.get("project_type") == "residential",
        on_failure="commercial_check"
    )
    
    workflow.add_step(
        "commercial_check",
        commercial,
        condition=lambda ctx: ctx.get("project_type") == "commercial",
        on_failure="mixed_use_check"
    )
    
    workflow.add_step(
        "mixed_use_check",
        mixed_use,
        condition=lambda ctx: ctx.get("project_type") == "mixed-use"
    )
    
    # Execute with different project types
    engine = WorkflowEngine(verbose=False)
    
    for project_type in ["residential", "commercial", "mixed-use"]:
        print(f"\nScenario: {project_type.upper()} Project")
        print("-" * 40)
        
        context = SkillContext(
            inputs={"project_type": project_type, "scale": "neighborhood"}
        )
        
        result = engine.execute(workflow, context)
        print(f"  Steps executed: {len(result['results'])}")
    
    print()


def example_5_domain_workflow():
    """Example 5: Apply same workflow across multiple domains"""
    print("=" * 70)
    print("EXAMPLE 5: Cross-Domain Workflow Application")
    print("=" * 70)
    
    patterns_path = Path("archetypal_patterns.json")
    if not patterns_path.exists():
        print("archetypal_patterns.json not found")
        return
    
    transformer = DomainTransformer(str(patterns_path))
    
    # Select patterns for workflow
    pattern_ids = ["12610010", "12610020", "12610030"]
    
    print("Applying workflow across domains:")
    print()
    
    for domain in [Domain.PHYSICAL, Domain.SOCIAL, Domain.CONCEPTUAL]:
        print(f"{domain.value.upper()} Domain Workflow:")
        print("-" * 40)
        
        # Build workflow for this domain
        workflow = SkillWorkflow(
            workflow_id=f"workflow_{domain.value}",
            name=f"Workflow in {domain.value} domain",
            execution_mode=ExecutionMode.SEQUENTIAL
        )
        
        # Transform each pattern and create skills
        for pattern_id in pattern_ids:
            transformed = transformer.transform_pattern(pattern_id, domain)
            
            if transformed:
                def make_executor(pid, dom):
                    def executor(context):
                        print(f"    Pattern {pid} in {dom}")
                        return {"pattern": pid, "domain": dom}
                    return executor
                
                skill = Skill(
                    pattern_id=f"{pattern_id}_{domain.value}",
                    name=transformed['name'],
                    description=transformed['transformed_pattern'][:60] + "...",
                    execute_fn=make_executor(pattern_id, domain.value)
                )
                
                workflow.add_step(pattern_id, skill)
        
        # Execute workflow
        context = SkillContext(domain=domain.value)
        engine = WorkflowEngine(verbose=False)
        result = engine.execute(workflow, context)
        
        print(f"  Completed {len(result['results'])} steps")
        print()


def main():
    """Run all integration examples"""
    print("\n")
    print("╔═════════════════════════════════════════════════════════════════════╗")
    print("║     SKILL FRAMEWORK INTEGRATION EXAMPLES                            ║")
    print("║  Real-World Integration with Pattern Language Data                  ║")
    print("╚═════════════════════════════════════════════════════════════════════╝")
    print("\n")
    
    examples = [
        ("Pattern Sequences", example_1_pattern_sequences),
        ("Archetypal Transformation", example_2_archetypal_transformation),
        ("Multi-Scale Workflow", example_3_multi_scale_workflow),
        ("Conditional Planning", example_4_conditional_planning),
        ("Cross-Domain Workflow", example_5_domain_workflow),
    ]
    
    for i, (name, example_fn) in enumerate(examples, 1):
        try:
            example_fn()
        except Exception as e:
            print(f"Error in {name}: {e}")
            import traceback
            traceback.print_exc()
        
        if i < len(examples):
            input("Press Enter to continue to next example...")
            print("\n" * 2)
    
    print("=" * 70)
    print("All integration examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()
