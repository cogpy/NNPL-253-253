#!/bin/bash
# regenerate_commons.sh
# Safely regenerate JSON commons from valley sources
# Part of Pattern 7 (THE COUNTRYSIDE) stewardship implementation

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "==================================================================="
echo "           COUNTRYSIDE REGENERATION - Steward Action"
echo "==================================================================="
echo
echo "This script regenerates JSON commons from valley sources (apl/, uia/)"
echo "Only maintainers should run this script."
echo

# Check if we're in the right directory
if [ ! -d "apl" ] || [ ! -d "uia" ]; then
    echo -e "${RED}❌ Error: apl/ and uia/ valleys not found${NC}"
    echo "This script must be run from repository root."
    exit 1
fi

echo -e "${YELLOW}⚠️  This action will regenerate all JSON commons files.${NC}"
echo
read -p "Continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Regeneration cancelled."
    exit 0
fi

# ============================================================================
# STEP 1: Backup current commons
# ============================================================================
echo
echo "📦 STEP 1: Backing up current commons..."
echo "-------------------------------------------------------------------"

BACKUP_DIR="backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_NAME="commons-${TIMESTAMP}"

mkdir -p "$BACKUP_DIR"

# List of JSON files to backup
JSON_FILES=(
    "pattern_language_generated.json"
    "archetypal_patterns.json"
    "pattern_sequences.json"
    "uia_pattern_list.json"
    "category_towns.json"
    "category_buildings.json"
    "category_construction.json"
    "archetypal_pattern_schema.json"
    "pattern_schema.json"
)

# Create backup
BACKUP_PATH="$BACKUP_DIR/${BACKUP_NAME}.tar.gz"
tar czf "$BACKUP_PATH" "${JSON_FILES[@]}" 2>/dev/null || true

if [ -f "$BACKUP_PATH" ]; then
    echo -e "${GREEN}✅ Backup created: $BACKUP_PATH${NC}"
    ls -lh "$BACKUP_PATH"
else
    echo -e "${YELLOW}⚠️  Backup creation had warnings (some files may not exist)${NC}"
fi

echo

# ============================================================================
# STEP 2: Verify valley sources
# ============================================================================
echo "🏔️  STEP 2: Verifying valley sources..."
echo "-------------------------------------------------------------------"

APL_COUNT=$(find apl -name "*.htm" -o -name "*.html" | wc -l)
UIA_COUNT=$(find uia -name "*.html" | wc -l)

echo "apl/ valley: $APL_COUNT HTML files"
echo "uia/ valley: $UIA_COUNT HTML files"

if [ "$APL_COUNT" -eq 0 ] || [ "$UIA_COUNT" -eq 0 ]; then
    echo -e "${RED}❌ Error: Valleys appear empty${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Valley sources verified${NC}"
echo

# ============================================================================
# STEP 3: Run generation scripts
# ============================================================================
echo "⚙️  STEP 3: Running generation scripts..."
echo "-------------------------------------------------------------------"

GENERATORS=(
    "generate_pattern_schema.py"
    "generate_archetypal_patterns.py"
    "generate_uia_pattern_list.py"
)

GENERATED_COUNT=0
FAILED_GENERATORS=()

for generator in "${GENERATORS[@]}"; do
    if [ -f "$generator" ]; then
        echo
        echo "Running: $generator"
        echo ".........................................."
        
        if python3 "$generator" 2>&1 | tee /tmp/gen_output.txt; then
            echo -e "${GREEN}✅ $generator completed${NC}"
            GENERATED_COUNT=$((GENERATED_COUNT + 1))
        else
            echo -e "${RED}❌ $generator failed${NC}"
            FAILED_GENERATORS+=("$generator")
        fi
        
        rm -f /tmp/gen_output.txt
    else
        echo -e "${YELLOW}⚠️  $generator not found - skipping${NC}"
    fi
done

echo
echo "Generation Results: $GENERATED_COUNT / ${#GENERATORS[@]} succeeded"

