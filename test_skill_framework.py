#!/usr/bin/env python3
"""
Test Suite for Skill Framework

Tests the generalized pattern-based workflow system.
"""

import sys
import unittest
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from skill_framework import (
    Skill, SkillResult, SkillStatus,
    SkillSequence, SequenceBuilder,
    SkillWorkflow, WorkflowEngine, ExecutionMode,
    SkillContext, ContextScope,
    DomainTransformer, Domain
)


class TestSkill(unittest.TestCase):
    """Test Skill class"""
    
    def test_create_skill(self):
        """Test creating a basic skill"""
        skill = Skill(
            pattern_id="apl1",
            name="Independent Regions",
            description="Create autonomous regions"
        )
        self.assertEqual(skill.pattern_id, "apl1")
        self.assertEqual(skill.name, "Independent Regions")
    
    def test_skill_execution(self):
        """Test executing a skill"""
        def execute_fn(context):
            return {"result": "success"}
        
        skill = Skill(
            pattern_id="test1",
            name="Test Skill",
            description="A test skill",
            execute_fn=execute_fn
        )
        
        context = SkillContext()
        result = skill.execute(context)
        
        self.assertEqual(result.status, SkillStatus.SUCCESS)
        self.assertEqual(result.output["result"], "success")
        self.assertIsNotNone(result.duration_ms)
    
    def test_skill_with_preconditions(self):
        """Test skill with preconditions"""
        def precondition(context):
            return context.has("required_input")
        
        skill = Skill(
            pattern_id="test2",
            name="Test Skill",
            description="Skill with precondition",
            preconditions=[precondition]
        )
        
        # Should fail without input
        context = SkillContext()
        result = skill.execute(context)
        self.assertEqual(result.status, SkillStatus.FAILED)
        self.assertIn("Precondition", result.error)
        
        # Should succeed with input
        context.set("required_input", True)
        result = skill.execute(context)
        self.assertEqual(result.status, SkillStatus.SUCCESS)
    
    def test_skill_with_postconditions(self):
        """Test skill with postconditions"""
        def execute_fn(context):
            return {"value": 42}
        
        def postcondition(context, result):
            return result.get("value") == 42
        
        skill = Skill(
            pattern_id="test3",
            name="Test Skill",
            description="Skill with postcondition",
            execute_fn=execute_fn,
            postconditions=[postcondition]
        )
        
        context = SkillContext()
        result = skill.execute(context)
        self.assertEqual(result.status, SkillStatus.SUCCESS)


class TestSkillContext(unittest.TestCase):
    """Test SkillContext class"""
    
    def test_context_scopes(self):
        """Test different context scopes"""
        context = SkillContext()
        
        # Set variables in different scopes
        context.set("global_var", "global", ContextScope.GLOBAL)
        context.set("seq_var", "sequence", ContextScope.SEQUENCE)
        context.set("local_var", "local", ContextScope.LOCAL)
        
        # Retrieve variables
        self.assertEqual(context.get("global_var", scope=ContextScope.GLOBAL), "global")
        self.assertEqual(context.get("seq_var", scope=ContextScope.SEQUENCE), "sequence")
        self.assertEqual(context.get("local_var", scope=ContextScope.LOCAL), "local")
    
    def test_context_clear(self):
        """Test clearing context scopes"""
        context = SkillContext()
        context.set("local_var", "value", ContextScope.LOCAL)
        context.set("seq_var", "value", ContextScope.SEQUENCE)
        
        context.clear_local()
        self.assertFalse(context.has("local_var", ContextScope.LOCAL))
        self.assertTrue(context.has("seq_var", ContextScope.SEQUENCE))
        
        context.clear_sequence()
        self.assertFalse(context.has("seq_var", ContextScope.SEQUENCE))
    
    def test_context_history(self):
        """Test execution history"""
        context = SkillContext()
        context.add_history("skill1", {"status": "success"})
        context.add_history("skill2", {"status": "success"})
        
        self.assertEqual(len(context.execution_history), 2)
        self.assertEqual(context.execution_history[0]["skill_id"], "skill1")
    
    def test_context_clone(self):
        """Test context cloning"""
        context = SkillContext()
        context.set("var1", "value1")
        context.domain = "physical"
        
        cloned = context.clone()
        cloned.set("var2", "value2")
        
        self.assertEqual(cloned.get("var1"), "value1")
        self.assertIsNone(context.get("var2"))
        self.assertEqual(cloned.domain, "physical")


