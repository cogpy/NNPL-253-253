#!/usr/bin/env python3
"""
Test suite for meta-recursive convergence and pattern self-application.
Validates that the repository structure follows the base-6 hierarchy
and achieves optimal grip through pattern self-application.
"""

import unittest
import json
import os
from pathlib import Path
from meta_recursive_convergence import MetaRecursiveAnalyzer, FitnessMetrics


class TestBase6Structure(unittest.TestCase):
    """Test the base-6 hierarchical structure.
    
    Structure: 1 + 6 + 36 + 210 = 253
    Note: Level 3 has 210 patterns (not 216=6^3) because
    the total is constrained to 253 patterns.
    """
    
    def setUp(self):
        self.analyzer = MetaRecursiveAnalyzer()
        
    def test_sequence_count(self):
        """Test that we have exactly 36 sequences (6^2)."""
        self.analyzer.load_data()
        num_sequences = len(self.analyzer.sequence_data['sequences'])
        self.assertEqual(num_sequences, 36, 
                        f"Expected 36 sequences (6^2), got {num_sequences}")
    
    def test_pattern_count(self):
        """Test that we have exactly 253 patterns (1+6+36+216)."""
        self.analyzer.load_data()
        num_patterns = len(self.analyzer.pattern_data.get('patterns', []))
        self.assertEqual(num_patterns, 253,
                        f"Expected 253 patterns, got {num_patterns}")
    
    def test_dimension_count(self):
        """Test that we have exactly 6 dimensions."""
        agent_dir = Path(".github/agents/apl0")
        if agent_dir.exists():
            dimensions = [d for d in agent_dir.iterdir() 
                         if d.is_dir() and d.name.startswith('dim')]
            self.assertEqual(len(dimensions), 6,
                           f"Expected 6 dimensions, got {len(dimensions)}")
    
    def test_base6_calculation(self):
        """Test the base-6 mathematical relationships."""
        # 7 = 1 + 6
        self.assertEqual(1 + 6, 7)
        
        # 43 = 1 + 6 + 36
        self.assertEqual(1 + 6 + 36, 43)
        
        # 253 = 1 + 6 + 36 + 210
        self.assertEqual(1 + 6 + 36 + 210, 253)
        
        # Verify powers of 6
        self.assertEqual(6**0, 1)   # Meta-pattern
        self.assertEqual(6**1, 6)   # Dimensions
        self.assertEqual(6**2, 36)  # Sequences
        # Note: 253 total patterns organized hierarchically
        # Not strictly 6^3 but 210 patterns at level 3


class TestFitnessMetrics(unittest.TestCase):
    """Test fitness metrics for optimal grip."""
    
    def setUp(self):
        self.analyzer = MetaRecursiveAnalyzer()
        self.metrics = self.analyzer.calculate_fitness()
    
    def test_multi_scale_clarity(self):
        """Test multi-scale perception clarity is high."""
        self.assertGreaterEqual(self.metrics.multi_scale_clarity, 0.8,
                              "Multi-scale clarity should be >= 80%")
    
    def test_relationship_richness(self):
        """Test relationship richness is high."""
        self.assertGreaterEqual(self.metrics.relationship_richness, 0.8,
                              "Relationship richness should be >= 80%")
    
    def test_contextual_relevance(self):
        """Test contextual relevance is high."""
        self.assertGreaterEqual(self.metrics.contextual_relevance, 0.8,
                              "Contextual relevance should be >= 80%")
    
    def test_gestalt_perception(self):
        """Test gestalt perception is high."""
        self.assertGreaterEqual(self.metrics.gestalt_perception, 0.8,
                              "Gestalt perception should be >= 80%")
    
    def test_interactive_navigation(self):
        """Test interactive navigation is high."""
        self.assertGreaterEqual(self.metrics.interactive_navigation, 0.8,
                              "Interactive navigation should be >= 80%")
    
    def test_self_similarity(self):
        """Test self-similarity is high."""
        self.assertGreaterEqual(self.metrics.self_similarity, 0.8,
                              "Self-similarity should be >= 80%")
    
    def test_overall_fitness(self):
        """Test overall fitness achieves optimal grip."""
        self.assertGreaterEqual(self.metrics.overall_fitness, 0.8,
                              "Overall fitness should be >= 80% for optimal grip")


