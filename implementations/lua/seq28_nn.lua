#!/usr/bin/env th
--[[
A Pattern Language - Sequence 28: Give the walls some depth
Torch Neural Network Implementation

Category: Buildings
Patterns: 197, 198, 199, 200, 201, 202, 203, 204

Sequence 28 focuses on give the walls some depth

Emergent Phenomenon: Walls with depth that provide storage, seating, and architectural richness

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

local SEQUENCE_INFO = {
  id = 28,
  heading = "Give the walls some depth",
  description = "Sequence 28 focuses on give the walls some depth",
  category = "Buildings",
  pattern_ids = {197, 198, 199, 200, 201, 202, 203, 204},
  emergent_phenomena = "Walls with depth that provide storage, seating, and architectural richness"
}

-- =============================================================================
-- PATTERN DATA
-- =============================================================================

local PATTERNS = {
  {
    id = 197,
    name = "PATTERN_197",
    problem = "Problem for pattern 197",
    solution = "Solution for pattern 197",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 198,
    name = "PATTERN_198",
    problem = "Problem for pattern 198",
    solution = "Solution for pattern 198",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 199,
    name = "PATTERN_199",
    problem = "Problem for pattern 199",
    solution = "Solution for pattern 199",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 200,
    name = "PATTERN_200",
    problem = "Problem for pattern 200",
    solution = "Solution for pattern 200",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 201,
    name = "PATTERN_201",
    problem = "Problem for pattern 201",
    solution = "Solution for pattern 201",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 202,
    name = "PATTERN_202",
    problem = "Problem for pattern 202",
    solution = "Solution for pattern 202",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 203,
    name = "PATTERN_203",
    problem = "Problem for pattern 203",
    solution = "Solution for pattern 203",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 204,
    name = "PATTERN_204",
    problem = "Problem for pattern 204",
    solution = "Solution for pattern 204",
    confidence = 2,
    preceding = {},
    following = {}
  }
}

-- Adjacency matrix for pattern relationships
local ADJACENCY_MATRIX = torch.FloatTensor({
  {0, 1, 0, 0, 0, 0, 0, 0},
  {0, 0, 1, 0, 0, 0, 0, 0},
  {0, 0, 0, 1, 0, 0, 0, 0},
  {0, 0, 0, 0, 1, 0, 0, 0},
  {0, 0, 0, 0, 0, 1, 0, 0},
  {0, 0, 0, 0, 0, 0, 1, 0},
  {0, 0, 0, 0, 0, 0, 0, 1},
  {0, 0, 0, 0, 0, 0, 0, 0}
})

-- =============================================================================
-- TEXT ENCODER
-- =============================================================================

local TextEncoder, parent = torch.class('nn.TextEncoder_Seq28', 'nn.Module')

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
  self.output = lstm_out[{{seq_len}}, {}, {}}]:view(batch_size, -1)
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

local PatternEncoder, parent = torch.class('nn.PatternEncoder_Seq28', 'nn.Module')

function PatternEncoder:__init(num_patterns, pattern_dim, text_hidden, output_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  pattern_dim = pattern_dim or 128
  text_hidden = text_hidden or 128
  output_dim = output_dim or 256
  
  self.pattern_embed = nn.LookupTable(num_patterns + 1, pattern_dim)
  self.confidence_embed = nn.LookupTable(3, 32)
  
  self.problem_encoder = nn.TextEncoder_Seq28(256, 64, text_hidden)
  self.solution_encoder = nn.TextEncoder_Seq28(256, 64, text_hidden)
  
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
  
  local combined = torch.cat({pat_emb, conf_emb, prob_emb, sol_emb}, 2)
  self.output = self.projection:forward(combined)
  return self.output
end

-- =============================================================================
-- GRAPH NEURAL NETWORK
-- =============================================================================

local PatternGNN, parent = torch.class('nn.PatternGNN_Seq28', 'nn.Module')

function PatternGNN:__init(input_dim, hidden_dim, num_layers)
  parent.__init(self)
  
  input_dim = input_dim or 256
  hidden_dim = hidden_dim or 256
  num_layers = num_layers or 2
  
  self.num_layers = num_layers
  self.layers = {}
  
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

local SequenceModel, parent = torch.class('nn.SequenceModel_Seq28', 'nn.Module')

function SequenceModel:__init(num_patterns, num_categories, embed_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  num_categories = num_categories or 3
  embed_dim = embed_dim or 256
  
  self.num_patterns = num_patterns
  self.embed_dim = embed_dim
  self.sequence_patterns = PATTERNS
  
  self.encoder = nn.PatternEncoder_Seq28(num_patterns, 128, 128, embed_dim)
  self.gnn = nn.PatternGNN_Seq28(embed_dim, embed_dim, 2)
  
  self.next_pattern_head = nn.Linear(embed_dim, num_patterns)
  self.category_head = nn.Linear(embed_dim, num_categories)
  self.similarity_head = nn.Linear(embed_dim, embed_dim)
end

function SequenceModel:encode_pattern(pattern)
  local pattern_id = torch.LongTensor({pattern.id})
  local confidence = torch.LongTensor({pattern.confidence + 1})
  local problem_ids = self.encoder.problem_encoder:text_to_ids(pattern.problem):view(1, -1)
  local solution_ids = self.encoder.solution_encoder:text_to_ids(pattern.solution):view(1, -1)
  
  return self.encoder:forward({pattern_id, confidence, problem_ids, solution_ids})
end

function SequenceModel:encode_all_patterns()
  local embeddings = {}
  for i = 1, #PATTERNS do
    local emb = self:encode_pattern(PATTERNS[i])
    table.insert(embeddings, emb)
  end
  return torch.cat(embeddings, 1)
end

function SequenceModel:forward(patterns)
  local embeddings = self:encode_all_patterns()
  local gnn_embeddings = self.gnn:forward({embeddings, ADJACENCY_MATRIX})
  local next_pattern_logits = self.next_pattern_head:forward(gnn_embeddings)
  local category_logits = self.category_head:forward(gnn_embeddings)
  
  return {
    embeddings = embeddings,
    gnn_embeddings = gnn_embeddings,
    next_pattern_logits = next_pattern_logits,
    category_logits = category_logits
  }
end

function SequenceModel:get_sequence_info()
  return SEQUENCE_INFO
end

-- =============================================================================
-- DEMO
-- =============================================================================

function demo()
  print(string.rep("=", 60))
  print(string.format("Sequence %d: %s", 28, "Give the walls some depth"))
  print(string.rep("=", 60))
  print(string.format("Category: %s", "Buildings"))
  print(string.format("Patterns: %s", "197, 198, 199, 200, 201, 202, 203, 204"))
  print(string.format("\nEmergent Phenomenon:\n%s", "Walls with depth that provide storage, seating, and architectural richness"))
  print(string.rep("=", 60))
  
  local model = nn.SequenceModel_Seq28(253, 3, 256)
  local params, _ = model:getParameters()
  print(string.format("\nModel created with %d parameters", params:nElement()))
  
  local embeddings = model:encode_all_patterns()
  print(string.format("\nPattern embeddings shape: %dx%d", 
    embeddings:size(1), embeddings:size(2)))
  
  local outputs = model:forward(PATTERNS)
  print(string.format("\nForward pass complete"))
  print(string.format("GNN embeddings: %dx%d", 
    outputs.gnn_embeddings:size(1), outputs.gnn_embeddings:size(2)))
  
  print("\n" .. string.rep("=", 60))
  print("Demo complete!")
  print(string.rep("=", 60))
end

if arg and arg[0]:match("seq28_nn.lua$") then
  demo()
end

return {
  SequenceModel = nn.SequenceModel_Seq28,
  PATTERNS = PATTERNS,
  SEQUENCE_INFO = SEQUENCE_INFO,
  demo = demo
}
