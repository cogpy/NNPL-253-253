⍝ patterns.apl - Core Pattern Language Data Structures
⍝ Implementation of Christopher Alexander's Pattern Language in APL
⍝ Author: APL-253 Project
⍝ License: MIT

⍝ ============================================================================
⍝ PATTERN DATA STRUCTURES
⍝ ============================================================================

⍝ Pattern structure indices
PATTERN_ID ← 1
PATTERN_NAME ← 2
PATTERN_CATEGORY ← 3
PATTERN_ASTERISKS ← 4
PATTERN_CONTEXT ← 5
PATTERN_PROBLEM ← 6
PATTERN_SOLUTION ← 7
PATTERN_DIAGRAM ← 8
PATTERN_CONNECTIONS ← 9

⍝ Categories
CATEGORY_TOWNS ← 'Towns'
CATEGORY_BUILDINGS ← 'Buildings'
CATEGORY_CONSTRUCTION ← 'Construction'

⍝ Category boundaries
TOWNS_START ← 1
TOWNS_END ← 94
BUILDINGS_START ← 95
BUILDINGS_END ← 204
CONSTRUCTION_START ← 205
CONSTRUCTION_END ← 253

⍝ ============================================================================
⍝ INITIALIZATION
⍝ ============================================================================

∇ InitializePatterns
  ⍝ Initialize the pattern database
  ⍝ Creates empty pattern arrays for 253 patterns
  
  ⍝ Initialize pattern storage
  PATTERNS ← 253⍴⊂9⍴⊂''
  
  ⍝ Initialize category mapping
  PATTERN_CATEGORIES ← 253⍴''
  
  ⍝ Initialize sequence storage (36 sequences)
  SEQUENCES ← 36⍴⊂⍬
  
  ⍝ Initialize archetypal patterns (102 patterns)
  ARCHETYPAL_PATTERNS ← 102⍴⊂''
  ARCHETYPAL_IDS ← 102⍴''
  
  ⍝ Initialize domain mappings
  DOMAINS ← 'physical' 'social' 'conceptual' 'psychic'
  
  ⍝ Set category ranges
  PATTERN_CATEGORIES[TOWNS_START..TOWNS_END] ← CATEGORY_TOWNS
  PATTERN_CATEGORIES[BUILDINGS_START..BUILDINGS_END] ← CATEGORY_BUILDINGS
  PATTERN_CATEGORIES[CONSTRUCTION_START..CONSTRUCTION_END] ← CATEGORY_CONSTRUCTION
  
  ⍞ ← 'Pattern database initialized with 253 patterns',⎕UCS 10
∇

⍝ ============================================================================
⍝ PATTERN STORAGE AND RETRIEVAL
⍝ ============================================================================

∇ result ← StorePattern args;id;name;category;asterisks;context;problem;solution;diagram;connections
  ⍝ Store a pattern in the database
  ⍝ args: id name category asterisks context problem solution diagram connections
  
  id name category asterisks context problem solution diagram connections ← args
  
  ⍝ Validate ID range
  →(~(id∊⍳253))/InvalidID
  
  ⍝ Create pattern record
  PATTERNS[id] ← ⊂id name category asterisks context problem solution diagram connections
  
  result ← 1 ⍝ Success
  →0
  
InvalidID:
  result ← 0 ⍝ Failure
∇

∇ pattern ← GetPatternByID id
  ⍝ Retrieve a pattern by its ID
  ⍝ Returns the pattern record or empty if not found
  
  →(~(id∊⍳253))/NotFound
  
  pattern ← PATTERNS[id]
  →0
  
NotFound:
  pattern ← ⍬
∇

∇ ids ← GetAllPatternIDs
  ⍝ Get all pattern IDs (1-253)
  ids ← ⍳253
∇

∇ count ← GetPatternCount
  ⍝ Get total number of patterns
  count ← 253
∇

⍝ ============================================================================
⍝ CATEGORY OPERATIONS
⍝ ============================================================================

∇ category ← GetPatternCategory id
  ⍝ Get the category of a pattern by ID
  
  →(~(id∊⍳253))/NotFound
  
  ⍝ Determine category based on ID range
  →((id≥TOWNS_START)∧(id≤TOWNS_END))/ReturnTowns
  →((id≥BUILDINGS_START)∧(id≤BUILDINGS_END))/ReturnBuildings
  →((id≥CONSTRUCTION_START)∧(id≤CONSTRUCTION_END))/ReturnConstruction
  
ReturnTowns:
  category ← CATEGORY_TOWNS
  →0
  
ReturnBuildings:
  category ← CATEGORY_BUILDINGS
  →0
  
ReturnConstruction:
  category ← CATEGORY_CONSTRUCTION
  →0
  
NotFound:
  category ← ''
∇

∇ ids ← GetPatternIDsByCategory cat
  ⍝ Get all pattern IDs in a category
  
  →(cat≡CATEGORY_TOWNS)/ReturnTowns
  →(cat≡CATEGORY_BUILDINGS)/ReturnBuildings
  →(cat≡CATEGORY_CONSTRUCTION)/ReturnConstruction
  →InvalidCategory
  
