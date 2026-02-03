# Skill Framework Quick Reference

Quick reference for the Skill Framework - a generalized pattern-based workflow system.

## Installation

The Skill Framework is included in the skipl-253 repository:

```bash
cd skipl-253
python3 -m skill_framework
```

## Quick Start

### 1. Create a Skill

```python
from skill_framework import Skill, SkillContext

def my_skill_fn(context):
    # Access inputs
    input_val = context.get("my_input")
    
    # Process...
    result = input_val * 2
    
    # Store results
    context.set("my_output", result)
    
    return {"result": result}

skill = Skill(
    pattern_id="custom1",
    name="My Custom Skill",
    description="Does something useful",
    execute_fn=my_skill_fn
)

# Execute
context = SkillContext(inputs={"my_input": 42})
result = skill.execute(context)
print(result.output)  # {'result': 84}
```

### 2. Build a Sequence

```python
from skill_framework import SequenceBuilder

sequence = (SequenceBuilder("seq1", "My Sequence")
           .with_description("A sequence of skills")
           .add_skill(skill1)
           .add_skill(skill2)
           .add_skill(skill3)
           .build())

results = sequence.execute(context)
```

### 3. Create a Workflow

```python
from skill_framework import SkillWorkflow, WorkflowEngine, ExecutionMode

# Sequential workflow
workflow = SkillWorkflow("wf1", "My Workflow", execution_mode=ExecutionMode.SEQUENTIAL)
workflow.add_step("step1", skill1)
workflow.add_step("step2", skill2)

# Execute
engine = WorkflowEngine(verbose=True)
result = engine.execute(workflow, context)
```

### 4. Transform Across Domains

```python
from skill_framework import DomainTransformer, Domain

transformer = DomainTransformer("archetypal_patterns.json")

# Transform pattern to different domains
physical = transformer.transform_pattern("12610010", Domain.PHYSICAL)
social = transformer.transform_pattern("12610010", Domain.SOCIAL)
conceptual = transformer.transform_pattern("12610010", Domain.CONCEPTUAL)
individual = transformer.transform_pattern("12610010", Domain.PSYCHIC)
```

## Common Patterns

### Conditional Execution

```python
workflow = SkillWorkflow("adaptive", "Adaptive Workflow", 
                        execution_mode=ExecutionMode.CONDITIONAL)

workflow.add_step("check", check_skill, on_success="process", on_failure="alternative")
workflow.add_step("process", process_skill, 
                 condition=lambda ctx: ctx.get("should_process"))
workflow.add_step("alternative", alternative_skill)
```

### Error Handling

```python
# Continue on errors
sequence = (SequenceBuilder("robust", "Robust Sequence")
           .add_skills([skill1, skill2, skill3])
           .continue_on_error(True)
           .build())

# Check for failures
results = sequence.execute(context)
for i, result in enumerate(results):
    if result.is_failed:
        print(f"Step {i} failed: {result.error}")
```

### Preconditions & Postconditions

```python
def check_input(context):
    return context.has("required_field")

def validate_output(context, result):
    return result.get("success") == True

skill = Skill(
    pattern_id="validated",
    name="Validated Skill",
    description="Skill with validation",
    execute_fn=execute_fn,
    preconditions=[check_input],
    postconditions=[validate_output]
)
```

### Scoped Variables

```python
from skill_framework import ContextScope

# Global: shared across all skills
context.set("global_var", "value", ContextScope.GLOBAL)

# Sequence: shared within a sequence
context.set("seq_var", "value", ContextScope.SEQUENCE)

# Local: only current skill
context.set("local_var", "value", ContextScope.LOCAL)

# Clear between steps
context.clear_local()  # Clear local scope
context.clear_sequence()  # Clear sequence + local
```

## Integration Examples

### With Pattern Sequences

```python
import json

# Load pattern sequences
with open("pattern_sequences.json") as f:
    data = json.load(f)

for seq_data in data["sequences"]:
    # Create skills from pattern IDs
    skills = []
    for pattern_id in seq_data["patterns"]:
        skill = create_skill_from_pattern(pattern_id)
        skills.append(skill)
    
    # Build sequence
    sequence = (SequenceBuilder(str(seq_data["id"]), seq_data["heading"])
               .with_description(seq_data["description"])
               .add_skills(skills)
               .with_metadata("emergent", seq_data["emergent_phenomena"])
               .build())
```

### With NPU-253 Coprocessor

```python
from npu253 import PatternCoprocessorDriver, NPUConfig
from skill_framework import Skill

# Initialize NPU
npu = PatternCoprocessorDriver(NPUConfig())
npu.load()

# Create skill from NPU pattern
pattern = npu.query_by_id(1)

def execute_pattern(context):
    # Use pattern data
    return {
        "pattern": pattern.name,
        "solution": pattern.solution
    }

skill = Skill(
    pattern_id="apl1",
    name=pattern.name,
    description=pattern.problem,
    execute_fn=execute_pattern
)
```

