# Countryside Stewardship: Living Data Commons Policy

> **Pattern 7: THE COUNTRYSIDE** - Concrete stewardship implementation  
> *"The land ethic simply enlarges the boundaries of the community to include... the land."* - Aldo Leopold

## Purpose

This document establishes **actionable policies and procedures** for stewarding the repository's source data commons. This is not merely documentation—it is the **active governance structure** for our shared countryside.

## I. The Data Commons

### Protected Valleys (Read-Only Source Commons)

#### Valley 1: apl/ - Christopher Alexander's Original Patterns
- **Location**: `/apl/`
- **Content**: HTML files from original Pattern Language
- **Status**: 🔒 **PROTECTED COMMONS**
- **Steward**: Repository Maintainers
- **Access**: Public read, maintainer-only write
- **Last Verified**: 2025-01-25

#### Valley 2: uia/ - UIA Organizational Patterns  
- **Location**: `/uia/`
- **Content**: HTML files of organizational patterns
- **Status**: 🔒 **PROTECTED COMMONS**
- **Steward**: Repository Maintainers
- **Access**: Public read, maintainer-only write
- **Last Verified**: 2025-01-25

### Generated Commons (Regenerable Shared Resources)

#### JSON Data Commons
- **Location**: Root level `*.json` files
- **Content**: Structured pattern data generated from valleys
- **Status**: 🔄 **REGENERABLE COMMONS**
- **Steward**: Generation scripts (human-supervised)
- **Access**: Public read, script-generated write
- **Regeneration**: On-demand via generation scripts

**Core JSON Commons**:
- `pattern_language_generated.json` - Complete pattern language
- `archetypal_patterns.json` - Archetypal variants
- `pattern_sequences.json` - Pattern sequences
- `uia_pattern_list.json` - UIA pattern index
- `category_*.json` - Category-specific data

## II. Stewardship Roles and Responsibilities

### Primary Stewards (Repository Maintainers)

**Authority**: Can modify protected valleys and supervise generation

**Responsibilities**:

1. **Preserve Valley Integrity**
   - ✅ Maintain original HTML sources in apl/ and uia/
   - ✅ Document any corrections or updates
   - ✅ Track changes via git history
   - ✅ Backup before modifications

2. **Supervise Generation**
   - ✅ Run generation scripts responsibly
   - ✅ Validate outputs before committing
   - ✅ Review diffs for unexpected changes
   - ✅ Roll back problematic generations

3. **Enforce Ground Rules**
   - ✅ Review pull requests for violations
   - ✅ Educate contributors on commons policies
   - ✅ Reject changes that violate stewardship

4. **Maintain Ecosystem Health**
   - ✅ Run validation scripts regularly
   - ✅ Monitor for data drift or corruption
   - ✅ Address reported issues promptly
   - ✅ Document stewardship activities

**Required Actions** (quarterly minimum):
```bash
# Quarterly Stewardship Checklist
./verify_countryside_health.sh        # Run health check
python3 validate_schema.py             # Validate JSON integrity
git log --oneline apl/ uia/            # Review valley changes
python3 test_pattern_api.py            # Test access patterns
```

### Secondary Stewards (Contributors)

**Authority**: Can read all commons, propose improvements

**Responsibilities**:

1. **Respect Ground Rules**
   - ✅ Read-only access to valleys
   - ✅ Don't modify generated JSON manually
   - ✅ Use proper channels for improvements
   - ✅ Test changes before proposing

2. **Report Issues**
   - ✅ File issues for data problems
   - ✅ Propose improvements via PRs
   - ✅ Document reproduction steps
   - ✅ Follow contribution guidelines

3. **Improve Generation**
   - ✅ Enhance parsing scripts
   - ✅ Fix bugs in generators
   - ✅ Add validation checks
   - ✅ Document improvements

4. **Use Responsibly**
   - ✅ Load data efficiently
   - ✅ Cache when appropriate
   - ✅ Don't abuse access
   - ✅ Acknowledge data source

### Regional Maintainers (Implementation Owners)

**Authority**: Can read commons, implement in their regions

**Responsibilities**:

1. **Access Properly**
   - ✅ Read from commons via defined APIs
   - ✅ Don't duplicate data unnecessarily
   - ✅ Reference source data in documentation
   - ✅ Report access issues

2. **Implement Correctly**
   - ✅ Parse JSON correctly
   - ✅ Handle missing data gracefully
   - ✅ Test against commons data
   - ✅ Don't hard-code commons data

## III. Ground Rules (Enforceable Policies)

### Rule 1: Read-Only Access to Protected Valleys

