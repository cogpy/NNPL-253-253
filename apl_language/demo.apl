⍝ demo.apl - Pattern Language APL Demo
⍝ Demonstrates the capabilities of the APL Pattern Language implementation
⍝ Author: APL-253 Project
⍝ License: MIT

⍝ ============================================================================
⍝ DEMO: BASIC PATTERN OPERATIONS
⍝ ============================================================================

∇ DemoBasicOperations
  ⍝ Demonstrate basic pattern storage and retrieval
  
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← 'DEMO: Basic Pattern Operations',⎕UCS 10
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Store a sample pattern
  ⍞ ← '1. Storing Pattern #1: Independent Regions',⎕UCS 10
  
  pattern ← 1 'Independent Regions' 'Towns' 2
  pattern ,← ⊂'Wherever possible, work toward independent regions'
  pattern ,← ⊂'People need control over their own government'
  pattern ,← ⊂'Create regions with natural boundaries'
  pattern ,← ⊂'[Diagram of regional boundaries]'
  pattern ,← ⊂(2 7 12 3 4)
  
  result ← StorePattern pattern
  
  ⍞ ← '   Status: ',(⍕result),⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Retrieve the pattern
  ⍞ ← '2. Retrieving Pattern #1:',⎕UCS 10
  retrieved ← GetPatternByID 1
  PrintPattern retrieved
  ⍞ ← ⎕UCS 10
  
  ⍝ Get pattern category
  ⍞ ← '3. Pattern Category:',⎕UCS 10
  category ← GetPatternCategory 1
  ⍞ ← '   Category: ',category,⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Show category counts
  ⍞ ← '4. Category Counts:',⎕UCS 10
  ShowCategoryCounts
  ⍞ ← ⎕UCS 10
∇

⍝ ============================================================================
⍝ DEMO: QUERY OPERATIONS
⍝ ============================================================================

∇ DemoQueryOperations
  ⍝ Demonstrate pattern query capabilities
  
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← 'DEMO: Query Operations',⎕UCS 10
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Query by category
  ⍞ ← '1. Get All Towns Patterns:',⎕UCS 10
  towns ← GetTownPatterns
  ⍞ ← '   Found ',(⍕≢towns),' patterns in Towns category',⎕UCS 10
  ⍞ ← '   IDs: ',(FormatIDList towns[⍳10]),⎕UCS 10 ⍝ Show first 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Get high-rated patterns
  ⍞ ← '2. Get High-Rated Patterns (2 asterisks):',⎕UCS 10
  high_rated ← GetHighRatedPatterns
  ⍞ ← '   Found ',(⍕≢high_rated),' high-rated patterns',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Show query statistics
  ⍞ ← '3. Query Statistics:',⎕UCS 10
  ShowQueryStats
  ⍞ ← ⎕UCS 10
∇

⍝ ============================================================================
⍝ DEMO: DOMAIN TRANSFORMATIONS
⍝ ============================================================================

∇ DemoDomainTransformations
  ⍝ Demonstrate domain transformation of archetypal patterns
  
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← 'DEMO: Domain Transformations',⎕UCS 10
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Store an archetypal pattern
  ⍞ ← '1. Store Archetypal Pattern:',⎕UCS 10
  
  archetypal ← 'Balance between {{domains}} will not be achieved'
  archetypal ,← ' unless each one is small and autonomous enough'
  archetypal ,← ' to be an independent sphere of {{influence-type}}.'
  
  placeholders ← 'domains' 'influence-type'
  
  result ← StoreArchetypalPattern '12610010' archetypal placeholders
  
  ⍞ ← '   Archetypal: ',archetypal,⎕UCS 10
  ⍞ ← '   Placeholders: ',(⍕placeholders),⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Show supported domains
  ⍞ ← '2. Supported Domains:',⎕UCS 10
  ShowDomainInfo
  ⍞ ← ⎕UCS 10
  
  ⍝ Transform to physical domain
  ⍞ ← '3. Transform to Physical Domain:',⎕UCS 10
  physical ← TransformToPhysical archetypal
  ⍞ ← '   ',physical,⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Transform to social domain
  ⍞ ← '4. Transform to Social Domain:',⎕UCS 10
  social ← TransformToSocial archetypal
  ⍞ ← '   ',social,⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Apply all transformations
  ⍞ ← '5. Apply All Domain Transformations:',⎕UCS 10
  all_domains ← ApplyAllDomains archetypal
  PrintDomainTransformations all_domains
  ⍞ ← ⎕UCS 10
∇

⍝ ============================================================================
⍝ DEMO: RELATIONSHIP OPERATIONS
⍝ ============================================================================

∇ DemoRelationshipOperations
  ⍝ Demonstrate pattern relationship navigation
  
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← 'DEMO: Relationship Operations',⎕UCS 10
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Add relationships for pattern #1
  ⍞ ← '1. Add Relationships for Pattern #1:',⎕UCS 10
  
  ⍝ Following patterns
  dummy ← AddFollowingPattern 1 2
  dummy ← AddFollowingPattern 1 7
  dummy ← AddFollowingPattern 1 12
  
  ⍝ Related patterns
  dummy ← AddRelatedPattern 1 3
  dummy ← AddRelatedPattern 1 4
  
  ⍞ ← '   Added following: 2, 7, 12',⎕UCS 10
  ⍞ ← '   Added related: 3, 4',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Show relationships
  ⍞ ← '2. Show All Relationships:',⎕UCS 10
  PrintRelationships 1
  ⍞ ← ⎕UCS 10
  
  ⍝ Count connections
  ⍞ ← '3. Connection Count:',⎕UCS 10
  count ← GetTotalConnections 1
  ⍞ ← '   Pattern #1 has ',(⍕count),' total connections',⎕UCS 10
  ⍞ ← ⎕UCS 10
