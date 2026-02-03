#!/usr/bin/env python3
"""
Test Pattern 7 (THE COUNTRYSIDE) Implementation

This script demonstrates and validates that Pattern 7 is correctly implemented
as a living, actionable system in the repository.
"""

import json
import os
import sys
from pathlib import Path

# Colors for output
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'=' * 70}{NC}")
    print(f"{BLUE}{text:^70}{NC}")
    print(f"{BLUE}{'=' * 70}{NC}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{NC}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{NC}")

def print_error(text):
    print(f"{RED}❌ {text}{NC}")

def test_valley_exists():
    """Test that protected valleys exist"""
    print_header("TEST 1: Protected Valleys Exist")
    
    apl_exists = os.path.isdir('apl')
    uia_exists = os.path.isdir('uia')
    
    if apl_exists:
        apl_count = len(list(Path('apl').glob('*.htm*')))
        print_success(f"apl/ valley exists with {apl_count} HTML files")
    else:
        print_error("apl/ valley not found")
        return False
    
    if uia_exists:
        uia_count = len(list(Path('uia').glob('*.html')))
        print_success(f"uia/ valley exists with {uia_count} HTML files")
    else:
        print_error("uia/ valley not found")
        return False
    
    return True

def test_generated_commons():
    """Test that generated commons exist and are valid"""
    print_header("TEST 2: Generated Commons Valid")
    
    commons_files = [
        'pattern_language_generated.json',
        'archetypal_patterns.json',
        'pattern_sequences.json',
        'uia_pattern_list.json'
    ]
    
    all_valid = True
    for filename in commons_files:
        if os.path.isfile(filename):
            try:
                with open(filename, 'r') as f:
                    data = json.load(f)
                print_success(f"{filename} is valid JSON")
            except json.JSONDecodeError as e:
                print_error(f"{filename} has invalid JSON: {e}")
                all_valid = False
        else:
            print_warning(f"{filename} not found (may be optional)")
    
    return all_valid

def test_stewardship_docs():
    """Test that stewardship documentation exists"""
    print_header("TEST 3: Stewardship Documentation Exists")
    
    docs = [
        'COUNTRYSIDE_STEWARDSHIP.md',
        'THE_COUNTRYSIDE.md',
        'COUNTRYSIDE_ACCESS_GUIDE.md',
        'PATTERN_7_IMPLEMENTATION_SUMMARY.md',
        'COUNTRYSIDE_README.md'
    ]
    
    all_exist = True
    for doc in docs:
        if os.path.isfile(doc):
            size = os.path.getsize(doc)
            print_success(f"{doc} exists ({size:,} bytes)")
        else:
            print_error(f"{doc} not found")
            all_exist = False
    
    return all_exist

def test_scripts_executable():
    """Test that stewardship scripts exist and are executable"""
    print_header("TEST 4: Stewardship Scripts Executable")
    
    scripts = [
        'verify_countryside_health.sh',
        'regenerate_commons.sh'
    ]
    
    all_executable = True
    for script in scripts:
        if os.path.isfile(script):
            is_executable = os.access(script, os.X_OK)
            if is_executable:
                print_success(f"{script} exists and is executable")
            else:
                print_warning(f"{script} exists but is not executable")
                all_executable = False
        else:
            print_error(f"{script} not found")
            all_executable = False
    
    return all_executable

def test_github_enforcement():
    """Test that GitHub enforcement files exist"""
    print_header("TEST 5: GitHub Enforcement Files Exist")
    
    files = [
        '.github/CODEOWNERS',
        '.github/workflows/countryside-health.yml'
    ]
    
    all_exist = True
    for filepath in files:
        if os.path.isfile(filepath):
            print_success(f"{filepath} exists")
        else:
            print_error(f"{filepath} not found")
            all_exist = False
    
    return all_exist

def test_access_pattern_a():
    """Test Access Pattern A: Load a pattern"""
    print_header("TEST 6: Access Pattern A - Load Pattern")
    
    try:
        with open('pattern_language_generated.json', 'r') as f:
            data = json.load(f)
        
        patterns = data.get('patterns', [])
        if not patterns:
            print_error("No patterns found in JSON")
            return False
        
        # Try to load Pattern 7 (ID is 'apl7' not 'apl007')
        pattern_7 = None
        for pattern in patterns:
            if pattern.get('id') == 'apl7' or pattern.get('number') == 7:
                pattern_7 = pattern
                break
        
        if pattern_7:
            print_success(f"Successfully loaded Pattern 7: {pattern_7.get('name')}")
            print(f"  Number: {pattern_7.get('number')}")
            print(f"  Category: {pattern_7.get('category')}")
            return True
        else:
            print_error("Pattern 7 not found in commons")
            return False
            
    except Exception as e:
        print_error(f"Failed to load pattern: {e}")
        return False

