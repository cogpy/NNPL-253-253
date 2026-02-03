⍝ relationships.apl - Pattern Relationship Operations
⍝ Navigate and analyze relationships between patterns
⍝ Author: APL-253 Project
⍝ License: MIT

⍝ ============================================================================
⍝ RELATIONSHIP STORAGE
⍝ ============================================================================

∇ InitializeRelationships
  ⍝ Initialize relationship storage structures
  
  ⍝ Storage for pattern relationships
  ⍝ Each pattern can have:
  ⍝   - Preceding patterns (patterns that lead to this one)
  ⍝   - Following patterns (patterns that follow from this one)
  ⍝   - Related patterns (patterns in same domain/context)
  
  PRECEDING_PATTERNS ← 253⍴⊂⍬
  FOLLOWING_PATTERNS ← 253⍴⊂⍬
  RELATED_PATTERNS ← 253⍴⊂⍬
  
  ⍞ ← 'Relationship storage initialized',⎕UCS 10
∇

⍝ ============================================================================
⍝ RELATIONSHIP MANAGEMENT
⍝ ============================================================================

∇ result ← AddPrecedingPattern args;id;preceding
  ⍝ Add a preceding pattern relationship
  ⍝ args: id preceding
  
  id preceding ← args
  
  →(~(id∊⍳253))/InvalidID
  →(~(preceding∊⍳253))/InvalidID
  
  ⍝ Get current preceding patterns
  current ← PRECEDING_PATTERNS[id]
  
  ⍝ Add new preceding if not already present
  →(preceding∊current)/AlreadyExists
  
  current ,← preceding
  PRECEDING_PATTERNS[id] ← ⊂current
  
AlreadyExists:
  result ← 1
  →0
  
InvalidID:
  result ← 0
∇

∇ result ← AddFollowingPattern args;id;following
  ⍝ Add a following pattern relationship
  ⍝ args: id following
  
  id following ← args
  
  →(~(id∊⍳253))/InvalidID
  →(~(following∊⍳253))/InvalidID
  
  ⍝ Get current following patterns
  current ← FOLLOWING_PATTERNS[id]
  
  ⍝ Add new following if not already present
  →(following∊current)/AlreadyExists
  
  current ,← following
  FOLLOWING_PATTERNS[id] ← ⊂current
  
AlreadyExists:
  result ← 1
  →0
  
InvalidID:
  result ← 0
∇

∇ result ← AddRelatedPattern args;id;related
  ⍝ Add a related pattern relationship
  ⍝ args: id related
  
  id related ← args
  
  →(~(id∊⍳253))/InvalidID
  →(~(related∊⍳253))/InvalidID
  
  ⍝ Get current related patterns
  current ← RELATED_PATTERNS[id]
  
  ⍝ Add new related if not already present
  →(related∊current)/AlreadyExists
  
  current ,← related
  RELATED_PATTERNS[id] ← ⊂current
  
AlreadyExists:
  result ← 1
  →0
  
InvalidID:
  result ← 0
∇

⍝ ============================================================================
⍝ RELATIONSHIP RETRIEVAL
⍝ ============================================================================

∇ patterns ← GetPrecedingPatterns id
  ⍝ Get all patterns that precede this pattern
  
  →(~(id∊⍳253))/InvalidID
  
  patterns ← PRECEDING_PATTERNS[id]
  →0
  
InvalidID:
  patterns ← ⍬
∇

∇ patterns ← GetFollowingPatterns id
  ⍝ Get all patterns that follow this pattern
  
  →(~(id∊⍳253))/InvalidID
  
  patterns ← FOLLOWING_PATTERNS[id]
  →0
  
InvalidID:
  patterns ← ⍬
∇

∇ patterns ← GetRelatedPatterns id
  ⍝ Get all related patterns
  
  →(~(id∊⍳253))/InvalidID
  
  patterns ← RELATED_PATTERNS[id]
  →0
  
InvalidID:
  patterns ← ⍬
∇

∇ patterns ← GetAllConnectedPatterns id
  ⍝ Get all patterns connected to this pattern
  ⍝ (preceding + following + related)
  
  →(~(id∊⍳253))/InvalidID
  
  preceding ← PRECEDING_PATTERNS[id]
  following ← FOLLOWING_PATTERNS[id]
  related ← RELATED_PATTERNS[id]
  
  ⍝ Combine and deduplicate
  patterns ← preceding,following,related
  patterns ← ∪patterns ⍝ Unique
  
  →0
  
InvalidID:
  patterns ← ⍬
∇

⍝ ============================================================================
⍝ RELATIONSHIP ANALYSIS
⍝ ============================================================================

∇ count ← CountPrecedingPatterns id
  ⍝ Count how many patterns precede this pattern
  
  patterns ← GetPrecedingPatterns id
  count ← ≢patterns
∇

∇ count ← CountFollowingPatterns id
  ⍝ Count how many patterns follow this pattern
  
  patterns ← GetFollowingPatterns id
  count ← ≢patterns
∇

∇ count ← CountRelatedPatterns id
  ⍝ Count how many related patterns exist
  
  patterns ← GetRelatedPatterns id
  count ← ≢patterns
∇

∇ count ← GetTotalConnections id
  ⍝ Get total number of connections for a pattern
  
  count ← CountPrecedingPatterns id
  count ← count + CountFollowingPatterns id
  count ← count + CountRelatedPatterns id
∇

