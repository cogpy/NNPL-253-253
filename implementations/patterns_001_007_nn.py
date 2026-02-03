#!/usr/bin/env python3
"""
A Pattern Language - Patterns 1-7: Regional Policies
PyTorch Neural Network Implementation

This module implements a neural network for pattern representation,
similarity computation, and sequence prediction for APL patterns 1-7.

Sequence 2: Regional Policies
Emergent Phenomenon: Balanced distribution of settlements that
preserves countryside while supporting urban vitality
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import json


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class PatternData:
    """Data structure for a single pattern."""
    id: int
    name: str
    problem: str
    solution: str
    confidence: int  # 0=uncertain, 1=progress, 2=invariant
    preceding: List[int]
    following: List[int]


# Pattern definitions for patterns 1-7
PATTERNS_1_7: Dict[int, PatternData] = {
    1: PatternData(
        id=1,
        name="INDEPENDENT REGIONS",
        problem="Metropolitan regions will not come to balance until each one is small and autonomous enough to be an independent sphere of culture.",
        solution="Work toward independent regions with 2-10 million people each, with own economy and self-government.",
        confidence=2,
        preceding=[],
        following=[2, 8]
    ),
    2: PatternData(
        id=2,
        name="DISTRIBUTION OF TOWNS",
        problem="Population weighted to cities ruins earth; too rural blocks civilization.",
        solution="Logarithmic distribution: 1 town of 1M, 10 of 100K, 100 of 10K, 1000 of 1K, evenly spread.",
        confidence=1,
        preceding=[1],
        following=[3, 4, 6]
    ),
    3: PatternData(
        id=3,
        name="CITY COUNTRY FINGERS",
        problem="Continuous sprawling urbanization destroys life, but city size is valuable.",
        solution="Interlocking fingers: urban ≤1 mile wide, farmland ≥1 mile wide.",
        confidence=2,
        preceding=[2],
        following=[4, 5, 8]
    ),
    4: PatternData(
        id=4,
        name="AGRICULTURAL VALLEYS",
        problem="Best farmland is best building land, but once destroyed, gone for centuries.",
        solution="Preserve all valleys as farmland, parks, wilds. Build on hillsides.",
        confidence=2,
        preceding=[1, 3],
        following=[7]
    ),
    5: PatternData(
        id=5,
        name="LACE OF COUNTRY STREETS",
        problem="The suburb is an obsolete and contradictory form of human settlement.",
        solution="Country roads 1 mile apart, enclosing 1 sq mile farmland, homesteads one lot deep.",
        confidence=1,
        preceding=[3],
        following=[7, 14, 37]
    ),
    6: PatternData(
        id=6,
        name="COUNTRY TOWNS",
        problem="Small country towns are dying as jobs move to cities.",
        solution="Self-sufficient towns of ~7000 people, 10-15 miles from cities, with local industry.",
        confidence=2,
        preceding=[2],
        following=[7, 12, 26]
    ),
    7: PatternData(
        id=7,
        name="THE COUNTRYSIDE",
        problem="Countryside is inaccessible to city dwellers; private ownership blocks access.",
        solution="Make countryside public with footpaths, commons, access rights. Ownership as stewardship.",
        confidence=1,
        preceding=[2, 3, 4, 5, 6],
        following=[37, 51]
    ),
}

# Adjacency matrix for pattern relationships (patterns 1-7)
ADJACENCY_MATRIX = torch.tensor([
    # 1  2  3  4  5  6  7
    [0, 1, 0, 0, 0, 0, 0],  # 1 -> 2
    [0, 0, 1, 1, 0, 1, 0],  # 2 -> 3, 4, 6
    [0, 0, 0, 1, 1, 0, 0],  # 3 -> 4, 5
    [0, 0, 0, 0, 0, 0, 1],  # 4 -> 7
    [0, 0, 0, 0, 0, 0, 1],  # 5 -> 7
    [0, 0, 0, 0, 0, 0, 1],  # 6 -> 7
    [0, 0, 0, 0, 0, 0, 0],  # 7 -> (outside range)
], dtype=torch.float32)


# =============================================================================
# TEXT ENCODER
# =============================================================================

class TextEncoder(nn.Module):
    """Simple text encoder using character-level embeddings and LSTM."""

    def __init__(self, vocab_size: int = 256, embed_dim: int = 64, hidden_dim: int = 128):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.output_dim = hidden_dim * 2

    def forward(self, text_ids: Tensor) -> Tensor:
        """Encode text to fixed-size vector."""
        # text_ids: (batch, seq_len)
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
    - Pattern ID embedding
    - Confidence level embedding
    - Text encoders for problem and solution
    - Graph convolution for relationship context
    """

    def __init__(
        self,
        num_patterns: int = 253,
        pattern_dim: int = 128,
        text_hidden: int = 128,
        output_dim: int = 256
    ):
        super().__init__()

        # Embeddings
        self.pattern_embed = nn.Embedding(num_patterns + 1, pattern_dim)  # +1 for padding
        self.confidence_embed = nn.Embedding(3, 32)  # 0, 1, 2 asterisks

        # Text encoders
        self.problem_encoder = TextEncoder(hidden_dim=text_hidden)
        self.solution_encoder = TextEncoder(hidden_dim=text_hidden)

        # Combine all features
        # pattern_dim + 32 (confidence) + 2*text_hidden (problem) + 2*text_hidden (solution)
        combined_dim = pattern_dim + 32 + text_hidden * 4

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
        problem_ids: Tensor,
        solution_ids: Tensor
    ) -> Tensor:
        """
        Encode patterns to dense vectors.

        Args:
            pattern_ids: (batch,) pattern numbers
            confidence: (batch,) confidence levels (0, 1, 2)
            problem_ids: (batch, seq_len) problem text as char IDs
            solution_ids: (batch, seq_len) solution text as char IDs

        Returns:
            (batch, output_dim) pattern embeddings
        """
        pat_emb = self.pattern_embed(pattern_ids)
        conf_emb = self.confidence_embed(confidence)
        prob_emb = self.problem_encoder(problem_ids)
        sol_emb = self.solution_encoder(solution_ids)

        combined = torch.cat([pat_emb, conf_emb, prob_emb, sol_emb], dim=-1)
        return self.projection(combined)


