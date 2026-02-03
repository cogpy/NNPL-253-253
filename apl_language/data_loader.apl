⍝ data_loader.apl - Pattern Data Initialization
⍝ Generated from JSON pattern files
⍝ Author: APL-253 Project
⍝ License: MIT

⍝ ============================================================================
⍝ LOAD PATTERN DATA
⍝ ============================================================================

∇ LoadAllPatternData
  ⍝ Load all pattern data from generated code
  
  ⍞ ← 'Loading pattern data...',⎕UCS 10
  
  ⍝ Load main patterns
  LoadMainPatterns
  
  ⍝ Load sequences
  LoadSequences
  
  ⍝ Load archetypal patterns
  LoadArchetypalPatterns
  
  ⍝ Load relationships
  LoadRelationships
  
  ⍞ ← 'Pattern data loaded successfully!',⎕UCS 10
∇

∇ LoadMainPatterns
  ⍝ Load main pattern data
  ⍝ Note: This loads a subset of patterns for demonstration
  
  ⍞ ← '  Loading main patterns...',⎕UCS 10
  
  ⍝ Pattern 1: INDEPENDENT REGIONS
  pattern ← 1 'INDEPENDENT REGIONS' 'Towns' 2
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂'Wherever possible, work toward the evolution of independent regions in the world; each with a popula'
  pattern ,← ⊂''
  pattern ,← ⊂(2 8)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 2: THE DISTRIBUTION OF TOWNS
  pattern ← 2 'THE DISTRIBUTION OF TOWNS' 'Towns' 2
  pattern ,← ⊂'. . . consider now the character of settlements within the region: what balance of villages, towns, '
  pattern ,← ⊂''
  pattern ,← ⊂'Encourage a birth and death process for towns within the region, which gradually has these effects:1'
  pattern ,← ⊂''
  pattern ,← ⊂(1 3 4 6)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 3: CITY COUNTRY FINGERS
  pattern ← 3 'CITY COUNTRY FINGERS' 'Towns' 2
  pattern ,← ⊂'. . . the distribution of towns required to make a balanced region - DISTRIBUTION OF TOWNS (2) - can'
  pattern ,← ⊂''
  pattern ,← ⊂'Keep interlocking fingers of farmland and urban land, even at the center of the metropolis. The urba'
  pattern ,← ⊂''
  pattern ,← ⊂(2 4 6 7 8)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 4: AGRICULTURAL VALLEYS
  pattern ← 4 'AGRICULTURAL VALLEYS' 'Towns' 2
  pattern ,← ⊂'. . . this pattern helps maintain the INDEPENDENT REGIONS (1) by making regions more self-sufficient'
  pattern ,← ⊂''
  pattern ,← ⊂'Preserve all agricultural valleys as farmland and protect this land from any development which would'
  pattern ,← ⊂''
  pattern ,← ⊂(1 3 7)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 5: LACE OF COUNTRY STREETS
  pattern ← 5 'LACE OF COUNTRY STREETS' 'Towns' 2
  pattern ,← ⊂'. . . according to the pattern CITY COUNTRY FINGERS (3), there is a rather sharp division between ci'
  pattern ,← ⊂''
  pattern ,← ⊂'In the zone where city and country meet, place country roads at least a mile apart, so that they enc'
  pattern ,← ⊂''
  pattern ,← ⊂(3 7 14 37)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 6: 6 COUNTRY TOWNS
  pattern ← 6 '6 COUNTRY TOWNS' 'Towns' 2
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂(2 7 12 26)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 7: 7 THE COUNTRYSIDE
  pattern ← 7 '7 THE COUNTRYSIDE' 'Towns' 2
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂(2 3 4 5 6)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 8: 8 MOSAIC OF SUBCULTURES
  pattern ← 8 '8 MOSAIC OF SUBCULTURES' 'Towns' 2
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂(3 4 12 13 37)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 9: 9 SCATTERED WORK
  pattern ← 9 '9 SCATTERED WORK' 'Towns' 2
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂(3 4 5 8 42)
  dummy ← StorePattern pattern
  
  ⍝ Pattern 10: 10 MAGIC OF THE CITY
  pattern ← 10 '10 MAGIC OF THE CITY' 'Towns' 2
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂''
  pattern ,← ⊂(3 8 11 16 21)
  dummy ← StorePattern pattern
  
  ⍞ ← '    Loaded sample patterns',⎕UCS 10
∇

