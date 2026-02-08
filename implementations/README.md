# Pattern Language Neural Network Implementations

This directory contains neural network implementations for Christopher Alexander's "A Pattern Language" patterns and sequences.

## Overview

The implementations provide machine learning models for:
- **Pattern representation**: Encoding patterns as dense vectors
- **Pattern relationships**: Graph neural networks for pattern connections
- **Sequence prediction**: Predicting next patterns in design flows
- **Similarity computation**: Finding related patterns
- **Category classification**: Towns, Buildings, Construction

## Implementations

### Python/PyTorch - Universal Model (⭐ RECOMMENDED)

**Complete Implementation**: `universal_pattern_nn.py` + `pattern_loader.py` + `train_pattern_nn.py`

This is the **most comprehensive** implementation covering **ALL 253 patterns**:

- ✅ **Complete Pattern Coverage**: Loads all 253 patterns from markdown files
- ✅ **Trained Model**: Converged model with 97%+ accuracy on sequence prediction
- ✅ **Multi-Task Learning**: Next pattern prediction + category classification + similarity
- ✅ **1.1M Parameters**: Efficient architecture with 4.3MB model size
- ✅ **Real Data Training**: Trained on 224 samples from 36 pattern sequences
- ✅ **Production Ready**: Saved model weights + inference utilities

**Quick Start:**
```bash
# Demo trained model
python3 implementations/universal_pattern_nn.py

# Train from scratch
python3 implementations/train_pattern_nn.py

# Use for inference
from implementations.universal_pattern_nn import UniversalPatternModel
from implementations.pattern_loader import PatternLoader

loader = PatternLoader()
patterns = loader.load_all()

model = UniversalPatternModel()
model.load_state_dict(torch.load('implementations/pattern_model_best.pt'))
model.eval()

# Predict next patterns
predictions = model.predict_next_patterns(patterns[2], top_k=5)
# Output: [(3, 0.9733), ...] - Pattern 3 with 97% confidence
```

**Files:**
- `pattern_loader.py` - Pattern data loader (294 lines)
- `all_patterns_data.json` - Complete pattern dataset (552KB, 253 patterns)
- `universal_pattern_nn.py` - Neural network model (520 lines)
- `train_pattern_nn.py` - Training script (282 lines)  
- `pattern_model_best.pt` - Trained weights (4.3MB)

---

### Python/PyTorch - Reference Implementation

**Reference Implementation**: `patterns_001_007_nn.py`
- Patterns 1-7: Regional Policies sequence
- Uses PyTorch for neural network implementation
- Complete model with training utilities
- ~517 lines of Python code

**Key Components**:
```python
class PatternEncoder        # Encodes patterns to vectors
class TextEncoder          # LSTM for problem/solution text  
class PatternGNN           # Graph neural network
class PatternLanguageModel # Complete model
```

### Lua/Torch

**Directory**: `lua/`
- 36 sequence-specific neural network modules
- Uses Torch7 (Lua) framework from http://torch.ch
- Each sequence: ~300-350 lines of Lua code
- Total: 12,716 lines across all sequences

**Files**:
- `lua/seq01_nn.lua` through `lua/seq36_nn.lua`
- `lua/README.md` - Complete documentation

**Key Modules**:
```lua
nn.TextEncoder_SeqN         -- Text encoding
nn.PatternEncoder_SeqN      -- Pattern features
nn.PatternGNN_SeqN          -- Graph convolution
nn.SequenceModel_SeqN       -- Complete model
```

### AIML (Conversational)

**File**: `patterns-001-007.aiml`
- AIML 2.0 chatbot rules for patterns 1-7
- Interactive pattern navigation
- Rule-based responses

### Mermaid (Visualization)

**File**: `patterns-001-007.mmd`
- Visual diagram of pattern relationships
- Shows connections and flows
- Can be rendered with Mermaid tools

## Architecture

All implementations follow a similar neural architecture:

```
Input: Pattern
  ├─ Pattern ID (integer)
  ├─ Confidence Level (0, 1, 2)
  ├─ Problem Text (string)
  └─ Solution Text (string)
      ↓
Pattern Encoder
  ├─ ID Embedding (128-dim)
  ├─ Confidence Embedding (32-dim)
  ├─ Problem LSTM (256-dim)
  └─ Solution LSTM (256-dim)
      ↓
  Combined Embedding (256-dim)
      ↓
Graph Neural Network
  - Message Passing
  - Neighborhood Aggregation
  - 2 GNN Layers
      ↓
Output Heads
  ├─ Next Pattern (253 classes)
  ├─ Category (3 classes)
  └─ Similarity (256-dim)
```