### Multi-Domain Application

```python
from skill_framework import DomainTransformer, Domain

transformer = DomainTransformer("archetypal_patterns.json")

# Apply pattern across all domains
pattern_id = "12610010"
domains = [Domain.PHYSICAL, Domain.SOCIAL, Domain.CONCEPTUAL, Domain.PSYCHIC]

for domain in domains:
    # Transform pattern
    transformed = transformer.transform_pattern(pattern_id, domain)
    
    # Create domain-specific context
    context = SkillContext(domain=domain.value)
    
    # Create and execute skill
    skill = create_skill_from_transformed(transformed)
    result = skill.execute(context)
    
    print(f"{domain.value}: {result.output}")
```

## Testing

### Run Tests

```bash
# Run all tests
python3 test_skill_framework.py

# Run specific test class
python3 test_skill_framework.py TestSkill
python3 test_skill_framework.py TestSkillWorkflow
```

### Run Demos

```bash
# Run comprehensive demo
python3 demo_skill_framework.py

# Demo shows:
# 1. Basic skill execution
# 2. Skill sequences
# 3. Conditional workflows
# 4. Domain transformation
# 5. Complete multi-scale workflow
```

## Architecture

```
┌─────────────────────────────────────────┐
│           Skill Framework               │
├─────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────────┐        │
│  │  Skill   │─▶│ SkillSequence│        │
│  └──────────┘  └──────────────┘        │
│       │               │                 │
│       └───────┬───────┘                 │
│               ▼                         │
│      ┌──────────────────┐               │
│      │  SkillWorkflow   │               │
│      └──────────────────┘               │
│               │                         │
│               ▼                         │
│      ┌──────────────────┐               │
│      │ WorkflowEngine   │               │
│      └──────────────────┘               │
├─────────────────────────────────────────┤
│      ┌──────────────────┐               │
│      │  SkillContext    │               │
│      └──────────────────┘               │
│               │                         │
│      ┌────────┴─────────┐              │
│      ▼                  ▼               │
│  ┌──────────┐  ┌────────────────┐     │
│  │  State   │  │ Domain         │     │
│  │  Flow    │  │ Transformer    │     │
│  └──────────┘  └────────────────┘     │
└─────────────────────────────────────────┘
```

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Skill** | Pattern + execution function |
| **Sequence** | Ordered list of skills |
| **Workflow** | Algorithmic orchestration of sequences |
| **Context** | State and data flow between skills |
| **Domain** | Physical/Social/Conceptual/Individual |
| **Transformer** | Convert patterns across domains |

## Execution Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Sequential** | Execute skills in order | Linear workflows |
| **Conditional** | Branch based on conditions | Adaptive workflows |
| **Parallel** | Execute concurrently (future) | Independent tasks |

## Context Scopes

| Scope | Lifetime | Use Case |
|-------|----------|----------|
| **Global** | Entire workflow | Shared state |
| **Sequence** | Within sequence | Sequence state |
| **Local** | Single skill | Temporary data |

## Status Values

| Status | Meaning |
|--------|---------|
| `PENDING` | Not yet executed |
| `RUNNING` | Currently executing |
| `SUCCESS` | Completed successfully |
| `FAILED` | Execution failed |
| `SKIPPED` | Skipped due to condition |

## Best Practices

1. **Use descriptive pattern IDs** - e.g., "apl1", "12610010"
2. **Validate inputs** - Use preconditions
3. **Validate outputs** - Use postconditions
4. **Clear scopes appropriately** - Between skills/sequences
5. **Handle errors gracefully** - Use continue_on_error
6. **Document workflows** - Use descriptions and metadata
7. **Test thoroughly** - Write tests for custom skills
8. **Use domain transformation** - For cross-domain applications

## Troubleshooting

### Skill fails with precondition error
- Check that required inputs are set in context
- Verify precondition logic

### Workflow doesn't reach certain steps
- Check conditions in conditional mode
- Verify on_success/on_failure paths

### Domain transformation returns None
- Ensure pattern_id exists in archetypal_patterns.json
- Check that pattern has domain mappings

### Context variables not available
- Check variable scope (Global/Sequence/Local)
- Ensure variables set before retrieval

## Further Reading

- [Complete Documentation](skill_framework/README.md)
- [API Reference](skill_framework/README.md#api-reference)
- [Pattern Language](README.md)
- [NPU-253 Documentation](NPU253_API.md)

## Support

For issues or questions:
1. Check test suite for examples
2. Run demo script to see framework in action
3. Review pattern language documentation
4. Open an issue on GitHub
