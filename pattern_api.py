#!/usr/bin/env python3
"""
Pattern Language REST API

Provides REST endpoints for:
- Pattern queries (Datalog)
- Salience scoring (ML)
- Gestalt detection
- Emergence tracking

Implements Phase 6 of OPTIMAL_GRIP_ANALYSIS.md
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Set, Dict, Any
import json
from pathlib import Path

# Import our pattern language modules
from pattern_salience_engine import PatternSalienceEngine, PatternContext, SalienceScore

app = FastAPI(
    title="Pattern Language API",
    description="Cognitive optimal grip on pattern language gestalt salience landscape",
    version="0.1.0"
)

# Global engine instance
salience_engine = None


@app.on_event("startup")
async def startup_event():
    """Initialize engines on startup"""
    global salience_engine
    print("Initializing Pattern Salience Engine...")
    salience_engine = PatternSalienceEngine('pattern_language_generated.json')
    print("API ready!")


# Pydantic models for requests/responses
class PatternResponse(BaseModel):
    """Pattern data response"""
    id: str
    number: int
    name: str
    asterisks: int
    problem: str
    solution: str
    category: Optional[str] = None
    preceding_patterns: List[int]
    following_patterns: List[int]


class SalienceRequest(BaseModel):
    """Request for salience scoring"""
    focus_patterns: Set[str] = Field(default_factory=set)
    current_category: Optional[str] = None
    keywords: Set[str] = Field(default_factory=set)
    domain: Optional[str] = None
    limit: int = Field(default=20, ge=1, le=100)


class SalienceResponse(BaseModel):
    """Salience score response"""
    pattern_id: str
    score: float
    reasons: List[str]
    pattern_name: str


class GestaltRequest(BaseModel):
    """Request for gestalt detection"""
    pattern_ids: List[str]
    threshold: float = Field(default=0.6, ge=0.0, le=1.0)


class EmergenceRequest(BaseModel):
    """Request for emergence tracking"""
    pattern_sequence: List[str]


# API Endpoints

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "Pattern Language API",
        "version": "0.1.0",
        "endpoints": {
            "patterns": "/patterns",
            "pattern_by_id": "/patterns/{pattern_id}",
            "salience": "/salience",
            "gestalt": "/gestalt",
            "emergence": "/emergence",
            "categories": "/categories"
        }
    }


@app.get("/patterns", response_model=List[PatternResponse])
async def list_patterns(
    category: Optional[str] = Query(None, description="Filter by category"),
    limit: int = Query(50, ge=1, le=253)
):
    """List patterns, optionally filtered by category"""
    if not salience_engine:
        raise HTTPException(status_code=503, detail="Engine not initialized")
    
    patterns = []
    count = 0
    
    for pattern_id, pattern in salience_engine.patterns.items():
        if category:
            pattern_category = salience_engine.category_map.get(pattern_id)
            if pattern_category != category:
                continue
        
        patterns.append(PatternResponse(
            id=pattern['id'],
            number=pattern['number'],
            name=pattern['name'],
            asterisks=pattern.get('asterisks', 0),
            problem=pattern.get('problem', ''),
            solution=pattern.get('solution', ''),
            category=salience_engine.category_map.get(pattern_id),
            preceding_patterns=pattern.get('preceding_patterns', []),
            following_patterns=pattern.get('following_patterns', [])
        ))
        
        count += 1
        if count >= limit:
            break
    
    return patterns


@app.get("/patterns/{pattern_id}", response_model=PatternResponse)
async def get_pattern(pattern_id: str):
    """Get a specific pattern by ID"""
    if not salience_engine:
        raise HTTPException(status_code=503, detail="Engine not initialized")
    
    if pattern_id not in salience_engine.patterns:
        raise HTTPException(status_code=404, detail=f"Pattern {pattern_id} not found")
    
    pattern = salience_engine.patterns[pattern_id]
    
    return PatternResponse(
        id=pattern['id'],
        number=pattern['number'],
        name=pattern['name'],
        asterisks=pattern.get('asterisks', 0),
        problem=pattern.get('problem', ''),
        solution=pattern.get('solution', ''),
        category=salience_engine.category_map.get(pattern_id),
        preceding_patterns=pattern.get('preceding_patterns', []),
        following_patterns=pattern.get('following_patterns', [])
    )


@app.post("/salience", response_model=List[SalienceResponse])
async def compute_salience(request: SalienceRequest):
    """
    Compute salience scores for patterns in given context
    
    Returns patterns ranked by relevance to the context.
    """
    if not salience_engine:
        raise HTTPException(status_code=503, detail="Engine not initialized")
    
    # Create context
    context = PatternContext(
        focus_patterns=request.focus_patterns,
        current_category=request.current_category,
        keywords=request.keywords,
        domain=request.domain
    )
    
    # Rank patterns
    scores = salience_engine.rank_patterns_by_salience(context, limit=request.limit)
    
    # Convert to response format
    responses = []
    for score in scores:
        pattern = salience_engine.patterns.get(score.pattern_id)
        if pattern:
            responses.append(SalienceResponse(
                pattern_id=score.pattern_id,
                score=score.score,
                reasons=score.reasons,
                pattern_name=pattern['name']
            ))
    
    return responses


@app.post("/gestalt")
async def detect_gestalt(request: GestaltRequest):
    """
    Detect gestalt patterns (emergent groupings) in a set of patterns
    
    Returns clusters of patterns that form coherent wholes.
    """
    if not salience_engine:
        raise HTTPException(status_code=503, detail="Engine not initialized")
    
    # Validate pattern IDs
    for pattern_id in request.pattern_ids:
        if pattern_id not in salience_engine.patterns:
            raise HTTPException(status_code=400, detail=f"Unknown pattern: {pattern_id}")
    
    # Detect gestalts
    gestalts = salience_engine.detect_gestalt_patterns(
        request.pattern_ids,
        threshold=request.threshold
    )
    
    # Enrich with pattern names
    enriched_gestalts = []
    for gestalt in gestalts:
        patterns_info = []
        for pattern_id in gestalt['patterns']:
            pattern = salience_engine.patterns[pattern_id]
            patterns_info.append({
                'id': pattern_id,
                'name': pattern['name']
            })
        
        enriched_gestalts.append({
            'patterns': patterns_info,
            'size': gestalt['size'],
            'coherence': gestalt['coherence']
        })
    
    return {
        'clusters_found': len(enriched_gestalts),
        'gestalts': enriched_gestalts
    }


@app.post("/emergence")
async def track_emergence(request: EmergenceRequest):
    """
    Track emergence in a pattern sequence
    
    Detects when patterns combine to create emergent properties.
    """
    if not salience_engine:
        raise HTTPException(status_code=503, detail="Engine not initialized")
    
    # Validate pattern IDs
    for pattern_id in request.pattern_sequence:
        if pattern_id not in salience_engine.patterns:
            raise HTTPException(status_code=400, detail=f"Unknown pattern: {pattern_id}")
    
    # Track emergence
    emergence = salience_engine.track_emergence(request.pattern_sequence)
    
    # Enrich with pattern names
    sequence_info = []
    for pattern_id in request.pattern_sequence:
        pattern = salience_engine.patterns[pattern_id]
        sequence_info.append({
            'id': pattern_id,
            'name': pattern['name']
        })
    
    return {
        'sequence': sequence_info,
        'emergence_detected': emergence['emergence_detected'],
        'emergence_score': emergence['emergence_score'],
        'sequence_coherence': emergence['sequence_coherence'],
        'categories_involved': emergence['categories_involved'],
        'interpretation': emergence['interpretation']
    }


@app.get("/categories")
async def list_categories():
    """List available pattern categories"""
    if not salience_engine:
        raise HTTPException(status_code=503, detail="Engine not initialized")
    
    # Count patterns per category
    category_counts = {}
    for pattern_id, category in salience_engine.category_map.items():
        category_counts[category] = category_counts.get(category, 0) + 1
    
    return {
        'categories': [
            {'name': cat, 'pattern_count': count}
            for cat, count in sorted(category_counts.items())
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "engine_loaded": salience_engine is not None,
        "pattern_count": len(salience_engine.patterns) if salience_engine else 0
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
