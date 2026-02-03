#!/usr/bin/env python3
"""
Test suite for docs/ region validation.

Validates that the docs/ region provides formal specifications,
architecture documentation, and technical reference materials.
"""

import os
from pathlib import Path

def test_docs_directory_exists():
    """Test that docs directory exists."""
    docs_dir = Path(__file__).parent.parent
    assert docs_dir.exists(), "docs/ directory should exist"
    assert docs_dir.is_dir(), "docs/ should be a directory"
    print("✓ docs/ directory exists")

def test_readme_exists():
    """Test that docs/README.md exists."""
    docs_dir = Path(__file__).parent.parent
    readme = docs_dir / "README.md"
    
    assert readme.exists(), "docs/README.md should exist"
    content = readme.read_text()
    assert len(content) > 1000, "README should be comprehensive"
    print("✓ docs/README.md exists and is comprehensive")

def test_formal_specifications():
    """Test that Z++ formal specifications exist."""
    docs_dir = Path(__file__).parent.parent
    
    zpp_files = list(docs_dir.glob("*.zpp"))
    assert len(zpp_files) >= 3, f"Should have at least 3 .zpp files, found {len(zpp_files)}"
    
    # Check for key specification files
    expected_specs = ['data_model.zpp', 'operations.zpp', 'system_state.zpp']
    found_specs = [f.name for f in zpp_files]
    
    for spec in expected_specs:
        if spec in found_specs:
            print(f"  ✓ {spec} exists")
            
    print(f"✓ Found {len(zpp_files)} Z++ formal specification files")

def test_architecture_docs():
    """Test that architecture documentation exists."""
    docs_dir = Path(__file__).parent.parent
    
    arch_doc = docs_dir / "architecture_overview.md"
    if arch_doc.exists():
        content = arch_doc.read_text()
        assert len(content) > 500, "Architecture doc should be substantial"
        print("✓ architecture_overview.md exists")
    else:
        print("⊘ architecture_overview.md not found (recommended)")

def test_zpp_files_have_schemas():
    """Test that Z++ files contain schema definitions."""
    docs_dir = Path(__file__).parent.parent
    
    schemas_found = 0
    for zpp_file in docs_dir.glob("*.zpp"):
        content = zpp_file.read_text()
        
        # Look for Z++ schema markers
        if '::' in content or 'where' in content or 'schema' in content.lower():
            schemas_found += 1
            
    assert schemas_found >= 3, f"Only {schemas_found} files contain schemas"
    print(f"✓ {schemas_found} Z++ files contain schema definitions")

def test_subdirectories():
    """Test that expected subdirectories exist."""
    docs_dir = Path(__file__).parent.parent
    
    expected_dirs = ['tests', 'examples', 'summaries']
    found_dirs = []
    
    for dirname in expected_dirs:
        dirpath = docs_dir / dirname
        if dirpath.exists() and dirpath.is_dir():
            found_dirs.append(dirname)
            
    assert len(found_dirs) >= 2, f"Only found {found_dirs}"
    print(f"✓ Found subdirectories: {', '.join(found_dirs)}")

def test_pdfs_for_reference():
    """Test that reference PDFs exist."""
    docs_dir = Path(__file__).parent.parent
    
    pdfs = list(docs_dir.glob("*.pdf"))
    if len(pdfs) > 0:
        print(f"✓ Found {len(pdfs)} reference PDF documents")
    else:
        print("⊘ No PDFs found (optional)")

def test_timeless_way_docs():
    """Test that Timeless Way documentation exists."""
    docs_dir = Path(__file__).parent.parent
    
    timeless = docs_dir / "The Timeless Way.md"
    if timeless.exists():
        content = timeless.read_text()
        assert len(content) > 500, "Timeless Way doc should be substantial"
        print("✓ The Timeless Way.md exists")
    else:
        print("⊘ The Timeless Way.md not found (optional)")

def test_line_count():
    """Test that formal specifications have substantial content."""
    docs_dir = Path(__file__).parent.parent
    
    total_lines = 0
    for zpp_file in docs_dir.glob("*.zpp"):
        lines = len(zpp_file.read_text().splitlines())
        total_lines += lines
        
    assert total_lines > 1000, f"Only {total_lines} lines of formal specs"
    print(f"✓ {total_lines} lines of Z++ formal specifications")

def test_integration_coverage():
    """Test that integrations.zpp exists."""
    docs_dir = Path(__file__).parent.parent
    
    integrations = docs_dir / "integrations.zpp"
    if integrations.exists():
        content = integrations.read_text()
        
        # Should cover file system, JSON, markdown
        has_filesystem = 'file' in content.lower()
        has_json = 'json' in content.lower()
        
        if has_filesystem and has_json:
            print("✓ integrations.zpp covers external systems")
    else:
        print("⊘ integrations.zpp not found (recommended)")

def run_all_tests():
    """Run all tests."""
    tests = [
        test_docs_directory_exists,
        test_readme_exists,
        test_formal_specifications,
        test_architecture_docs,
        test_zpp_files_have_schemas,
        test_subdirectories,
        test_pdfs_for_reference,
        test_timeless_way_docs,
        test_line_count,
        test_integration_coverage
    ]
    
    print("=" * 70)
    print("DOCS REGION VALIDATION")
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
