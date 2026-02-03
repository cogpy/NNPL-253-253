#!/usr/bin/env python3
"""
Test suite for APL Pattern Language implementation.
Validates the APL code structure and demonstrates usage.
"""

import subprocess
from pathlib import Path


def check_file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    path = Path(filepath)
    exists = path.exists()
    print(f"  {'✓' if exists else '✗'} {filepath}")
    return exists


def test_file_structure():
    """Test that all APL files are present."""
    print("\n" + "=" * 70)
    print("TEST: File Structure")
    print("=" * 70)
    
    files = [
        'apl_language/README.md',
        'apl_language/patterns.apl',
        'apl_language/queries.apl',
        'apl_language/transformations.apl',
        'apl_language/relationships.apl',
        'apl_language/demo.apl',
        'apl_language/data_loader.apl',
    ]
    
    all_exist = True
    for f in files:
        if not check_file_exists(f):
            all_exist = False
    
    print(f"\nResult: {'PASS' if all_exist else 'FAIL'}")
    return all_exist


def test_apl_syntax():
    """Test APL file syntax (basic checks)."""
    print("\n" + "=" * 70)
    print("TEST: APL Syntax")
    print("=" * 70)
    
    files = [
        'apl_language/patterns.apl',
        'apl_language/queries.apl',
        'apl_language/transformations.apl',
        'apl_language/relationships.apl',
        'apl_language/demo.apl',
        'apl_language/data_loader.apl',
    ]
    
    all_valid = True
    for filepath in files:
        try:
            path = Path(filepath)
            if not path.exists():
                print(f"  ✗ {filepath} - File not found")
                all_valid = False
                continue
                
            content = path.read_text(encoding='utf-8')
            
            # Basic syntax checks
            checks = {
                'Has nabla functions': '∇' in content,
                'Has assignment': '←' in content,
                'Has comments': '⍝' in content,
                'Non-empty': len(content) > 0,
            }
            
            file_valid = all(checks.values())
            status = '✓' if file_valid else '✗'
            print(f"  {status} {filepath}")
            
            for check_name, result in checks.items():
                if not result:
                    print(f"      ✗ {check_name}")
                    all_valid = False
                    
        except Exception as e:
            print(f"  ✗ {filepath} - Error: {e}")
            all_valid = False
    
    print(f"\nResult: {'PASS' if all_valid else 'FAIL'}")
    return all_valid


def test_module_structure():
    """Test module structure."""
    print("\n" + "=" * 70)
    print("TEST: Module Structure")
    print("=" * 70)
    
    # Check patterns.apl
    patterns_path = Path('apl_language/patterns.apl')
    if patterns_path.exists():
        content = patterns_path.read_text(encoding='utf-8')
        
        required_functions = [
            'InitializePatterns',
            'StorePattern',
            'GetPatternByID',
            'GetPatternCategory',
            'GetPatternIDsByCategory',
        ]
        
        all_found = True
        for func in required_functions:
            # Check for various function signature patterns
            found = (f'∇ {func}' in content or 
                    f'∇ result ← {func}' in content or 
                    f'∇ pattern ← {func}' in content or
                    f'∇ category ← {func}' in content or
                    f'∇ ids ← {func}' in content or
                    f'∇ count ← {func}' in content)
            status = '✓' if found else '✗'
            print(f"  {status} Function: {func}")
            if not found:
                all_found = False
        
        print(f"\nResult: {'PASS' if all_found else 'FAIL'}")
        return all_found
    else:
        print("  ✗ patterns.apl not found")
        return False


def test_data_loader():
    """Test data loader module."""
    print("\n" + "=" * 70)
    print("TEST: Data Loader")
    print("=" * 70)
    
    data_path = Path('apl_language/data_loader.apl')
    if data_path.exists():
        content = data_path.read_text(encoding='utf-8')
        
        required_functions = [
            'LoadAllPatternData',
            'LoadMainPatterns',
            'LoadSequences',
            'LoadArchetypalPatterns',
            'LoadRelationships',
        ]
        
        all_found = True
        for func in required_functions:
            found = f'∇ {func}' in content or f'∇ result ← {func}' in content
            status = '✓' if found else '✗'
            print(f"  {status} Function: {func}")
            if not found:
                all_found = False
        
        # Check that it has pattern data
        has_data = 'StorePattern' in content
        print(f"  {'✓' if has_data else '✗'} Contains pattern data")
        
        result = all_found and has_data
        print(f"\nResult: {'PASS' if result else 'FAIL'}")
        return result
    else:
        print("  ✗ data_loader.apl not found")
        return False


def test_documentation():
    """Test documentation completeness."""
    print("\n" + "=" * 70)
    print("TEST: Documentation")
    print("=" * 70)
    
    readme_path = Path('apl_language/README.md')
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')
        
        required_sections = [
            'Overview',
            'Features',
            'Usage',
            'APL Language Basics',
            'Data Structures',
            'Examples',
        ]
        
        all_found = True
        for section in required_sections:
            found = section in content
            status = '✓' if found else '✗'
            print(f"  {status} Section: {section}")
            if not found:
                all_found = False
        
        print(f"\nResult: {'PASS' if all_found else 'FAIL'}")
        return all_found
    else:
        print("  ✗ README.md not found")
        return False


def count_lines_of_code():
    """Count lines of code."""
    print("\n" + "=" * 70)
    print("STATISTICS: Lines of Code")
    print("=" * 70)
    
    files = [
        'apl_language/patterns.apl',
        'apl_language/queries.apl',
        'apl_language/transformations.apl',
        'apl_language/relationships.apl',
        'apl_language/demo.apl',
        'apl_language/data_loader.apl',
    ]
    
    total_lines = 0
    total_code = 0
    total_comments = 0
    
    for filepath in files:
        path = Path(filepath)
        if not path.exists():
            continue
            
        content = path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        code_lines = 0
        comment_lines = 0
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('⍝'):
                comment_lines += 1
            else:
                code_lines += 1
        
        file_lines = len(lines)
        total_lines += file_lines
        total_code += code_lines
        total_comments += comment_lines
        
        print(f"  {path.name:30} {file_lines:5} lines ({code_lines:4} code, {comment_lines:4} comments)")
    
    print(f"  {'-'*30} {'-'*5} {'='*30}")
    print(f"  {'TOTAL':30} {total_lines:5} lines ({total_code:4} code, {total_comments:4} comments)")


def main():
    """Run all tests."""
    print("\n" + "╔" + "=" * 68 + "╗")
    print("║  APL Pattern Language Implementation - Test Suite" + " " * 18 + "║")
    print("╚" + "=" * 68 + "╝")
    
    tests = [
        test_file_structure,
        test_apl_syntax,
        test_module_structure,
        test_data_loader,
        test_documentation,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"\nTest failed with error: {e}")
            results.append(False)
    
    count_lines_of_code()
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    passed = sum(results)
    total = len(results)
    
    print(f"  Tests passed: {passed}/{total}")
    print(f"  Success rate: {100 * passed / total:.1f}%")
    
    if all(results):
        print("\n  ✓ All tests passed!")
        return 0
    else:
        print("\n  ✗ Some tests failed")
        return 1


if __name__ == '__main__':
    exit(main())
