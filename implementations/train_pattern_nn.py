#!/usr/bin/env python3
"""
Train the Universal Pattern Language Neural Network

This script trains the model to:
1. Predict next patterns in sequences
2. Classify pattern categories
3. Learn meaningful pattern embeddings
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from typing import List, Tuple, Dict
import json
import random

from pattern_loader import PatternLoader, PatternData
from universal_pattern_nn import (
    UniversalPatternModel,
    build_adjacency_matrix,
    prepare_batch
)


class PatternSequenceDataset(Dataset):
    """
    Dataset for pattern sequences.
    
    Creates training samples:
    - Input: A pattern
    - Target: Next pattern in sequence
    - Category: Pattern category (towns/buildings/construction)
    """
    
    def __init__(self, patterns: Dict[int, PatternData], sequences: List[Dict]):
        self.patterns = patterns
        self.sequences = sequences
        self.samples = []
        
        # Create samples from sequences
        for seq in sequences:
            seq_patterns = seq.get('patterns', [])
            for i in range(len(seq_patterns) - 1):
                current_pid = seq_patterns[i]
                next_pid = seq_patterns[i + 1]
                
                if current_pid in patterns and next_pid in patterns:
                    self.samples.append({
                        'current': patterns[current_pid],
                        'next': next_pid - 1,  # Convert to 0-indexed
                        'category': self._category_to_idx(patterns[current_pid].category)
                    })
        
        print(f"Created {len(self.samples)} training samples from {len(sequences)} sequences")
    
    def _category_to_idx(self, category: str) -> int:
        """Convert category name to index."""
        mapping = {'towns': 0, 'buildings': 1, 'construction': 2}
        return mapping.get(category, 0)
    
    def __len__(self):
        return len(self.samples)
    
    def __getitem__(self, idx):
        return self.samples[idx]


def collate_fn(batch, encoder):
    """Custom collate function for DataLoader."""
    patterns = [item['current'] for item in batch]
    next_patterns = torch.tensor([item['next'] for item in batch], dtype=torch.long)
    categories = torch.tensor([item['category'] for item in batch], dtype=torch.long)
    
    # Prepare pattern inputs
    pattern_ids, confidence, category, problem_ids, solution_ids = prepare_batch(
        patterns, encoder
    )
    
    return {
        'pattern_ids': pattern_ids,
        'confidence': confidence,
        'category': category,
        'problem_ids': problem_ids,
        'solution_ids': solution_ids,
        'next_patterns': next_patterns,
        'target_categories': categories
    }


def train_epoch(
    model: UniversalPatternModel,
    dataloader: DataLoader,
    optimizer: optim.Optimizer,
    device: torch.device,
    adjacency: torch.Tensor
) -> Tuple[float, float, float]:
    """Train for one epoch."""
    model.train()
    total_loss = 0.0
    total_next_loss = 0.0
    total_category_loss = 0.0
    
    criterion_next = nn.CrossEntropyLoss()
    criterion_category = nn.CrossEntropyLoss()
    
    for batch in dataloader:
        # Move to device
        pattern_ids = batch['pattern_ids'].to(device)
        confidence = batch['confidence'].to(device)
        category = batch['category'].to(device)
        problem_ids = batch['problem_ids'].to(device)
        solution_ids = batch['solution_ids'].to(device)
        next_patterns = batch['next_patterns'].to(device)
        target_categories = batch['target_categories'].to(device)
        
        # Forward pass
        next_logits, category_logits, _ = model(
            pattern_ids, confidence, category, problem_ids, solution_ids
        )
        
        # Compute losses
        loss_next = criterion_next(next_logits, next_patterns)
        loss_category = criterion_category(category_logits, target_categories)
        
        # Combined loss (weight next pattern prediction more heavily)
        loss = 2.0 * loss_next + 1.0 * loss_category
        
        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Accumulate losses
        total_loss += loss.item()
        total_next_loss += loss_next.item()
        total_category_loss += loss_category.item()
    
    n_batches = len(dataloader)
    return (total_loss / n_batches, 
            total_next_loss / n_batches, 
            total_category_loss / n_batches)


def evaluate(
    model: UniversalPatternModel,
    dataloader: DataLoader,
    device: torch.device
) -> Tuple[float, float]:
    """Evaluate model accuracy."""
    model.eval()
    correct_next = 0
    correct_category = 0
    total = 0
    
    with torch.no_grad():
        for batch in dataloader:
            # Move to device
            pattern_ids = batch['pattern_ids'].to(device)
            confidence = batch['confidence'].to(device)
            category = batch['category'].to(device)
            problem_ids = batch['problem_ids'].to(device)
            solution_ids = batch['solution_ids'].to(device)
            next_patterns = batch['next_patterns'].to(device)
            target_categories = batch['target_categories'].to(device)
            
            # Forward pass
            next_logits, category_logits, _ = model(
                pattern_ids, confidence, category, problem_ids, solution_ids
            )
            
            # Get predictions
            _, predicted_next = torch.max(next_logits, 1)
            _, predicted_category = torch.max(category_logits, 1)
            
            # Compute accuracy
            total += next_patterns.size(0)
            correct_next += (predicted_next == next_patterns).sum().item()
            correct_category += (predicted_category == target_categories).sum().item()
    
    next_accuracy = 100 * correct_next / total
    category_accuracy = 100 * correct_category / total
    
    return next_accuracy, category_accuracy


def main():
    """Main training script."""
    print("=" * 70)
    print("TRAINING UNIVERSAL PATTERN LANGUAGE NEURAL NETWORK")
    print("=" * 70)
    
    # Device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"\nUsing device: {device}")
    
    # Load patterns
    print("\n=== Loading Patterns ===")
    loader = PatternLoader()
    patterns = loader.load_all()
    print(f"✓ Loaded {len(patterns)} patterns")
    
    # Load sequences
    with open('pattern_sequences.json', 'r') as f:
        seq_data = json.load(f)
        sequences = seq_data['sequences']
    print(f"✓ Loaded {len(sequences)} sequences")
    
    # Create dataset
    print("\n=== Creating Dataset ===")
    dataset = PatternSequenceDataset(patterns, sequences)
    
    # Split into train/val (80/20)
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(
        dataset, [train_size, val_size]
    )
    print(f"✓ Train samples: {len(train_dataset)}")
    print(f"✓ Val samples: {len(val_dataset)}")
    
    # Create model
    print("\n=== Creating Model ===")
    model = UniversalPatternModel(
        num_patterns=253,
        num_categories=3,
        embedding_dim=256,
        hidden_dim=256
    ).to(device)
    print(f"✓ Model parameters: {sum(p.numel() for p in model.parameters()):,}")
    
    # Build adjacency matrix
    adjacency = build_adjacency_matrix(patterns).to(device)
    
    # Create dataloaders
    train_loader = DataLoader(
        train_dataset,
        batch_size=16,
        shuffle=True,
        collate_fn=lambda batch: collate_fn(batch, model.encoder)
    )
    
    val_loader = DataLoader(
        val_dataset,
        batch_size=16,
        shuffle=False,
        collate_fn=lambda batch: collate_fn(batch, model.encoder)
    )
    
    # Optimizer
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Training loop
    print("\n=== Training ===")
    num_epochs = 10
    best_val_acc = 0.0
    
    for epoch in range(num_epochs):
        # Train
        train_loss, train_next_loss, train_cat_loss = train_epoch(
            model, train_loader, optimizer, device, adjacency
        )
        
        # Evaluate
        val_next_acc, val_cat_acc = evaluate(model, val_loader, device)
        
        print(f"Epoch {epoch+1}/{num_epochs}")
        print(f"  Train Loss: {train_loss:.4f} (next: {train_next_loss:.4f}, cat: {train_cat_loss:.4f})")
        print(f"  Val Acc: Next={val_next_acc:.2f}%, Category={val_cat_acc:.2f}%")
        
        # Save best model
        if val_next_acc > best_val_acc:
            best_val_acc = val_next_acc
            torch.save(model.state_dict(), 'implementations/pattern_model_best.pt')
            print(f"  ✓ Saved best model (acc={best_val_acc:.2f}%)")
    
    print(f"\n✓ Training complete! Best val accuracy: {best_val_acc:.2f}%")
    
    # Demo predictions with trained model
    print("\n=== Demo: Trained Model Predictions ===")
    model.eval()
    for pid in [1, 2, 3, 4, 5]:
        if pid in patterns:
            pattern = patterns[pid]
            predictions = model.predict_next_patterns(pattern, top_k=5, device=device)
            print(f"\nPattern {pid}: {pattern.name}")
            print(f"  Actual following: {pattern.following}")
            print(f"  Predicted:")
            for next_id, prob in predictions:
                next_pattern = patterns.get(next_id)
                next_name = next_pattern.name if next_pattern else "Unknown"
                match = "✓" if next_id in pattern.following else " "
                print(f"    {match} Pattern {next_id:3d} ({next_name[:30]:30s}): {prob:.4f}")


if __name__ == '__main__':
    main()
