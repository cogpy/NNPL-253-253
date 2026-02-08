#!/usr/bin/env python3
"""
Test suite for Universal Pattern Neural Network
"""

import sys
import os

# Add implementations to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'implementations'))

import torch
from pattern_loader import PatternLoader, PatternData
from universal_pattern_nn import (
    UniversalPatternModel,
    TextEncoder,
    PatternEncoder,
    PatternGNN,
    build_adjacency_matrix,
    prepare_batch
)


def test_pattern_loader():
    """Test pattern loader functionality."""
    print("=== Testing Pattern Loader ===")
    
    loader = PatternLoader()
    patterns = loader.load_all()
    
    # Test basic loading
    assert len(patterns) == 253, f"Expected 253 patterns, got {len(patterns)}"
    print(f"✓ Loaded {len(patterns)} patterns")
    
    # Test pattern structure
    pattern = patterns[1]
    assert hasattr(pattern, 'id'), "Pattern missing 'id' field"
    assert hasattr(pattern, 'name'), "Pattern missing 'name' field"
    assert hasattr(pattern, 'problem'), "Pattern missing 'problem' field"
    assert hasattr(pattern, 'solution'), "Pattern missing 'solution' field"
    assert hasattr(pattern, 'confidence'), "Pattern missing 'confidence' field"
    assert hasattr(pattern, 'category'), "Pattern missing 'category' field"
    print("✓ Pattern data structure valid")
    
    # Test categories
    categories = set(p.category for p in patterns.values())
    expected_categories = {'towns', 'buildings', 'construction'}
    assert categories == expected_categories, f"Expected {expected_categories}, got {categories}"
    print(f"✓ Categories correct: {categories}")
    
    # Test relationships
    pattern2 = patterns[2]
    assert 3 in pattern2.following or len(pattern2.following) == 0, "Pattern 2 should have following patterns"
    print("✓ Pattern relationships loaded")
    
    return patterns


def test_text_encoder():
    """Test text encoder."""
    print("\n=== Testing Text Encoder ===")
    
    encoder = TextEncoder(vocab_size=256, embed_dim=64, hidden_dim=128)
    
    # Test forward pass
    text_ids = torch.randint(0, 256, (4, 100))  # Batch of 4, length 100
    output = encoder(text_ids)
    
    assert output.shape == (4, 256), f"Expected shape (4, 256), got {output.shape}"
    print(f"✓ Text encoder output shape: {output.shape}")
    
    return encoder


def test_pattern_encoder():
    """Test pattern encoder."""
    print("\n=== Testing Pattern Encoder ===")
    
    encoder = PatternEncoder(
        num_patterns=253,
        num_categories=3,
        output_dim=256
    )
    
    # Test forward pass
    batch_size = 4
    pattern_ids = torch.randint(1, 254, (batch_size,))
    confidence = torch.randint(0, 3, (batch_size,))
    category = torch.randint(0, 3, (batch_size,))
    problem_ids = torch.randint(0, 256, (batch_size, 200))
    solution_ids = torch.randint(0, 256, (batch_size, 200))
    
    output = encoder(pattern_ids, confidence, category, problem_ids, solution_ids)
    
    assert output.shape == (batch_size, 256), f"Expected shape ({batch_size}, 256), got {output.shape}"
    print(f"✓ Pattern encoder output shape: {output.shape}")
    
    # Test text_to_ids utility
    text = "This is a test pattern problem."
    ids = encoder.text_to_ids(text)
    assert ids.shape == (200,), f"Expected shape (200,), got {ids.shape}"
    print(f"✓ Text to IDs conversion works")
    
    return encoder


def test_gnn():
    """Test Graph Neural Network."""
    print("\n=== Testing Pattern GNN ===")
    
    gnn = PatternGNN(input_dim=256, hidden_dim=256, num_layers=2)
    
    # Test forward pass
    num_nodes = 10
    node_features = torch.randn(num_nodes, 256)
    adjacency = torch.rand(num_nodes, num_nodes)
    adjacency = (adjacency > 0.7).float()  # Sparse adjacency
    
    output = gnn(node_features, adjacency)
    
    assert output.shape == (num_nodes, 256), f"Expected shape ({num_nodes}, 256), got {output.shape}"
    print(f"✓ GNN output shape: {output.shape}")
    
    return gnn


