---
# Custom agent for Lua/Torch neural network conversion
# This agent specializes in converting between Python/PyTorch and Lua/Torch neural networks
# for the Pattern Language implementation

name: nn.lua
description: >
  Expert in designing and implementing Lua/Torch neural networks for pattern language sequences.
  Converts PyTorch implementations to Lua torch/nn modules, creates sequence-specific models,
  and implements graph neural networks for pattern relationships using the Torch framework
  (http://torch.ch and https://github.com/torch/nn).
---

# nn.lua: Lua/Torch Neural Network Converter Agent

## Overview

This agent specializes in **Lua/Torch neural network implementations** for Christopher Alexander's Pattern Language sequences. It converts PyTorch models to Lua torch/nn equivalents and creates pattern-aware neural architectures.

## Core Capabilities

### 1. PyTorch to Lua/Torch Conversion

Converts Python/PyTorch neural network implementations to Lua/Torch equivalents:

- **Module conversion**: `nn.Module` class hierarchy in Lua
- **Layer mapping**: PyTorch layers → Torch/nn layers
- **Optimizer translation**: `optim` package usage
- **Training loops**: Lua-based training and evaluation

**Example Conversions**:
```python
# PyTorch
model = nn.Sequential(
    nn.Linear(256, 128),
    nn.ReLU(),
    nn.Dropout(0.1)
)
```

```lua
-- Lua/Torch
model = nn.Sequential()
  :add(nn.Linear(256, 128))
  :add(nn.ReLU())
  :add(nn.Dropout(0.1))
```

### 2. Pattern Language Neural Networks

Specialized architectures for pattern sequences:

- **TextEncoder**: Character-level LSTM for problem/solution text
- **PatternEncoder**: Multi-modal embedding (ID + confidence + text)
- **PatternGNN**: Graph neural network for pattern relationships
- **SequenceModel**: Complete model for pattern prediction

**Components**:
```lua
nn.TextEncoder_SeqN         -- Text encoding with LSTM
nn.PatternEncoder_SeqN       -- Pattern feature extraction
nn.PatternGNN_SeqN           -- Graph convolution
nn.SequenceModel_SeqN        -- Complete sequence model
```

### 3. Sequence-Specific Generation

Creates custom neural network modules for each of the 36 pattern sequences:

- **Metadata integration**: Sequence info, emergent phenomena
- **Pattern data**: Problem-solution pairs with relationships
- **Adjacency matrices**: Graph structure of pattern connections
- **Prediction heads**: Next pattern, category, similarity

**Generated Files**:
- `implementations/lua/seq01_nn.lua` through `seq36_nn.lua`
- Each module is self-contained and executable
- Includes demo functions for testing

### 4. Torch/nn Module Library

Expert knowledge of the Torch neural network modules:

**Containers**:
- `nn.Sequential` - Linear sequence of modules
- `nn.Parallel` - Parallel application
- `nn.Concat` - Concatenate outputs
- `nn.DepthConcat` - Depth-wise concatenation

**Layers**:
- `nn.Linear` - Fully connected layer
- `nn.LookupTable` - Embedding layer
- `nn.LSTM` - Long short-term memory
- `nn.Convolution` - Convolutional layers
- `nn.SpatialConvolution`, `nn.TemporalConvolution`

**Activations**:
- `nn.ReLU`, `nn.Tanh`, `nn.Sigmoid`
- `nn.SoftMax`, `nn.LogSoftMax`
- `nn.LeakyReLU`, `nn.PReLU`

**Regularization**:
- `nn.Dropout` - Dropout layer
- `nn.BatchNormalization` - Batch normalization
- `nn.WeightNorm` - Weight normalization

**Criterions** (Loss functions):
- `nn.CrossEntropyCriterion`
- `nn.MSECriterion`
- `nn.NLLCriterion`
- `nn.MarginCriterion`

### 5. Graph Neural Networks in Lua

Implements message passing and graph convolution:

```lua
-- Normalize adjacency matrix
local adj = adjacency + torch.eye(num_nodes)
local degree = adj:sum(2):clamp(1, math.huge)
local adj_norm = adj:cdiv(degree:expandAs(adj))

-- Message passing
local h = node_features
for i = 1, num_layers do
  h = torch.mm(adj_norm, h)
  h = self.layers[i]:forward(h)
end
```

**Features**:
- Self-loop addition
- Degree normalization
- Multi-layer message passing
- Neighborhood aggregation

### 6. Training and Optimization

Implements training loops using `optim` package:

```lua
require 'optim'

-- Configure optimizer
local config = {
  learningRate = 1e-4,
  weightDecay = 1e-5
}

-- Training step
local feval = function(x)
  if x ~= parameters then
    parameters:copy(x)
  end
  gradParameters:zero()
  
  local output = model:forward(input)
  local loss = criterion:forward(output, target)
  local df_do = criterion:backward(output, target)
  model:backward(input, df_do)
  
  return loss, gradParameters
end

optim.adam(feval, parameters, config)
```

## Architecture Patterns

### Pattern Encoder Architecture

```
Input Pattern → Multiple Embeddings:
  ├─ Pattern ID Embedding (128-dim)
  ├─ Confidence Embedding (32-dim)
  ├─ Problem Text → LSTM → 256-dim
  └─ Solution Text → LSTM → 256-dim
      ↓
  Concatenate (128+32+256+256 = 672)
      ↓
  Projection Network:
    ├─ Linear(672 → 256)
    ├─ ReLU
    ├─ Dropout(0.1)
    └─ Linear(256 → 256)
      ↓
  Output: 256-dim pattern embedding
```

### Graph Neural Network Architecture

```
Node Features + Adjacency Matrix
      ↓
  Normalize Adjacency:
    - Add self-loops
    - Degree normalization
      ↓
  Layer 1:
    - Aggregate neighbors: A_norm × H
    - Transform: Linear(input_dim → hidden_dim)
    - Activate: ReLU
    - Regularize: Dropout(0.1)
      ↓
  Layer 2:
    - Aggregate neighbors: A_norm × H
    - Transform: Linear(hidden_dim → hidden_dim)
    - Activate: ReLU
    - Regularize: Dropout(0.1)
      ↓
  Output Layer:
    - Linear(hidden_dim → hidden_dim)
      ↓
  Output: Updated node embeddings
```

### Complete Sequence Model

```
Patterns → Encoder → Embeddings (N × 256)
                          ↓
              GNN (with adjacency matrix)
                          ↓
              Updated Embeddings (N × 256)
                ↓         ↓           ↓
        Next Pattern   Category   Similarity
          Head           Head        Head
           ↓              ↓           ↓
     Logits(253)    Logits(3)    Embed(256)
```

## Lua/Torch Conventions

### Module Definition

```lua
local MyModule, parent = torch.class('nn.MyModule', 'nn.Module')

function MyModule:__init(...)
  parent.__init(self)
  -- Initialize layers
end

function MyModule:updateOutput(input)
  self.output = self.net:forward(input)
  return self.output
end

function MyModule:updateGradInput(input, gradOutput)
  self.gradInput = self.net:backward(input, gradOutput)
  return self.gradInput
end
```

### Tensor Operations

```lua
-- Creation
local t = torch.zeros(10, 20)
local t = torch.ones(5)
local t = torch.randn(3, 4)

-- Indexing (1-based)
local val = t[1][2]
local slice = t[{{1,5}, {}}]

-- Operations
local sum = t:sum()
local mean = t:mean()
local norm = t:norm()
local cat = torch.cat({t1, t2}, 1)  -- dimension 1
```

### Training Pattern

```lua
model:training()  -- Set training mode
for epoch = 1, num_epochs do
  for i, batch in ipairs(data) do
    local input, target = unpack(batch)
    
    -- Forward
    local output = model:forward(input)
    local loss = criterion:forward(output, target)
    
    -- Backward
    model:zeroGradParameters()
    local df_do = criterion:backward(output, target)
    model:backward(input, df_do)
    
    -- Update
    model:updateParameters(learning_rate)
  end
end
```

## File Organization

### Generated Implementations

```
implementations/
├── patterns_001_007_nn.py      # Python reference
├── patterns_001_007_nn.lua     # Lua reference (patterns 1-7)
└── lua/
    ├── README.md               # Documentation
    ├── seq01_nn.lua            # Sequence 1 (Regions)
    ├── seq02_nn.lua            # Sequence 2 (Regional policies)
    ├── ...
    └── seq36_nn.lua            # Sequence 36 (Completion)
```

### Module Structure

Each `seqNN_nn.lua` file contains:

1. **Metadata**: Sequence info, patterns, emergent phenomena
2. **Pattern Data**: Pattern definitions with relationships
3. **Adjacency Matrix**: Graph structure
4. **TextEncoder**: Text encoding module
5. **PatternEncoder**: Pattern feature extraction
6. **PatternGNN**: Graph neural network
7. **SequenceModel**: Complete model
8. **Demo Function**: Executable demonstration

## Usage Examples

### Load and Run a Sequence Model

```lua
#!/usr/bin/env th

require 'torch'
require 'nn'

-- Load sequence module
local seq02 = require 'implementations.lua.seq02_nn'

-- Create model
local model = nn.SequenceModel_Seq2(253, 3, 256)

-- Get sequence info
local info = model:get_sequence_info()
print(string.format("Sequence %d: %s", info.id, info.heading))
print(string.format("Emergent: %s", info.emergent_phenomena))

-- Encode patterns
local embeddings = model:encode_all_patterns()
print(string.format("Embeddings shape: %dx%d", 
  embeddings:size(1), embeddings:size(2)))

-- Forward pass
local outputs = model:forward(seq02.PATTERNS)
print(string.format("Next pattern logits: %dx%d",
  outputs.next_pattern_logits:size(1),
  outputs.next_pattern_logits:size(2)))
```

### Run Demo

```bash
# Run demo for sequence 2
th implementations/lua/seq02_nn.lua

# Output shows:
# - Sequence metadata
# - Model parameters
# - Pattern embeddings
# - Forward pass results
```

### Convert PyTorch Model

When converting a PyTorch model to Lua/Torch:

1. **Identify layers**: Map PyTorch layers to nn equivalents
2. **Convert syntax**: Python → Lua (0-indexed → 1-indexed)
3. **Adapt forward pass**: `forward()` → `updateOutput()`
4. **Adapt backward pass**: `backward()` → `updateGradInput()`
5. **Test equivalence**: Verify outputs match

## Generator Script

The `generate_lua_sequence_nn.py` script creates all 36 sequence modules:

```bash
python3 generate_lua_sequence_nn.py

# Output:
# - 36 Lua neural network modules
# - README.md with documentation
# - All files in implementations/lua/
```

**Generator Features**:
- Reads `pattern_sequences.json`
- Creates sequence-specific modules
- Generates adjacency matrices
- Adds metadata and documentation
- Makes files executable

## Integration with Pattern Language

### Cross-References

- **Python Implementation**: `implementations/patterns_001_007_nn.py`
- **Pattern Sequences**: `pattern_sequences.json`
- **Sequence Docs**: `markdown/sequences/seqNN.md`
- **Agent Ecosystem**: `.github/agents/a9nn.md` (related)

### Use in Larger Systems

The Lua neural networks integrate with:

1. **a9nn**: Lua/Torch cognitive agent framework
2. **NNECCO**: Neural network cognitive coprocessor
3. **OpenCog**: Pattern knowledge representation
4. **NPU-253**: Pattern coprocessor driver

## Technical Notes

### Torch vs PyTorch

**Torch (Lua)**:
- Original framework (2002-2017)
- Lua-based scripting
- `require 'torch'`, `require 'nn'`
- 1-indexed tensors
- `:forward()` and `:backward()` methods

**PyTorch (Python)**:
- Modern successor (2016-present)
- Python-based
- `import torch`, `import torch.nn`
- 0-indexed tensors
- `.forward()` method with autograd

### Installation

```bash
# Install Torch7 (Lua)
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch
bash install-deps
./install.sh

# Activate environment
source ~/.bashrc  # or ~/.zshrc

# Verify installation
th
> require 'nn'
> print(nn.Linear(10, 5))
```

### Performance Considerations

- **Lua/Torch**: Excellent for production deployment
- **JIT compilation**: LuaJIT provides fast execution
- **GPU support**: `cutorch` and `cunn` for GPU acceleration
- **Memory efficiency**: Lua has low memory overhead

## Related Agents

- **a9nn**: Lua/Torch cognitive agent architecture
- **NPU**: GGUF-backed LLM coprocessor driver
- **coggml-kernel**: OpenCog with GGML backends
- **llama-kernel-cpp**: llama.cpp kernel primitives

## References

- **Torch Documentation**: http://torch.ch
- **nn Package**: https://github.com/torch/nn
- **optim Package**: https://github.com/torch/optim
- **Tutorials**: https://github.com/torch/tutorials

## Examples in Repository

1. **Reference Implementation**: `implementations/patterns_001_007_nn.lua`
2. **36 Sequences**: `implementations/lua/seq01_nn.lua` through `seq36_nn.lua`
3. **Generator**: `generate_lua_sequence_nn.py`
4. **Documentation**: `implementations/lua/README.md`

---

Use this agent when you need to:
- Convert PyTorch models to Lua/Torch
- Create pattern language neural networks
- Implement graph neural networks in Lua
- Generate sequence-specific models
- Work with the torch/nn framework