∇ LoadSequences
  ⍝ Load pattern sequences
  
  ⍞ ← '  Loading sequences...',⎕UCS 10
  
  ⍝ Sequence 1
  dummy ← StoreSequence 1 (1)
  ⍝ Sequence 2
  dummy ← StoreSequence 2 (2 3 4 5 6 7)
  ⍝ Sequence 3
  dummy ← StoreSequence 3 (8 9 10 11)
  ⍝ Sequence 4
  dummy ← StoreSequence 4 (12 13 14 15)
  ⍝ Sequence 5
  dummy ← StoreSequence 5 (16 17 18 19 20)
  ⍝ Sequence 6
  dummy ← StoreSequence 6 (21 22 23 24 25 26 27)
  ⍝ Sequence 7
  dummy ← StoreSequence 7 (28 29 30 31 32 33 34)
  ⍝ Sequence 8
  dummy ← StoreSequence 8 (35 36 37 38 39 40)
  ⍝ Sequence 9
  dummy ← StoreSequence 9 (41 42 43 44 45 46 47 48 49 50)
  ⍝ Sequence 10
  dummy ← StoreSequence 10 (51 52 53 54 55 56 57)
  
  ⍞ ← '    Loaded sequences',⎕UCS 10
∇

∇ LoadArchetypalPatterns
  ⍝ Load archetypal patterns
  
  ⍞ ← '  Loading archetypal patterns...',⎕UCS 10
  
  ⍝ Archetypal pattern 12610010
  archetypal ← 'Balance between {{domains}} will not be achieved unless each one is small and autonomous enough to be an independent sphere of {{influence-type}}.'
  placeholders ← 'domains' 'influence-type'
  dummy ← StoreArchetypalPattern '12610010' archetypal placeholders
  
  ⍝ Archetypal pattern 12610020
  archetypal ← 'If a domain is characterized by small clusters of {{organization-type}} to too great an extent, more comprehensive forms of {{organization-type}} cann'
  placeholders ← 'organization-type' 'organization-type' 'organization-type'
  dummy ← StoreArchetypalPattern '12610020' archetypal placeholders
  
  ⍝ Archetypal pattern 12610030
  archetypal ← 'A continuous pattern of {{organization-type}} and definition denies the existence and emergence of the underdefined and severely diminishes the value '
  placeholders ← 'organization-type' 'patterns' 'organization-type'
  dummy ← StoreArchetypalPattern '12610030' archetypal placeholders
  
  ⍝ Archetypal pattern 12610040
  archetypal ← 'Those {{areas}} in which {{resources}} can best be regenerated are also those most favourable for the construction of {{frameworks}}. The availability'
  placeholders ← 'areas' 'resources' 'frameworks'
  dummy ← StoreArchetypalPattern '12610040' archetypal placeholders
  
  ⍝ Archetypal pattern 12610050
  archetypal ← 'There is advantage in relating to centrally organized {{frameworks}} as well as to those which are minimally organized. In order to reconcile these co'
  placeholders ← 'frameworks' 'positions' 'areas'
  dummy ← StoreArchetypalPattern '12610050' archetypal placeholders
  
  ⍞ ← '    Loaded archetypal patterns',⎕UCS 10
∇

∇ LoadRelationships
  ⍝ Load pattern relationships
  
  ⍞ ← '  Loading relationships...',⎕UCS 10
  
  dummy ← AddFollowingPattern 1 2
  dummy ← AddFollowingPattern 1 8
  dummy ← AddFollowingPattern 2 3
  dummy ← AddFollowingPattern 2 4
  dummy ← AddFollowingPattern 2 6
  dummy ← AddFollowingPattern 3 4
  dummy ← AddFollowingPattern 3 6
  dummy ← AddFollowingPattern 3 7
  dummy ← AddFollowingPattern 4 7
  dummy ← AddFollowingPattern 5 7
  dummy ← AddFollowingPattern 5 14
  dummy ← AddFollowingPattern 5 37
  dummy ← AddFollowingPattern 6 7
  dummy ← AddFollowingPattern 6 12
  dummy ← AddFollowingPattern 6 26
  dummy ← AddFollowingPattern 7 37
  dummy ← AddFollowingPattern 7 51
  dummy ← AddFollowingPattern 8 12
  dummy ← AddFollowingPattern 8 13
  dummy ← AddFollowingPattern 8 37
  dummy ← AddFollowingPattern 9 42
  dummy ← AddFollowingPattern 9 80
  dummy ← AddFollowingPattern 9 157
  dummy ← AddFollowingPattern 10 11
  dummy ← AddFollowingPattern 10 16
  dummy ← AddFollowingPattern 10 21
  
  ⍞ ← '    Loaded relationships',⎕UCS 10
∇

⍞ ← 'Data Loader Module Loaded',⎕UCS 10