if [ ${#FAILED_GENERATORS[@]} -gt 0 ]; then
    echo -e "${RED}❌ Failed generators:${NC}"
    for gen in "${FAILED_GENERATORS[@]}"; do
        echo "  - $gen"
    done
fi

echo

# ============================================================================
# STEP 4: Validate generated data
# ============================================================================
echo "✔️  STEP 4: Validating generated data..."
echo "-------------------------------------------------------------------"

# Validate JSON syntax
echo "Checking JSON syntax..."
INVALID_JSON=()

for json_file in "${JSON_FILES[@]}"; do
    if [ -f "$json_file" ]; then
        if python3 -c "import json; json.load(open('$json_file'))" 2>/dev/null; then
            echo -e "${GREEN}✅ $json_file${NC}"
        else
            echo -e "${RED}❌ $json_file - invalid JSON${NC}"
            INVALID_JSON+=("$json_file")
        fi
    fi
done

# Run schema validation if available
echo
if [ -f "validate_schema.py" ]; then
    echo "Running schema validation..."
    if python3 validate_schema.py; then
        echo -e "${GREEN}✅ Schema validation passed${NC}"
    else
        echo -e "${YELLOW}⚠️  Schema validation had warnings${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  validate_schema.py not found - skipping schema validation${NC}"
fi

# Run pattern API tests if available
echo
if [ -f "test_pattern_api.py" ]; then
    echo "Running pattern API tests..."
    if python3 test_pattern_api.py; then
        echo -e "${GREEN}✅ Pattern API tests passed${NC}"
    else
        echo -e "${YELLOW}⚠️  Pattern API tests had warnings${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  test_pattern_api.py not found - skipping API tests${NC}"
fi

echo

# ============================================================================
# STEP 5: Review changes
# ============================================================================
echo "📊 STEP 5: Reviewing changes..."
echo "-------------------------------------------------------------------"

# Show git diff statistics
if git diff --stat *.json 2>/dev/null; then
    echo
    echo -e "${YELLOW}⚠️  Review the changes above carefully.${NC}"
    echo
    echo "To see detailed changes, run:"
    echo "  git diff pattern_language_generated.json"
    echo "  git diff archetypal_patterns.json"
    echo "  (etc.)"
else
    echo -e "${GREEN}✅ No changes detected (commons already up to date)${NC}"
fi

echo

# ============================================================================
# STEP 6: Commit decision
# ============================================================================
echo "💾 STEP 6: Commit changes?"
echo "-------------------------------------------------------------------"

if [ ${#INVALID_JSON[@]} -gt 0 ]; then
    echo -e "${RED}❌ Cannot commit: Invalid JSON detected${NC}"
    echo "The following files have invalid JSON:"
    for json in "${INVALID_JSON[@]}"; do
        echo "  - $json"
    done
    echo
    echo "Regeneration incomplete. Restore from backup if needed:"
    echo "  tar xzf $BACKUP_PATH"
    exit 1
fi

if [ ${#FAILED_GENERATORS[@]} -gt 0 ]; then
    echo -e "${YELLOW}⚠️  Warning: Some generators failed${NC}"
    echo
fi

echo "Options:"
echo "  1. Review changes: git diff *.json"
echo "  2. Commit changes: git add *.json && git commit -m 'Regenerate commons from valleys'"
echo "  3. Restore backup: tar xzf $BACKUP_PATH"
echo "  4. Discard changes: git checkout *.json"
echo

read -p "Commit regenerated commons now? (yes/no): " COMMIT_NOW

if [ "$COMMIT_NOW" = "yes" ]; then
    echo
    echo "Staging changes..."
    git add "${JSON_FILES[@]}" 2>/dev/null || true
    
    read -p "Enter commit message: " COMMIT_MSG
    if [ -z "$COMMIT_MSG" ]; then
        COMMIT_MSG="Regenerate JSON commons from valleys (${TIMESTAMP})"
    fi
    
    git commit -m "$COMMIT_MSG"
    
    echo -e "${GREEN}✅ Changes committed${NC}"
    echo
    echo "Don't forget to:"
    echo "  1. Update COUNTRYSIDE_STEWARDSHIP.md log"
    echo "  2. Run health check: ./verify_countryside_health.sh"
else
    echo
    echo "Changes not committed. Review and commit manually when ready."
fi

echo

# ============================================================================
# SUMMARY
# ============================================================================
echo "==================================================================="
echo "                    REGENERATION COMPLETE"
echo "==================================================================="
echo
echo "Summary:"
echo "  - Backup: $BACKUP_PATH"
echo "  - Generators run: $GENERATED_COUNT"
echo "  - Failed generators: ${#FAILED_GENERATORS[@]}"
echo "  - Invalid JSON: ${#INVALID_JSON[@]}"
echo
echo "Stewardship Log Entry:"
echo "-------------------------------------------------------------------"
echo "#### $(date +%Y-%m-%d): Countryside Regeneration"
echo "- **Action**: Regenerated JSON commons from valley sources"
echo "- **Steward**: $(git config user.name || echo 'Unknown')"
echo "- **Rationale**: [Add reason here]"
echo "- **Generators**: $GENERATED_COUNT succeeded, ${#FAILED_GENERATORS[@]} failed"
echo "- **Status**: $([ ${#INVALID_JSON[@]} -eq 0 ] && echo '✅ Complete' || echo '⚠️ Incomplete')"
echo "-------------------------------------------------------------------"
echo
echo "Copy the above entry to COUNTRYSIDE_STEWARDSHIP.md Section VIII"
echo
echo "==================================================================="
