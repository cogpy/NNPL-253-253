⍝ queries.apl - Pattern Query Operations
⍝ Advanced query functions for the Pattern Language
⍝ Author: APL-253 Project
⍝ License: MIT

⍝ ============================================================================
⍝ SEARCH OPERATIONS
⍝ ============================================================================

∇ ids ← SearchPatternsByName searchTerm;i;pattern;name;matches
  ⍝ Search patterns by name (case-insensitive substring match)
  ⍝ Returns array of matching pattern IDs
  
  matches ← ⍬
  
  ⍝ Convert search term to uppercase for case-insensitive search
  searchTerm ← UpperCase searchTerm
  
  ⍝ Search through all patterns
  :For i :In ⍳253
    pattern ← GetPatternByID i
    →(0=≢pattern)/NextPattern
    
    name ← pattern[PATTERN_NAME]
    →(0=≢name)/NextPattern
    
    ⍝ Check if search term is in name
    →(~(searchTerm⍷(UpperCase name)))/NextPattern
    
    ⍝ Add to matches
    matches ,← i
    
  NextPattern:
  :EndFor
  
  ids ← matches
∇

∇ ids ← SearchPatternsByKeyword keyword;i;pattern;context;problem;solution;text
  ⍝ Search patterns by keyword in context, problem, or solution
  ⍝ Returns array of matching pattern IDs
  
  matches ← ⍬
  keyword ← UpperCase keyword
  
  :For i :In ⍳253
    pattern ← GetPatternByID i
    →(0=≢pattern)/NextPattern
    
    ⍝ Combine searchable text fields
    context ← pattern[PATTERN_CONTEXT]
    problem ← pattern[PATTERN_PROBLEM]
    solution ← pattern[PATTERN_SOLUTION]
    text ← context,problem,solution
    
    ⍝ Check if keyword appears in text
    →(~(keyword⍷(UpperCase text)))/NextPattern
    
    matches ,← i
    
  NextPattern:
  :EndFor
  
  ids ← matches
∇

∇ ids ← GetPatternsByAsterisks asterisks;i;pattern;rating
  ⍝ Get all patterns with a specific asterisk rating (1-2)
  ⍝ Returns array of pattern IDs
  
  matches ← ⍬
  
  →(~(asterisks∊1 2))/InvalidRating
  
  :For i :In ⍳253
    pattern ← GetPatternByID i
    →(0=≢pattern)/NextPattern
    
    rating ← pattern[PATTERN_ASTERISKS]
    →(rating≠asterisks)/NextPattern
    
    matches ,← i
    
  NextPattern:
  :EndFor
  
InvalidRating:
  ids ← matches
∇

⍝ ============================================================================
⍝ FILTERING OPERATIONS
⍝ ============================================================================

∇ patterns ← FilterPatternsByCategory ids category;filtered;id;cat
  ⍝ Filter pattern IDs by category
  ⍝ Returns filtered array of pattern IDs
  
  filtered ← ⍬
  
  :For id :In ids
    cat ← GetPatternCategory id
    →(cat≢category)/NextPattern
    
    filtered ,← id
    
  NextPattern:
  :EndFor
  
  patterns ← filtered
∇

∇ patterns ← FilterPatternsByAsterisks ids asterisks;filtered;id;pattern;rating
  ⍝ Filter pattern IDs by asterisk rating
  ⍝ Returns filtered array of pattern IDs
  
  filtered ← ⍬
  
  :For id :In ids
    pattern ← GetPatternByID id
    →(0=≢pattern)/NextPattern
    
    rating ← pattern[PATTERN_ASTERISKS]
    →(rating≠asterisks)/NextPattern
    
    filtered ,← id
    
  NextPattern:
  :EndFor
  
  patterns ← filtered
∇

∇ patterns ← FilterPatternsByIDRange ids min max;filtered;id
  ⍝ Filter pattern IDs by ID range
  ⍝ Returns filtered array of pattern IDs in range [min, max]
  
  filtered ← ⍬
  
  :For id :In ids
    →((id<min)∨(id>max))/NextPattern
    
    filtered ,← id
    
  NextPattern:
  :EndFor
  
  patterns ← filtered
∇

⍝ ============================================================================
⍝ ADVANCED QUERIES
⍝ ============================================================================

∇ result ← QueryPatternsComplex args;category;asterisks;keyword;ids;filtered
  ⍝ Complex query combining multiple filters
  ⍝ args: category asterisks keyword
  ⍝ Use '' or 0 for any parameter to skip that filter
  
  category asterisks keyword ← args
  
  ⍝ Start with all pattern IDs
  ids ← ⍳253
  
  ⍝ Apply category filter if specified
  →(0=≢category)/SkipCategory
  filtered ← FilterPatternsByCategory ids category
  ids ← filtered
  
SkipCategory:
  
  ⍝ Apply asterisks filter if specified
  →(asterisks=0)/SkipAsterisks
  filtered ← FilterPatternsByAsterisks ids asterisks
  ids ← filtered
  
