#!/usr/bin/env th
--[[
A Pattern Language - Patterns 1-7: Regional Policies
Torch Neural Network Implementation

This module implements a neural network for pattern representation,
similarity computation, and sequence prediction for APL patterns 1-7.

Sequence 2: Regional Policies
Emergent Phenomenon: Balanced distribution of settlements that
preserves countryside while supporting urban vitality

Requirements:
  - torch (http://torch.ch)
  - nn (https://github.com/torch/nn)
  - optim (https://github.com/torch/optim)
--]]

require 'torch'
require 'nn'
require 'optim'

-- =============================================================================
-- DATA STRUCTURES
-- =============================================================================

-- Pattern definitions for patterns 1-7
local PATTERNS_1_7 = {
  {
    id = 1,
    name = "INDEPENDENT REGIONS",
    problem = "Metropolitan regions will not come to balance until each one is small and autonomous enough to be an independent sphere of culture.",
    solution = "Work toward independent regions with 2-10 million people each, with own economy and self-government.",
    confidence = 2,  -- 0=uncertain, 1=progress, 2=invariant
    preceding = {},
    following = {2, 8}
  },
  {
    id = 2,
    name = "DISTRIBUTION OF TOWNS",
    problem = "Population weighted to cities ruins earth; too rural blocks civilization.",
    solution = "Logarithmic distribution: 1 town of 1M, 10 of 100K, 100 of 10K, 1000 of 1K, evenly spread.",
    confidence = 1,
    preceding = {1},
    following = {3, 4, 6}
  },
  {
    id = 3,
    name = "CITY COUNTRY FINGERS",
    problem = "Continuous sprawling urbanization destroys life, but city size is valuable.",
    solution = "Interlocking fingers: urban ≤1 mile wide, farmland ≥1 mile wide.",
    confidence = 2,
    preceding = {2},
    following = {4, 5, 8}
  },
  {
    id = 4,
    name = "AGRICULTURAL VALLEYS",
    problem = "Best farmland is best building land, but once destroyed, gone for centuries.",
    solution = "Preserve all valleys as farmland, parks, wilds. Build on hillsides.",
    confidence = 2,
    preceding = {1, 3},
    following = {7}
  },
  {
    id = 5,
    name = "LACE OF COUNTRY STREETS",
    problem = "The suburb is an obsolete and contradictory form of human settlement.",
    solution = "Country roads 1 mile apart, enclosing 1 sq mile farmland, homesteads one lot deep.",
    confidence = 1,
    preceding = {3},
    following = {7, 14, 37}
  },
  {
    id = 6,
    name = "COUNTRY TOWNS",
    problem = "Small country towns are dying as jobs move to cities.",
    solution = "Self-sufficient towns of ~7000 people, 10-15 miles from cities, with local industry.",
    confidence = 2,
    preceding = {2},
    following = {7, 12, 26}
  },
  {
    id = 7,
    name = "THE COUNTRYSIDE",
    problem = "Countryside is inaccessible to city dwellers; private ownership blocks access.",
    solution = "Make countryside public with footpaths, commons, access rights. Ownership as stewardship.",
    confidence = 1,
    preceding = {2, 3, 4, 5, 6},
    following = {37, 51}
  }
}

-- Adjacency matrix for pattern relationships (patterns 1-7)
local ADJACENCY_MATRIX = torch.FloatTensor({
  -- 1  2  3  4  5  6  7
  {0, 1, 0, 0, 0, 0, 0},  -- 1 -> 2
  {0, 0, 1, 1, 0, 1, 0},  -- 2 -> 3, 4, 6
  {0, 0, 0, 1, 1, 0, 0},  -- 3 -> 4, 5
  {0, 0, 0, 0, 0, 0, 1},  -- 4 -> 7
  {0, 0, 0, 0, 0, 0, 1},  -- 5 -> 7
  {0, 0, 0, 0, 0, 0, 1},  -- 6 -> 7
  {0, 0, 0, 0, 0, 0, 0}   -- 7 -> (outside range)
})

-- =============================================================================
-- TEXT ENCODER
-- =============================================================================

local TextEncoder, parent = torch.class('nn.TextEncoder', 'nn.Module')

function TextEncoder:__init(vocab_size, embed_dim, hidden_dim)
  parent.__init(self)
  
  vocab_size = vocab_size or 256
  embed_dim = embed_dim or 64
  hidden_dim = hidden_dim or 128
  
  self.embed = nn.LookupTable(vocab_size, embed_dim)
  self.lstm = nn.LSTM(embed_dim, hidden_dim, nil, true)  -- bidirectional
  self.output_dim = hidden_dim * 2
  
  -- Build sequential container
  self.net = nn.Sequential()
    :add(self.embed)
    :add(self.lstm)
end

function TextEncoder:updateOutput(input)
  -- input: (batch, seq_len) tensor of character IDs
  local lstm_out = self.net:forward(input)
  
  -- Get last hidden state (for both directions)
  -- lstm_out is (seq_len, batch, hidden_dim*2) for bidirectional
  local batch_size = input:size(1)
  local seq_len = input:size(2)
  
  -- Extract final hidden states
  self.output = lstm_out[{{seq_len}, {}, {}}]:view(batch_size, -1)
  return self.output
end

function TextEncoder:updateGradInput(input, gradOutput)
  -- Backprop through LSTM
  local seq_len = input:size(2)
  local grad_lstm = torch.zeros(seq_len, input:size(1), self.output_dim)
  grad_lstm[seq_len]:copy(gradOutput:view(input:size(1), self.output_dim))
  
  self.gradInput = self.net:backward(input, grad_lstm)
  return self.gradInput
end

function TextEncoder:text_to_ids(text, max_len)
  -- Convert text string to tensor of character IDs
  max_len = max_len or 200
  local ids = torch.zeros(max_len):long()
  
  for i = 1, math.min(#text, max_len) do
    ids[i] = string.byte(text:sub(i,i)) % 256 + 1  -- 1-indexed for Lua
  end
  
  return ids
end

-- =============================================================================
-- PATTERN ENCODER
-- =============================================================================

local PatternEncoder, parent = torch.class('nn.PatternEncoder', 'nn.Module')

function PatternEncoder:__init(num_patterns, pattern_dim, text_hidden, output_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  pattern_dim = pattern_dim or 128
  text_hidden = text_hidden or 128
  output_dim = output_dim or 256
  
  -- Embeddings
  self.pattern_embed = nn.LookupTable(num_patterns + 1, pattern_dim)
  self.confidence_embed = nn.LookupTable(3, 32)
  
  -- Text encoders
  self.problem_encoder = nn.TextEncoder(256, 64, text_hidden)
  self.solution_encoder = nn.TextEncoder(256, 64, text_hidden)
  
  -- Combine all features
  -- pattern_dim + 32 (confidence) + text_hidden*4 (problem + solution)
  local combined_dim = pattern_dim + 32 + text_hidden * 4
  
  -- Projection layers
  self.projection = nn.Sequential()
    :add(nn.Linear(combined_dim, output_dim))
    :add(nn.ReLU())
    :add(nn.Dropout(0.1))
    :add(nn.Linear(output_dim, output_dim))
  
  self.output_dim = output_dim
  
  -- Store components for manual forward pass
  self.modules = {
    self.pattern_embed,
    self.confidence_embed,
    self.problem_encoder,
    self.solution_encoder,
    self.projection
  }
end

function PatternEncoder:updateOutput(input)
  -- input is a table: {pattern_ids, confidence, problem_ids, solution_ids}
  local pattern_ids = input[1]
  local confidence = input[2]
  local problem_ids = input[3]
  local solution_ids = input[4]
  
  -- Get embeddings
  local pat_emb = self.pattern_embed:forward(pattern_ids)
  local conf_emb = self.confidence_embed:forward(confidence)
  local prob_emb = self.problem_encoder:forward(problem_ids)
  local sol_emb = self.solution_encoder:forward(solution_ids)
  
  -- Concatenate all features
  local combined = torch.cat({pat_emb, conf_emb, prob_emb, sol_emb}, 2)
  
  -- Project to output dimension
  self.output = self.projection:forward(combined)
  return self.output
end

function PatternEncoder:updateGradInput(input, gradOutput)
  -- Backward pass through projection
  local grad_combined = self.projection:backward(
    torch.cat({
      self.pattern_embed.output,
      self.confidence_embed.output,
      self.problem_encoder.output,
      self.solution_encoder.output
    }, 2),
    gradOutput
  )
  
  -- Split gradients
  local pat_dim = self.pattern_embed.weight:size(2)
  local conf_dim = self.confidence_embed.weight:size(2)
  local prob_dim = self.problem_encoder.output_dim
  local sol_dim = self.solution_encoder.output_dim
  
  local grad_pat = grad_combined[{{}, {1, pat_dim}}]
  local grad_conf = grad_combined[{{}, {pat_dim+1, pat_dim+conf_dim}}]
  local grad_prob = grad_combined[{{}, {pat_dim+conf_dim+1, pat_dim+conf_dim+prob_dim}}]
  local grad_sol = grad_combined[{{}, {pat_dim+conf_dim+prob_dim+1, -1}}]
  
  -- Backward through embeddings and encoders
  self.pattern_embed:backward(input[1], grad_pat)
  self.confidence_embed:backward(input[2], grad_conf)
  self.problem_encoder:backward(input[3], grad_prob)
  self.solution_encoder:backward(input[4], grad_sol)
  
  return self.gradInput
end

-- =============================================================================
-- GRAPH NEURAL NETWORK
-- =============================================================================

local PatternGNN, parent = torch.class('nn.PatternGNN', 'nn.Module')

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
  
  -- Store all modules
  self.modules = self.layers
  table.insert(self.modules, self.output_layer)
end

function PatternGNN:updateOutput(input)
  -- input is a table: {node_features, adjacency}
  local node_features = input[1]
  local adjacency = input[2]
  
  -- Normalize adjacency (add self-loops)
  local num_nodes = adjacency:size(1)
  local adj = adjacency + torch.eye(num_nodes)
  local degree = adj:sum(2):clamp(1, math.huge)
  local adj_norm = adj:cdiv(degree:expandAs(adj))
  
  -- Message passing
  local h = node_features
  for i = 1, self.num_layers do
    -- Aggregate neighbor features
    h = torch.mm(adj_norm, h)
    h = self.layers[i]:forward(h)
  end
  
  self.output = self.output_layer:forward(h)
  return self.output
end

function PatternGNN:updateGradInput(input, gradOutput)
  -- Simplified backward pass
  local grad = self.output_layer:backward(self.output, gradOutput)
  
  for i = self.num_layers, 1, -1 do
    grad = self.layers[i]:backward(self.layers[i].output, grad)
  end
  
  self.gradInput = grad
  return self.gradInput
end

-- =============================================================================
-- PATTERN LANGUAGE MODEL
-- =============================================================================

local PatternLanguageModel, parent = torch.class('nn.PatternLanguageModel', 'nn.Module')

function PatternLanguageModel:__init(num_patterns, num_categories, embed_dim)
  parent.__init(self)
  
  num_patterns = num_patterns or 253
  num_categories = num_categories or 3
  embed_dim = embed_dim or 256
  
  self.num_patterns = num_patterns
  self.embed_dim = embed_dim
  
  -- Pattern encoder
  self.encoder = nn.PatternEncoder(num_patterns, 128, 128, embed_dim)
  
  -- Graph neural network
  self.gnn = nn.PatternGNN(embed_dim, embed_dim, 2)
  
  -- Output heads
  self.next_pattern_head = nn.Linear(embed_dim, num_patterns)
  self.category_head = nn.Linear(embed_dim, num_categories)
  self.similarity_head = nn.Linear(embed_dim, embed_dim)
  
  self.modules = {
    self.encoder,
    self.gnn,
    self.next_pattern_head,
    self.category_head,
    self.similarity_head
  }
end

function PatternLanguageModel:encode_pattern(pattern)
  -- Encode a single pattern to a vector
  local pattern_id = torch.LongTensor({pattern.id})
  local confidence = torch.LongTensor({pattern.confidence + 1})  -- 1-indexed
  local problem_ids = self.encoder.problem_encoder:text_to_ids(pattern.problem):view(1, -1)
  local solution_ids = self.encoder.solution_encoder:text_to_ids(pattern.solution):view(1, -1)
  
  return self.encoder:forward({pattern_id, confidence, problem_ids, solution_ids})
end

function PatternLanguageModel:encode_patterns_1_7()
  -- Encode all patterns 1-7 to vectors
  local embeddings = {}
  
  for i = 1, 7 do
    local emb = self:encode_pattern(PATTERNS_1_7[i])
    table.insert(embeddings, emb)
  end
  
  return torch.cat(embeddings, 1)  -- (7, embed_dim)
end

function PatternLanguageModel:forward(patterns)
  -- Forward pass for patterns 1-7
  -- Returns table with embeddings, gnn_embeddings, next_pattern_logits, category_logits
  
  local embeddings = self:encode_patterns_1_7()
  
  -- Apply GNN
  local gnn_embeddings = self.gnn:forward({embeddings, ADJACENCY_MATRIX})
  
  -- Predictions
  local next_pattern_logits = self.next_pattern_head:forward(gnn_embeddings)
  local category_logits = self.category_head:forward(gnn_embeddings)
  
  return {
    embeddings = embeddings,
    gnn_embeddings = gnn_embeddings,
    next_pattern_logits = next_pattern_logits,
    category_logits = category_logits
  }
end

function PatternLanguageModel:compute_similarity(emb1, emb2)
  -- Compute cosine similarity between pattern embeddings
  local emb1_proj = self.similarity_head:forward(emb1)
  local emb2_proj = self.similarity_head:forward(emb2)
  
  -- Normalize and compute cosine similarity
  local norm1 = emb1_proj:norm()
  local norm2 = emb2_proj:norm()
  local similarity = torch.dot(emb1_proj, emb2_proj) / (norm1 * norm2)
  
  return similarity
end

function PatternLanguageModel:predict_next_patterns(pattern_id, top_k)
  -- Predict most likely next patterns given current pattern
  top_k = top_k or 3
  
  local embeddings = self:encode_patterns_1_7()
  local gnn_embeddings = self.gnn:forward({embeddings, ADJACENCY_MATRIX})
  
  local idx = pattern_id  -- 1-indexed already
  local logits = self.next_pattern_head:forward(gnn_embeddings[idx]:view(1, -1))
  local probs = nn.SoftMax():forward(logits):squeeze()
  
  -- Get top-k predictions
  local sorted_probs, sorted_indices = torch.sort(probs, true)
  
  local predictions = {}
  for i = 1, math.min(top_k, sorted_probs:size(1)) do
    table.insert(predictions, {
      pattern = sorted_indices[i],
      prob = sorted_probs[i]
    })
  end
  
  return predictions
end

-- =============================================================================
-- TRAINING UTILITIES
-- =============================================================================

function create_training_batch(patterns)
  -- Create a training batch from pattern data
  local pattern_ids = torch.LongTensor(#patterns)
  local confidence = torch.LongTensor(#patterns)
  local next_pattern_labels = torch.LongTensor(#patterns)
  local category_labels = torch.LongTensor(#patterns):zero()
  
  local encoder = nn.PatternEncoder()
  local problem_ids_list = {}
  local solution_ids_list = {}
  
  for i, pattern in ipairs(patterns) do
    pattern_ids[i] = pattern.id
    confidence[i] = pattern.confidence + 1  -- 1-indexed
    
    -- Next pattern label
    if #pattern.following > 0 then
      next_pattern_labels[i] = pattern.following[1]
    else
      next_pattern_labels[i] = 0
    end
    
    -- Text IDs
    table.insert(problem_ids_list, encoder.problem_encoder:text_to_ids(pattern.problem))
    table.insert(solution_ids_list, encoder.solution_encoder:text_to_ids(pattern.solution))
  end
  
  local problem_ids = torch.cat(problem_ids_list, 1):view(#patterns, -1)
  local solution_ids = torch.cat(solution_ids_list, 1):view(#patterns, -1)
  
  return {
    pattern_ids = pattern_ids,
    confidence = confidence,
    problem_ids = problem_ids,
    solution_ids = solution_ids,
    next_pattern_labels = next_pattern_labels,
    category_labels = category_labels
  }
end

function train_step(model, criterion_next, criterion_cat, patterns, config)
  -- Single training step
  config = config or {}
  
  -- Forward pass
  local outputs = model:forward(patterns)
  
  -- Create batch
  local batch = create_training_batch(patterns)
  
  -- Compute losses
  local next_pattern_loss = criterion_next:forward(
    outputs.next_pattern_logits,
    batch.next_pattern_labels
  )
  
  local category_loss = criterion_cat:forward(
    outputs.category_logits,
    batch.category_labels
  )
  
  local total_loss = next_pattern_loss + category_loss
  
  -- Backward pass
  local grad_next = criterion_next:backward(
    outputs.next_pattern_logits,
    batch.next_pattern_labels
  )
  
  local grad_cat = criterion_cat:backward(
    outputs.category_logits,
    batch.category_labels
  )
  
  -- Simple gradient accumulation (would need proper backward through model)
  -- In a full implementation, would call model:backward(patterns, {grad_next, grad_cat})
  
  return {
    total_loss = total_loss,
    next_pattern_loss = next_pattern_loss,
    category_loss = category_loss
  }
end

-- =============================================================================
-- DEMO
-- =============================================================================

function demo()
  print(string.rep("=", 60))
  print("A Pattern Language - Patterns 1-7 Neural Network Demo")
  print(string.rep("=", 60))
  
  -- Create model
  local model = nn.PatternLanguageModel(253, 3, 256)
  
  -- Count parameters
  local params, _ = model:getParameters()
  print(string.format("\nModel created with %d parameters", params:nElement()))
  
  -- Encode patterns
  print("\n--- Pattern Embeddings ---")
  local embeddings = model:encode_patterns_1_7()
  print(string.format("Embeddings shape: %dx%d", embeddings:size(1), embeddings:size(2)))
  
  -- Compute similarity matrix
  print("\n--- Pattern Similarity Matrix ---")
  print("    " .. table.concat({"P1", "P2", "P3", "P4", "P5", "P6", "P7"}, "  "))
  
  for i = 1, 7 do
    local row = {}
    for j = 1, 7 do
      local sim = model:compute_similarity(embeddings[i], embeddings[j])
      table.insert(row, string.format("%.2f", sim))
    end
    print(string.format("P%d: %s", i, table.concat(row, " ")))
  end
  
  -- Forward pass
  print("\n--- Forward Pass ---")
  local outputs = model:forward(PATTERNS_1_7)
  print(string.format("GNN embeddings shape: %dx%d",
    outputs.gnn_embeddings:size(1),
    outputs.gnn_embeddings:size(2)))
  print(string.format("Next pattern logits shape: %dx%d",
    outputs.next_pattern_logits:size(1),
    outputs.next_pattern_logits:size(2)))
  print(string.format("Category logits shape: %dx%d",
    outputs.category_logits:size(1),
    outputs.category_logits:size(2)))
  
  -- Predict next patterns
  print("\n--- Next Pattern Predictions ---")
  for i = 1, 7 do
    local predictions = model:predict_next_patterns(i, 3)
    local pattern_name = PATTERNS_1_7[i].name:sub(1, 20)
    local pred_strs = {}
    for _, pred in ipairs(predictions) do
      table.insert(pred_strs, string.format("P%d(%.2f)", pred.pattern, pred.prob))
    end
    print(string.format("P%d (%s...): %s", i, pattern_name, table.concat(pred_strs, ", ")))
  end
  
  -- Training demo
  print("\n--- Training Step ---")
  local criterion_next = nn.CrossEntropyCriterion()
  local criterion_cat = nn.CrossEntropyCriterion()
  local losses = train_step(model, criterion_next, criterion_cat, PATTERNS_1_7, {})
  print(string.format("Total Loss: %.4f", losses.total_loss))
  print(string.format("Next Pattern Loss: %.4f", losses.next_pattern_loss))
  print(string.format("Category Loss: %.4f", losses.category_loss))
  
  print("\n" .. string.rep("=", 60))
  print("Demo complete!")
  print(string.rep("=", 60))
end

-- Run demo if executed directly
if arg and arg[0]:match("patterns_001_007_nn.lua$") then
  demo()
end

-- Export module
return {
  TextEncoder = nn.TextEncoder,
  PatternEncoder = nn.PatternEncoder,
  PatternGNN = nn.PatternGNN,
  PatternLanguageModel = nn.PatternLanguageModel,
  PATTERNS_1_7 = PATTERNS_1_7,
  ADJACENCY_MATRIX = ADJACENCY_MATRIX,
  demo = demo
}
