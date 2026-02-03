# Skill Framework

A generalized pattern-based workflow system that implements sequences of skills as ordered routines defined by algorithmic workflows, where each step applies a pattern as a skill.

## Overview

The Skill Framework provides a domain-agnostic system for applying Christopher Alexander's Pattern Language principles as executable workflows. It supports application across any domain of inquiry:

- **Physical domains** - Spatial, material, architectural
- **Social domains** - Organizational, community, institutional
- **Conceptual domains** - Knowledge, theoretical, paradigmatic
- **Psychic domains** - Awareness, consciousness, mental

## Core Concepts

### Skills

A **Skill** wraps a pattern with execution semantics. Each skill:
- Has a unique pattern ID (e.g., "apl1", "12610010")
- Can be executed with context
- Produces structured results
- Supports preconditions and postconditions
- Can be composed into sequences

```python
from skill_framework import Skill, SkillContext

# Define execution function
def design_region(context):
    region_name = context.get("region_name")
    return {"designed": True, "name": region_name}

# Create skill
skill = Skill(
    pattern_id="apl1",
    name="Independent Regions",
    description="Design autonomous regions",
    execute_fn=design_region
)

# Execute skill
context = SkillContext(inputs={"region_name": "Pacific Northwest"})
result = skill.execute(context)

print(f"Status: {result.status}")
print(f"Output: {result.output}")
```

### Skill Sequences

A **SkillSequence** represents an ordered collection of skills forming a coherent routine:

```python
from skill_framework import SkillSequence, SequenceBuilder

# Build sequence using fluent API
sequence = (SequenceBuilder("seq2", "Regional Policies")
           .with_description("Patterns 2-7: Regional planning")
           .add_skill(skill1)
           .add_skill(skill2)
           .add_skill(skill3)
           .continue_on_error(True)
           .build())

# Execute sequence
results = sequence.execute(context)
```

### Workflows

A **SkillWorkflow** orchestrates multiple sequences with algorithmic control flow:

```python
from skill_framework import SkillWorkflow, WorkflowEngine, ExecutionMode

# Create workflow
workflow = SkillWorkflow(
    workflow_id="planning",
    name="Adaptive Planning",
    execution_mode=ExecutionMode.CONDITIONAL
)

# Add steps with conditional branching
workflow.add_step("assess", assess_skill, on_success="urban_check")
workflow.add_step("urban_check", urban_skill, 
                 condition=lambda ctx: ctx.get("site_type") == "urban",
                 on_success="finalize")
workflow.add_step("finalize", finalize_skill)

# Execute workflow
engine = WorkflowEngine(verbose=True)
result = engine.execute(workflow, context)
```

### Context & State Management

**SkillContext** manages state and data flow between skills:

```python
from skill_framework import SkillContext, ContextScope

# Create context with inputs
context = SkillContext(
    inputs={"project": "city_planning"},
    domain="physical"
)

# Set variables in different scopes
context.set("global_var", "value", ContextScope.GLOBAL)
context.set("sequence_var", "value", ContextScope.SEQUENCE)
context.set("local_var", "value", ContextScope.LOCAL)

# Retrieve variables
value = context.get("global_var", scope=ContextScope.GLOBAL)

# Clear scopes between steps
context.clear_local()  # Clear local scope
context.clear_sequence()  # Clear sequence scope
```

### Domain Transformation

**DomainTransformer** applies patterns across different domains:

```python
from skill_framework import DomainTransformer, Domain

# Load archetypal patterns
transformer = DomainTransformer("archetypal_patterns.json")

# Transform pattern to physical domain
physical = transformer.transform_pattern("12610010", Domain.PHYSICAL)
print(physical["transformed_pattern"])
# "Balance between regions/areas will not be achieved..."

# Transform to social domain
social = transformer.transform_pattern("12610010", Domain.SOCIAL)
print(social["transformed_pattern"])
# "Balance between functional domains/communities will not be achieved..."

# Get domain-specific content
content = transformer.get_domain_specific_content("12610010", Domain.CONCEPTUAL)
```