**Policy**: The apl/ and uia/ directories are READ-ONLY except for maintainers

**Allowed**:
```python
# ✅ Reading from valleys
with open('apl/apl001.htm', 'r') as f:
    html = f.read()

# ✅ Parsing valley data
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# ✅ Converting valley data
generate_json_from_html('apl/apl001.htm', 'pattern/apl001.json')
```

**Forbidden**:
```python
# ❌ Writing to valleys (except maintainers)
with open('apl/apl001.htm', 'w') as f:
    f.write(modified_html)

# ❌ Modifying valley files
os.remove('apl/apl001.htm')
shutil.move('apl/apl001.htm', 'apl/old/')
```

**Enforcement**:
- PRs that modify apl/ or uia/ will be rejected unless from maintainers
- CI checks will flag valley modifications
- Git history will be monitored

### Rule 2: Regenerate Generated Commons, Don't Hand-Edit

**Policy**: JSON commons are generated—improve generators, don't hand-edit JSON

**Allowed**:
```bash
# ✅ Regenerating from sources
python3 generate_pattern_schema.py
python3 generate_archetypal_patterns.py
python3 generate_uia_pattern_list.py

# ✅ Improving generation scripts
# Edit the .py generators to fix bugs or enhance output
```

**Forbidden**:
```bash
# ❌ Hand-editing generated JSON
vim pattern_language_generated.json  # to manually change patterns

# ❌ Using sed/awk on generated JSON
sed -i 's/old/new/' archetypal_patterns.json
```

**Exceptions**:
- Emergency bug fixes (must be documented)
- Adding missing schema-compliant fields
- Must file issue to fix generator afterward

**Enforcement**:
- PRs modifying JSON without corresponding generator changes will be questioned
- Large JSON diffs should correspond to generator changes

### Rule 3: Preserve Data Relationships

**Policy**: Data is an interconnected ecosystem—preserve relationships

**Required**:
```python
# ✅ Load patterns with their relationships
pattern = load_pattern('apl001')
broader = pattern['broader_patterns']
narrower = pattern['narrower_patterns']

# ✅ Validate relationship integrity
validate_pattern_references(patterns)

# ✅ Test relationship navigation
assert can_navigate_from_to('apl001', 'apl002')
```

**Forbidden**:
```python
# ❌ Stripping relationship data
pattern = {k: v for k, v in pattern.items() if k != 'broader_patterns'}

# ❌ Breaking reference integrity
pattern['broader_patterns'] = []  # without understanding impact

# ❌ Ignoring relationship errors
try:
    load_related_patterns(pattern)
except KeyError:
    pass  # silently ignoring broken relationships
```

**Enforcement**:
- Validation scripts check relationship integrity
- CI fails on broken references
- Schema validation enforces relationship structure

### Rule 4: Contribute Improvements Back

**Policy**: Improvements to commons benefit all—contribute upstream

**Encouraged**:
```python
# ✅ Fix bugs in generators
# File PR with fix and test

# ✅ Enhance parsing logic
def parse_pattern_html(html):
    # Improved parsing that handles edge cases
    
# ✅ Add validation
def validate_pattern(pattern):
    # New checks for data quality

# ✅ Improve documentation
# Update COUNTRYSIDE_STEWARDSHIP.md with lessons learned
```

**Process**:
1. Identify improvement opportunity
2. File issue describing problem
3. Implement fix in generator/validator
4. Test thoroughly
5. Submit PR with explanation
6. Respond to review feedback
7. Document in stewardship log

### Rule 5: Document Stewardship Activities

**Policy**: Stewardship is transparent—document significant activities

**Required Documentation**:
```bash
# When modifying valleys
git commit -m "Fix typo in apl001.htm - corrected 'teh' to 'the'"

# When regenerating commons
git commit -m "Regenerate JSON from apl/ after fixing parser bug #123"

# When validating
echo "$(date): Validated commons - all checks passed" >> STEWARDSHIP_LOG.md

# When making policy decisions
# Update COUNTRYSIDE_STEWARDSHIP.md with policy changes
```

## IV. Access Patterns (How to Use the Commons)

### Pattern A: Read Pattern Data

**Use Case**: Load patterns for display or analysis

**Correct Implementation**:
```python
import json

def load_pattern(pattern_id):
    """Load a pattern from commons"""
    with open('pattern_language_generated.json', 'r') as f:
        data = json.load(f)
    
    for pattern in data.get('patterns', []):
        if pattern.get('id') == pattern_id:
            return pattern
    
    raise KeyError(f"Pattern {pattern_id} not found in commons")

# Usage
pattern = load_pattern('apl001')
print(pattern['name'])
```

