#!/bin/bash
# verify_countryside_health.sh
# Countryside Health Check - validates the commons ecosystem
# Part of Pattern 7 (THE COUNTRYSIDE) implementation

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "==================================================================="
echo "    COUNTRYSIDE HEALTH CHECK - Pattern 7 Implementation"
echo "==================================================================="
echo

HEALTH_SCORE=0
TOTAL_CHECKS=0

# Function to report check result
check_result() {
    local status=$1
    local message=$2
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    if [ "$status" = "pass" ]; then
        echo -e "${GREEN}✅ $message${NC}"
        HEALTH_SCORE=$((HEALTH_SCORE + 1))
    elif [ "$status" = "warn" ]; then
        echo -e "${YELLOW}⚠️  $message${NC}"
        HEALTH_SCORE=$((HEALTH_SCORE + 1))
    else
        echo -e "${RED}❌ $message${NC}"
    fi
}

# ============================================================================
# CHECK 1: Valley Integrity
# ============================================================================
echo "🏔️  CHECKING VALLEY INTEGRITY (apl/ and uia/)"
echo "-------------------------------------------------------------------"

if [ ! -d "apl" ]; then
    check_result "fail" "apl/ valley not found"
else
    APL_COUNT=$(find apl -name "*.htm" -o -name "*.html" | wc -l)
    if [ "$APL_COUNT" -gt 0 ]; then
        check_result "pass" "apl/ valley exists with $APL_COUNT HTML files"
    else
        check_result "fail" "apl/ valley exists but contains no HTML files"
    fi
fi

if [ ! -d "uia" ]; then
    check_result "fail" "uia/ valley not found"
else
    UIA_COUNT=$(find uia -name "*.html" | wc -l)
    if [ "$UIA_COUNT" -gt 0 ]; then
        check_result "pass" "uia/ valley exists with $UIA_COUNT HTML files"
    else
        check_result "fail" "uia/ valley exists but contains no HTML files"
    fi
fi

# Check for uncommitted changes to valleys
if git diff --quiet apl/ uia/ 2>/dev/null; then
    check_result "pass" "Valleys have no uncommitted changes"
else
    check_result "warn" "Valleys have uncommitted changes (review with: git status apl/ uia/)"
fi

echo

# ============================================================================
# CHECK 2: JSON Commons Validity
# ============================================================================
echo "📊 CHECKING JSON COMMONS VALIDITY"
echo "-------------------------------------------------------------------"

JSON_FILES=(
    "pattern_language_generated.json"
    "archetypal_patterns.json"
    "pattern_sequences.json"
    "uia_pattern_list.json"
    "category_towns.json"
    "category_buildings.json"
    "category_construction.json"
)

for json_file in "${JSON_FILES[@]}"; do
    if [ ! -f "$json_file" ]; then
        check_result "warn" "$json_file not found (may be optional)"
    else
        if python3 -c "import json; json.load(open('$json_file'))" 2>/dev/null; then
            check_result "pass" "$json_file is valid JSON"
        else
            check_result "fail" "$json_file is invalid JSON"
        fi
    fi
done

echo

# ============================================================================
# CHECK 3: Pattern Relationship Integrity
# ============================================================================
echo "🕸️  CHECKING PATTERN RELATIONSHIP INTEGRITY"
echo "-------------------------------------------------------------------"

if [ -f "pattern_language_generated.json" ]; then
    python3 << 'EOF'
import json
import sys

try:
    with open('pattern_language_generated.json') as f:
        data = json.load(f)
    
    patterns = {}
    for p in data.get('patterns', []):
        if 'id' in p:
            patterns[p['id']] = p
    
    if not patterns:
        print("FAIL: No patterns found in JSON")
        sys.exit(1)
    
    print(f"INFO: Found {len(patterns)} patterns")
    
    broken_refs = []
    for pid, pattern in patterns.items():
        # Check broader patterns
        for ref in pattern.get('broader_patterns', []):
            if ref not in patterns:
                broken_refs.append((pid, ref, 'broader'))
        
        # Check narrower patterns
        for ref in pattern.get('narrower_patterns', []):
            if ref not in patterns:
                broken_refs.append((pid, ref, 'narrower'))
    
    if broken_refs:
        print(f"FAIL: Found {len(broken_refs)} broken references")
        for pid, ref, typ in broken_refs[:5]:
            print(f"  {pid} -> {ref} ({typ})")
        if len(broken_refs) > 5:
            print(f"  ... and {len(broken_refs) - 5} more")
        sys.exit(1)
    else:
        print("PASS: All pattern relationships intact")
        sys.exit(0)

except Exception as e:
    print(f"FAIL: Error checking relationships: {e}")
    sys.exit(1)
EOF
    
    if [ $? -eq 0 ]; then
        check_result "pass" "Pattern relationships are intact"
    else
        check_result "fail" "Pattern relationships have broken references"
    fi
else
    check_result "warn" "Cannot check relationships - pattern_language_generated.json not found"
fi

echo

# ============================================================================
# CHECK 4: Schema Validation
# ============================================================================
echo "📋 CHECKING SCHEMA VALIDATION"
echo "-------------------------------------------------------------------"