∇

⍝ ============================================================================
⍝ DEMO: SEQUENCES
⍝ ============================================================================

∇ DemoSequenceOperations
  ⍝ Demonstrate pattern sequence operations
  
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← 'DEMO: Pattern Sequences',⎕UCS 10
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Store a sequence
  ⍞ ← '1. Store Pattern Sequence #1:',⎕UCS 10
  
  sequence ← 1 2 7 12 3
  result ← StoreSequence 1 sequence
  
  ⍞ ← '   Sequence: ',(FormatIDList sequence),⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Retrieve sequence
  ⍞ ← '2. Retrieve Sequence #1:',⎕UCS 10
  retrieved ← GetPatternSequence 1
  ⍞ ← '   Retrieved: ',(FormatIDList retrieved),⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Sequence count
  ⍞ ← '3. Total Sequences:',⎕UCS 10
  count ← GetSequenceCount
  ⍞ ← '   ',(⍕count),' sequences available',⎕UCS 10
  ⍞ ← ⎕UCS 10
∇

⍝ ============================================================================
⍝ DEMO: ADVANCED FEATURES
⍝ ============================================================================

∇ DemoAdvancedFeatures
  ⍝ Demonstrate advanced features
  
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← 'DEMO: Advanced Features',⎕UCS 10
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Pattern similarity
  ⍞ ← '1. Pattern Similarity:',⎕UCS 10
  score ← ComparePatterns 1 2
  ⍞ ← '   Similarity between #1 and #2: ',(⍕score),'%',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Array operations demo
  ⍞ ← '2. APL Array Operations:',⎕UCS 10
  ids ← ⍳10 ⍝ First 10 pattern IDs
  ⍞ ← '   Pattern IDs 1-10: ',(⍕ids),⎕UCS 10
  
  ⍝ Filter to Towns category
  towns_mask ← ids ≤ TOWNS_END
  towns_ids ← towns_mask/ids
  ⍞ ← '   Towns patterns: ',(⍕towns_ids),⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  ⍝ Category distribution
  ⍞ ← '3. Category Distribution:',⎕UCS 10
  total ← GetPatternCount
  towns_pct ← 100 × (CountPatternsInCategory CATEGORY_TOWNS) ÷ total
  buildings_pct ← 100 × (CountPatternsInCategory CATEGORY_BUILDINGS) ÷ total
  construction_pct ← 100 × (CountPatternsInCategory CATEGORY_CONSTRUCTION) ÷ total
  
  ⍞ ← '   Towns: ',(⍕towns_pct),'%',⎕UCS 10
  ⍞ ← '   Buildings: ',(⍕buildings_pct),'%',⎕UCS 10
  ⍞ ← '   Construction: ',(⍕construction_pct),'%',⎕UCS 10
  ⍞ ← ⎕UCS 10
∇

⍝ ============================================================================
⍝ MAIN DEMO RUNNER
⍝ ============================================================================

∇ RunAllDemos
  ⍝ Run all demonstration functions
  
  ⍞ ← ⎕UCS 10
  ⍞ ← '╔═══════════════════════════════════════════════════════════════════════╗',⎕UCS 10
  ⍞ ← '║  Pattern Language APL Implementation - Complete Demo                 ║',⎕UCS 10
  ⍞ ← '║  Christopher Alexander''s A Pattern Language in Array Programming     ║',⎕UCS 10
  ⍞ ← '╚═══════════════════════════════════════════════════════════════════════╝',⎕UCS 10
  ⍞ ← ⎕UCS 10
  
  DemoBasicOperations
  DemoQueryOperations
  DemoDomainTransformations
  DemoRelationshipOperations
  DemoSequenceOperations
  DemoAdvancedFeatures
  
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← 'Demo Complete!',⎕UCS 10
  ⍞ ← '═══════════════════════════════════════════════════════════════════════',⎕UCS 10
  ⍞ ← ⎕UCS 10
∇

⍝ ============================================================================
⍝ QUICK START
⍝ ============================================================================

∇ QuickStart
  ⍝ Quick start guide
  
  ⍞ ← 'Pattern Language APL - Quick Start',⎕UCS 10
  ⍞ ← ⎕UCS 10
  ⍞ ← 'To run the full demo:',⎕UCS 10
  ⍞ ← '  RunAllDemos',⎕UCS 10
  ⍞ ← ⎕UCS 10
  ⍞ ← 'Individual demos:',⎕UCS 10
  ⍞ ← '  DemoBasicOperations',⎕UCS 10
  ⍞ ← '  DemoQueryOperations',⎕UCS 10
  ⍞ ← '  DemoDomainTransformations',⎕UCS 10
  ⍞ ← '  DemoRelationshipOperations',⎕UCS 10
  ⍞ ← '  DemoSequenceOperations',⎕UCS 10
  ⍞ ← '  DemoAdvancedFeatures',⎕UCS 10
  ⍞ ← ⎕UCS 10
∇

⍝ Show quick start on load
QuickStart

⍞ ← 'Pattern Language Demo Module Loaded',⎕UCS 10