∇ ids ← GetMostConnectedPatterns n;i;connections;counts;sorted
  ⍝ Get the n most connected patterns
  ⍝ Returns array of pattern IDs sorted by connection count
  
  ⍝ Calculate connection counts for all patterns
  counts ← ⍬
  :For i :In ⍳253
    counts ,← GetTotalConnections i
  :EndFor
  
  ⍝ Sort indices by counts (descending)
  sorted ← ⍒counts ⍝ Grade down
  
  ⍝ Take top n
  →(n>253)/TakeAll
  
  ids ← n↑sorted[⍳253]
  →0
  
TakeAll:
  ids ← sorted[⍳253]
∇

∇ ids ← GetLeastConnectedPatterns n;i;connections;counts;sorted
  ⍝ Get the n least connected patterns
  ⍝ Returns array of pattern IDs sorted by connection count (ascending)
  
  ⍝ Calculate connection counts for all patterns
  counts ← ⍬
  :For i :In ⍳253
    counts ,← GetTotalConnections i
  :EndFor
  
  ⍝ Sort indices by counts (ascending)
  sorted ← ⍋counts ⍝ Grade up
  
  ⍝ Take bottom n
  →(n>253)/TakeAll
  
  ids ← n↑sorted[⍳253]
  →0
  
TakeAll:
  ids ← sorted[⍳253]
∇

⍝ ============================================================================
⍝ PATTERN PATHS
⍝ ============================================================================

∇ path ← FindPathBetweenPatterns args;start;end;visited;queue;current;next;found
  ⍝ Find shortest path between two patterns using BFS
  ⍝ args: start end
  ⍝ Returns path as array of pattern IDs, or empty if no path
  
  start end ← args
  
  →(~((start∊⍳253)∧(end∊⍳253)))/InvalidID
  →(start=end)/SamePath
  
  ⍝ BFS initialization
  visited ← 253⍴0
  queue ← ⊂(,start) ⍝ Queue of paths
  
  ⍝ BFS loop
  :While (0<≢queue)
    ⍝ Dequeue first path
    current ← ⊃queue
    queue ← 1↓queue
    
    ⍝ Get last pattern in current path
    last ← ¯1↑current
    
    ⍝ Get all connected patterns
    connected ← GetAllConnectedPatterns last
    
    ⍝ Check each connected pattern
    :For next :In connected
      →(visited[next])/NextConnected ⍝ Skip if visited
      
      ⍝ Create new path
      newpath ← current,next
      
      ⍝ Check if we reached the end
      →(next≠end)/NotEnd
      path ← newpath
      →FoundPath
      
    NotEnd:
      ⍝ Mark as visited and enqueue
      visited[next] ← 1
      queue ,← ⊂newpath
      
    NextConnected:
    :EndFor
  :EndWhile
  
  ⍝ No path found
  path ← ⍬
  →0
  
SamePath:
  path ← ,start
  →0
  
FoundPath:
  →0
  
InvalidID:
  path ← ⍬
∇

∇ distance ← GetPatternDistance args;start;end;path
  ⍝ Get distance between two patterns
  ⍝ args: start end
  ⍝ Returns number of hops, or 0 if no path
  
  start end ← args
  
  path ← FindPathBetweenPatterns start end
  →(0=≢path)/NoPath
  
  distance ← (≢path) - 1 ⍝ Number of edges
  →0
  
NoPath:
  distance ← 0
∇

⍝ ============================================================================
⍝ RELATIONSHIP VISUALIZATION
⍝ ============================================================================

∇ result ← FormatRelationships id;pattern;preceding;following;related
  ⍝ Format relationships for display
  
  →(~(id∊⍳253))/InvalidID
  
  pattern ← GetPatternByID id
  preceding ← GetPrecedingPatterns id
  following ← GetFollowingPatterns id
  related ← GetRelatedPatterns id
  
  result ← 'Relationships for Pattern #',(⍕id),':',⎕UCS 10
  result ,← FormatPatternSummary pattern
  result ,← ⎕UCS 10
  
  result ,← '  Preceding patterns (',(⍕≢preceding),'): '
  result ,← FormatIDList preceding
  result ,← ⎕UCS 10
  
  result ,← '  Following patterns (',(⍕≢following),'): '
  result ,← FormatIDList following
  result ,← ⎕UCS 10
  
  result ,← '  Related patterns (',(⍕≢related),'): '
  result ,← FormatIDList related
  result ,← ⎕UCS 10
  
  →0
  
InvalidID:
  result ← 'Invalid pattern ID',⎕UCS 10
∇

∇ result ← FormatIDList ids;i;id
  ⍝ Format list of pattern IDs
  
  →(0=≢ids)/Empty
  
  result ← ''
  :For id :In ids
    result ,← (⍕id),' '
  :EndFor
  
  →0
  
Empty:
  result ← '(none)'
∇

∇ PrintRelationships id
  ⍝ Print relationships to console
  
  ⍞ ← FormatRelationships id
∇

∇ ShowRelationshipStats
  ⍝ Display relationship statistics
  
  ⍞ ← 'Relationship Statistics:',⎕UCS 10
  
  most_connected ← GetMostConnectedPatterns 5
  ⍞ ← '  Most connected patterns: ',(FormatIDList most_connected),⎕UCS 10
  
  least_connected ← GetLeastConnectedPatterns 5
  ⍞ ← '  Least connected patterns: ',(FormatIDList least_connected),⎕UCS 10
∇

⍝ ============================================================================
⍝ INITIALIZATION
⍝ ============================================================================

InitializeRelationships

⍞ ← 'Pattern Relationship Module Loaded',⎕UCS 10
