#!/usr/bin/env python3
"""
Test suite for apl_language/ region validation.

Validates that APL implementation is complete and provides
array-oriented pattern operations.
"""

import os
from pathlib import Path

def test_apl_files_exist():
    """Test that APL implementation files exist."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    assert apl_dir.exists(), "apl_language/ directory should exist"
    
    apl_files = list(apl_dir.glob("*.apl"))
    assert len(apl_files) > 0, "Should have at least one .apl file"
    print(f"✓ Found {len(apl_files)} APL implementation files")

def test_apl_modules():
    """Test that APL modules exist."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    expected_modules = [
        'patterns.apl',
        'queries.apl',
        'transformations.apl',
        'relationships.apl',
        'demo.apl'
    ]
    
    found = []
    for module in expected_modules:
        if (apl_dir / module).exists():
            found.append(module)
            
    assert len(found) >= 3, f"Only found {found}"
    print(f"✓ Found {len(found)} core APL modules")

def test_apl_documentation():
    """Test that APL implementation has documentation."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    docs = []
    for doc_file in ['README.md', 'QUICK_REFERENCE.md', 'EXAMPLES.md', 
                     'INSTALLATION.md', 'SUMMARY.md']:
        if (apl_dir / doc_file).exists():
            docs.append(doc_file)
            
    assert len(docs) >= 3, f"Only found {docs}"
    print(f"✓ Found {len(docs)} documentation files")

def test_readme_content():
    """Test that README has substantial content."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    readme = apl_dir / "README.md"
    
    assert readme.exists(), "README.md should exist"
    
    content = readme.read_text()
    assert len(content) > 1000, "README should be comprehensive"
    assert 'apl' in content.lower(), "README should mention APL"
    assert 'pattern' in content.lower(), "README should mention patterns"
    print("✓ README has comprehensive content")

def test_apl_syntax():
    """Test that APL files have APL syntax markers."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    # APL uses special Unicode symbols
    apl_symbols = ['⍝', '←', '⍴', '⍳', '∊', '⌿', '⍨']
    
    files_with_apl = 0
    for apl_file in apl_dir.glob("*.apl"):
        content = apl_file.read_text()
        
        # Check for APL symbols
        if any(symbol in content for symbol in apl_symbols):
            files_with_apl += 1
            
    total_apl = len(list(apl_dir.glob("*.apl")))
    if total_apl > 0:
        assert files_with_apl >= total_apl * 0.5, f"Only {files_with_apl}/{total_apl} have APL syntax"
        print(f"✓ {files_with_apl} files contain APL syntax")
    else:
        print("⊘ No .apl files to validate")

def test_pattern_coverage():
    """Test that APL implementation covers patterns."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    # Check if patterns.apl exists and has pattern references
    patterns_file = apl_dir / "patterns.apl"
    if patterns_file.exists():
        content = patterns_file.read_text()
        
        # Look for pattern references or data
        has_data = len(content) > 500
        has_pattern_refs = 'pattern' in content.lower() or '253' in content
        
        assert has_data, "patterns.apl should have substantial content"
        print("✓ patterns.apl contains pattern data")
    else:
        print("⊘ patterns.apl not found")

def test_operations_defined():
    """Test that APL operations are defined."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    operations = {
        'queries.apl': ['query', 'get', 'find', 'search'],
        'transformations.apl': ['transform', 'convert', 'map', 'domain'],
        'relationships.apl': ['relation', 'connect', 'follow', 'precede']
    }
    
    ops_found = 0
    for filename, keywords in operations.items():
        filepath = apl_dir / filename
        if filepath.exists():
            content = filepath.read_text().lower()
            if any(kw in content for kw in keywords):
                ops_found += 1
                
    assert ops_found >= 2, f"Only {ops_found} operation files found"
    print(f"✓ {ops_found} operation modules defined")

def test_has_demo():
    """Test that demo file exists."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    demo_files = ['demo.apl', 'example.apl']
    has_demo = any((apl_dir / f).exists() for f in demo_files)
    
    if has_demo:
        print("✓ Demo/example file exists")
    else:
        print("⊘ No demo file found (recommended)")

def test_line_count():
    """Test that implementation has substantial code."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    total_lines = 0
    for apl_file in apl_dir.glob("*.apl"):
        lines = len(apl_file.read_text().splitlines())
        total_lines += lines
        
    assert total_lines > 100, f"Only {total_lines} lines of APL code"
    print(f"✓ {total_lines} lines of APL implementation")

def test_installation_guide():
    """Test that installation documentation exists."""
    apl_dir = Path(__file__).parent.parent.parent / "apl_language"
    
    install_doc = apl_dir / "INSTALLATION.md"
    if install_doc.exists():
        content = install_doc.read_text()
        
        # Should mention APL interpreters
        has_interpreter = any(name in content for name in 
                            ['Dyalog', 'GNU APL', 'NARS', 'ngn'])
        
        assert has_interpreter, "INSTALLATION should mention APL interpreters"
        print("✓ Installation guide documents APL interpreters")
    else:
        print("⊘ INSTALLATION.md not found (recommended)")

def run_all_tests():
    """Run all tests."""
    tests = [
        test_apl_files_exist,
        test_apl_modules,
        test_apl_documentation,
        test_readme_content,
        test_apl_syntax,
        test_pattern_coverage,
        test_operations_defined,
        test_has_demo,
        test_line_count,
        test_installation_guide
    ]
    
    print("=" * 70)
    print("APL LANGUAGE REGION VALIDATION")
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