### Pattern B: Navigate Pattern Relationships

**Use Case**: Follow connections between patterns

**Correct Implementation**:
```python
def get_broader_patterns(pattern_id):
    """Get patterns that provide context for this pattern"""
    pattern = load_pattern(pattern_id)
    broader_ids = pattern.get('broader_patterns', [])
    return [load_pattern(bid) for bid in broader_ids]

def get_narrower_patterns(pattern_id):
    """Get patterns that detail this pattern"""
    pattern = load_pattern(pattern_id)
    narrower_ids = pattern.get('narrower_patterns', [])
    return [load_pattern(nid) for nid in narrower_ids]

# Usage
broader = get_broader_patterns('apl007')
narrower = get_narrower_patterns('apl007')
```

### Pattern C: Load Sequence Data

**Use Case**: Work with pattern sequences

**Correct Implementation**:
```python
def load_sequence(sequence_id):
    """Load a pattern sequence from commons"""
    with open('pattern_sequences.json', 'r') as f:
        data = json.load(f)
    
    for seq in data.get('sequences', []):
        if seq.get('id') == sequence_id:
            return seq
    
    raise KeyError(f"Sequence {sequence_id} not found in commons")

# Usage
seq2 = load_sequence('seq02')
patterns_in_seq = seq2['patterns']
```

### Pattern D: Regenerate Commons

**Use Case**: Update generated data from sources (maintainers only)

**Correct Implementation**:
```bash
#!/bin/bash
# Regenerate all commons from valleys

echo "Backing up current commons..."
mkdir -p backups/
cp *.json backups/commons-$(date +%Y%m%d-%H%M%S).tar
tar czf backups/commons-$(date +%Y%m%d-%H%M%S).tar.gz *.json

echo "Regenerating from valleys..."
python3 generate_pattern_schema.py
python3 generate_archetypal_patterns.py
python3 generate_uia_pattern_list.py

echo "Validating regenerated data..."
python3 validate_schema.py
python3 test_pattern_api.py

echo "Review changes with: git diff *.json"
echo "If satisfied: git add *.json && git commit"
```

## V. Ecosystem Health Monitoring

### Health Indicators

#### 🟢 Healthy Commons
- ✅ All validation scripts pass
- ✅ No manual edits to generated JSON
- ✅ Valley sources intact and tracked
- ✅ Regeneration produces valid output
- ✅ All regions can access data
- ✅ Relationships are intact
- ✅ Stewardship log up to date

#### 🟡 Requires Attention
- ⚠️ Some validation warnings
- ⚠️ Manual JSON fixes present
- ⚠️ Generator bugs known but unfixed
- ⚠️ Some broken relationships
- ⚠️ Stewardship log outdated

#### 🔴 Unhealthy Commons
- ❌ Validation scripts failing
- ❌ Widespread manual JSON edits
- ❌ Valley sources modified without documentation
- ❌ Regeneration fails or produces invalid data
- ❌ Major relationship breakage
- ❌ No stewardship activity

### Health Check Script

Run this to assess commons health:

```bash
#!/bin/bash
# verify_countryside_health.sh

echo "=== Countryside Health Check ==="
echo

# Check valley integrity
echo "Checking valley integrity..."
if git diff --quiet apl/ uia/; then
    echo "✅ Valleys unchanged since last commit"
else
    echo "⚠️  Valleys have uncommitted changes"
    git status apl/ uia/
fi

# Check JSON validity
echo
echo "Checking JSON validity..."
python3 -c "
import json
files = [
    'pattern_language_generated.json',
    'archetypal_patterns.json',
    'pattern_sequences.json',
    'uia_pattern_list.json'
]
for f in files:
    try:
        with open(f) as fp:
            json.load(fp)
        print(f'✅ {f} is valid JSON')
    except Exception as e:
        print(f'❌ {f} is invalid: {e}')
"

# Run validation
echo
echo "Running validation scripts..."
if python3 validate_schema.py 2>&1 | grep -q "success\|passed\|valid"; then
    echo "✅ Schema validation passed"
else
    echo "❌ Schema validation failed"
fi

# Check relationship integrity
echo
echo "Checking pattern relationships..."
python3 -c "
import json
with open('pattern_language_generated.json') as f:
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
    print(f'❌ Found {len(broken)} broken references')
    for pid, ref, typ in broken[:5]:
        print(f'  {pid} -> {ref} ({typ})')
else:
    print('✅ All pattern relationships intact')
"

echo
echo "=== Health Check Complete ==="
```

