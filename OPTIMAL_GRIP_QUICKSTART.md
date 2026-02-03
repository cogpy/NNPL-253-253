# Optimal Grip Implementation - Quick Start Guide

This guide covers the newly implemented features from OPTIMAL_GRIP_ANALYSIS.md:
- Phase 2: Datalog Query Layer ✅
- Phase 4: ML-based Salience Engine ✅  
- Phase 5: D3.js Interactive Visualization ✅
- Phase 6: REST API Integration ✅

## Quick Start

### 1. Install Dependencies

```bash
pip install pyDatalog numpy fastapi uvicorn
```

### 2. Run the Datalog Query Demo

```bash
python3 demo_datalog_queries.py
```

This demonstrates:
- Category queries (find patterns in Towns, Buildings, Construction)
- Transitive dependency queries
- Pattern relationship discovery
- Context-aware pattern searches

### 3. Run the Salience Engine Demo

```bash
python3 pattern_salience_engine.py
```

This demonstrates:
- Context-aware salience scoring
- Gestalt pattern detection  
- Emergence tracking in pattern sequences
- Multi-scale perception

### 4. Start the REST API

```bash
python3 pattern_api.py
```

The API will be available at `http://localhost:8000`

API Documentation (Swagger): `http://localhost:8000/docs`

### 5. Open the Interactive Visualization

**Important**: Make sure the API is running first (step 4)

Then open in your browser:
```
file:///path/to/skipl-253/pattern_explorer.html
```

Or serve with a local HTTP server:
```bash
python3 -m http.server 8080
# Then visit: http://localhost:8080/pattern_explorer.html
```

## API Endpoints

### Pattern Queries

**List patterns:**
```bash
curl http://localhost:8000/patterns?limit=10
curl http://localhost:8000/patterns?category=Towns
```

**Get specific pattern:**
```bash
curl http://localhost:8000/patterns/apl1
```

### Salience Computation

**Compute salience scores:**
```bash
curl -X POST http://localhost:8000/salience \
  -H "Content-Type: application/json" \
  -d '{
    "focus_patterns": ["apl1", "apl2"],
    "current_category": "Towns",
    "keywords": ["region", "city"],
    "limit": 10
  }'
```

### Gestalt Detection

**Detect emergent pattern groupings:**
```bash
curl -X POST http://localhost:8000/gestalt \
  -H "Content-Type: application/json" \
  -d '{
    "pattern_ids": ["apl1", "apl2", "apl3", "apl4", "apl5"],
    "threshold": 0.5
  }'
```

### Emergence Tracking

**Track emergence in a sequence:**
```bash
curl -X POST http://localhost:8000/emergence \
  -H "Content-Type: application/json" \
  -d '{
    "pattern_sequence": ["apl1", "apl2", "apl3", "apl12", "apl51", "apl95"]
  }'
```

### Categories

**List available categories:**
```bash
curl http://localhost:8000/categories
```

## Interactive Visualization Features

The Pattern Explorer (`pattern_explorer.html`) provides:

### 1. Network Visualization
- Force-directed graph of all 253 patterns
- Color-coded by category (Towns, Buildings, Construction)
- Node size indicates pattern importance (asterisks)
- Interactive drag and zoom

### 2. Pattern Selection
- Click any pattern to view details
- Shows connections (preceding/following patterns)
- Highlights connected patterns in the network
- Displays problem statement

### 3. Category Filtering
- Filter by Towns, Buildings, or Construction
- Dim unrelated patterns
- Focus on specific scales

### 4. Keyword Search
- Search across pattern names, problems, and solutions
- Highlights matching patterns
- Enlarges matched nodes

### 5. Legend
- Color coding reference
- Pattern categories and ranges

## Cognitive Affordances

Each implementation provides specific cognitive affordances for "optimal grip":

### Datalog Query Layer
- **Multi-scale perception**: Query patterns at different hierarchical levels
- **Relationship richness**: Discover transitive dependencies and connections
- **Contextual relevance**: Find patterns relevant to specific contexts