## Execution Modes

### Sequential Execution

Skills execute one after another in order:

```python
workflow = SkillWorkflow("wf", "Sequential", execution_mode=ExecutionMode.SEQUENTIAL)
workflow.add_step("step1", skill1)
workflow.add_step("step2", skill2)
workflow.add_step("step3", skill3)
```

### Conditional Execution

Skills execute based on conditions with branching:

```python
workflow = SkillWorkflow("wf", "Conditional", execution_mode=ExecutionMode.CONDITIONAL)

workflow.add_step("assess", assess_skill, on_success="check")
workflow.add_step("check", check_skill,
                 condition=lambda ctx: ctx.get("proceed"),
                 on_success="execute",
                 on_failure="alternative")
workflow.add_step("execute", execute_skill)
workflow.add_step("alternative", alternative_skill)
```

## Preconditions & Postconditions

Skills can validate conditions before and after execution:

```python
# Precondition: check required inputs
def check_inputs(context):
    return context.has("required_input")

# Postcondition: validate output
def validate_output(context, result):
    return result.get("success") == True

skill = Skill(
    pattern_id="validated",
    name="Validated Skill",
    description="Skill with validation",
    execute_fn=execute_fn,
    preconditions=[check_inputs],
    postconditions=[validate_output]
)
```

## Error Handling

Control error behavior at sequence and workflow levels:

```python
# Continue execution on errors
sequence = (SequenceBuilder("robust", "Robust Sequence")
           .add_skills([skill1, skill2, skill3])
           .continue_on_error(True)
           .build())

# Check results
results = sequence.execute(context)
for result in results:
    if result.is_failed:
        print(f"Error: {result.error}")
```

## Integration with Pattern Language

The framework integrates with existing pattern data:

### From Pattern Sequences

```python
import json

# Load pattern sequences
with open("pattern_sequences.json") as f:
    sequences = json.load(f)["sequences"]

# Create skills from pattern IDs
for seq in sequences:
    pattern_ids = seq["patterns"]
    skills = [create_skill_from_pattern(pid) for pid in pattern_ids]
    
    sequence = (SequenceBuilder(seq["id"], seq["heading"])
               .with_description(seq["description"])
               .add_skills(skills)
               .build())
```

### With NPU-253 Coprocessor

```python
from npu253 import PatternCoprocessorDriver, NPUConfig

# Load patterns
npu = PatternCoprocessorDriver(NPUConfig())
npu.load()

# Create skill from NPU pattern
pattern = npu.query_by_id(1)
skill = Skill(
    pattern_id="apl1",
    name=pattern.name,
    description=pattern.solution,
    execute_fn=lambda ctx: apply_pattern(pattern, ctx)
)
```

## Examples

### Example 1: Regional Planning Sequence

```python
# Pattern Sequence 2: Regional Policies (Patterns 2-7)

def distribute_towns(context):
    context.set("towns_distributed", True)
    return {"pattern": 2, "towns": 12}

def create_city_fingers(context):
    context.set("city_fingers", True)
    return {"pattern": 3, "green_belts": 8}

sequence = (SequenceBuilder("seq2", "Regional Policies")
           .add_skill(Skill("apl2", "Distribution of Towns", "", distribute_towns))
           .add_skill(Skill("apl3", "City Country Fingers", "", create_city_fingers))
           .with_metadata("category", "Towns")
           .build())

context = SkillContext(domain="physical")
results = sequence.execute(context)
```

### Example 2: Multi-Domain Workflow

```python
# Apply same pattern across domains
transformer = DomainTransformer("archetypal_patterns.json")

domains = [Domain.PHYSICAL, Domain.SOCIAL, Domain.CONCEPTUAL, Domain.PSYCHIC]
results = {}

for domain in domains:
    # Transform pattern
    transformed = transformer.transform_pattern("12610010", domain)
    
    # Create domain-specific skill
    skill = Skill(
        pattern_id=f"12610010_{domain.value}",
        name=f"{transformed['name']} ({domain.value})",
        description=transformed['transformed_pattern'],
        execute_fn=lambda ctx: apply_transformed_pattern(ctx, domain)
    )
    
    # Execute
    context = SkillContext(domain=domain.value)
    result = skill.execute(context)
    results[domain.value] = result
```