ReturnTowns:
  ids ← TOWNS_START..TOWNS_END
  →0
  
ReturnBuildings:
  ids ← BUILDINGS_START..BUILDINGS_END
  →0
  
ReturnConstruction:
  ids ← CONSTRUCTION_START..CONSTRUCTION_END
  →0
  
InvalidCategory:
  ids ← ⍬
∇

∇ count ← CountPatternsInCategory cat
  ⍝ Count patterns in a category
  
  →(cat≡CATEGORY_TOWNS)/ReturnTowns
  →(cat≡CATEGORY_BUILDINGS)/ReturnBuildings
  →(cat≡CATEGORY_CONSTRUCTION)/ReturnConstruction
  →InvalidCategory
  
ReturnTowns:
  count ← (TOWNS_END - TOWNS_START) + 1
  →0
  
ReturnBuildings:
  count ← (BUILDINGS_END - BUILDINGS_START) + 1
  →0
  
ReturnConstruction:
  count ← (CONSTRUCTION_END - CONSTRUCTION_START) + 1
  →0
  
InvalidCategory:
  count ← 0
∇

⍝ ============================================================================
⍝ SEQUENCE OPERATIONS
⍝ ============================================================================

∇ result ← StoreSequence args;id;patterns
  ⍝ Store a pattern sequence
  ⍝ args: id patterns
  
  id patterns ← args
  
  ⍝ Validate sequence ID range
  →(~(id∊⍳36))/InvalidID
  
  ⍝ Store sequence
  SEQUENCES[id] ← ⊂patterns
  
  result ← 1 ⍝ Success
  →0
  
InvalidID:
  result ← 0 ⍝ Failure
∇

∇ patterns ← GetPatternSequence id
  ⍝ Get patterns in a sequence
  
  →(~(id∊⍳36))/NotFound
  
  patterns ← SEQUENCES[id]
  →0
  
NotFound:
  patterns ← ⍬
∇

∇ count ← GetSequenceCount
  ⍝ Get total number of sequences
  count ← 36
∇

⍝ ============================================================================
⍝ ARCHETYPAL PATTERN OPERATIONS
⍝ ============================================================================

∇ result ← StoreArchetypalPattern args;id;pattern;placeholders
  ⍝ Store an archetypal pattern with placeholders
  ⍝ args: id pattern placeholders
  
  id pattern placeholders ← args
  
  ⍝ Find or add ID in archetypal IDs
  idx ← ARCHETYPAL_IDS⍳⊂id
  →(idx≤≢ARCHETYPAL_IDS)/UpdateExisting
  
  ⍝ Add new pattern
  ARCHETYPAL_IDS ,← ⊂id
  ARCHETYPAL_PATTERNS ,← ⊂pattern placeholders
  result ← 1
  →0
  
UpdateExisting:
  ARCHETYPAL_PATTERNS[idx] ← ⊂pattern placeholders
  result ← 1
∇

∇ pattern ← GetArchetypalPattern id
  ⍝ Get an archetypal pattern by ID
  
  idx ← ARCHETYPAL_IDS⍳⊂id
  →(idx>≢ARCHETYPAL_IDS)/NotFound
  
  pattern ← ARCHETYPAL_PATTERNS[idx]
  →0
  
NotFound:
  pattern ← ⍬
∇

⍝ ============================================================================
⍝ UTILITY FUNCTIONS
⍝ ============================================================================

∇ result ← FormatPatternSummary pattern;id;name;category;asterisks
  ⍝ Format a pattern for display
  
  →(0=≢pattern)/Empty
  
  id name category asterisks ← 4↑pattern
  
  result ← 'Pattern #',(⍕id),': ',name
  result ,← ⎕UCS 10
  result ,← 'Category: ',category,' | Rating: ',(asterisks⍴'*')
  →0
  
Empty:
  result ← 'Empty pattern'
∇

∇ PrintPattern pattern
  ⍝ Print a pattern to the console
  
  ⍞ ← FormatPatternSummary pattern
  ⍞ ← ⎕UCS 10
∇

∇ ShowCategoryCounts
  ⍝ Display counts for each category
  
  ⍞ ← 'Pattern Categories:',⎕UCS 10
  ⍞ ← '  Towns: ',(⍕CountPatternsInCategory CATEGORY_TOWNS),⎕UCS 10
  ⍞ ← '  Buildings: ',(⍕CountPatternsInCategory CATEGORY_BUILDINGS),⎕UCS 10
  ⍞ ← '  Construction: ',(⍕CountPatternsInCategory CATEGORY_CONSTRUCTION),⎕UCS 10
  ⍞ ← '  Total: ',(⍕GetPatternCount),⎕UCS 10
∇

⍝ ============================================================================
⍝ INITIALIZATION ON LOAD
⍝ ============================================================================

⍝ Auto-initialize when loaded
InitializePatterns

⍞ ← 'Pattern Language Core Module Loaded',⎕UCS 10
⍞ ← 'Version 1.0 - 253 Patterns',⎕UCS 10
