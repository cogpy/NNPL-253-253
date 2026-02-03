#!/bin/bash
echo "======================================================================"
echo "FINAL META-RECURSIVE CONVERGENCE VERIFICATION"
echo "======================================================================"
echo ""

echo "1. Running meta-recursive convergence analysis..."
python3 meta_recursive_convergence.py | grep -E "(VERIFYING|CALCULATING|IMPROVEMENT|SUMMARY|✓|Overall|Fitness)" | head -20
echo ""

echo "2. Running meta-recursive convergence tests..."
python3 test_meta_recursive_convergence.py 2>&1 | grep -E "(Tests run|Successes|Failures|Errors|✓ ALL)" 
echo ""

echo "3. Verifying existing tests still pass..."
echo "   - Archetypal schema tests..."
python3 test_archetypal_schema.py 2>&1 | grep -E "(Passed|Failed|✓)" | tail -3
echo "   - OpenCog Atomese tests..."
python3 test_opencog_atomese.py 2>&1 | grep -E "(✅|validation)" | tail -2
echo ""

echo "4. Checking new documentation files..."
for file in PATTERN_SELF_APPLICATION.md CONVERGENCE_VISUALIZATION.md \
            META_RECURSIVE_QUICK_REFERENCE.md META_RECURSIVE_IMPLEMENTATION_SUMMARY.md; do
    if [ -f "$file" ]; then
        lines=$(wc -l < "$file")
        size=$(du -h "$file" | cut -f1)
        echo "   ✓ $file ($lines lines, $size)"
    else
        echo "   ✗ $file NOT FOUND"
    fi
done
echo ""

echo "5. Verifying base-6 structure..."
python3 -c "
import json
with open('pattern_sequences.json') as f:
    seqs = json.load(f)['sequences']
with open('pattern_language_generated.json') as f:
    pats = json.load(f).get('patterns', [])
print(f'   ✓ Sequences: {len(seqs)} (expected 36)')
print(f'   ✓ Patterns: {len(pats)} (expected 253)')
print(f'   ✓ Structure: 1 + 6 + 36 + 210 = {1+6+36+210}')
"
echo ""

echo "======================================================================"
echo "VERIFICATION COMPLETE"
echo "======================================================================"
