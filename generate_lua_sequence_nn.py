#!/usr/bin/env python3
"""
Generate Lua/Torch neural network implementations for all 36 pattern sequences.

This script reads pattern_sequences.json and generates individual Lua modules
for each sequence using the torch/nn framework.
"""

import json
import os
from pathlib import Path


def generate_sequence_nn_lua(sequence_data, patterns_data):
    """Generate Lua neural network code for a sequence."""
    
    seq_id = sequence_data['id']
    heading = sequence_data['heading']
    description = sequence_data.get('description', '')
    category = sequence_data.get('category', 'Unknown')
    patterns = sequence_data.get('patterns', [])
    emergent = sequence_data.get('emergent_phenomena', '')
    
    # Build pattern definitions
    pattern_defs = []
    for pid in patterns:
        # Find pattern in patterns_data if available
        pattern_info = {
            'id': pid,
            'name': f'PATTERN_{pid}',
            'problem': f'Problem for pattern {pid}',
            'solution': f'Solution for pattern {pid}',
            'confidence': 2,
            'preceding': [],
            'following': []
        }
        pattern_defs.append(pattern_info)
    
    # Build adjacency matrix
    n = len(patterns)
    adj_matrix = []
    for i, pid in enumerate(patterns):
        row = [0] * n
        # Connect sequential patterns
        if i < n - 1:
            row[i + 1] = 1
        adj_matrix.append(row)
    
    # Format adjacency matrix for Lua
    adj_lines = []
    for row in adj_matrix:
        adj_lines.append('  {' + ', '.join(map(str, row)) + '}')
    adj_str = ',\n'.join(adj_lines) if adj_lines else '  {}'
    
    # Format pattern definitions for Lua
    pattern_lua = []
    for i, p in enumerate(pattern_defs, 1):
        prec = '{' + ', '.join(map(str, p['preceding'])) + '}'
        foll = '{' + ', '.join(map(str, p['following'])) + '}'
        
        pattern_lua.append(f"""  {{
    id = {p['id']},
    name = "{p['name']}",
    problem = "{p['problem']}",
    solution = "{p['solution']}",
    confidence = {p['confidence']},
    preceding = {prec},
    following = {foll}
  }}""")
    
    patterns_lua_str = ',\n'.join(pattern_lua) if pattern_lua else ''
    pattern_ids_comment = ', '.join(map(str, patterns)) if patterns else 'none'
    
    lua_code = f'''#!/usr/bin/env th
--[[
A Pattern Language - Sequence {seq_id}: {heading}
Torch Neural Network Implementation

Category: {category}
Patterns: {pattern_ids_comment}

{description}

Emergent Phenomenon: {emergent}

Requirements:
  - torch (http://torch.ch)
  - nn (https://github.com/torch/nn)
  - optim (https://github.com/torch/optim)
--]]

require 'torch'
require 'nn'
require 'optim'

-- =============================================================================
-- SEQUENCE METADATA
-- =============================================================================

local SEQUENCE_INFO = {{
  id = {seq_id},
  heading = "{heading}",
  description = "{description}",
  category = "{category}",
  pattern_ids = {{{pattern_ids_comment}}},
  emergent_phenomena = "{emergent}"
}}

-- =============================================================================
-- PATTERN DATA
-- =============================================================================

local PATTERNS = {{
{patterns_lua_str}
}}

-- Adjacency matrix for pattern relationships
local ADJACENCY_MATRIX = torch.FloatTensor({{
{adj_str}
}})

-- =============================================================================
-- TEXT ENCODER
-- =============================================================================

local TextEncoder, parent = torch.class('nn.TextEncoder_Seq{seq_id}', 'nn.Module')

function TextEncoder:__init(vocab_size, embed_dim, hidden_dim)
  parent.__init(self)
  
  vocab_size = vocab_size or 256
  embed_dim = embed_dim or 64
  hidden_dim = hidden_dim or 128
  
  self.embed = nn.LookupTable(vocab_size, embed_dim)
  self.lstm = nn.LSTM(embed_dim, hidden_dim, nil, true)
  self.output_dim = hidden_dim * 2
  
  self.net = nn.Sequential()
    :add(self.embed)
    :add(self.lstm)
end

function TextEncoder:updateOutput(input)
  local lstm_out = self.net:forward(input)
  local batch_size = input:size(1)
  local seq_len = input:size(2)
  self.output = lstm_out[{{{{seq_len}}}}, {{}}, {{}}}}]:view(batch_size, -1)
  return self.output
end

function TextEncoder:text_to_ids(text, max_len)
  max_len = max_len or 200
  local ids = torch.zeros(max_len):long()
  for i = 1, math.min(#text, max_len) do
    ids[i] = string.byte(text:sub(i,i)) % 256 + 1
  end
  return ids
end

-- =============================================================================
-- PATTERN ENCODER
-- =============================================================================

local PatternEncoder, parent = torch.class('nn.PatternEncoder_Seq{seq_id}', 'nn.Module')

function PatternEncoder:__init(num_patterns, pattern_dim, text_hidden, output_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  pattern_dim = pattern_dim or 128
  text_hidden = text_hidden or 128
  output_dim = output_dim or 256
  
  self.pattern_embed = nn.LookupTable(num_patterns + 1, pattern_dim)
  self.confidence_embed = nn.LookupTable(3, 32)
  
  self.problem_encoder = nn.TextEncoder_Seq{seq_id}(256, 64, text_hidden)
  self.solution_encoder = nn.TextEncoder_Seq{seq_id}(256, 64, text_hidden)
  
  local combined_dim = pattern_dim + 32 + text_hidden * 4
  
  self.projection = nn.Sequential()
    :add(nn.Linear(combined_dim, output_dim))
    :add(nn.ReLU())
    :add(nn.Dropout(0.1))
    :add(nn.Linear(output_dim, output_dim))
  
  self.output_dim = output_dim
end

function PatternEncoder:updateOutput(input)
  local pattern_ids = input[1]
  local confidence = input[2]
  local problem_ids = input[3]
  local solution_ids = input[4]
  
  local pat_emb = self.pattern_embed:forward(pattern_ids)
  local conf_emb = self.confidence_embed:forward(confidence)
  local prob_emb = self.problem_encoder:forward(problem_ids)
  local sol_emb = self.solution_encoder:forward(solution_ids)
  
  local combined = torch.cat({{pat_emb, conf_emb, prob_emb, sol_emb}}, 2)
  self.output = self.projection:forward(combined)
  return self.output
end

-- =============================================================================
-- GRAPH NEURAL NETWORK
-- =============================================================================

local PatternGNN, parent = torch.class('nn.PatternGNN_Seq{seq_id}', 'nn.Module')

function PatternGNN:__init(input_dim, hidden_dim, num_layers)
  parent.__init(self)
  
  input_dim = input_dim or 256
  hidden_dim = hidden_dim or 256
  num_layers = num_layers or 2
  
  self.num_layers = num_layers
  self.layers = {{}}
  
  for i = 1, num_layers do
    local layer_input = (i == 1) and input_dim or hidden_dim
    local layer = nn.Sequential()
      :add(nn.Linear(layer_input, hidden_dim))
      :add(nn.ReLU())
      :add(nn.Dropout(0.1))
    table.insert(self.layers, layer)
  end
  
  self.output_layer = nn.Linear(hidden_dim, hidden_dim)
end

function PatternGNN:updateOutput(input)
  local node_features = input[1]
  local adjacency = input[2]
  
  local num_nodes = adjacency:size(1)
  local adj = adjacency + torch.eye(num_nodes)
  local degree = adj:sum(2):clamp(1, math.huge)
  local adj_norm = adj:cdiv(degree:expandAs(adj))
  
  local h = node_features
  for i = 1, self.num_layers do
    h = torch.mm(adj_norm, h)
    h = self.layers[i]:forward(h)
  end
  
  self.output = self.output_layer:forward(h)
  return self.output
end

-- =============================================================================
-- SEQUENCE MODEL
-- =============================================================================

local SequenceModel, parent = torch.class('nn.SequenceModel_Seq{seq_id}', 'nn.Module')

function SequenceModel:__init(num_patterns, num_categories, embed_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  num_categories = num_categories or 3
  embed_dim = embed_dim or 256
  
  self.num_patterns = num_patterns
  self.embed_dim = embed_dim
  self.sequence_patterns = PATTERNS
  
  self.encoder = nn.PatternEncoder_Seq{seq_id}(num_patterns, 128, 128, embed_dim)
  self.gnn = nn.PatternGNN_Seq{seq_id}(embed_dim, embed_dim, 2)
  
  self.next_pattern_head = nn.Linear(embed_dim, num_patterns)
  self.category_head = nn.Linear(embed_dim, num_categories)
  self.similarity_head = nn.Linear(embed_dim, embed_dim)
end

function SequenceModel:encode_pattern(pattern)
  local pattern_id = torch.LongTensor({{pattern.id}})
  local confidence = torch.LongTensor({{pattern.confidence + 1}})
  local problem_ids = self.encoder.problem_encoder:text_to_ids(pattern.problem):view(1, -1)
  local solution_ids = self.encoder.solution_encoder:text_to_ids(pattern.solution):view(1, -1)
  
  return self.encoder:forward({{pattern_id, confidence, problem_ids, solution_ids}})
end

function SequenceModel:encode_all_patterns()
  local embeddings = {{}}
  for i = 1, #PATTERNS do
    local emb = self:encode_pattern(PATTERNS[i])
    table.insert(embeddings, emb)
  end
  return torch.cat(embeddings, 1)
end

function SequenceModel:forward(patterns)
  local embeddings = self:encode_all_patterns()
  local gnn_embeddings = self.gnn:forward({{embeddings, ADJACENCY_MATRIX}})
  local next_pattern_logits = self.next_pattern_head:forward(gnn_embeddings)
  local category_logits = self.category_head:forward(gnn_embeddings)
  
  return {{
    embeddings = embeddings,
    gnn_embeddings = gnn_embeddings,
    next_pattern_logits = next_pattern_logits,
    category_logits = category_logits
  }}
end

function SequenceModel:get_sequence_info()
  return SEQUENCE_INFO
end

-- =============================================================================
-- DEMO
-- =============================================================================

function demo()
  print(string.rep("=", 60))
  print(string.format("Sequence %d: %s", {seq_id}, "{heading}"))
  print(string.rep("=", 60))
  print(string.format("Category: %s", "{category}"))
  print(string.format("Patterns: %s", "{pattern_ids_comment}"))
  print(string.format("\\nEmergent Phenomenon:\\n%s", "{emergent}"))
  print(string.rep("=", 60))
  
  local model = nn.SequenceModel_Seq{seq_id}(253, 3, 256)
  local params, _ = model:getParameters()
  print(string.format("\\nModel created with %d parameters", params:nElement()))
  
  local embeddings = model:encode_all_patterns()
  print(string.format("\\nPattern embeddings shape: %dx%d", 
    embeddings:size(1), embeddings:size(2)))
  
  local outputs = model:forward(PATTERNS)
  print(string.format("\\nForward pass complete"))
  print(string.format("GNN embeddings: %dx%d", 
    outputs.gnn_embeddings:size(1), outputs.gnn_embeddings:size(2)))
  
  print("\\n" .. string.rep("=", 60))
  print("Demo complete!")
  print(string.rep("=", 60))
end

if arg and arg[0]:match("seq{seq_id:02d}_nn.lua$") then
  demo()
end

return {{
  SequenceModel = nn.SequenceModel_Seq{seq_id},
  PATTERNS = PATTERNS,
  SEQUENCE_INFO = SEQUENCE_INFO,
  demo = demo
}}
'''
    
    return lua_code