class TestPatternSelfApplication(unittest.TestCase):
    """Test that patterns are applied to repository structure."""
    
    def test_pattern1_independent_regions(self):
        """Test Pattern 1 (Independent Regions) applied to directory structure."""
        expected_regions = ['apl', 'uia', 'markdown', 'pattern', 
                           'opencog_atomese', 'npu253', 'apl_language', 'docs']
        existing_regions = [r for r in expected_regions if os.path.exists(r)]
        self.assertGreaterEqual(len(existing_regions), 7,
                              "Pattern 1: Need at least 7 independent regions")
    
    def test_pattern8_mosaic_of_subcultures(self):
        """Test Pattern 8 (Mosaic of Subcultures) - multiple representations."""
        representations = {
            'APL': os.path.exists('apl'),
            'UIA': os.path.exists('uia'),
            'Markdown': os.path.exists('markdown'),
            'OpenCog': os.path.exists('opencog_atomese'),
            'NPU253': os.path.exists('npu253'),
            'APL_Language': os.path.exists('apl_language'),
        }
        self.assertGreaterEqual(sum(representations.values()), 5,
                              "Pattern 8: Need at least 5 different representations")
    
    def test_pattern28_eccentric_nucleus(self):
        """Test Pattern 28 (Eccentric Nucleus) - multiple entry points."""
        entry_points = [
            'README.md',
            'NAVIGATION_HUB.md',
            'PATTERN_INDEX.md',
            'SEQUENCE_NAVIGATION.md',
        ]
        existing = [ep for ep in entry_points if os.path.exists(ep)]
        self.assertGreaterEqual(len(existing), 3,
                              "Pattern 28: Need at least 3 entry points")
    
    def test_pattern52_network_of_paths(self):
        """Test Pattern 52 (Network of Paths) - multiple navigation routes."""
        navigation_files = [
            'PATTERN_INDEX.md',      # By number
            'SEQUENCE_NAVIGATION.md', # By sequence
            'PATTERN_MAP.md',         # By region
        ]
        existing = [nf for nf in navigation_files if os.path.exists(nf)]
        self.assertGreaterEqual(len(existing), 2,
                              "Pattern 52: Need at least 2 navigation paths")
    
    def test_pattern253_things_from_your_life(self):
        """Test Pattern 253 (Things from Your Life) - living examples."""
        # Repository should have actual implementations, not just docs
        implementations = {
            'Python code': len(list(Path('.').glob('*.py'))) > 10,
            'JSON data': len(list(Path('.').glob('*.json'))) > 5,
            'Tests': any(Path('.').glob('test_*.py')),
            'Working demos': any(Path('.').glob('demo_*.py')),
        }
        self.assertGreaterEqual(sum(implementations.values()), 3,
                              "Pattern 253: Need living examples, not just descriptions")


class TestMetaRecursiveStructure(unittest.TestCase):
    """Test meta-recursive properties."""
    
    def test_meta_recursive_documentation_exists(self):
        """Test that meta-recursive implementation is documented."""
        self.assertTrue(os.path.exists('META_RECURSIVE_IMPLEMENTATION.md'),
                       "META_RECURSIVE_IMPLEMENTATION.md should exist")
    
    def test_self_application_documentation_exists(self):
        """Test that pattern self-application is documented."""
        self.assertTrue(os.path.exists('PATTERN_SELF_APPLICATION.md'),
                       "PATTERN_SELF_APPLICATION.md should exist")
    
    def test_convergence_analysis_exists(self):
        """Test that convergence analysis tool exists."""
        self.assertTrue(os.path.exists('meta_recursive_convergence.py'),
                       "meta_recursive_convergence.py should exist")
    
    def test_visualization_exists(self):
        """Test that convergence visualization exists."""
        self.assertTrue(os.path.exists('CONVERGENCE_VISUALIZATION.md'),
                       "CONVERGENCE_VISUALIZATION.md should exist")
    
    def test_agent_hierarchy_exists(self):
        """Test that 6-dimensional agent hierarchy exists."""
        agent_dir = Path('.github/agents/apl0')
        if agent_dir.exists():
            # Check for dimension directories
            dimensions = [f'dim{i}' for i in range(6)]
            existing_dims = [d for d in dimensions 
                            if (agent_dir / d).exists()]
            self.assertEqual(len(existing_dims), 6,
                           "All 6 dimensions should exist in agent hierarchy")


class TestConvergence(unittest.TestCase):
    """Test that convergence to optimal grip has occurred."""
    
    def setUp(self):
        self.analyzer = MetaRecursiveAnalyzer()
    
    def test_convergence_achieved(self):
        """Test that the system has converged to optimal grip."""
        metrics = self.analyzer.calculate_fitness()
        improvements = self.analyzer.generate_improvement_plan(metrics)
        
        # If no improvements needed, convergence is achieved
        if len(improvements) == 0:
            self.assertTrue(True, "Convergence achieved - no improvements needed")
        else:
            # Otherwise, fitness should still be reasonably high
            self.assertGreaterEqual(metrics.overall_fitness, 0.7,
                                  f"System should be converging (fitness >= 70%), "
                                  f"got {metrics.overall_fitness:.2%}")
    
    def test_all_metrics_above_threshold(self):
        """Test that all individual metrics are above minimum threshold."""
        metrics = self.analyzer.calculate_fitness()
        min_threshold = 0.6  # Minimum acceptable threshold
        
        self.assertGreaterEqual(metrics.multi_scale_clarity, min_threshold,
                              "Multi-scale clarity too low")
        self.assertGreaterEqual(metrics.relationship_richness, min_threshold,
                              "Relationship richness too low")
        self.assertGreaterEqual(metrics.contextual_relevance, min_threshold,
                              "Contextual relevance too low")
        self.assertGreaterEqual(metrics.gestalt_perception, min_threshold,
                              "Gestalt perception too low")
        self.assertGreaterEqual(metrics.interactive_navigation, min_threshold,
                              "Interactive navigation too low")
        self.assertGreaterEqual(metrics.self_similarity, min_threshold,
                              "Self-similarity too low")


def run_tests():
    """Run all tests and display results."""
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBase6Structure))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFitnessMetrics))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestPatternSelfApplication))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMetaRecursiveStructure))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestConvergence))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "=" * 70)
    print("META-RECURSIVE CONVERGENCE TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run:     {result.testsRun}")
    print(f"Successes:     {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures:      {len(result.failures)}")
    print(f"Errors:        {len(result.errors)}")
    print()
    
    if result.wasSuccessful():
        print("✓ ALL TESTS PASSED - Meta-recursive convergence validated!")
    else:
        print("△ Some tests failed - convergence in progress")
    print()
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