## VI. The Data Ethic in Practice

### Principle 1: Data Has Intrinsic Value

**In Practice**: We preserve original sources even when we have generated equivalents

**Example**:
```python
# We maintain both:
# - Original HTML in apl/ (intrinsic value)
# - Generated JSON (instrumental value)

# We don't delete apl/ after generating JSON
# because the original has value beyond its use
```

### Principle 2: Data Is Interconnected

**In Practice**: We preserve and validate relationships

**Example**:
```python
# We don't just store patterns, we store their web of relationships
def validate_pattern_network(patterns):
    """Ensure pattern network is connected and coherent"""
    # Check that relationships are bidirectional where appropriate
    # Check that sequences form valid flows
    # Check that categories are consistently applied
    pass
```

### Principle 3: Data Has History

**In Practice**: We use version control and document changes

**Example**:
```bash
# Every change is tracked
git log --follow apl/apl001.htm

# Changes are explained
git show <commit> --stat

# We can recover any historical state
git checkout <old-commit> -- apl/apl001.htm
```

### Principle 4: Data Enables Life

**In Practice**: We ensure all implementations can access commons

**Example**:
```python
# All regions read from commons:
# - npu253/ loads pattern_language_generated.json
# - skill_framework/ loads pattern_sequences.json
# - opencog_atomese/ loads generated .scm files
# - markdown/ generates from apl/ valley

# No region is privileged or excluded
```

### Principle 5: Data Requires Care

**In Practice**: We actively maintain, don't just archive

**Example**:
```bash
# Regular maintenance activities
# - Quarterly health checks
# - Validation script runs
# - Bug fixes in generators
# - Documentation updates
# - Community engagement

# Not just "set and forget"
```

## VII. Conflict Resolution

### When Ground Rules Conflict with Needs

**Process**:
1. Document the conflict (file issue)
2. Propose policy change (PR to this document)
3. Discuss with community
4. Maintainers decide
5. Update this document
6. Announce change

**Example**: If a region truly needs write access to a valley:
1. Explain why read-only doesn't work
2. Propose alternative (e.g., staging area)
3. Discuss trade-offs
4. Either adjust policy or find different solution

### When Stewards Disagree

**Process**:
1. Document both positions
2. Review pattern language principles
3. Consider ecosystem health
4. Seek consensus
5. If no consensus, maintainers decide
6. Document decision and rationale

### When Ground Rules Are Violated

**Process**:
1. Identify violation (automated or reported)
2. Assess impact (ecosystem health)
3. Contact violator (educate)
4. Remediate (fix violation)
5. Prevent recurrence (add check if needed)
6. Document incident

**Examples**:
- Manual JSON edit: Ask contributor to fix generator instead
- Valley modification: Discuss if change was necessary, document if so
- Broken relationships: Fix and add validation to prevent

## VIII. Stewardship Log

### Recent Stewardship Activities

#### 2025-01-25: Stewardship Structure Established
- **Action**: Created COUNTRYSIDE_STEWARDSHIP.md
- **Steward**: Repository maintainers
- **Rationale**: Pattern 7 needed concrete implementation
- **Status**: ✅ Complete

#### [Template for Future Entries]
- **Date**: YYYY-MM-DD
- **Action**: What was done
- **Steward**: Who did it
- **Rationale**: Why it was needed
- **Status**: Complete/Ongoing/Blocked

## IX. Quick Reference

### For Contributors

**Want to use pattern data?**
→ Read from JSON commons files (see Section IV, Pattern A)

**Want to improve data quality?**
→ Improve generators, file PR (see Section III, Rule 4)

**Found a bug?**
→ File issue, include reproduction steps

**Want to add a feature?**
→ Discuss in issue first, then implement

### For Maintainers

**Need to regenerate data?**
→ Run Pattern D (Section IV)

**Need to modify valley?**
→ Document reason, test thoroughly, commit with explanation

**Need to validate health?**
→ Run health check script (Section V)

**Need to make policy decision?**
→ Follow conflict resolution (Section VII)

## X. Living Document

This document evolves with the repository. Proposed changes follow the same stewardship principles:
- Discuss changes openly
- Document rationale
- Review impact on ecosystem
- Update with clear commits

**Last Updated**: 2025-01-25  
**Next Review**: 2025-04-25 (quarterly)

---

*"A thing is right when it tends to preserve the integrity, stability and beauty of the biotic community. It is wrong when it tends otherwise."* - Aldo Leopold

*In our repository: A change is right when it preserves the integrity, stability, and coherence of our data commons. It is wrong when it tends otherwise.*