def main():
    """Generate Lua neural network implementations for all sequences."""
    
    # Load pattern sequences
    with open('pattern_sequences.json', 'r') as f:
        data = json.load(f)
    
    sequences = data.get('sequences', [])
    
    # Create output directory
    output_dir = Path('implementations/lua')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Generating Lua neural network implementations for {len(sequences)} sequences...")
    
    generated_files = []
    
    for seq in sequences:
        seq_id = seq['id']
        filename = f"seq{seq_id:02d}_nn.lua"
        filepath = output_dir / filename
        
        print(f"  Generating {filename}...")
        
        # Generate Lua code
        lua_code = generate_sequence_nn_lua(seq, {})
        
        # Write to file
        with open(filepath, 'w') as f:
            f.write(lua_code)
        
        # Make executable
        os.chmod(filepath, 0o755)
        
        generated_files.append(filename)
    
    # Create README
    readme_content = f"""# Lua/Torch Neural Network Implementations

This directory contains Lua neural network implementations using the Torch framework
for all 36 pattern sequences in Christopher Alexander's "A Pattern Language."

## Requirements

- **Torch** (http://torch.ch)
- **nn** (https://github.com/torch/nn)
- **optim** (https://github.com/torch/optim)

## Installation

```bash
# Install Torch (follow instructions at http://torch.ch)
curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch
./install.sh

# The nn and optim packages are included by default
```

## Generated Files

This directory contains {len(generated_files)} generated Lua neural network modules:

"""
    
    for i, filename in enumerate(generated_files, 1):
        seq_num = int(filename.split('_')[0].replace('seq', ''))
        seq_data = sequences[seq_num - 1]
        readme_content += f"- `{filename}` - Sequence {seq_num}: {seq_data['heading']}\n"
    
    readme_content += """
## Usage

Each sequence module can be used independently:

```lua
-- Load a specific sequence module
local seq02 = require 'implementations.lua.seq02_nn'

-- Create model
local model = nn.SequenceModel_Seq2(253, 3, 256)

-- Run demo
seq02.demo()
```

## Module Structure

Each module contains:

1. **Pattern Data**: Pattern definitions for the sequence
2. **Adjacency Matrix**: Graph structure of pattern relationships
3. **TextEncoder**: Character-level LSTM for encoding text
4. **PatternEncoder**: Combines pattern ID, confidence, and text embeddings
5. **PatternGNN**: Graph neural network for relationship modeling
6. **SequenceModel**: Complete model with prediction heads

## API Reference

### SequenceModel Methods

- `encode_pattern(pattern)` - Encode a single pattern to vector
- `encode_all_patterns()` - Encode all patterns in sequence
- `forward(patterns)` - Complete forward pass
- `get_sequence_info()` - Get sequence metadata

## Cross-Reference

- Python implementation: `../patterns_001_007_nn.py`
- Original pattern data: `../../pattern_sequences.json`
- Pattern documentation: `../../markdown/sequences/`

## Architecture

The neural network architecture for each sequence includes:

```
Input: Pattern (id, confidence, problem text, solution text)
  ↓
Pattern Encoder:
  - Pattern ID Embedding (128-dim)
  - Confidence Embedding (32-dim)
  - Problem Text LSTM (256-dim)
  - Solution Text LSTM (256-dim)
  - Projection Layer → 256-dim embedding
  ↓
Graph Neural Network:
  - Message Passing (2 layers)
  - Neighborhood Aggregation
  - Non-linear Transformation
  ↓
Output Heads:
  - Next Pattern Prediction (253 classes)
  - Category Classification (3 classes)
  - Pattern Similarity (256-dim)
```

## Related Files

- `../patterns_001_007_nn.lua` - Reference implementation for patterns 1-7
- `../../generate_lua_sequence_nn.py` - Generator script for these files
- `../../.github/agents/nn.lua.md` - Agent definition for Lua neural net converter

## Notes

- These implementations use Torch7 (Lua), not PyTorch (Python)
- Each sequence has its own module namespace (e.g., `_Seq1`, `_Seq2`, etc.)
- Adjacency matrices represent sequential pattern connections
- Patterns can be extended with actual problem/solution text from markdown files

## License

Same as parent project (see ../../LICENSE)
"""
    
    readme_path = output_dir / 'README.md'
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    print(f"\n✅ Generated {len(generated_files)} Lua neural network implementations")
    print(f"✅ Created README.md")
    print(f"\nOutput directory: {output_dir.absolute()}")
    
    return len(generated_files)


if __name__ == '__main__':
    count = main()
    print(f"\nComplete! Generated {count} files in implementations/lua/")
