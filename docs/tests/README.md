# Test Scripts

> **Pattern 2: Distribution of Towns** - Test scripts organized in dedicated region

## Overview

This directory contains test scripts that validate the functionality of various components in the pattern language system.

## Contents

This directory contains 9 test scripts:

- `test_npu253.py` - NPU253 Neural Pattern Unit tests
- `test_apl_implementation.py` - APL implementation tests
- (Additional test files as identified)

## Usage

Test scripts provide:
- **Validation** of component functionality
- **Regression testing** to catch breakage
- **Documentation** through test cases
- **Quality assurance** for implementations

### Running Tests

```bash
cd /home/runner/work/skipl-253/skipl-253

# Run specific test
python3 docs/tests/test_npu253.py

# Run all tests
python3 -m pytest docs/tests/

# Run with verbose output
python3 -m pytest docs/tests/ -v
```

## Test Organization

Tests are organized by component:
- **npu253/** - Neural Pattern Unit tests
- **apl/** - A Pattern Language tests
- **pattern/** - Pattern system tests
- (Additional test categories as system grows)

## Related Content

- `../examples/` - Demonstration scripts
- `../scripts/` - Generator and utility scripts
- `../../npu253/` - NPU253 implementation
- Root directory - Main implementation files

## Pattern 2 Benefits

Centralizing tests here:
- ✅ Reduces root directory clutter (was 9 files at root)
- ✅ Groups validation scripts
- ✅ Creates clear testing structure
- ✅ Separates tests from production code
- ✅ Enables systematic quality assurance
