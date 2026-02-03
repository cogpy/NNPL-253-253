# Countryside Access Guide for Contributors

> **Pattern 7: THE COUNTRYSIDE** - How to access and use the commons
> 
> *"The public is free to visit the land, hike there, picnic, explore... so long as they conform to the ground rules."* - Christopher Alexander

## Quick Start

### What is the Countryside?

The **countryside** refers to our shared source data:
- **apl/** - Original Pattern Language HTML files
- **uia/** - UIA organizational patterns  
- **JSON files** - Generated structured data

### Golden Rules

1. ✅ **Read freely** - All regions can access commons data
2. ❌ **Don't modify valleys** - apl/ and uia/ are read-only
3. 🔄 **Improve generators** - Fix bugs in generation scripts, not JSON
4. 🤝 **Contribute back** - Share improvements with the community

## Access Patterns

### Pattern 1: Read a Pattern from Commons

**Goal**: Load pattern data for display or analysis

```python
import json

def load_pattern(pattern_id):
    """
    Load a single pattern from the commons.
    
    Args:
        pattern_id: Pattern identifier (e.g., 'apl001')
    
    Returns:
        dict: Pattern data
    
    Raises:
        KeyError: If pattern not found
    """
    with open('pattern_language_generated.json', 'r') as f:
        data = json.load(f)
    
    patterns = data.get('patterns', [])
    for pattern in patterns:
        if pattern.get('id') == pattern_id:
            return pattern
    
    raise KeyError(f"Pattern {pattern_id} not found in commons")

# Example usage
try:
    pattern = load_pattern('apl007')
    print(f"Name: {pattern['name']}")
    print(f"Number: {pattern['number']}")
    print(f"Category: {pattern['category']}")
except KeyError as e:
    print(f"Error: {e}")
```

### Pattern 2: Load All Patterns

**Goal**: Load entire pattern collection

```python
import json

def load_all_patterns():
    """
    Load all patterns from the commons.
    
    Returns:
        list: List of all pattern dictionaries
    """
    with open('pattern_language_generated.json', 'r') as f:
        data = json.load(f)
    
    return data.get('patterns', [])

# Example usage
patterns = load_all_patterns()
print(f"Loaded {len(patterns)} patterns")

# Filter by category
towns = [p for p in patterns if p.get('category') == 'Towns']
print(f"Found {len(towns)} town patterns")
```

### Pattern 3: Navigate Pattern Relationships

**Goal**: Follow connections between patterns

```python
def get_related_patterns(pattern_id, relation='broader'):
    """
    Get patterns related to a given pattern.
    
    Args:
        pattern_id: Source pattern ID
        relation: 'broader' or 'narrower'
    
    Returns:
        list: Related pattern objects
    """
    pattern = load_pattern(pattern_id)
    
    # Get relationship IDs
    if relation == 'broader':
        related_ids = pattern.get('broader_patterns', [])
    elif relation == 'narrower':
        related_ids = pattern.get('narrower_patterns', [])
    else:
        raise ValueError(f"Unknown relation: {relation}")
    
    # Load related patterns
    related = []
    for rid in related_ids:
        try:
            related.append(load_pattern(rid))
        except KeyError:
            print(f"Warning: Referenced pattern {rid} not found")
    
    return related

# Example usage
broader = get_related_patterns('apl007', 'broader')
print(f"Patterns that provide context for Pattern 7:")
for p in broader:
    print(f"  - {p['number']}: {p['name']}")

narrower = get_related_patterns('apl007', 'narrower')
print(f"\nPatterns that detail Pattern 7:")
for p in narrower:
    print(f"  - {p['number']}: {p['name']}")
```

### Pattern 4: Work with Sequences

**Goal**: Access pattern sequences

```python
def load_sequence(sequence_id):
    """
    Load a pattern sequence from commons.
    
    Args:
        sequence_id: Sequence identifier (e.g., 'seq02')
    
    Returns:
        dict: Sequence data with pattern IDs
    """
    with open('pattern_sequences.json', 'r') as f:
        data = json.load(f)
    
    sequences = data.get('sequences', [])
    for seq in sequences:
        if seq.get('id') == sequence_id:
            return seq
    
    raise KeyError(f"Sequence {sequence_id} not found")

def get_sequence_patterns(sequence_id):
    """
    Get all patterns in a sequence.
    
    Args:
        sequence_id: Sequence identifier
    
    Returns:
        list: Pattern objects in sequence order
    """
    sequence = load_sequence(sequence_id)
    pattern_ids = sequence.get('patterns', [])
    
    return [load_pattern(pid) for pid in pattern_ids]

# Example usage
seq2_patterns = get_sequence_patterns('seq02')
print("Sequence 2: Regional Policies")
for i, p in enumerate(seq2_patterns, 1):
    print(f"  {i}. Pattern {p['number']}: {p['name']}")
```

### Pattern 5: Parse Valley HTML

**Goal**: Read original HTML from valleys (for generators)

```python
from bs4 import BeautifulSoup

def read_valley_html(pattern_id):
    """
    Read original HTML from apl/ valley.
    
    IMPORTANT: This is READ-ONLY. Never write back to valleys.
    
    Args:
        pattern_id: Pattern identifier (e.g., 'apl001')
    
    Returns:
        str: HTML content
    """
    # Extract pattern number from ID
    number = pattern_id.replace('apl', '')
    
    # Try common naming patterns
    possible_files = [
        f'apl/apl{number}.htm',
        f'apl/apl{number}.html',
        f'apl/{number}.htm',
    ]
    
    for filepath in possible_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            continue
    
    raise FileNotFoundError(f"HTML file for {pattern_id} not found in apl/")

def parse_pattern_html(html_content):
    """
    Parse pattern HTML to extract structured data.
    
    Args:
        html_content: HTML string from valley
    
    Returns:
        dict: Extracted pattern data
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # This is example parsing logic - adapt as needed
    pattern_data = {
        'title': None,
        'problem': None,
        'solution': None,
    }
    
    # Extract title
    title_elem = soup.find('h1') or soup.find('title')
    if title_elem:
        pattern_data['title'] = title_elem.get_text().strip()
    
    # Extract problem and solution sections
    # (This would need to match actual HTML structure)
    
    return pattern_data

# Example usage (for generator scripts)
html = read_valley_html('apl001')
data = parse_pattern_html(html)
print(f"Parsed: {data['title']}")
```

### Pattern 6: Cache Commons Data

**Goal**: Efficiently access commons without repeated file reads

```python
class PatternCommons:
    """
    Cached access to pattern commons.
    
    Use this for applications that need to access patterns frequently.
    """
    
    def __init__(self):
        self._patterns = None
        self._sequences = None
        self._pattern_index = None
    
    def _load_patterns(self):
        """Lazy load patterns on first access"""
        if self._patterns is None:
            with open('pattern_language_generated.json', 'r') as f:
                data = json.load(f)
            self._patterns = data.get('patterns', [])
            
            # Build index for fast lookup
            self._pattern_index = {
                p['id']: p for p in self._patterns
            }
        
        return self._patterns
    
    def _load_sequences(self):
        """Lazy load sequences on first access"""
        if self._sequences is None:
            with open('pattern_sequences.json', 'r') as f:
                data = json.load(f)
            self._sequences = data.get('sequences', [])
        
        return self._sequences
    
    def get_pattern(self, pattern_id):
        """Get pattern by ID with caching"""
        self._load_patterns()
        
        if pattern_id not in self._pattern_index:
            raise KeyError(f"Pattern {pattern_id} not found")
        
        return self._pattern_index[pattern_id]
    
    def get_all_patterns(self):
        """Get all patterns with caching"""
        return self._load_patterns()
    
    def get_sequence(self, sequence_id):
        """Get sequence by ID with caching"""
        sequences = self._load_sequences()
        
        for seq in sequences:
            if seq.get('id') == sequence_id:
                return seq
        
        raise KeyError(f"Sequence {sequence_id} not found")
    
    def search_patterns(self, query, field='name'):
        """
        Search patterns by field value.
        
        Args:
            query: Search string
            field: Field to search in
        
        Returns:
            list: Matching patterns
        """
        patterns = self._load_patterns()
        query_lower = query.lower()
        
        matches = []
        for p in patterns:
            value = str(p.get(field, '')).lower()
            if query_lower in value:
                matches.append(p)
        
        return matches

# Example usage
commons = PatternCommons()

# First access loads from file
p1 = commons.get_pattern('apl001')
print(f"Pattern 1: {p1['name']}")

# Subsequent accesses use cache
p7 = commons.get_pattern('apl007')
print(f"Pattern 7: {p7['name']}")

# Search
countryside = commons.search_patterns('countryside', field='name')
print(f"\nPatterns matching 'countryside': {len(countryside)}")
```

## Common Tasks

### Task: Build a Pattern Navigator

```python
def navigate_pattern(pattern_id):
    """Interactive pattern navigation"""
    commons = PatternCommons()
    
    while True:
        # Show current pattern
        pattern = commons.get_pattern(pattern_id)
        print(f"\n{'=' * 60}")
        print(f"Pattern {pattern['number']}: {pattern['name']}")
        print(f"{'=' * 60}")
        print(f"Category: {pattern.get('category', 'Unknown')}")
        
        # Show navigation options
        broader = pattern.get('broader_patterns', [])
        narrower = pattern.get('narrower_patterns', [])
        
        print("\nNavigate:")
        if broader:
            print(f"  [B]roader patterns: {', '.join(broader)}")
        if narrower:
            print(f"  [N]arrower patterns: {', '.join(narrower)}")
        print("  [Q]uit")
        
        choice = input("\nChoice: ").strip().lower()
        
        if choice == 'q':
            break
        elif choice == 'b' and broader:
            pattern_id = broader[0]  # Navigate to first broader
        elif choice == 'n' and narrower:
            pattern_id = narrower[0]  # Navigate to first narrower
        else:
            print("Invalid choice")

# Usage
# navigate_pattern('apl007')
```

### Task: Generate Pattern Report

```python
def generate_pattern_report(category=None):
    """Generate a report of patterns"""
    commons = PatternCommons()
    patterns = commons.get_all_patterns()
    
    # Filter by category if specified
    if category:
        patterns = [p for p in patterns if p.get('category') == category]
    
    # Group by category
    by_category = {}
    for p in patterns:
        cat = p.get('category', 'Unknown')
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(p)
    
    # Generate report
    print("# Pattern Language Report")
    print()
    print(f"Total patterns: {len(patterns)}")
    print()
    
    for cat, cat_patterns in sorted(by_category.items()):
        print(f"## {cat} ({len(cat_patterns)} patterns)")
        print()
        
        for p in sorted(cat_patterns, key=lambda x: x.get('number', 0)):
            print(f"- Pattern {p.get('number')}: {p.get('name')}")
        
        print()

# Usage
# generate_pattern_report()
# generate_pattern_report(category='Towns')
```

### Task: Validate Pattern Data

```python
def validate_pattern_structure(pattern):
    """
    Validate that a pattern has required fields.
    
    Returns:
        tuple: (is_valid, list of issues)
    """
    required_fields = ['id', 'number', 'name', 'category']
    optional_fields = ['broader_patterns', 'narrower_patterns', 'description']
    
    issues = []
    
    # Check required fields
    for field in required_fields:
        if field not in pattern:
            issues.append(f"Missing required field: {field}")
        elif not pattern[field]:
            issues.append(f"Empty required field: {field}")
    
    # Check field types
    if 'number' in pattern and not isinstance(pattern['number'], int):
        issues.append(f"'number' should be int, got {type(pattern['number'])}")
    
    if 'broader_patterns' in pattern:
        if not isinstance(pattern['broader_patterns'], list):
            issues.append("'broader_patterns' should be list")
    
    if 'narrower_patterns' in pattern:
        if not isinstance(pattern['narrower_patterns'], list):
            issues.append("'narrower_patterns' should be list")
    
    return len(issues) == 0, issues

def validate_all_patterns():
    """Validate all patterns in commons"""
    commons = PatternCommons()
    patterns = commons.get_all_patterns()
    
    invalid_patterns = []
    
    for pattern in patterns:
        is_valid, issues = validate_pattern_structure(pattern)
        if not is_valid:
            invalid_patterns.append((pattern.get('id', 'unknown'), issues))
    
    if invalid_patterns:
        print(f"Found {len(invalid_patterns)} invalid patterns:")
        for pid, issues in invalid_patterns:
            print(f"\n{pid}:")
            for issue in issues:
                print(f"  - {issue}")
    else:
        print(f"✅ All {len(patterns)} patterns are valid")
    
    return len(invalid_patterns) == 0

# Usage
# validate_all_patterns()
```

## Ground Rules Checklist

Before committing code that accesses the commons:

- [ ] ✅ I only read from apl/ and uia/ (never write)
- [ ] ✅ I don't manually edit JSON commons files
- [ ] ✅ I parse JSON correctly and handle missing fields
- [ ] ✅ I test my code against actual commons data
- [ ] ✅ I cache commons data if accessing frequently
- [ ] ✅ I handle errors gracefully (missing patterns, broken refs)
- [ ] ✅ I preserve pattern relationships in my code
- [ ] ✅ I document my usage of commons in my code
- [ ] ✅ If I find issues, I file a bug report
- [ ] ✅ If I improve parsing, I contribute back

## Getting Help

### Common Issues

**Issue**: "Pattern not found"
- Check that pattern ID is correct (e.g., 'apl007' not 'pattern7')
- Verify pattern exists in pattern_language_generated.json
- Check that JSON file is up to date

**Issue**: "Broken pattern references"
- File issue - this indicates data integrity problem
- Run health check: `./verify_countryside_health.sh`
- Report to maintainers

**Issue**: "JSON file missing"
- Check that you're in repository root
- Verify commons have been generated
- May need to run: `./regenerate_commons.sh` (maintainers)

**Issue**: "Need to modify valley HTML"
- You probably don't! Explain your use case in an issue
- Maintainers can help find alternative approach
- True modifications are rare and need discussion

### Resources

- **COUNTRYSIDE_STEWARDSHIP.md** - Complete stewardship policies
- **THE_COUNTRYSIDE.md** - Pattern 7 explanation
- **verify_countryside_health.sh** - Check commons health
- **regenerate_commons.sh** - Regenerate commons (maintainers)

### Contact

File issues for:
- Data quality problems
- Missing patterns
- Broken relationships
- Access difficulties
- Feature requests

## Examples from Real Regions

### npu253/ Region

```python
# From npu253/pattern_api.py
class PatternAPI:
    def _load_patterns(self):
        """Load patterns from commons"""
        with open('pattern_language_generated.json', 'r') as f:
            data = json.load(f)
        return data.get('patterns', [])
```

### skill_framework/ Region

```python
# From skill_framework/sequence_loader.py
def load_sequences():
    """Load pattern sequences from commons"""
    with open('pattern_sequences.json', 'r') as f:
        return json.load(f).get('sequences', [])
```

### markdown/ Region

```python
# From markdown/generate_from_apl.py
def read_apl_html(pattern_num):
    """Read from apl/ valley (read-only)"""
    filepath = f'apl/apl{pattern_num:03d}.htm'
    with open(filepath, 'r') as f:
        return f.read()
```

## Summary

The countryside commons is our shared resource. By following the ground rules and using these access patterns, you help maintain a healthy ecosystem that benefits everyone.

**Remember**:
- Read freely ✅
- Modify valleys never ❌
- Improve generators ✅
- Contribute back ✅

---

*"The public is free to visit the land, hike there, picnic, explore... so long as they conform to the ground rules."*

Happy exploring! 🏔️
