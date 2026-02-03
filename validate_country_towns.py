#!/usr/bin/env python3
"""
Pattern 6: Country Towns Validation Script

Validates that smaller regions are self-sustaining "country towns" with:
1. Clear README documentation
2. Unique value proposition (local industry)
3. Tests or validation mechanisms
4. Independent usability (not just dormitories)
5. Complete functionality to support activities

This implements Pattern 6 from Christopher Alexander's "A Pattern Language":
"Preserve country towns where they exist; and encourage the growth of new 
self-contained towns... able to sustain the whole of life."
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class CountryTownValidator:
    """Validates that regions are viable country towns, not dormitories."""
    
    # Regions to validate as potential country towns
    COUNTRY_TOWNS = [
        'skill_framework',
        'diagrams',
        'implementations',
        'docs',
        'npu253',
        'apl_language',
        'opencog_atomese'
    ]
    
    # Criteria for viability
    MIN_SCORE = 4  # Out of 5
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.results = {}
        
    def validate_all(self) -> Dict:
        """Validate all country towns."""
        print("=" * 70)
        print("PATTERN 6: COUNTRY TOWNS VALIDATION")
        print("=" * 70)
        print()
        print("Validating that smaller regions are self-sustaining,")
        print("not just dormitory directories for file storage.")
        print()
        
        for town in self.COUNTRY_TOWNS:
            self.results[town] = self.validate_town(town)
            
        return self.generate_report()
        
    def validate_town(self, town_name: str) -> Dict:
        """Validate a single country town."""
        town_path = self.repo_root / town_name
        
        if not town_path.exists():
            return {
                'exists': False,
                'score': 0,
                'viable': False,
                'reason': 'Directory does not exist'
            }
            
        print(f"Validating {town_name}/")
        print("-" * 70)
        
        # Criterion 1: Has README
        has_readme, readme_quality = self.check_readme(town_path)
        
        # Criterion 2: Has unique value (industry)
        has_unique_value, industry_description = self.check_unique_value(town_path, town_name)
        
        # Criterion 3: Has tests/validation
        has_tests, test_info = self.check_tests(town_name)
        
        # Criterion 4: Has demos/examples
        has_demos, demo_info = self.check_demos(town_name)
        
        # Criterion 5: Independent usability
        is_independent, independence_info = self.check_independence(town_path, town_name)
        
        # Calculate score
        score = sum([has_readme, has_unique_value, has_tests, has_demos, is_independent])
        viable = score >= self.MIN_SCORE
        
        result = {
            'exists': True,
            'readme': {'present': has_readme, 'quality': readme_quality},
            'unique_value': {'present': has_unique_value, 'industry': industry_description},
            'tests': {'present': has_tests, 'info': test_info},
            'demos': {'present': has_demos, 'info': demo_info},
            'independence': {'present': is_independent, 'info': independence_info},
            'score': score,
            'viable': viable,
            'status': 'Country Town' if viable else 'Dormitory Risk'
        }
        
        self.print_town_result(town_name, result)
        return result
        
    def check_readme(self, town_path: Path) -> Tuple[bool, str]:
        """Check if town has a comprehensive README."""
        readme = town_path / "README.md"
        if not readme.exists():
            return False, "No README found"
            
        content = readme.read_text()
        
        # Quality checks
        has_overview = any(word in content.lower() for word in ['overview', 'introduction', 'about'])
        has_usage = any(word in content.lower() for word in ['usage', 'how to', 'getting started'])
        has_examples = 'example' in content.lower() or '```' in content
        
        length = len(content)
        
        if length > 2000 and has_overview and has_usage:
            quality = "Excellent - comprehensive documentation"
        elif length > 1000 and has_overview:
            quality = "Good - solid documentation"
        elif length > 500:
            quality = "Adequate - basic documentation"
        else:
            quality = "Minimal - needs expansion"
            
        return True, quality
        
    def check_unique_value(self, town_path: Path, town_name: str) -> Tuple[bool, str]:
        """Check if town provides unique value (local industry)."""
        
        # Define unique value propositions for each town
        industries = {
            'skill_framework': 'Pattern-based workflow execution engine',
            'diagrams': 'Visual representation and Mermaid diagram generation',
            'implementations': 'Multi-paradigm pattern demonstrations (PyTorch, Lua, AIML)',
            'docs': 'Formal specifications (Z++) and architecture documentation',
            'npu253': 'Virtual hardware pattern coprocessor with MMIO interface',
            'apl_language': 'Array-oriented pattern operations in APL',
            'opencog_atomese': 'Hypergraph knowledge representation for AI/AGI'
        }
        
        if town_name not in industries:
            return False, "No unique value identified"
            
        industry = industries[town_name]
        
        # Verify the industry exists by checking for implementation files
        file_count = sum(1 for _ in town_path.rglob('*') if _.is_file())
        
        if file_count < 3:
            return False, f"Claimed: {industry}, but insufficient implementation"
            
        return True, industry
        
    def check_tests(self, town_name: str) -> Tuple[bool, str]:
        """Check if town has test files."""
        test_dir = self.repo_root / "docs" / "tests"
        
        # Look for test files for this town
        test_patterns = [
            f"test_{town_name}.py",
            f"test_{town_name}_*.py",
        ]
        
        tests_found = []
        if test_dir.exists():
            for test_file in test_dir.glob("test_*.py"):
                if town_name in test_file.name or town_name.replace('_', '') in test_file.name:
                    tests_found.append(test_file.name)
                    
        if tests_found:
            return True, f"Tests: {', '.join(tests_found)}"
        else:
            return False, "No test files found"
            
    def check_demos(self, town_name: str) -> Tuple[bool, str]:
        """Check if town has demo/example files."""
        demo_dir = self.repo_root / "docs" / "examples"
        
        demos_found = []
        if demo_dir.exists():
            for demo_file in demo_dir.glob("demo_*.py"):
                if town_name in demo_file.name or town_name.replace('_', '') in demo_file.name:
                    demos_found.append(demo_file.name)
                    
        if demos_found:
            return True, f"Demos: {', '.join(demos_found)}"
        else:
            return False, "No demo files found"
            
    def check_independence(self, town_path: Path, town_name: str) -> Tuple[bool, str]:
        """Check if town can be used independently."""
        
        # Check for clear entry points
        has_init = (town_path / "__init__.py").exists()
        has_main = any((town_path / name).exists() for name in ['main.py', 'cli.py', 'driver.py'])
        
        # Check file count - should have substantial content
        py_files = list(town_path.glob("*.py"))
        other_files = list(town_path.glob("*.*"))
        
        total_files = len(other_files)
        
        # Independence criteria
        independence_factors = []
        
        if has_init and town_name in ['skill_framework', 'npu253']:
            independence_factors.append("Python package structure")
            
        if total_files >= 5:
            independence_factors.append(f"{total_files} files of substantial content")
            
        # Check for self-contained functionality
        readme = town_path / "README.md"
        if readme.exists():
            content = readme.read_text()
            if 'import' in content and town_name in content:
                independence_factors.append("Documented import interface")
                
        if len(independence_factors) >= 2:
            return True, "; ".join(independence_factors)
        elif len(independence_factors) == 1:
            return True, independence_factors[0]
        else:
            return False, "Lacks clear independent usage pattern"
            
    def print_town_result(self, town_name: str, result: Dict):
        """Print validation results for a town."""
        if not result['exists']:
            print(f"  ❌ {result['reason']}")
            print()
            return
            
        print(f"  README:         {'✅' if result['readme']['present'] else '❌'} {result['readme']['quality']}")
        print(f"  Unique Value:   {'✅' if result['unique_value']['present'] else '❌'} {result['unique_value']['industry']}")
        print(f"  Tests:          {'✅' if result['tests']['present'] else '❌'} {result['tests']['info']}")
        print(f"  Demos:          {'✅' if result['demos']['present'] else '❌'} {result['demos']['info']}")
        print(f"  Independence:   {'✅' if result['independence']['present'] else '❌'} {result['independence']['info']}")
        print()
        print(f"  Score: {result['score']}/5")
        print(f"  Status: {'✅ ' if result['viable'] else '⚠️  '}{result['status']}")
        print()
        
    def generate_report(self) -> Dict:
        """Generate final validation report."""
        print("=" * 70)
        print("VALIDATION SUMMARY")
        print("=" * 70)
        print()
        
        viable_towns = [name for name, result in self.results.items() 
                       if result.get('viable', False)]
        dormitory_risks = [name for name, result in self.results.items() 
                          if not result.get('viable', False)]
        
        print(f"Viable Country Towns: {len(viable_towns)}/{len(self.COUNTRY_TOWNS)}")
        for town in viable_towns:
            score = self.results[town]['score']
            print(f"  ✅ {town}/ ({score}/5)")
        print()
        
        if dormitory_risks:
            print(f"Dormitory Risks: {len(dormitory_risks)}")
            for town in dormitory_risks:
                score = self.results[town].get('score', 0)
                print(f"  ⚠️  {town}/ ({score}/5) - needs strengthening")
            print()
        
        # Pattern 6 compliance check
        compliance = len(viable_towns) >= 7
        
        print("Pattern 6 Compliance:")
        print(f"  Required: 7+ viable country towns")
        print(f"  Achieved: {len(viable_towns)} viable country towns")
        print(f"  Status: {'✅ COMPLIANT' if compliance else '⚠️  NEEDS WORK'}")
        print()
        
        # Recommendations
        if dormitory_risks:
            print("Recommendations:")
            for town in dormitory_risks:
                result = self.results[town]
                print(f"\n  {town}/:")
                if not result['readme']['present']:
                    print("    - Add comprehensive README.md")
                if not result['tests']['present']:
                    print(f"    - Create test_{town}.py in docs/tests/")
                if not result['demos']['present']:
                    print(f"    - Create demo_{town}.py in docs/examples/")
                if not result['independence']['present']:
                    print("    - Add clear usage examples and import interface")
            print()
        
        return {
            'total_towns': len(self.COUNTRY_TOWNS),
            'viable_towns': len(viable_towns),
            'dormitory_risks': len(dormitory_risks),
            'compliance': compliance,
            'results': self.results
        }

def main():
    """Main validation function."""
    repo_root = os.path.dirname(os.path.abspath(__file__))
    validator = CountryTownValidator(repo_root)
    report = validator.validate_all()
    
    # Save report
    report_path = Path(repo_root) / "country_towns_validation_report.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Full report saved to: {report_path}")
    print()
    
    # Return exit code based on compliance
    return 0 if report['compliance'] else 1

if __name__ == '__main__':
    exit(main())