# =============================================================================
# GRAPH NEURAL NETWORK FOR PATTERN RELATIONSHIPS
# =============================================================================

class PatternGNN(nn.Module):
    """
    Graph Neural Network for learning pattern relationships.

    Uses message passing to incorporate information from
    preceding and following patterns.
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
            node_features: (num_nodes, input_dim) node embeddings
            adjacency: (num_nodes, num_nodes) adjacency matrix

        Returns:
            (num_nodes, hidden_dim) updated embeddings
        """
        # Normalize adjacency (add self-loops)
        adj = adjacency + torch.eye(adjacency.size(0), device=adjacency.device)
        degree = adj.sum(dim=1, keepdim=True).clamp(min=1)
        adj_norm = adj / degree

        h = node_features
        for layer in self.layers:
            # Message passing: aggregate neighbor features
            h = torch.matmul(adj_norm, h)
            h = layer(h)

        return self.output(h)


# =============================================================================
# PATTERN LANGUAGE MODEL
# =============================================================================

class PatternLanguageModel(nn.Module):
    """
    Complete neural network for A Pattern Language.

    Capabilities:
    1. Encode patterns to dense vectors
    2. Predict next patterns in sequence
    3. Compute pattern similarity
    4. Classify patterns by category
    """

    def __init__(
        self,
        num_patterns: int = 253,
        num_categories: int = 3,
        embed_dim: int = 256
    ):
        super().__init__()

        self.num_patterns = num_patterns
        self.embed_dim = embed_dim

        # Pattern encoder
        self.encoder = PatternEncoder(
            num_patterns=num_patterns,
            output_dim=embed_dim
        )

        # Graph neural network
        self.gnn = PatternGNN(input_dim=embed_dim, hidden_dim=embed_dim)

        # Output heads
        self.next_pattern_head = nn.Linear(embed_dim, num_patterns)
        self.category_head = nn.Linear(embed_dim, num_categories)
        self.similarity_head = nn.Linear(embed_dim, embed_dim)

    def encode_pattern(self, pattern: PatternData) -> Tensor:
        """Encode a single pattern to a vector."""
        pattern_id = torch.tensor([pattern.id])
        confidence = torch.tensor([pattern.confidence])
        problem_ids = self.encoder.text_to_ids(pattern.problem).unsqueeze(0)
        solution_ids = self.encoder.text_to_ids(pattern.solution).unsqueeze(0)

        return self.encoder(pattern_id, confidence, problem_ids, solution_ids)

    def encode_patterns_1_7(self) -> Tensor:
        """Encode all patterns 1-7 to vectors."""
        embeddings = []
        for i in range(1, 8):
            emb = self.encode_pattern(PATTERNS_1_7[i])
            embeddings.append(emb)
        return torch.cat(embeddings, dim=0)  # (7, embed_dim)

    def forward(self, patterns: Dict[int, PatternData]) -> Dict[str, Tensor]:
        """
        Forward pass for patterns 1-7.

        Returns dict with:
        - embeddings: (7, embed_dim) pattern embeddings
        - gnn_embeddings: (7, embed_dim) after graph convolution
        - next_pattern_logits: (7, num_patterns) next pattern predictions
        - category_logits: (7, num_categories) category predictions
        """
        # Encode all patterns
        embeddings = self.encode_patterns_1_7()

        # Apply GNN
        gnn_embeddings = self.gnn(embeddings, ADJACENCY_MATRIX)

        # Predictions
        next_pattern_logits = self.next_pattern_head(gnn_embeddings)
        category_logits = self.category_head(gnn_embeddings)

        return {
            "embeddings": embeddings,
            "gnn_embeddings": gnn_embeddings,
            "next_pattern_logits": next_pattern_logits,
            "category_logits": category_logits
        }

    def compute_similarity(self, emb1: Tensor, emb2: Tensor) -> Tensor:
        """Compute cosine similarity between pattern embeddings."""
        emb1_proj = F.normalize(self.similarity_head(emb1), dim=-1)
        emb2_proj = F.normalize(self.similarity_head(emb2), dim=-1)
        return F.cosine_similarity(emb1_proj, emb2_proj, dim=-1)

    def predict_next_patterns(self, pattern_id: int, top_k: int = 3) -> List[Tuple[int, float]]:
        """Predict most likely next patterns given current pattern."""
        embeddings = self.encode_patterns_1_7()
        gnn_embeddings = self.gnn(embeddings, ADJACENCY_MATRIX)

        idx = pattern_id - 1  # 0-indexed
        logits = self.next_pattern_head(gnn_embeddings[idx])
        probs = F.softmax(logits, dim=-1)

        top_probs, top_indices = torch.topk(probs, top_k)
        return [(idx.item() + 1, prob.item()) for idx, prob in zip(top_indices, top_probs)]