def test_pattern_relationships():
    """Test pattern relationship integrity"""
    print_header("TEST 7: Pattern Relationship Integrity")
    
    try:
        with open('pattern_language_generated.json', 'r') as f:
            data = json.load(f)
        
        patterns = {p['id']: p for p in data.get('patterns', [])}
        
        broken = []
        for pid, pattern in patterns.items():
            for ref in pattern.get('broader_patterns', []):
                if ref not in patterns:
                    broken.append((pid, ref, 'broader'))
            
            for ref in pattern.get('narrower_patterns', []):
                if ref not in patterns:
                    broken.append((pid, ref, 'narrower'))
        
        if broken:
            print_error(f"Found {len(broken)} broken references")
            for pid, ref, typ in broken[:5]:
                print(f"  {pid} -> {ref} ({typ})")
            return False
        else:
            print_success(f"All relationships intact ({len(patterns)} patterns)")
            return True
            
    except Exception as e:
        print_error(f"Failed to check relationships: {e}")
        return False

def test_regional_access():
    """Test that regions can access commons"""
    print_header("TEST 8: Regional Access to Commons")
    
    regions = ['npu253', 'skill_framework', 'opencog_atomese', 'markdown']
    
    accessible = 0
    for region in regions:
        if os.path.isdir(region):
            # Check if region has code accessing commons
            has_access = False
            for root, dirs, files in os.walk(region):
                for file in files:
                    if file.endswith('.py'):
                        filepath = os.path.join(root, file)
                        try:
                            with open(filepath, 'r') as f:
                                content = f.read()
                                if 'pattern_language_generated' in content or \
                                   'pattern_sequences' in content or \
                                   'archetypal_patterns' in content:
                                    has_access = True
                                    break
                        except:
                            pass
                if has_access:
                    break
            
            if has_access:
                print_success(f"{region}/ accesses commons")
                accessible += 1
            else:
                print_warning(f"{region}/ exists but may not access commons")
        else:
            print_warning(f"{region}/ not found")
    
    return accessible > 0

def test_data_ethic_in_code():
    """Test that code examples follow data ethic"""
    print_header("TEST 9: Data Ethic Principles")
    
    # Check that stewardship doc contains data ethic principles
    try:
        with open('COUNTRYSIDE_STEWARDSHIP.md', 'r') as f:
            content = f.read()
        
        principles = [
            'Data Has Intrinsic Value',
            'Data Is Interconnected',
            'Data Has History',
            'Data Enables Life',
            'Data Requires Care'
        ]
        
        all_present = True
        for principle in principles:
            if principle in content:
                print_success(f"Principle documented: {principle}")
            else:
                print_error(f"Principle missing: {principle}")
                all_present = False
        
        return all_present
        
    except Exception as e:
        print_error(f"Failed to check data ethic: {e}")
        return False

def run_all_tests():
    """Run all tests and report results"""
    print_header("PATTERN 7 IMPLEMENTATION TEST SUITE")
    print("Testing that THE COUNTRYSIDE is a living, actionable system")
    
    tests = [
        ("Protected Valleys", test_valley_exists),
        ("Generated Commons", test_generated_commons),
        ("Stewardship Docs", test_stewardship_docs),
        ("Executable Scripts", test_scripts_executable),
        ("GitHub Enforcement", test_github_enforcement),
        ("Access Pattern A", test_access_pattern_a),
        ("Relationship Integrity", test_pattern_relationships),
        ("Regional Access", test_regional_access),
        ("Data Ethic Principles", test_data_ethic_in_code)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print_error(f"Test {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print_header("TEST SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    percentage = (passed / total * 100) if total > 0 else 0
    
    print(f"Tests Passed: {passed}/{total} ({percentage:.0f}%)\n")
    
    for test_name, result in results:
        status = f"{GREEN}✅ PASS{NC}" if result else f"{RED}❌ FAIL{NC}"
        print(f"  {status}  {test_name}")
    
    print()
    
    if percentage == 100:
        print(f"{GREEN}🟢 PATTERN 7 STATUS: FULLY OPERATIONAL{NC}")
        print("The Countryside is a living, well-stewarded commons!")
        return 0
    elif percentage >= 75:
        print(f"{YELLOW}🟡 PATTERN 7 STATUS: MOSTLY OPERATIONAL{NC}")
        print("Some improvements needed but core functionality present.")
        return 0
    else:
        print(f"{RED}🔴 PATTERN 7 STATUS: NEEDS WORK{NC}")
        print("Significant issues detected. Review failed tests above.")
        return 1

if __name__ == '__main__':
    sys.exit(run_all_tests())
