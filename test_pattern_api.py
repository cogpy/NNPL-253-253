#!/usr/bin/env python3
"""
Test Pattern Language REST API
"""

import requests
import json
import time
import subprocess
import os
import signal

def test_api():
    """Test the Pattern Language API"""
    base_url = "http://localhost:8000"
    
    print("="*70)
    print("Testing Pattern Language REST API")
    print("="*70)
    print()
    
    # Test 1: Health check
    print("1. Health check")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        print()
    except requests.exceptions.RequestException as e:
        print(f"   Error: {e}")
        return False
    
    # Test 2: List patterns
    print("2. List patterns (limit 5)")
    try:
        response = requests.get(f"{base_url}/patterns?limit=5", timeout=5)
        patterns = response.json()
        print(f"   Retrieved {len(patterns)} patterns")
        if patterns:
            print(f"   First pattern: {patterns[0]['id']} - {patterns[0]['name']}")
        print()
    except requests.exceptions.RequestException as e:
        print(f"   Error: {e}")
        return False
    
    # Test 3: Get specific pattern
    print("3. Get pattern apl1")
    try:
        response = requests.get(f"{base_url}/patterns/apl1", timeout=5)
        pattern = response.json()
        print(f"   Pattern: {pattern['name']}")
        print(f"   Category: {pattern['category']}")
        print()
    except requests.exceptions.RequestException as e:
        print(f"   Error: {e}")
        return False
    
    # Test 4: Compute salience
    print("4. Compute salience scores")
    try:
        payload = {
            "focus_patterns": ["apl1", "apl2"],
            "current_category": "Towns",
            "keywords": ["region", "city"],
            "limit": 5
        }
        response = requests.post(f"{base_url}/salience", json=payload, timeout=5)
        scores = response.json()
        print(f"   Top {len(scores)} salient patterns:")
        for score in scores[:3]:
            print(f"   - {score['pattern_id']}: {score['pattern_name']}")
            print(f"     Score: {score['score']:.2f}")
        print()
    except requests.exceptions.RequestException as e:
        print(f"   Error: {e}")
        return False
    
    # Test 5: Detect gestalt
    print("5. Detect gestalt patterns")
    try:
        payload = {
            "pattern_ids": ["apl1", "apl2", "apl3", "apl4", "apl5"],
            "threshold": 0.5
        }
        response = requests.post(f"{base_url}/gestalt", json=payload, timeout=5)
        result = response.json()
        print(f"   Found {result['clusters_found']} gestalt clusters")
        if result['gestalts']:
            print(f"   Largest cluster: {len(result['gestalts'][0]['patterns'])} patterns")
        print()
    except requests.exceptions.RequestException as e:
        print(f"   Error: {e}")
        return False
    
    # Test 6: Track emergence
    print("6. Track emergence in sequence")
    try:
        payload = {
            "pattern_sequence": ["apl1", "apl2", "apl3", "apl12", "apl51"]
        }
        response = requests.post(f"{base_url}/emergence", json=payload, timeout=5)
        result = response.json()
        print(f"   Emergence detected: {result['emergence_detected']}")
        print(f"   Emergence score: {result['emergence_score']:.2f}")
        print(f"   Interpretation: {result['interpretation']}")
        print()
    except requests.exceptions.RequestException as e:
        print(f"   Error: {e}")
        return False
    
    # Test 7: List categories
    print("7. List categories")
    try:
        response = requests.get(f"{base_url}/categories", timeout=5)
        result = response.json()
        print(f"   Categories:")
        for cat in result['categories']:
            print(f"   - {cat['name']}: {cat['pattern_count']} patterns")
        print()
    except requests.exceptions.RequestException as e:
        print(f"   Error: {e}")
        return False
    
    print("="*70)
    print("All tests passed!")
    print("="*70)
    return True


if __name__ == '__main__':
    import sys
    
    # Check if server is running
    try:
        response = requests.get("http://localhost:8000/health", timeout=2)
        print("API server is already running")
        print()
        test_api()
    except:
        print("Starting API server...")
        print("Run: python3 pattern_api.py")
        print("Then run this test script again")
        print()
        print("Or test manually with curl:")
        print("  curl http://localhost:8000/health")
        print("  curl http://localhost:8000/patterns?limit=5")
        sys.exit(1)
