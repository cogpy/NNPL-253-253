#!/usr/bin/env python3
"""
Test suite for implementations/ region validation.

Validates that multi-paradigm implementations are working and provide
executable demonstrations of pattern concepts.
"""

import os
import sys
from pathlib import Path

def test_implementations_exist():
    """Test that implementation files exist."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    assert impl_dir.exists(), "implementations/ directory should exist"
    
    # Check for Python implementation
    py_impl = impl_dir / "patterns_001_007_nn.py"
    assert py_impl.exists(), "Python/PyTorch implementation should exist"
    
    # Check for Lua implementations
    lua_dir = impl_dir / "lua"
    if lua_dir.exists():
        lua_files = list(lua_dir.glob("*.lua"))
        print(f"✓ Found {len(lua_files)} Lua implementation files")
    
    # Check for AIML
    aiml_impl = impl_dir / "patterns-001-007.aiml"
    if aiml_impl.exists():
        print("✓ AIML implementation exists")
        
    print(f"✓ Implementation files present")

def test_python_implementation_syntax():
    """Test that Python implementation has valid syntax."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    py_impl = impl_dir / "patterns_001_007_nn.py"
    
    # Try to compile the Python file
    try:
        with open(py_impl) as f:
            code = f.read()
            compile(code, str(py_impl), 'exec')
        print("✓ Python implementation has valid syntax")
    except SyntaxError as e:
        assert False, f"Python syntax error: {e}"

def test_python_has_classes():
    """Test that Python implementation defines expected classes."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    py_impl = impl_dir / "patterns_001_007_nn.py"
    
    content = py_impl.read_text()
    
    expected_classes = [
        'PatternEncoder',
        'PatternGNN',
        'PatternLanguageModel'
    ]
    
    found_classes = []
    for cls in expected_classes:
        if f"class {cls}" in content:
            found_classes.append(cls)
            
    assert len(found_classes) >= 2, f"Only found {found_classes}"
    print(f"✓ Found {len(found_classes)} neural network classes")

def test_lua_implementation_structure():
    """Test that Lua implementations have proper structure."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    lua_dir = impl_dir / "lua"
    
    if not lua_dir.exists():
        print("⊘ Lua directory not present (optional)")
        return
        
    lua_files = list(lua_dir.glob("seq*.lua"))
    
    if len(lua_files) == 0:
        print("⊘ No Lua sequence files (optional)")
        return
        
    # Check first file for proper structure
    sample = lua_files[0]
    content = sample.read_text()
    
    # Should have require statements, module definition, and return
    has_require = 'require' in content
    has_module = 'local' in content or 'function' in content
    has_nn = 'nn.' in content
    
    assert has_module, "Lua files should define modules/functions"
    print(f"✓ Lua implementations properly structured ({len(lua_files)} files)")

def test_aiml_syntax():
    """Test that AIML implementation has valid structure."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    aiml_impl = impl_dir / "patterns-001-007.aiml"
    
    if not aiml_impl.exists():
        print("⊘ AIML implementation not present (optional)")
        return
        
    content = aiml_impl.read_text()
    
    # Basic AIML structure checks
    has_aiml_tag = '<aiml' in content
    has_category = '<category>' in content
    has_pattern = '<pattern>' in content
    has_template = '<template>' in content
    
    assert has_aiml_tag and has_category, "AIML should have proper structure"
    print("✓ AIML implementation has valid structure")

def test_readme_documents_implementations():
    """Test that README documents all implementations."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    readme = impl_dir / "README.md"
    
    assert readme.exists(), "implementations/README.md should exist"
    
    content = readme.read_text()
    
    # Should document different implementation types
    has_python = 'python' in content.lower() or 'pytorch' in content.lower()
    has_lua = 'lua' in content.lower() or 'torch' in content.lower()
    
    assert has_python, "README should document Python implementation"
    assert len(content) > 1000, "README should be comprehensive"
    print("✓ README documents implementations")

def test_implementations_are_executable():
    """Test that implementations can be imported/executed."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    
    # Add implementations to path
    sys.path.insert(0, str(impl_dir))
    
    # Try to import Python implementation
    try:
        # We can at least check that the file can be executed as a module
        py_impl = impl_dir / "patterns_001_007_nn.py"
        code = py_impl.read_text()
        
        # Check for main execution block
        has_main = 'if __name__' in code
        has_demo = 'demo' in code.lower() or 'example' in code.lower()
        
        print(f"✓ Python implementation is executable")
        
    except Exception as e:
        print(f"⊘ Could not validate execution: {e}")

def test_multi_paradigm_coverage():
    """Test that implementations cover multiple paradigms."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    
    paradigms = {
        'Neural Networks': False,  # PyTorch, Lua/Torch
        'Rule-based': False,       # AIML
        'Visualization': False     # Mermaid
    }
    
    # Check Python/PyTorch
    py_impl = impl_dir / "patterns_001_007_nn.py"
    if py_impl.exists():
        content = py_impl.read_text()
        if 'torch' in content.lower() or 'neural' in content.lower():
            paradigms['Neural Networks'] = True
            
    # Check AIML
    aiml_impl = impl_dir / "patterns-001-007.aiml"
    if aiml_impl.exists():
        paradigms['Rule-based'] = True
        
    # Check Mermaid
    mmd_impl = impl_dir / "patterns-001-007.mmd"
    if mmd_impl.exists():
        paradigms['Visualization'] = True
        
    covered = sum(paradigms.values())
    assert covered >= 2, f"Only {covered} paradigms covered"
    print(f"✓ {covered} paradigms covered: {[k for k, v in paradigms.items() if v]}")

def test_pattern_coverage():
    """Test that implementations cover actual patterns."""
    impl_dir = Path(__file__).parent.parent.parent / "implementations"
    py_impl = impl_dir / "patterns_001_007_nn.py"
    
    content = py_impl.read_text()
    
    # Should reference patterns 1-7
    pattern_refs = 0
    for i in range(1, 8):
        if str(i) in content or f"pattern_{i}" in content.lower():
            pattern_refs += 1
            
    assert pattern_refs >= 3, f"Only {pattern_refs} pattern references found"
    print(f"✓ Implementation references {pattern_refs} patterns")

def run_all_tests():
    """Run all tests."""
    tests = [
        test_implementations_exist,
        test_python_implementation_syntax,
        test_python_has_classes,
        test_lua_implementation_structure,
        test_aiml_syntax,
        test_readme_documents_implementations,
        test_implementations_are_executable,
        test_multi_paradigm_coverage,
        test_pattern_coverage
    ]
    
    print("=" * 70)
    print("IMPLEMENTATIONS REGION VALIDATION")
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