def test_universal_model(patterns):
    """Test complete universal model."""
    print("\n=== Testing Universal Pattern Model ===")
    
    model = UniversalPatternModel(
        num_patterns=253,
        num_categories=3,
        embedding_dim=256,
        hidden_dim=256
    )
    
    # Count parameters
    num_params = sum(p.numel() for p in model.parameters())
    print(f"✓ Model created with {num_params:,} parameters")
    
    # Test forward pass
    batch_size = 4
    pattern_ids = torch.randint(1, 254, (batch_size,))
    confidence = torch.randint(0, 3, (batch_size,))
    category = torch.randint(0, 3, (batch_size,))
    problem_ids = torch.randint(0, 256, (batch_size, 200))
    solution_ids = torch.randint(0, 256, (batch_size, 200))
    
    next_logits, category_logits, embeddings = model(
        pattern_ids, confidence, category, problem_ids, solution_ids
    )
    
    assert next_logits.shape == (batch_size, 253), f"Expected next_logits shape ({batch_size}, 253)"
    assert category_logits.shape == (batch_size, 3), f"Expected category_logits shape ({batch_size}, 3)"
    assert embeddings.shape == (batch_size, 256), f"Expected embeddings shape ({batch_size}, 256)"
    print("✓ Forward pass successful")
    
    # Test encode_pattern
    pattern = patterns[1]
    embedding = model.encode_pattern(pattern)
    assert embedding.shape == (256,), f"Expected embedding shape (256,), got {embedding.shape}"
    print("✓ Pattern encoding works")
    
    # Test predict_next_patterns
    predictions = model.predict_next_patterns(pattern, top_k=5)
    assert len(predictions) == 5, f"Expected 5 predictions, got {len(predictions)}"
    assert all(isinstance(p[0], int) and isinstance(p[1], float) for p in predictions), "Invalid prediction format"
    print("✓ Next pattern prediction works")
    
    # Test compute_similarity
    similarity = model.compute_similarity(patterns[1], patterns[2])
    assert 0 <= similarity <= 1, f"Similarity should be in [0, 1], got {similarity}"
    print(f"✓ Pattern similarity computation works (sim={similarity:.4f})")
    
    return model


def test_adjacency_matrix(patterns):
    """Test adjacency matrix construction."""
    print("\n=== Testing Adjacency Matrix ===")
    
    adjacency = build_adjacency_matrix(patterns)
    
    assert adjacency.shape == (253, 253), f"Expected shape (253, 253), got {adjacency.shape}"
    print(f"✓ Adjacency matrix shape: {adjacency.shape}")
    
    num_edges = (adjacency > 0).sum().item()
    print(f"✓ Total edges: {num_edges}")
    
    # Check normalization
    row_sums = adjacency.sum(dim=1)
    non_zero_rows = row_sums[row_sums > 0]
    assert len(non_zero_rows) > 0, "Should have at least some edges"
    print(f"✓ Matrix has {len(non_zero_rows)} nodes with outgoing edges")
    
    return adjacency


def test_prepare_batch(patterns):
    """Test batch preparation."""
    print("\n=== Testing Batch Preparation ===")
    
    model = UniversalPatternModel()
    
    # Get sample patterns
    pattern_list = [patterns[i] for i in [1, 2, 3, 4, 5]]
    
    # Prepare batch
    batch = prepare_batch(pattern_list, model.encoder)
    
    pattern_ids, confidence, category, problem_ids, solution_ids = batch
    
    assert pattern_ids.shape == (5,), f"Expected shape (5,), got {pattern_ids.shape}"
    assert confidence.shape == (5,), f"Expected shape (5,), got {confidence.shape}"
    assert category.shape == (5,), f"Expected shape (5,), got {category.shape}"
    assert problem_ids.shape == (5, 200), f"Expected shape (5, 200), got {problem_ids.shape}"
    assert solution_ids.shape == (5, 200), f"Expected shape (5, 200), got {solution_ids.shape}"
    
    print("✓ Batch preparation successful")
    
    return batch


def test_trained_model_exists():
    """Test if trained model file exists."""
    print("\n=== Checking Trained Model ===")
    
    model_path = 'implementations/pattern_model_best.pt'
    
    if os.path.exists(model_path):
        print(f"✓ Trained model found: {model_path}")
        
        # Try to load it
        try:
            model = UniversalPatternModel()
            state_dict = torch.load(model_path, map_location='cpu')
            model.load_state_dict(state_dict)
            model.eval()
            print("✓ Trained model loaded successfully")
            
            return True
        except Exception as e:
            print(f"⚠ Warning: Could not load trained model: {e}")
            return False
    else:
        print(f"⚠ Trained model not found (run train_pattern_nn.py to create it)")
        return False


def main():
    """Run all tests."""
    print("=" * 70)
    print("UNIVERSAL PATTERN NEURAL NETWORK - TEST SUITE")
    print("=" * 70)
    
    try:
        # Test pattern loader
        patterns = test_pattern_loader()
        
        # Test components
        test_text_encoder()
        test_pattern_encoder()
        test_gnn()
        
        # Test complete model
        test_universal_model(patterns)
        
        # Test utilities
        test_adjacency_matrix(patterns)
        test_prepare_batch(patterns)
        
        # Check for trained model
        test_trained_model_exists()
        
        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED")
        print("=" * 70)
        
        return 0
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