class TestSkillSequence(unittest.TestCase):
    """Test SkillSequence class"""
    
    def test_create_sequence(self):
        """Test creating a sequence"""
        skill1 = Skill("test1", "Skill 1", "First skill")
        skill2 = Skill("test2", "Skill 2", "Second skill")
        
        sequence = SkillSequence(
            sequence_id="seq1",
            name="Test Sequence",
            description="A test sequence"
        )
        sequence.add_skill(skill1)
        sequence.add_skill(skill2)
        
        self.assertEqual(len(sequence), 2)
        self.assertEqual(sequence.skills[0], skill1)
    
    def test_sequence_execution(self):
        """Test executing a sequence"""
        def execute1(context):
            context.set("step1_done", True)
            return {"step": 1}
        
        def execute2(context):
            context.set("step2_done", True)
            return {"step": 2}
        
        skill1 = Skill("test1", "Skill 1", "First", execute_fn=execute1)
        skill2 = Skill("test2", "Skill 2", "Second", execute_fn=execute2)
        
        sequence = SkillSequence("seq1", "Test", "")
        sequence.add_skill(skill1).add_skill(skill2)
        
        context = SkillContext()
        results = sequence.execute(context)
        
        self.assertEqual(len(results), 2)
        self.assertTrue(results[0].is_success)
        self.assertTrue(results[1].is_success)
        self.assertTrue(context.get("step1_done"))
        self.assertTrue(context.get("step2_done"))
    
    def test_sequence_builder(self):
        """Test SequenceBuilder fluent interface"""
        skill1 = Skill("test1", "Skill 1", "First")
        skill2 = Skill("test2", "Skill 2", "Second")
        
        sequence = (SequenceBuilder("seq1", "Test Sequence")
                   .with_description("A test sequence")
                   .add_skill(skill1)
                   .add_skill(skill2)
                   .with_metadata("category", "test")
                   .continue_on_error(True)
                   .build())
        
        self.assertEqual(sequence.sequence_id, "seq1")
        self.assertEqual(len(sequence), 2)
        self.assertEqual(sequence.metadata["category"], "test")
        self.assertTrue(sequence.metadata["continue_on_error"])


class TestSkillWorkflow(unittest.TestCase):
    """Test SkillWorkflow and WorkflowEngine"""
    
    def test_create_workflow(self):
        """Test creating a workflow"""
        workflow = SkillWorkflow(
            workflow_id="wf1",
            name="Test Workflow",
            description="A test workflow"
        )
        
        skill1 = Skill("test1", "Skill 1", "First")
        skill2 = Skill("test2", "Skill 2", "Second")
        
        workflow.add_step("step1", skill1)
        workflow.add_step("step2", skill2)
        
        self.assertEqual(len(workflow.steps), 2)
        self.assertEqual(workflow.start_step, "step1")
    
    def test_sequential_workflow_execution(self):
        """Test executing a sequential workflow"""
        def execute1(context):
            context.set("step1", "done")
            return {"step": 1}
        
        def execute2(context):
            context.set("step2", "done")
            return {"step": 2}
        
        skill1 = Skill("test1", "Skill 1", "First", execute_fn=execute1)
        skill2 = Skill("test2", "Skill 2", "Second", execute_fn=execute2)
        
        workflow = SkillWorkflow("wf1", "Test", execution_mode=ExecutionMode.SEQUENTIAL)
        workflow.add_step("step1", skill1)
        workflow.add_step("step2", skill2)
        
        engine = WorkflowEngine(verbose=False)
        context = SkillContext()
        result = engine.execute(workflow, context)
        
        self.assertEqual(result["status"], "completed")
        self.assertEqual(len(result["results"]), 2)
        self.assertEqual(context.get("step1"), "done")
        self.assertEqual(context.get("step2"), "done")
    
    def test_conditional_workflow_execution(self):
        """Test conditional workflow execution"""
        def check_condition(context):
            return context.get("execute_step2", False)
        
        def execute1(context):
            context.set("step1", "done")
            context.set("execute_step2", True)
            return {"step": 1}
        
        def execute2(context):
            context.set("step2", "done")
            return {"step": 2}
        
        skill1 = Skill("test1", "Skill 1", "First", execute_fn=execute1)
        skill2 = Skill("test2", "Skill 2", "Second", execute_fn=execute2)
        
        workflow = SkillWorkflow("wf1", "Test", execution_mode=ExecutionMode.CONDITIONAL)
        workflow.add_step("step1", skill1, on_success="step2")
        workflow.add_step("step2", skill2, condition=check_condition)
        
        engine = WorkflowEngine(verbose=False)
        context = SkillContext()
        result = engine.execute(workflow, context)
        
        self.assertEqual(result["status"], "completed")
        self.assertEqual(context.get("step1"), "done")
        self.assertEqual(context.get("step2"), "done")


class TestDomainTransformer(unittest.TestCase):
    """Test DomainTransformer"""
    
    def test_create_transformer(self):
        """Test creating a transformer"""
        transformer = DomainTransformer()
        self.assertIsNotNone(transformer)
    
    def test_load_patterns(self):
        """Test loading archetypal patterns"""
        # Try to load if file exists
        patterns_path = Path(__file__).parent / "archetypal_patterns.json"
        if patterns_path.exists():
            transformer = DomainTransformer(str(patterns_path))
            self.assertGreater(len(transformer.archetypal_patterns), 0)
    
    def test_transform_pattern(self):
        """Test pattern transformation"""
        # Create mock transformer with test data
        transformer = DomainTransformer()
        transformer.archetypal_patterns["test1"] = {
            "pattern_id": "test1",
            "name": "Test Pattern",
            "archetypal_pattern": "Balance between {{domains}} is essential",
            "domain_mappings": {
                "domains": {
                    "physical": "regions",
                    "social": "communities",
                    "conceptual": "paradigms",
                    "psychic": "awareness modes"
                }
            },
            "domain_specific_content": {
                "physical": "Balance between regions is essential for development.",
                "social": "Balance between communities is essential for harmony."
            }
        }
        
        # Transform to physical domain
        result = transformer.transform_pattern("test1", Domain.PHYSICAL)
        self.assertIsNotNone(result)
        self.assertEqual(result["domain"], "physical")
        self.assertIn("regions", result["transformed_pattern"])
        
        # Transform to social domain
        result = transformer.transform_pattern("test1", Domain.SOCIAL)
        self.assertIsNotNone(result)
        self.assertIn("communities", result["transformed_pattern"])


def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(run_tests())