SkipAsterisks:
  
  ⍝ Apply keyword filter if specified
  →(0=≢keyword)/SkipKeyword
  
  ⍝ Filter IDs by keyword
  filtered ← ids∩SearchPatternsByKeyword keyword
  ids ← filtered
  
SkipKeyword:
  
  result ← ids
∇

∇ ids ← GetHighRatedPatterns
  ⍝ Get all 2-asterisk patterns (most important patterns)
  ids ← GetPatternsByAsterisks 2
∇

∇ ids ← GetTownPatterns
  ⍝ Get all patterns in Towns category
  ids ← GetPatternIDsByCategory CATEGORY_TOWNS
∇

∇ ids ← GetBuildingPatterns
  ⍝ Get all patterns in Buildings category
  ids ← GetPatternIDsByCategory CATEGORY_BUILDINGS
∇

∇ ids ← GetConstructionPatterns
  ⍝ Get all patterns in Construction category
  ids ← GetPatternIDsByCategory CATEGORY_CONSTRUCTION
∇

⍝ ============================================================================
⍝ PATTERN COMPARISON
⍝ ============================================================================

∇ similarity ← ComparePatterns args;id1;id2;p1;p2;score
  ⍝ Calculate similarity score between two patterns
  ⍝ args: id1 id2
  ⍝ Returns similarity score (0-100)
  
  id1 id2 ← args
  
  p1 ← GetPatternByID id1
  p2 ← GetPatternByID id2
  
  →((0=≢p1)∨(0=≢p2))/NotFound
  
  score ← 0
  
  ⍝ Same category: +30 points
  →(p1[PATTERN_CATEGORY]≢p2[PATTERN_CATEGORY])/SkipCategoryScore
  score ← score + 30
  
SkipCategoryScore:
  
  ⍝ Same asterisks: +20 points
  →(p1[PATTERN_ASTERISKS]≢p2[PATTERN_ASTERISKS])/SkipAsterisksScore
  score ← score + 20
  
SkipAsterisksScore:
  
  ⍝ Close IDs (within 10): +50 points, scaled by distance
  dist ← |id1 - id2
  →(dist>10)/SkipDistanceScore
  score ← score + 50 × (1 - dist÷10)
  
SkipDistanceScore:
  
  similarity ← score
  →0
  
NotFound:
  similarity ← 0
∇

∇ similar ← FindSimilarPatterns args;id;threshold;i;score;matches
  ⍝ Find patterns similar to given pattern
  ⍝ args: id threshold
  ⍝ Returns array of pattern IDs with similarity >= threshold
  
  id threshold ← args
  matches ← ⍬
  
  :For i :In ⍳253
    →(i=id)/NextPattern ⍝ Skip self
    
    score ← ComparePatterns id i
    →(score<threshold)/NextPattern
    
    matches ,← i
    
  NextPattern:
  :EndFor
  
  similar ← matches
∇

⍝ ============================================================================
⍝ STATISTICS
⍝ ============================================================================

∇ ShowQueryStats
  ⍝ Display query statistics
  
  ⍞ ← 'Pattern Query Statistics:',⎕UCS 10
  ⍞ ← '  Total Patterns: ',(⍕GetPatternCount),⎕UCS 10
  ⍞ ← '  High Rated (2*): ',(⍕≢GetHighRatedPatterns),⎕UCS 10
  ⍞ ← '  Towns: ',(⍕≢GetTownPatterns),⎕UCS 10
  ⍞ ← '  Buildings: ',(⍕≢GetBuildingPatterns),⎕UCS 10
  ⍞ ← '  Construction: ',(⍕≢GetConstructionPatterns),⎕UCS 10
  ⍞ ← '  Sequences: ',(⍕GetSequenceCount),⎕UCS 10
∇

⍝ ============================================================================
⍝ UTILITY FUNCTIONS
⍝ ============================================================================

∇ upper ← UpperCase text
  ⍝ Convert text to uppercase (simplified)
  ⍝ Note: In real APL, use ⎕C or proper Unicode handling
  
  upper ← text ⍝ Placeholder - in real APL would use proper conversion
∇

∇ results ← FormatQueryResults ids;i;id;pattern;result
  ⍝ Format query results for display
  
  results ← ''
  
  →(0=≢ids)/NoResults
  
  results ← 'Found ',(⍕≢ids),' pattern(s):',⎕UCS 10,⎕UCS 10
  
  :For id :In ids
    pattern ← GetPatternByID id
    result ← FormatPatternSummary pattern
    results ,← result,⎕UCS 10
  :EndFor
  
  →0
  
NoResults:
  results ← 'No patterns found.',⎕UCS 10
∇

∇ PrintQueryResults ids
  ⍝ Print query results to console
  
  ⍞ ← FormatQueryResults ids
∇

⍞ ← 'Pattern Query Module Loaded',⎕UCS 10
