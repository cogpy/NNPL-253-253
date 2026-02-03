#!/usr/bin/env python3
"""
Integration test for Optimal Grip implementation

Tests all components working together:
- Datalog queries
- Salience engine
- API endpoints
- Data consistency
"""

import json
import sys

def test_datalog():
    """Test Datalog query system"""
    print("Testing Datalog Query System...")
    try:
        # Import separately to avoid conflicts
        import demo_datalog_queries
        
        # Just verify the module loads and has expected components
        assert hasattr(demo_datalog_queries, 'PatternLanguageQuerySystem'), \
            "Missing PatternLanguageQuerySystem class"
        
        # Create instance (this tests the basic functionality)
        system = demo_datalog_queries.PatternLanguageQuerySystem(
            'pattern_language_generated.json'
        )
        
        assert len(system.patterns) == 253, "Should load 253 patterns"
        print(f"  ✓ Loaded {len(system.patterns)} patterns")
        print(f"  ✓ Datalog system initialized successfully")
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_salience_engine():
    """Test ML salience engine"""
    print("Testing Salience Engine...")
    try:
        from pattern_salience_engine import PatternSalienceEngine, PatternContext
        
        # Create engine
        engine = PatternSalienceEngine('pattern_language_generated.json')
        
        # Test salience scoring
        context = PatternContext(
            focus_patterns={'apl1', 'apl2'},
            current_category='Towns'
        )
        
        scores = engine.rank_patterns_by_salience(context, limit=10)
        assert len(scores) > 0, "Should return salience scores"
        assert scores[0].score > 0, "Top score should be positive"
        print(f"  ✓ Computed salience for {len(scores)} patterns")
        
        # Test gestalt detection
        pattern_set = ['apl1', 'apl2', 'apl3', 'apl4', 'apl5']
        gestalts = engine.detect_gestalt_patterns(pattern_set, threshold=0.5)
        print(f"  ✓ Detected {len(gestalts)} gestalt clusters")
        
        # Test emergence tracking
        sequence = ['apl1', 'apl2', 'apl3']
        emergence = engine.track_emergence(sequence)
        assert 'emergence_score' in emergence, "Should return emergence data"
        print(f"  ✓ Tracked emergence (score: {emergence['emergence_score']:.2f})")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_api_structure():
    """Test API structure without running server"""
    print("Testing API Structure...")
    try:
        from pattern_api import app
        
        # Check endpoints exist
        routes = [route.path for route in app.routes]
        required_endpoints = [
            '/patterns',
            '/patterns/{pattern_id}',
            '/salience',
            '/gestalt',
            '/emergence',
            '/categories',
            '/health'
        ]
        
        for endpoint in required_endpoints:
            assert endpoint in routes, f"Missing endpoint: {endpoint}"
        
        print(f"  ✓ All {len(required_endpoints)} endpoints defined")
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def test_data_consistency():
    """Test data consistency across components"""
    print("Testing Data Consistency...")
    try:
        # Load pattern data
        with open('pattern_language_generated.json', 'r') as f:
            data = json.load(f)
        
        patterns = data.get('patterns', [])
        assert len(patterns) == 253, f"Should have 253 patterns, got {len(patterns)}"
        print(f"  ✓ Pattern data: {len(patterns)} patterns")
        
        # Check category files
        categories = ['category_towns.json', 'category_buildings.json', 'category_construction.json']
        total = 0
        for cat_file in categories:
            with open(cat_file, 'r') as f:
                cat_data = json.load(f)
                count = len(cat_data.get('patterns', []))
                total += count
                print(f"  ✓ {cat_file}: {count} patterns")
        
        assert total == 253, f"Category totals should be 253, got {total}"
        
        # Check pattern structure
        sample = patterns[0]
        required_fields = ['id', 'number', 'name', 'problem', 'solution', 
                          'preceding_patterns', 'following_patterns']
        for field in required_fields:
            assert field in sample, f"Pattern missing field: {field}"
        
        print(f"  ✓ Pattern structure validated")
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def test_visualization_exists():
    """Test visualization file exists and has content"""
    print("Testing Visualization...")
    try:
        import os
        
        assert os.path.exists('pattern_explorer.html'), "Visualization file missing"
        
        with open('pattern_explorer.html', 'r') as f:
            content = f.read()
        
        # Check for key components
        assert 'd3js.org/d3' in content, "Missing D3.js import"
        assert 'API_BASE' in content, "Missing API configuration"
        assert 'createVisualization' in content, "Missing visualization code"
        
        print(f"  ✓ Visualization file present ({len(content)} bytes)")
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    """Run all tests"""
    print("="*70)
    print("Optimal Grip Implementation - Integration Tests")
    print("="*70)
    print()
    
    tests = [
        test_data_consistency,
        test_salience_engine,
        test_datalog,
        test_api_structure,
        test_visualization_exists,
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
        print()
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print("="*70)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed!")
        print("="*70)
        return 0
    else:
        print("✗ Some tests failed")
        print("="*70)
        return 1


if __name__ == '__main__':
    sys.exit(main())
