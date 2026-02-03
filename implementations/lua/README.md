# Lua/Torch Neural Network Implementations

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

This directory contains 36 generated Lua neural network modules:

- `seq01_nn.lua` - Sequence 1: Regions instead of countries
- `seq02_nn.lua` - Sequence 2: Regional policies
- `seq03_nn.lua` - Sequence 3: Major structures which define the city
- `seq04_nn.lua` - Sequence 4: Communities and neighborhoods
- `seq05_nn.lua` - Sequence 5: Community networks
- `seq06_nn.lua` - Sequence 6: Character of local environments
- `seq07_nn.lua` - Sequence 7: Local centers
- `seq08_nn.lua` - Sequence 8: Housing
- `seq09_nn.lua` - Sequence 9: Work
- `seq10_nn.lua` - Sequence 10: Local road and path network
- `seq11_nn.lua` - Sequence 11: Public open land
- `seq12_nn.lua` - Sequence 12: Local common land
- `seq13_nn.lua` - Sequence 13: Transformation of the family
- `seq14_nn.lua` - Sequence 14: Transformation of work and learning
- `seq15_nn.lua` - Sequence 15: Transformation of local shops and gathering places
- `seq16_nn.lua` - Sequence 16: The overall arrangement of a group of buildings
- `seq17_nn.lua` - Sequence 17: The position of individual buildings
- `seq18_nn.lua` - Sequence 18: Entrances, gardens, courtyards, roofs and terraces
- `seq19_nn.lua` - Sequence 19: Paths and squares
- `seq20_nn.lua` - Sequence 20: Gradients and connection of space
- `seq21_nn.lua` - Sequence 21: The most important areas and rooms (in a house)
- `seq22_nn.lua` - Sequence 22: The most important areas and rooms (in offices, workshops and public buildings)
- `seq23_nn.lua` - Sequence 23: Outbuildings and access to the street and gardens
- `seq24_nn.lua` - Sequence 24: Knit the inside of the building to the outside
- `seq25_nn.lua` - Sequence 25: Arrange the gardens, and the places in the gardens
- `seq26_nn.lua` - Sequence 26: Inside, attach necessary minor rooms and alcoves
- `seq27_nn.lua` - Sequence 27: Fine tune the shape and size of rooms and alcoves
- `seq28_nn.lua` - Sequence 28: Give the walls some depth
- `seq29_nn.lua` - Sequence 29: Let the structure grow directly from your plans and your conception of the buildings
- `seq30_nn.lua` - Sequence 30: Work out the complete structural layout
- `seq31_nn.lua` - Sequence 31: Mark the column locations and erect the main frame
- `seq32_nn.lua` - Sequence 32: Fix the exact positions for openings and frame them
- `seq33_nn.lua` - Sequence 33: Put in the following subsidiary patterns
- `seq34_nn.lua` - Sequence 34: Put in the surfaces and indoor details
- `seq35_nn.lua` - Sequence 35: Build outdoor details
- `seq36_nn.lua` - Sequence 36: Complete the building

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