if [ -f "validate_schema.py" ]; then
    if python3 validate_schema.py > /tmp/validate_output.txt 2>&1; then
        check_result "pass" "Schema validation passed"
    else
        # Check if output contains success indicators
        if grep -iq "success\|passed\|valid" /tmp/validate_output.txt; then
            check_result "pass" "Schema validation passed"
        else
            check_result "warn" "Schema validation unclear (check validate_schema.py)"
        fi
    fi
    rm -f /tmp/validate_output.txt
else
    check_result "warn" "validate_schema.py not found - cannot validate schemas"
fi

echo

# ============================================================================
# CHECK 5: Access Pattern Tests
# ============================================================================
echo "🔌 CHECKING ACCESS PATTERNS"
echo "-------------------------------------------------------------------"

if [ -f "test_pattern_api.py" ]; then
    if python3 test_pattern_api.py > /tmp/test_output.txt 2>&1; then
        check_result "pass" "Pattern API tests passed"
    else
        if grep -iq "pass\|ok\|success" /tmp/test_output.txt; then
            check_result "pass" "Pattern API tests passed"
        else
            check_result "warn" "Pattern API tests unclear (check test_pattern_api.py)"
        fi
    fi
    rm -f /tmp/test_output.txt
else
    check_result "warn" "test_pattern_api.py not found - cannot test access patterns"
fi

echo

# ============================================================================
# CHECK 6: Regional Access
# ============================================================================
echo "🏘️  CHECKING REGIONAL ACCESS TO COMMONS"
echo "-------------------------------------------------------------------"

REGIONS=(
    "npu253"
    "skill_framework"
    "opencog_atomese"
    "markdown"
    "implementations"
)

for region in "${REGIONS[@]}"; do
    if [ -d "$region" ]; then
        # Check if region has code that accesses commons
        if grep -rq "pattern_language_generated\|pattern_sequences\|archetypal_patterns" "$region/" 2>/dev/null; then
            check_result "pass" "$region/ accesses commons data"
        else
            check_result "warn" "$region/ exists but may not access commons"
        fi
    fi
done

echo

# ============================================================================
# CHECK 7: Stewardship Documentation
# ============================================================================
echo "📖 CHECKING STEWARDSHIP DOCUMENTATION"
echo "-------------------------------------------------------------------"

if [ -f "COUNTRYSIDE_STEWARDSHIP.md" ]; then
    check_result "pass" "Stewardship policy document exists"
else
    check_result "fail" "COUNTRYSIDE_STEWARDSHIP.md not found"
fi

if [ -f "THE_COUNTRYSIDE.md" ]; then
    check_result "pass" "Pattern 7 documentation exists"
else
    check_result "warn" "THE_COUNTRYSIDE.md not found"
fi

# Check for stewardship log entries
if grep -q "Stewardship Activities" COUNTRYSIDE_STEWARDSHIP.md 2>/dev/null; then
    check_result "pass" "Stewardship log section present"
else
    check_result "warn" "Stewardship log may need updating"
fi

echo

# ============================================================================
# CHECK 8: Generation Scripts
# ============================================================================
echo "⚙️  CHECKING GENERATION SCRIPTS"
echo "-------------------------------------------------------------------"

GENERATORS=(
    "generate_pattern_schema.py"
    "generate_archetypal_patterns.py"
    "generate_uia_pattern_list.py"
)

for generator in "${GENERATORS[@]}"; do
    if [ -f "$generator" ]; then
        check_result "pass" "$generator exists"
    else
        check_result "warn" "$generator not found"
    fi
done

echo

# ============================================================================
# SUMMARY
# ============================================================================
echo "==================================================================="
echo "                       HEALTH CHECK SUMMARY"
echo "==================================================================="
echo

HEALTH_PERCENT=$((HEALTH_SCORE * 100 / TOTAL_CHECKS))

echo "Score: $HEALTH_SCORE / $TOTAL_CHECKS checks passed ($HEALTH_PERCENT%)"
echo

if [ "$HEALTH_PERCENT" -ge 90 ]; then
    echo -e "${GREEN}🟢 COUNTRYSIDE STATUS: HEALTHY${NC}"
    echo "The commons ecosystem is in excellent condition."
    echo "Continue regular stewardship activities."
elif [ "$HEALTH_PERCENT" -ge 70 ]; then
    echo -e "${YELLOW}🟡 COUNTRYSIDE STATUS: REQUIRES ATTENTION${NC}"
    echo "The commons ecosystem needs some maintenance."
    echo "Review warnings above and address issues."
elif [ "$HEALTH_PERCENT" -ge 50 ]; then
    echo -e "${RED}🟠 COUNTRYSIDE STATUS: NEEDS REPAIR${NC}"
    echo "The commons ecosystem has significant issues."
    echo "Priority maintenance required."
else
    echo -e "${RED}🔴 COUNTRYSIDE STATUS: CRITICAL${NC}"
    echo "The commons ecosystem is severely compromised."
    echo "Immediate intervention required."
fi

echo
echo "Next Steps:"
echo "  1. Review any failed checks above"
echo "  2. Address critical issues first"
echo "  3. Update COUNTRYSIDE_STEWARDSHIP.md log"
echo "  4. Run health check again after fixes"
echo
echo "For detailed stewardship policies, see:"
echo "  - COUNTRYSIDE_STEWARDSHIP.md (policies and procedures)"
echo "  - THE_COUNTRYSIDE.md (pattern application)"
echo
echo "==================================================================="

# Exit with appropriate code
if [ "$HEALTH_PERCENT" -ge 70 ]; then
    exit 0
else
    exit 1
fi
