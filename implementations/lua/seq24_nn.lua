#!/usr/bin/env th
--[[
A Pattern Language - Sequence 24: Knit the inside of the building to the outside
Torch Neural Network Implementation

Category: Buildings
Patterns: 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182

Sequence 24 focuses on knit the inside of the building to the outside

Emergent Phenomenon: Buildings that open to and engage with their surroundings rather than turning inward

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
  id = 24,
  heading = "Knit the inside of the building to the outside",
  description = "Sequence 24 focuses on knit the inside of the building to the outside",
  category = "Buildings",
  pattern_ids = {172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182},
  emergent_phenomena = "Buildings that open to and engage with their surroundings rather than turning inward"
}

-- =============================================================================
-- PATTERN DATA
-- =============================================================================

local PATTERNS = {
  {
    id = 172,
    name = "PATTERN_172",
    problem = "Problem for pattern 172",
    solution = "Solution for pattern 172",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 173,
    name = "PATTERN_173",
    problem = "Problem for pattern 173",
    solution = "Solution for pattern 173",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 174,
    name = "PATTERN_174",
    problem = "Problem for pattern 174",
    solution = "Solution for pattern 174",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 175,
    name = "PATTERN_175",
    problem = "Problem for pattern 175",
    solution = "Solution for pattern 175",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 176,
    name = "PATTERN_176",
    problem = "Problem for pattern 176",
    solution = "Solution for pattern 176",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 177,
    name = "PATTERN_177",
    problem = "Problem for pattern 177",
    solution = "Solution for pattern 177",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 178,
    name = "PATTERN_178",
    problem = "Problem for pattern 178",
    solution = "Solution for pattern 178",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 179,
    name = "PATTERN_179",
    problem = "Problem for pattern 179",
    solution = "Solution for pattern 179",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 180,
    name = "PATTERN_180",
    problem = "Problem for pattern 180",
    solution = "Solution for pattern 180",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 181,
    name = "PATTERN_181",
    problem = "Problem for pattern 181",
    solution = "Solution for pattern 181",
    confidence = 2,
    preceding = {},
    following = {}
  },
  {
    id = 182,
    name = "PATTERN_182",
    problem = "Problem for pattern 182",
    solution = "Solution for pattern 182",
    confidence = 2,
    preceding = {},
    following = {}
  }
}

-- Adjacency matrix for pattern relationships
local ADJACENCY_MATRIX = torch.FloatTensor({
  {0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
})

-- =============================================================================
-- TEXT ENCODER
-- =============================================================================

local TextEncoder, parent = torch.class('nn.TextEncoder_Seq24', 'nn.Module')

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

local PatternEncoder, parent = torch.class('nn.PatternEncoder_Seq24', 'nn.Module')

function PatternEncoder:__init(num_patterns, pattern_dim, text_hidden, output_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  pattern_dim = pattern_dim or 128
  text_hidden = text_hidden or 128
  output_dim = output_dim or 256
  
  self.pattern_embed = nn.LookupTable(num_patterns + 1, pattern_dim)
  self.confidence_embed = nn.LookupTable(3, 32)
  
  self.problem_encoder = nn.TextEncoder_Seq24(256, 64, text_hidden)
  self.solution_encoder = nn.TextEncoder_Seq24(256, 64, text_hidden)
  
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

local PatternGNN, parent = torch.class('nn.PatternGNN_Seq24', 'nn.Module')

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

local SequenceModel, parent = torch.class('nn.SequenceModel_Seq24', 'nn.Module')

function SequenceModel:__init(num_patterns, num_categories, embed_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  num_categories = num_categories or 3
  embed_dim = embed_dim or 256
  
  self.num_patterns = num_patterns
  self.embed_dim = embed_dim
  self.sequence_patterns = PATTERNS
  
  self.encoder = nn.PatternEncoder_Seq24(num_patterns, 128, 128, embed_dim)
  self.gnn = nn.PatternGNN_Seq24(embed_dim, embed_dim, 2)
  
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
  print(string.format("Sequence %d: %s", 24, "Knit the inside of the building to the outside"))
  print(string.rep("=", 60))
  print(string.format("Category: %s", "Buildings"))
  print(string.format("Patterns: %s", "172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182"))
  print(string.format("\nEmergent Phenomenon:\n%s", "Buildings that open to and engage with their surroundings rather than turning inward"))
  print(string.rep("=", 60))
  
  local model = nn.SequenceModel_Seq24(253, 3, 256)
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

if arg and arg[0]:match("seq24_nn.lua$") then
  demo()
end

return {
  SequenceModel = nn.SequenceModel_Seq24,
  PATTERNS = PATTERNS,
  SEQUENCE_INFO = SEQUENCE_INFO,
  demo = demo
}