# =============================================================================
# TRAINING UTILITIES
# =============================================================================

def create_training_batch(patterns: Dict[int, PatternData]) -> Dict[str, Tensor]:
    """Create a training batch from pattern data."""
    encoder = PatternEncoder()

    pattern_ids = torch.tensor([p.id for p in patterns.values()])
    confidence = torch.tensor([p.confidence for p in patterns.values()])

    problem_ids = torch.stack([
        encoder.text_to_ids(p.problem) for p in patterns.values()
    ])
    solution_ids = torch.stack([
        encoder.text_to_ids(p.solution) for p in patterns.values()
    ])

    # Create labels for next pattern prediction
    # For each pattern, the label is the first following pattern (if any)
    next_pattern_labels = torch.tensor([
        p.following[0] if p.following else 0
        for p in patterns.values()
    ])

    # Category labels (all patterns 1-7 are Towns = 0)
    category_labels = torch.zeros(len(patterns), dtype=torch.long)

    return {
        "pattern_ids": pattern_ids,
        "confidence": confidence,
        "problem_ids": problem_ids,
        "solution_ids": solution_ids,
        "next_pattern_labels": next_pattern_labels,
        "category_labels": category_labels
    }


def train_step(
    model: PatternLanguageModel,
    optimizer: torch.optim.Optimizer,
    patterns: Dict[int, PatternData]
) -> Dict[str, float]:
    """Single training step."""
    model.train()
    optimizer.zero_grad()

    # Forward pass
    outputs = model(patterns)

    # Compute losses
    batch = create_training_batch(patterns)

    # Next pattern prediction loss
    next_pattern_loss = F.cross_entropy(
        outputs["next_pattern_logits"],
        batch["next_pattern_labels"],
        ignore_index=0  # Ignore patterns without following
    )

    # Category prediction loss
    category_loss = F.cross_entropy(
        outputs["category_logits"],
        batch["category_labels"]
    )

    # Total loss
    total_loss = next_pattern_loss + category_loss

    # Backward pass
    total_loss.backward()
    optimizer.step()

    return {
        "total_loss": total_loss.item(),
        "next_pattern_loss": next_pattern_loss.item(),
        "category_loss": category_loss.item()
    }


