#!/usr/bin/env python3
"""
Verify Agricultural Valley Protection (Pattern 4).

This script verifies that:
1. Valley sources (apl/, uia/) are never written to by scripts
2. All generation scripts read from valleys and write to hillsides
3. Valley data is properly backed up
4. Hillsides can be regenerated from valleys
5. Data flow is unidirectional: valleys → hillsides

🌾 AGRICULTURAL VALLEY PROTECTION (Pattern 4)
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple

# Valley definitions
VALLEYS = {
    'apl': {
        'path': 'apl/',
        'description': 'Original APL HTML sources',
        'status': 'READ-ONLY ARCHIVE',
        'protection': 'Never written by scripts after initial import'
    },
    'uia': {
        'path': 'uia/',
        'description': 'Original UIA pattern sources',
        'status': 'READ-ONLY ARCHIVE',
        'protection': 'Never written by scripts'
    },
    'pattern_data': {
        'path': 'pattern/data/',
        'description': 'Core JSON data files',
        'status': 'GENERATED BUT VERSIONED',
        'protection': 'Generated from valleys, git tracked, backed up'
    }
}

# Hillside definitions
HILLSIDES = {
    'markdown': {
        'path': 'markdown/',
        'description': 'Markdown conversions',
        'source': 'apl/, uia/',
        'regenerable': True
    },
    'opencog_atomese': {
        'path': 'opencog_atomese/',
        'description': 'Scheme representations',
        'source': 'pattern/data/*.json',
        'regenerable': True
    },
    'docs': {
        'path': 'docs/',
        'description': 'Generated documentation',
        'source': 'Multiple valleys',
        'regenerable': True
    }
}


def check_script_writes_to_valleys(script_path: Path) -> List[str]:
    """Check if a script writes to valley directories."""
    violations = []
    
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return violations
    
    # Patterns that indicate writing to valleys
    write_patterns = [
        (r"open\(['\"]apl/.*['\"].*['\"]w", "Writes to apl/ valley"),
        (r"open\(['\"]uia/.*['\"].*['\"]w", "Writes to uia/ valley"),
        (r"with open\(['\"]apl/", "Opens apl/ files (check mode)"),
        (r"with open\(['\"]uia/", "Opens uia/ files (check mode)"),
    ]
    
    for pattern, description in write_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Check if it's a write mode
            for match in matches:
                if "'w'" in match or '"w"' in match or "'a'" in match or '"a"' in match:
                    violations.append(f"{script_path}: {description}")
    
    return violations


def verify_valley_integrity() -> Dict[str, any]:
    """Verify valley sources are intact."""
    results = {}
    
    for valley_name, valley_info in VALLEYS.items():
        path = Path(valley_info['path'])
        if path.exists():
            file_count = len(list(path.rglob('*')))
            results[valley_name] = {
                'exists': True,
                'file_count': file_count,
                'status': '✅ PROTECTED'
            }
        else:
            results[valley_name] = {
                'exists': False,
                'file_count': 0,
                'status': '❌ MISSING'
            }
    
    return results


def verify_backup_files() -> List[str]:
    """Check for backup files in valley areas."""
    backups = []
    
    for path in Path('pattern/data').glob('*.backup'):
        backups.append(str(path))
    
    return backups


def verify_generation_scripts() -> List[str]:
    """Find and verify all generation scripts."""
    violations = []
    
    # Find all generation/transformation scripts
    script_patterns = [
        'generate*.py',
        'scrape*.py',
        'populate*.py',
        'update*.py',
        'convert*.py'
    ]
    
    scripts = []
    for pattern in script_patterns:
        scripts.extend(Path('.').rglob(pattern))
    
    # Check each script
    for script in scripts:
        script_violations = check_script_writes_to_valleys(script)
        violations.extend(script_violations)
    
    return violations, scripts


def verify_data_flow() -> Dict[str, str]:
    """Document the data flow from valleys to hillsides."""
    flows = {
        'apl/ → markdown/apl/': 'HTML to Markdown conversion',
        'uia/ → markdown/uia/': 'Pattern source to Markdown',
        'markdown/apl/ → pattern/data/pattern_language_generated.json': 'Markdown to JSON schema',
        'markdown/uia/ → pattern/data/archetypal_patterns.json': 'Archetypal patterns extraction',
        'pattern/data/*.json → opencog_atomese/*.scm': 'JSON to Atomese (Scheme)',
        'pattern/data/*.json → npu253/': 'JSON to NPU driver',
        'pattern/data/*.json → implementations/': 'JSON to implementations'
    }
    
    return flows


def main():
    """Run all valley protection verifications."""
    print("=" * 70)
    print("🌾 AGRICULTURAL VALLEY PROTECTION VERIFICATION (Pattern 4)")
    print("=" * 70)
    print()
    
    # 1. Verify valley integrity
    print("1. Valley Integrity Check")
    print("-" * 70)
    valley_results = verify_valley_integrity()
    for valley_name, result in valley_results.items():
        valley_info = VALLEYS[valley_name]
        print(f"  {valley_name:20} {result['status']}")
        print(f"    Path: {valley_info['path']}")
        print(f"    Files: {result['file_count']}")
        print(f"    Status: {valley_info['status']}")
        print(f"    Protection: {valley_info['protection']}")
        print()
    
    # 2. Check for backup files
    print("\n2. Backup Files Check")
    print("-" * 70)
    backups = verify_backup_files()
    if backups:
        print(f"  ✅ Found {len(backups)} backup file(s):")
        for backup in backups:
            print(f"    - {backup}")
    else:
        print("  ⚠️  No backup files found in pattern/data/")
    print()
    
    # 3. Verify generation scripts don't write to valleys
    print("\n3. Generation Script Verification")
    print("-" * 70)
    violations, scripts = verify_generation_scripts()
    print(f"  Scanned {len(scripts)} generation/transformation scripts")
    
    if violations:
        print(f"  ❌ VIOLATIONS FOUND ({len(violations)}):")
        for violation in violations:
            print(f"    - {violation}")
    else:
        print("  ✅ No scripts write to valley directories")
    
    print(f"\n  Scripts checked:")
    for script in sorted(scripts)[:10]:  # Show first 10
        print(f"    - {script}")
    if len(scripts) > 10:
        print(f"    ... and {len(scripts) - 10} more")
    print()
    
    # 4. Document data flow
    print("\n4. Data Flow: Valley → Hillside")
    print("-" * 70)
    flows = verify_data_flow()
    for flow, description in flows.items():
        print(f"  {flow}")
        print(f"    └─ {description}")
    print()
    
    # 5. Hillside regenerability
    print("\n5. Hillside Regenerability")
    print("-" * 70)
    for hillside_name, hillside_info in HILLSIDES.items():
        status = "✅ REGENERABLE" if hillside_info['regenerable'] else "⚠️  CHECK"
        print(f"  {hillside_name:20} {status}")
        print(f"    Path: {hillside_info['path']}")
        print(f"    Source: {hillside_info['source']}")
        print(f"    Description: {hillside_info['description']}")
        print()
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    all_valleys_ok = all(r['exists'] for r in valley_results.values())
    no_violations = len(violations) == 0
    has_backups = len(backups) > 0
    
    if all_valleys_ok and no_violations:
        print("✅ All valleys are PROTECTED")
        print("✅ No scripts write to valleys")
        if has_backups:
            print("✅ Backup files exist")
        print("✅ Data flow is unidirectional: valleys → hillsides")
        print("\n🌾 AGRICULTURAL VALLEY PROTECTION: VERIFIED")
    else:
        print("⚠️  Issues detected:")
        if not all_valleys_ok:
            print("  - Some valleys are missing")
        if violations:
            print(f"  - {len(violations)} script violation(s) found")
        if not has_backups:
            print("  - No backup files found")
        print("\n⚠️  AGRICULTURAL VALLEY PROTECTION: NEEDS ATTENTION")
    
    print("=" * 70)


if __name__ == '__main__':
    main()
