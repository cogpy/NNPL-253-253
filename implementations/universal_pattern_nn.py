#!/usr/bin/env python3
"""
Universal Pattern Language Neural Network
PyTorch implementation for all 253 APL patterns

This module provides a comprehensive neural network architecture for:
- Pattern encoding and representation learning
- Pattern relationship modeling via graph neural networks
- Sequence prediction and pattern recommendations
- Category classification (towns/buildings/construction)
- Pattern similarity computation
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Dict, List, Tuple, Optional
import json
import os

# Import the pattern loader
from pattern_loader import PatternLoader, PatternData


# =============================================================================
# TEXT ENCODER
# =============================================================================

class TextEncoder(nn.Module):
    """
    Bidirectional LSTM text encoder with character-level embeddings.
    Encodes problem and solution text into fixed-size vectors.
    """

    def __init__(self, vocab_size: int = 256, embed_dim: int = 64, hidden_dim: int = 128):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.output_dim = hidden_dim * 2

    def forward(self, text_ids: Tensor) -> Tensor:
        """
        Encode text to fixed-size vector.
        
        Args:
            text_ids: (batch, seq_len) character IDs
            
        Returns:
            (batch, hidden_dim*2) text embeddings
        """
        embedded = self.embed(text_ids)  # (batch, seq_len, embed_dim)
        _, (hidden, _) = self.lstm(embedded)  # hidden: (2, batch, hidden_dim)
        # Concatenate forward and backward hidden states
        return torch.cat([hidden[0], hidden[1]], dim=-1)  # (batch, hidden_dim*2)


# =============================================================================
# PATTERN ENCODER
# =============================================================================

class PatternEncoder(nn.Module):
    """
    Encodes a pattern into a dense vector representation.

    Components:
    - Pattern ID embedding (253 patterns)
    - Confidence level embedding (3 levels)
    - Category embedding (3 categories)
    - Text encoders for problem and solution
    - Feature projection layer
    """

    def __init__(
        self,
        num_patterns: int = 253,
        num_categories: int = 3,
        pattern_dim: int = 128,
        text_hidden: int = 128,
        output_dim: int = 256
    ):
        super().__init__()

        # Embeddings
        self.pattern_embed = nn.Embedding(num_patterns + 1, pattern_dim)  # +1 for padding
        self.confidence_embed = nn.Embedding(3, 32)  # 0, 1, 2
        self.category_embed = nn.Embedding(num_categories, 32)  # towns, buildings, construction

        # Text encoders
        self.problem_encoder = TextEncoder(hidden_dim=text_hidden)
        self.solution_encoder = TextEncoder(hidden_dim=text_hidden)

        # Combine all features
        # pattern_dim + 32 (confidence) + 32 (category) + 2*text_hidden (problem) + 2*text_hidden (solution)
        combined_dim = pattern_dim + 32 + 32 + text_hidden * 4

        self.projection = nn.Sequential(
            nn.Linear(combined_dim, output_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(output_dim, output_dim),
            nn.LayerNorm(output_dim)
        )

        self.output_dim = output_dim

    def text_to_ids(self, text: str, max_len: int = 200) -> Tensor:
        """Convert text string to tensor of character IDs."""
        ids = [ord(c) % 256 for c in text[:max_len]]
        ids = ids + [0] * (max_len - len(ids))  # Pad
        return torch.tensor(ids, dtype=torch.long)

    def forward(
        self,
        pattern_ids: Tensor,
        confidence: Tensor,
        category: Tensor,
        problem_ids: Tensor,
        solution_ids: Tensor
    ) -> Tensor:
        """
        Encode patterns to dense vectors.

        Args:
            pattern_ids: (batch,) pattern numbers (1-253)
            confidence: (batch,) confidence levels (0, 1, 2)
            category: (batch,) categories (0=towns, 1=buildings, 2=construction)
            problem_ids: (batch, seq_len) problem text as char IDs
            solution_ids: (batch, seq_len) solution text as char IDs

        Returns:
            (batch, output_dim) pattern embeddings
        """
        pat_emb = self.pattern_embed(pattern_ids)
        conf_emb = self.confidence_embed(confidence)
        cat_emb = self.category_embed(category)
        prob_emb = self.problem_encoder(problem_ids)
        sol_emb = self.solution_encoder(solution_ids)

        combined = torch.cat([pat_emb, conf_emb, cat_emb, prob_emb, sol_emb], dim=-1)
        return self.projection(combined)


# =============================================================================
# GRAPH NEURAL NETWORK
# =============================================================================

class PatternGNN(nn.Module):
    """
    Graph Neural Network for learning pattern relationships.

    Uses message passing to incorporate information from
    related patterns (preceding and following in sequences).
    """

    def __init__(self, input_dim: int = 256, hidden_dim: int = 256, num_layers: int = 2):
        super().__init__()

        self.layers = nn.ModuleList([
            nn.Sequential(
                nn.Linear(input_dim if i == 0 else hidden_dim, hidden_dim),
                nn.ReLU(),
                nn.Dropout(0.1)
            )
            for i in range(num_layers)
        ])

        self.output = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, node_features: Tensor, adjacency: Tensor) -> Tensor:
        """
        Apply graph convolution.

        Args:
            node_features: (num_nodes, input_dim) node feature matrix
            adjacency: (num_nodes, num_nodes) adjacency matrix

        Returns:
            (num_nodes, hidden_dim) updated node features
        """
        x = node_features

        for layer in self.layers:
            # Message passing: aggregate neighbor features
            # adjacency @ x gives weighted sum of neighbor features
            messages = torch.matmul(adjacency, x)
            # Apply layer transformation
            x = layer(messages)

        return self.output(x)


# =============================================================================
# UNIVERSAL PATTERN LANGUAGE MODEL
# =============================================================================

class UniversalPatternModel(nn.Module):
    """
    Complete neural network model for the Pattern Language.

    Architecture:
    1. Pattern Encoder - Encode patterns with text and metadata
    2. Graph Neural Network - Learn from pattern relationships
    3. Output Heads:
       - Next pattern prediction (sequence continuation)
       - Category classification (towns/buildings/construction)
       - Similarity computation (for pattern search)
    """

    def __init__(
        self,
        num_patterns: int = 253,
        num_categories: int = 3,
        embedding_dim: int = 256,
        hidden_dim: int = 256
    ):
        super().__init__()

        self.num_patterns = num_patterns
        self.num_categories = num_categories

        # Pattern encoder
        self.encoder = PatternEncoder(
            num_patterns=num_patterns,
            num_categories=num_categories,
            output_dim=embedding_dim
        )

        # Graph neural network
        self.gnn = PatternGNN(
            input_dim=embedding_dim,
            hidden_dim=hidden_dim,
            num_layers=2
        )

        # Output heads
        self.next_pattern_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, num_patterns)
        )

        self.category_head = nn.Sequential(
            nn.Linear(hidden_dim, 64),
            nn.ReLU(),
            nn.Linear(64, num_categories)
        )

        self.similarity_head = nn.Linear(hidden_dim, embedding_dim)

    def forward(
        self,
        pattern_ids: Tensor,
        confidence: Tensor,
        category: Tensor,
        problem_ids: Tensor,
        solution_ids: Tensor,
        adjacency: Optional[Tensor] = None
    ) -> Tuple[Tensor, Tensor, Tensor]:
        """
        Forward pass through the model.

        Args:
            pattern_ids: (batch,) pattern IDs
            confidence: (batch,) confidence levels
            category: (batch,) categories
            problem_ids: (batch, seq_len) problem text
            solution_ids: (batch, seq_len) solution text
            adjacency: (batch, batch) optional adjacency matrix

        Returns:
            next_pattern_logits: (batch, num_patterns) logits for next pattern
            category_logits: (batch, num_categories) logits for category
            embeddings: (batch, embedding_dim) pattern embeddings for similarity
        """
        # Encode patterns
        embeddings = self.encoder(
            pattern_ids, confidence, category, problem_ids, solution_ids
        )

        # Apply GNN if adjacency matrix provided
        if adjacency is not None:
            embeddings = self.gnn(embeddings, adjacency)

        # Compute outputs
        next_pattern_logits = self.next_pattern_head(embeddings)
        category_logits = self.category_head(embeddings)
        similarity_embeddings = self.similarity_head(embeddings)

        return next_pattern_logits, category_logits, similarity_embeddings

    def encode_pattern(
        self,
        pattern_data: PatternData,
        device: torch.device = torch.device('cpu')
    ) -> Tensor:
        """
        Encode a single pattern to an embedding vector.

        Args:
            pattern_data: PatternData object
            device: torch device

        Returns:
            (embedding_dim,) pattern embedding
        """
        # Prepare inputs
        pattern_id = torch.tensor([pattern_data.id], dtype=torch.long, device=device)
        confidence = torch.tensor([pattern_data.confidence], dtype=torch.long, device=device)
        
        # Map category to integer
        category_map = {'towns': 0, 'buildings': 1, 'construction': 2}
        category = torch.tensor([category_map[pattern_data.category]], dtype=torch.long, device=device)
        
        # Convert text to IDs
        problem_ids = self.encoder.text_to_ids(pattern_data.problem).unsqueeze(0).to(device)
        solution_ids = self.encoder.text_to_ids(pattern_data.solution).unsqueeze(0).to(device)

        # Encode
        with torch.no_grad():
            embedding = self.encoder(pattern_id, confidence, category, problem_ids, solution_ids)
        
        return embedding.squeeze(0)

    def predict_next_patterns(
        self,
        pattern_data: PatternData,
        top_k: int = 5,
        device: torch.device = torch.device('cpu')
    ) -> List[Tuple[int, float]]:
        """
        Predict the next most likely patterns to follow this one.

        Args:
            pattern_data: Current pattern
            top_k: Number of predictions to return
            device: torch device

        Returns:
            List of (pattern_id, probability) tuples
        """
        # Prepare inputs (same as encode_pattern)
        pattern_id = torch.tensor([pattern_data.id], dtype=torch.long, device=device)
        confidence = torch.tensor([pattern_data.confidence], dtype=torch.long, device=device)
        
        category_map = {'towns': 0, 'buildings': 1, 'construction': 2}
        category = torch.tensor([category_map[pattern_data.category]], dtype=torch.long, device=device)
        
        problem_ids = self.encoder.text_to_ids(pattern_data.problem).unsqueeze(0).to(device)
        solution_ids = self.encoder.text_to_ids(pattern_data.solution).unsqueeze(0).to(device)

        # Forward pass
        with torch.no_grad():
            next_logits, _, _ = self.forward(
                pattern_id, confidence, category, problem_ids, solution_ids
            )
            probs = F.softmax(next_logits, dim=-1).squeeze(0)

        # Get top-k predictions
        top_probs, top_indices = torch.topk(probs, top_k)
        
        return [(idx.item() + 1, prob.item()) for idx, prob in zip(top_indices, top_probs)]

    def compute_similarity(
        self,
        pattern1: PatternData,
        pattern2: PatternData,
        device: torch.device = torch.device('cpu')
    ) -> float:
        """
        Compute cosine similarity between two patterns.

        Args:
            pattern1: First pattern
            pattern2: Second pattern
            device: torch device

        Returns:
            Similarity score (0-1)
        """
        emb1 = self.encode_pattern(pattern1, device)
        emb2 = self.encode_pattern(pattern2, device)
        
        similarity = F.cosine_similarity(emb1.unsqueeze(0), emb2.unsqueeze(0))
        return similarity.item()


# =============================================================================
# DATA UTILITIES
# =============================================================================

def build_adjacency_matrix(patterns: Dict[int, PatternData]) -> Tensor:
    """
    Build adjacency matrix from pattern relationships.

    Args:
        patterns: Dictionary mapping pattern ID to PatternData

    Returns:
        (253, 253) adjacency matrix
    """
    num_patterns = 253
    adj = torch.zeros(num_patterns, num_patterns)

    for pid, pattern in patterns.items():
        if 1 <= pid <= num_patterns:
            # Add edges to following patterns
            for next_pid in pattern.following:
                if 1 <= next_pid <= num_patterns:
                    adj[pid - 1, next_pid - 1] = 1.0

    # Normalize by degree (or use identity for self-loops)
    degree = adj.sum(dim=1, keepdim=True).clamp(min=1)
    adj_normalized = adj / degree

    return adj_normalized


def prepare_batch(
    patterns: List[PatternData],
    encoder: PatternEncoder,
    device: torch.device = torch.device('cpu')
) -> Tuple[Tensor, Tensor, Tensor, Tensor, Tensor]:
    """
    Prepare a batch of patterns for training/inference.

    Args:
        patterns: List of PatternData objects
        encoder: PatternEncoder instance (for text_to_ids)
        device: torch device

    Returns:
        Tuple of tensors (pattern_ids, confidence, category, problem_ids, solution_ids)
    """
    category_map = {'towns': 0, 'buildings': 1, 'construction': 2}

    pattern_ids = torch.tensor([p.id for p in patterns], dtype=torch.long, device=device)
    confidence = torch.tensor([p.confidence for p in patterns], dtype=torch.long, device=device)
    category = torch.tensor([category_map[p.category] for p in patterns], dtype=torch.long, device=device)

    problem_ids = torch.stack([encoder.text_to_ids(p.problem) for p in patterns]).to(device)
    solution_ids = torch.stack([encoder.text_to_ids(p.solution) for p in patterns]).to(device)

    return pattern_ids, confidence, category, problem_ids, solution_ids


# =============================================================================
# DEMO
# =============================================================================

def main():
    """Demo: Create model, load patterns, and run inference."""
    print("=" * 70)
    print("UNIVERSAL PATTERN LANGUAGE NEURAL NETWORK - DEMO")
    print("=" * 70)

    # Load all patterns
    print("\n=== Loading Patterns ===")
    loader = PatternLoader()
    patterns = loader.load_all()
    print(f"✓ Loaded {len(patterns)} patterns")

    # Create model
    print("\n=== Creating Model ===")
    model = UniversalPatternModel(
        num_patterns=253,
        num_categories=3,
        embedding_dim=256,
        hidden_dim=256
    )
    print(f"✓ Model created with {sum(p.numel() for p in model.parameters()):,} parameters")

    # Build adjacency matrix
    print("\n=== Building Adjacency Matrix ===")
    adjacency = build_adjacency_matrix(patterns)
    print(f"✓ Adjacency matrix shape: {adjacency.shape}")
    print(f"  Total edges: {adjacency.sum().item():.0f}")

    # Demo 1: Encode patterns
    print("\n=== Demo 1: Encoding Patterns ===")
    model.eval()
    for pid in [1, 50, 100, 150, 200, 253]:
        if pid in patterns:
            pattern = patterns[pid]
            embedding = model.encode_pattern(pattern)
            print(f"Pattern {pid:3d} ({pattern.name[:30]:30s}): embedding shape {embedding.shape}")

    # Demo 2: Predict next patterns
    print("\n=== Demo 2: Predicting Next Patterns ===")
    for pid in [1, 2, 3]:
        if pid in patterns:
            pattern = patterns[pid]
            predictions = model.predict_next_patterns(pattern, top_k=5)
            print(f"\nPattern {pid}: {pattern.name}")
            print(f"  Actual following: {pattern.following}")
            print(f"  Predicted (untrained):")
            for next_id, prob in predictions:
                next_pattern = patterns.get(next_id)
                next_name = next_pattern.name if next_pattern else "Unknown"
                print(f"    Pattern {next_id:3d} ({next_name[:30]:30s}): {prob:.4f}")

    # Demo 3: Compute similarities
    print("\n=== Demo 3: Computing Pattern Similarities ===")
    if 1 in patterns and 2 in patterns and 50 in patterns:
        sim_1_2 = model.compute_similarity(patterns[1], patterns[2])
        sim_1_50 = model.compute_similarity(patterns[1], patterns[50])
        print(f"Similarity between patterns 1 and 2: {sim_1_2:.4f}")
        print(f"Similarity between patterns 1 and 50: {sim_1_50:.4f}")

    print("\n=== Model Summary ===")
    print(f"Total parameters: {sum(p.numel() for p in model.parameters()):,}")
    print(f"Trainable parameters: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")
    print(f"Model size: {sum(p.numel() * p.element_size() for p in model.parameters()) / 1024 / 1024:.2f} MB")

    print("\n✓ Demo complete!")
    print("\nNote: Predictions are from an untrained model.")
    print("For meaningful results, train the model with pattern sequence data.")


if __name__ == '__main__':
    main()