# =============================================================================
# DEMO
# =============================================================================

def demo():
    """Demonstrate the pattern neural network."""
    print("=" * 60)
    print("A Pattern Language - Patterns 1-7 Neural Network Demo")
    print("=" * 60)

    # Create model
    model = PatternLanguageModel(num_patterns=253, num_categories=3)
    print(f"\nModel created with {sum(p.numel() for p in model.parameters()):,} parameters")

    # Encode patterns
    print("\n--- Pattern Embeddings ---")
    embeddings = model.encode_patterns_1_7()
    print(f"Embeddings shape: {embeddings.shape}")

    # Compute similarity matrix
    print("\n--- Pattern Similarity Matrix ---")
    sim_matrix = torch.zeros(7, 7)
    for i in range(7):
        for j in range(7):
            sim_matrix[i, j] = model.compute_similarity(
                embeddings[i:i+1], embeddings[j:j+1]
            ).item()

    print("    " + "  ".join([f"P{i+1:2d}" for i in range(7)]))
    for i in range(7):
        row = " ".join([f"{sim_matrix[i, j]:.2f}" for j in range(7)])
        print(f"P{i+1}: {row}")

    # Forward pass
    print("\n--- Forward Pass ---")
    outputs = model(PATTERNS_1_7)
    print(f"GNN embeddings shape: {outputs['gnn_embeddings'].shape}")
    print(f"Next pattern logits shape: {outputs['next_pattern_logits'].shape}")
    print(f"Category logits shape: {outputs['category_logits'].shape}")

    # Predict next patterns
    print("\n--- Next Pattern Predictions ---")
    for i in range(1, 8):
        predictions = model.predict_next_patterns(i, top_k=3)
        pattern_name = PATTERNS_1_7[i].name
        pred_str = ", ".join([f"P{p}({prob:.2f})" for p, prob in predictions])
        print(f"P{i} ({pattern_name[:20]}...): {pred_str}")

    # Training demo
    print("\n--- Training Step ---")
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    losses = train_step(model, optimizer, PATTERNS_1_7)
    print(f"Total Loss: {losses['total_loss']:.4f}")
    print(f"Next Pattern Loss: {losses['next_pattern_loss']:.4f}")
    print(f"Category Loss: {losses['category_loss']:.4f}")

    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)


if __name__ == "__main__":
    demo()
