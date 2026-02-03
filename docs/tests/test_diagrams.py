#!/usr/bin/env python3
"""
Test suite for diagrams/ region validation.

Validates that Mermaid diagrams are syntactically correct and provide
complete visualization coverage of the pattern language system.
"""

import os
import re
from pathlib import Path

def test_diagrams_exist():
    """Test that diagram files exist."""
    diagrams_dir = Path(__file__).parent.parent.parent / "diagrams"
    assert diagrams_dir.exists(), "diagrams/ directory should exist"
    
    diagram_files = list(diagrams_dir.glob("*.mmd"))
    assert len(diagram_files) > 0, "Should have at least one .mmd file"
    print(f"✓ Found {len(diagram_files)} diagram files")
    
def test_mermaid_syntax():
    """Test that diagrams have valid Mermaid syntax."""
    diagrams_dir = Path(__file__).parent.parent.parent / "diagrams"
    
    # Valid Mermaid diagram types
    valid_diagram_types = [
        'graph', 'flowchart', 'sequenceDiagram', 'classDiagram',
        'stateDiagram', 'erDiagram', 'journey', 'gantt', 'pie',
        'gitGraph', 'mindmap', 'timeline'
    ]
    
    errors = []
    for diagram_file in diagrams_dir.glob("*.mmd"):
        content = diagram_file.read_text()
        
        # Check for diagram type declaration
        first_line = content.split('\n')[0].strip()
        has_valid_type = any(dtype in first_line for dtype in valid_diagram_types)
        
        if not has_valid_type:
            errors.append(f"{diagram_file.name}: No valid Mermaid diagram type found")
            
    assert len(errors) == 0, f"Syntax errors: {errors}"
    print(f"✓ All diagrams have valid Mermaid syntax")
    
def test_diagram_coverage():
    """Test that diagrams cover key aspects of the system."""
    diagrams_dir = Path(__file__).parent.parent.parent / "diagrams"
    
    required_diagrams = {
        'hierarchy': False,
        'sequence': False,
        'architecture': False,
        'relationship': False,
        'transformation': False,
        'pattern': False
    }
    
    for diagram_file in diagrams_dir.glob("*.mmd"):
        name = diagram_file.stem.lower()
        for key in required_diagrams:
            if key in name:
                required_diagrams[key] = True
                
    missing = [key for key, found in required_diagrams.items() if not found]
    assert len(missing) == 0, f"Missing diagram coverage: {missing}"
    print(f"✓ All required diagram types present")
    
def test_diagrams_have_content():
    """Test that diagrams are not empty."""
    diagrams_dir = Path(__file__).parent.parent.parent / "diagrams"
    
    empty_diagrams = []
    for diagram_file in diagrams_dir.glob("*.mmd"):
        content = diagram_file.read_text().strip()
        
        # Should have more than just diagram type declaration
        lines = [line for line in content.split('\n') if line.strip() and not line.strip().startswith('%')]
        
        if len(lines) < 3:
            empty_diagrams.append(diagram_file.name)
            
    assert len(empty_diagrams) == 0, f"Empty diagrams: {empty_diagrams}"
    print(f"✓ All diagrams have substantial content")
    
def test_readme_exists():
    """Test that diagrams/ has a README."""
    diagrams_dir = Path(__file__).parent.parent.parent / "diagrams"
    readme = diagrams_dir / "README.md"
    
    assert readme.exists(), "diagrams/README.md should exist"
    
    content = readme.read_text()
    assert len(content) > 500, "README should have substantial content"
    assert 'diagram' in content.lower(), "README should explain diagrams"
    print(f"✓ README exists and documents diagrams")
    
def test_diagrams_visualize_patterns():
    """Test that diagrams reference pattern concepts."""
    diagrams_dir = Path(__file__).parent.parent.parent / "diagrams"
    
    pattern_refs = 0
    for diagram_file in diagrams_dir.glob("*.mmd"):
        content = diagram_file.read_text().lower()
        
        # Look for pattern-related terms
        if any(term in content for term in ['pattern', 'sequence', 'category', 'town', 'building']):
            pattern_refs += 1
            
    assert pattern_refs >= 5, f"Only {pattern_refs} diagrams reference patterns"
    print(f"✓ {pattern_refs} diagrams visualize pattern concepts")
    
def test_can_generate_from_diagrams():
    """Test that diagrams can theoretically be rendered."""
    diagrams_dir = Path(__file__).parent.parent.parent / "diagrams"
    
    # Check that diagrams could be processed by mermaid-cli
    valid_for_processing = 0
    
    for diagram_file in diagrams_dir.glob("*.mmd"):
        content = diagram_file.read_text()
        
        # Basic checks for processability
        has_diagram_type = any(dtype in content for dtype in ['graph', 'flowchart', 'classDiagram'])
        no_syntax_errors = '-->' in content or ':::' in content or '[' in content
        
        if has_diagram_type and (no_syntax_errors or len(content) > 100):
            valid_for_processing += 1
            
    total = len(list(diagrams_dir.glob("*.mmd")))
    assert valid_for_processing >= total * 0.8, f"Only {valid_for_processing}/{total} processable"
    print(f"✓ {valid_for_processing}/{total} diagrams can be rendered")

def run_all_tests():
    """Run all tests."""
    tests = [
        test_diagrams_exist,
        test_mermaid_syntax,
        test_diagram_coverage,
        test_diagrams_have_content,
        test_readme_exists,
        test_diagrams_visualize_patterns,
        test_can_generate_from_diagrams
    ]
    
    print("=" * 70)
    print("DIAGRAMS REGION VALIDATION")
    print("=" * 70)
    print()
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error: {e}")
            failed += 1
            
    print()
    print(f"Results: {passed} passed, {failed} failed")
    print()
    
    return failed == 0

if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