### Example 3: Complete Community Development

```python
# Multi-scale workflow: Region → City → Neighborhood → Building

workflow = SkillWorkflow("community", "Complete Community Development")

# Add sequences at each scale
workflow.add_step("regional", regional_sequence)
workflow.add_step("city", city_sequence)
workflow.add_step("neighborhood", neighborhood_sequence)
workflow.add_step("building", building_sequence)

# Execute complete workflow
engine = WorkflowEngine(verbose=True)
context = SkillContext(domain="physical")
result = engine.execute(workflow, context)

print(f"Completed {len(result['results'])} sequences")
print(f"Total time: {result['duration_ms']:.2f}ms")
```

## API Reference

### Core Classes

- **Skill** - Pattern wrapper with execution semantics
- **SkillResult** - Result of skill execution
- **SkillStatus** - Execution status enum
- **SkillSequence** - Ordered collection of skills
- **SequenceBuilder** - Fluent API for building sequences
- **SkillWorkflow** - Algorithmic workflow orchestrator
- **WorkflowEngine** - Workflow execution engine
- **ExecutionMode** - Workflow execution mode enum
- **SkillContext** - Execution context and state management
- **ContextScope** - Variable scope enum
- **DomainTransformer** - Pattern domain transformation
- **Domain** - Domain enum

### Key Methods

#### Skill
- `execute(context)` - Execute skill with context
- `check_preconditions(context)` - Validate preconditions
- `check_postconditions(context, result)` - Validate postconditions

#### SkillSequence
- `add_skill(skill)` - Add skill to sequence
- `execute(context)` - Execute all skills in order

#### SkillWorkflow
- `add_step(id, skill_or_sequence, condition, on_success, on_failure)` - Add workflow step
- `set_start_step(step_id)` - Set starting step

#### WorkflowEngine
- `execute(workflow, context)` - Execute workflow

#### SkillContext
- `get(key, default, scope)` - Get variable
- `set(key, value, scope)` - Set variable
- `has(key, scope)` - Check if variable exists
- `clear_local()` - Clear local scope
- `clear_sequence()` - Clear sequence scope
- `add_history(skill_id, result)` - Add to execution history
- `clone()` - Deep copy context

#### DomainTransformer
- `load_patterns(path)` - Load archetypal patterns
- `transform_pattern(pattern_id, domain)` - Transform to domain
- `get_domain_specific_content(pattern_id, domain)` - Get domain content
- `get_available_domains(pattern_id)` - List available domains

## Testing

Run the comprehensive test suite:

```bash
python3 test_skill_framework.py
```

Run the demonstration:

```bash
python3 demo_skill_framework.py
```

## Architecture

```
skill_framework/
├── __init__.py        # Package exports
├── skill.py           # Skill class and execution
├── context.py         # Context and state management
├── sequence.py        # Sequence and builder
├── workflow.py        # Workflow and engine
└── transforms.py      # Domain transformation
```

## Design Principles

1. **Domain-Agnostic** - Patterns can be applied to any domain
2. **Composable** - Skills compose into sequences, sequences into workflows
3. **Declarative** - Workflows defined declaratively, executed algorithmically
4. **Validated** - Preconditions and postconditions enforce correctness
5. **Stateful** - Context manages state flow between steps
6. **Flexible** - Multiple execution modes and control flow patterns
7. **Extensible** - Easy to add new skills, patterns, and domains

## Future Enhancements

- Parallel execution mode for concurrent skill execution
- Asynchronous workflows for long-running operations
- Workflow persistence and resumption
- Visual workflow designer
- Integration with OpenCog Atomese for reasoning
- Machine learning for workflow optimization
- Real-time monitoring and telemetry
- Distributed workflow execution

## License

This framework is part of the skipl-253 repository and follows the same license.
