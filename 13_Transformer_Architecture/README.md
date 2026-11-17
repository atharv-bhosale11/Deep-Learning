# Transformer Architecture

## Overview

This section contains Python implementations and practical demonstrations of Transformer architecture concepts using NumPy.

The programs focus on understanding how Transformers process input sequences using attention mechanisms, positional encoding, and encoder architecture to generate contextual representations of words.

## Programs

| Sr. No. | Program Name | Description |
|---|---|---|
| 01 | Transformer Self-Attention | Implements manual self-attention with detailed mathematical calculations, including Query, Key, Value, attention scores, scaling, Softmax and final output. |
| 02 | Transformer Multi-Head Attention | Demonstrates multi-head attention using two attention heads, separate weight matrices, attention calculations and concatenation of head outputs. |
| 03 | Transformer Positional Encoding | Implements sinusoidal positional encoding using sine and cosine functions and combines it with word embeddings. |
| 04 | Transformer Encoder | Demonstrates a complete Transformer encoder workflow using positional encoding, self-attention, residual connections, layer normalization and feed-forward networks. |

## Key Concepts Covered

- Transformer Architecture Fundamentals
- Input Word Embeddings
- Self-Attention Mechanism
- Multi-Head Attention
- Query (Q), Key (K) and Value (V) Matrices
- Weight Matrices (Wq, Wk, Wv)
- Attention Score Calculation
- Matrix Multiplication
- Scaled Dot-Product Attention
- Softmax Activation
- Attention Weight Calculation
- Sinusoidal Positional Encoding
- Sine and Cosine Functions
- Contextual Word Representations
- Multiple Attention Heads
- Concatenation of Attention Head Outputs
- Residual Connections
- Layer Normalization
- Feed-Forward Neural Networks
- ReLU Activation
- Transformer Encoder Architecture

## Technologies Used

- Python
- NumPy

## Libraries

```python id="q7k4ma"
import numpy as np
```


## Learning Objectives

- Understand the fundamentals of Transformer architecture.
- Learn how Self-Attention processes input sequences.
- Understand Query, Key and Value representations.
- Perform manual attention score calculations.
- Understand scaled dot-product attention.
- Learn how Softmax generates attention probabilities.
- Understand how positional encoding provides word position information.
- Explore how multiple attention heads process information.
- Understand residual connections and layer normalization.
- Learn how feed-forward networks work inside Transformer encoders.
- Implement Transformer components using NumPy.

## Author

**Atharv Bhosale**