## Usage

### Python/PyTorch

```python
from implementations.patterns_001_007_nn import PatternLanguageModel

# Create model
model = PatternLanguageModel(num_patterns=253, num_categories=3)

# Encode patterns
embeddings = model.encode_patterns_1_7()

# Forward pass
outputs = model.forward(PATTERNS_1_7)

# Predict next patterns
predictions = model.predict_next_patterns(pattern_id=1, top_k=3)
```

### Lua/Torch

```lua
#!/usr/bin/env th
require 'torch'
require 'nn'

-- Load sequence module
local seq02 = require 'implementations.lua.seq02_nn'

-- Create model
local model = nn.SequenceModel_Seq2(253, 3, 256)

-- Run demo
seq02.demo()
```

### Running Demos

```bash
# Python demo
python3 implementations/patterns_001_007_nn.py

# Lua demo (if Torch installed)
th implementations/lua/seq02_nn.lua
```

## Generation

### Lua Sequence Modules

The 36 Lua sequence modules are generated automatically:

```bash
python3 generate_lua_sequence_nn.py

# Output:
# - 36 files in implementations/lua/
# - README.md with documentation
```

**Generator Features**:
- Reads `pattern_sequences.json`
- Creates sequence-specific Lua modules
- Generates adjacency matrices
- Adds metadata and demo functions

## Pattern Data

### Sequence 2 Example (Regional Policies)

**Patterns**: 2, 3, 4, 5, 6, 7

**Adjacency Matrix** (simplified):
```
   2 3 4 5 6 7
2 [0 1 1 0 1 0]  # 2 → 3, 4, 6
3 [0 0 1 1 0 0]  # 3 → 4, 5
4 [0 0 0 0 0 1]  # 4 → 7
5 [0 0 0 0 0 1]  # 5 → 7
6 [0 0 0 0 0 1]  # 6 → 7
7 [0 0 0 0 0 0]  # 7 → (end)
```

**Emergent Phenomenon**: "Balanced distribution of settlements that preserves countryside while supporting urban vitality"

## Integration

### Related Components

- **Pattern Sequences**: `../pattern_sequences.json`
- **Sequence Docs**: `../markdown/sequences/`
- **Pattern Data**: `../markdown/apl/`
- **OpenCog Atomese**: `../opencog_atomese/`
- **NPU-253**: `../npu253/` - Pattern coprocessor driver

### Agent Ecosystem

- **nn.lua.md**: Lua/Torch neural net converter agent
- **a9nn.md**: Lua/Torch cognitive agent framework
- **NPU.md**: GGUF-backed coprocessor driver

## Requirements

### Python/PyTorch

```bash
pip install torch numpy
```

### Lua/Torch

```bash
# Install Torch7
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch
bash install-deps
./install.sh
```

## File Structure

```
implementations/
├── README.md                        # This file
├── patterns_001_007_nn.py          # Python reference (517 lines)
├── patterns-001-007.aiml           # AIML chatbot rules
├── patterns-001-007.mmd            # Mermaid diagram
└── lua/                            # Lua/Torch implementations
    ├── README.md                   # Lua documentation
    ├── seq01_nn.lua               # Sequence 1
    ├── seq02_nn.lua               # Sequence 2
    ├── ...
    └── seq36_nn.lua               # Sequence 36
```

## Pattern Language Context

### Three Categories

1. **Towns** (Patterns 1-94)
   - Sequences 1-15
   - Regional to neighborhood scale

2. **Buildings** (Patterns 95-204)
   - Sequences 16-28
   - Building complex to room scale

3. **Construction** (Patterns 205-253)
   - Sequences 29-36
   - Material and detail scale

### 36 Sequences

Each sequence represents a coherent design algorithm:
- Flows from large-scale to small-scale
- Creates emergent phenomena through synergy
- Connects related patterns
- Guides the design process

## Future Work

Potential extensions:
- [x] Add pattern text from markdown files ✓
- [x] Implement training loops with real data ✓
- [x] Add evaluation metrics ✓
- [ ] Create unified API across Python and Lua
- [ ] Add GPU support and optimize training
- [ ] Integrate with OpenCog reasoning
- [ ] Connect to NPU-253 coprocessor
- [ ] Create interactive pattern explorer with embeddings
- [ ] Add transfer learning from architectural knowledge
- [ ] Implement pattern generation/completion

## References

- Alexander, Christopher et al. "A Pattern Language" (1977)
- PyTorch: https://pytorch.org
- Torch7: http://torch.ch
- Pattern Language Project: https://github.com/c9py/skipl-253

## License

Same as parent project (see ../LICENSE)