### Salience Engine
- **Context-aware relevance**: Scores patterns by relevance to current focus
- **Gestalt detection**: Identifies emergent pattern groupings
- **Emergence tracking**: Detects when patterns create synergies
- **Network analysis**: Computes pattern centrality and importance

### REST API
- **Programmatic access**: Integrate patterns into other systems
- **Standardized interface**: REST/JSON for universal compatibility
- **Composability**: Combine multiple queries and analyses

### Interactive Visualization
- **Gestalt perception**: See the whole pattern language at once
- **Fluid navigation**: Explore patterns interactively
- **Immediate feedback**: Real-time visual responses
- **Multiple perspectives**: Filter and search for different views

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│         Presentation Layer (pattern_explorer.html)        │
│  • D3.js force-directed graph                            │
│  • Interactive pattern selection                         │
│  • Category filtering and search                         │
└──────────────────────────────────────────────────────────┘
                            ↓ REST API
┌──────────────────────────────────────────────────────────┐
│        Integration Layer (pattern_api.py)                │
│  • FastAPI REST endpoints                                │
│  • Request/response validation                           │
│  • Error handling                                        │
└──────────────────────────────────────────────────────────┘
               ↓                              ↓
┌────────────────────────┐    ┌────────────────────────────┐
│  Query Layer           │    │  Salience Layer            │
│  (demo_datalog_        │    │  (pattern_salience_        │
│   queries.py)          │    │   engine.py)               │
│                        │    │                            │
│  • Pattern discovery   │    │  • Context scoring         │
│  • Relationship        │    │  • Gestalt detection       │
│    inference           │    │  • Emergence tracking      │
│  • Transitive deps     │    │                            │
└────────────────────────┘    └────────────────────────────┘
               ↓                              ↓
┌──────────────────────────────────────────────────────────┐
│     Foundation Layer (pattern_language_generated.json)    │
│  • 253 APL patterns                                      │
│  • Categories, sequences, relationships                  │
│  • Pattern properties and metadata                       │
└──────────────────────────────────────────────────────────┘
```

## Next Steps

### For Developers
1. Explore the API documentation at `http://localhost:8000/docs`
2. Review `pattern_salience_engine.py` for ML algorithms
3. Study `pattern_explorer.html` for D3.js techniques
4. Check `demo_datalog_queries.py` for query examples

### For Users
1. Start with the interactive visualization
2. Try searching for keywords like "region", "city", "community"
3. Click on patterns to explore connections
4. Filter by category to focus on specific scales

### For Researchers
1. Experiment with salience scoring parameters
2. Analyze gestalt detection thresholds
3. Study emergence patterns in sequences
4. Benchmark query performance

## Troubleshooting

**API won't start:**
- Check if port 8000 is available
- Install missing dependencies: `pip install fastapi uvicorn`

**Visualization not loading:**
- Make sure the API is running first
- Check browser console for errors
- Enable CORS if serving from different origin

**Datalog queries fail:**
- Install pyDatalog: `pip install pyDatalog`
- Check pattern JSON files are present

**Salience engine errors:**
- Install numpy: `pip install numpy`
- Verify pattern data is loaded correctly

## References

- [OPTIMAL_GRIP_ANALYSIS.md](OPTIMAL_GRIP_ANALYSIS.md) - Original analysis
- [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) - Detailed examples
- [PARADIGM_LANGUAGE_ANALYSIS.md](PARADIGM_LANGUAGE_ANALYSIS.md) - Paradigm comparison
- [Pattern Language Generated JSON](pattern_language_generated.json) - Data source

## Contributing

To extend this implementation:

1. **Add new salience factors**: Modify `PatternSalienceEngine.compute_salience()`
2. **Create new visualizations**: Add modes to `pattern_explorer.html`
3. **Add API endpoints**: Extend `pattern_api.py`
4. **Improve queries**: Add rules to `demo_datalog_queries.py`

## License

Same as the main repository (see [LICENSE](LICENSE))
