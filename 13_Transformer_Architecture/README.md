# Transformer Architecture

## Overview

This section contains concept-wise Python implementations and practical applications of Transformer architecture.

The programs focus on understanding how Transformers process sequential data using attention mechanisms, positional encoding, encoder and decoder architectures, and pre-trained Transformer models. They also demonstrate practical applications such as sentiment classification, neural machine translation and autoregressive text generation.

## Programs

| Sr. No. | Program Name | Description |
|---|---|---|
| 01 | Transformer Self-Attention | Implements manual self-attention with detailed mathematical calculations, including Query, Key, Value, attention scores, scaling, Softmax and final output. |
| 02 | Transformer Multi-Head Attention | Demonstrates multi-head attention using multiple attention heads, separate weight matrices, attention calculations and concatenation of head outputs. |
| 03 | Transformer Positional Encoding | Implements sinusoidal positional encoding using sine and cosine functions and combines it with word embeddings. |
| 04 | Transformer Encoder | Demonstrates the Transformer encoder using self-attention, residual connections, layer normalization and feed-forward networks. |
| 05 | Transformer Decoder | Implements the Transformer decoder and demonstrates its architecture and components for sequence generation. |
| 06 | Transformer Sentiment Classification (Encoder-Only) | Implements sentiment classification using an encoder-only Transformer architecture to process text and predict sentiment. |
| 07 | Transformer Neural Machine Translation (Encoder-Decoder) | Implements an encoder-decoder Transformer for English-to-Marathi neural machine translation. |
| 08 | Generative Pre-trained Transformer (Decoder-Only) | Implements a GPT-style decoder-only Transformer with masked self-attention, next-token prediction and autoregressive text generation. |

## Key Concepts Covered

- Transformer Architecture Fundamentals
- Input Word Embeddings
- Tokenization and Text Vectorization
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
- Transformer Encoder Architecture
- Transformer Decoder Architecture
- Masked Self-Attention
- Causal Attention Masking
- Residual Connections
- Layer Normalization
- Feed-Forward Neural Networks
- ReLU Activation
- Encoder-Only Transformers
- Encoder-Decoder Transformers
- Decoder-Only Transformers
- Neural Machine Translation
- English-to-Marathi Translation
- Sentiment Classification
- GPT Architecture Fundamentals
- Next-Token Prediction
- Autoregressive Text Generation

## Technologies Used

- Python
- NumPy
- TensorFlow
- Keras

## Libraries

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
```

## Prerequisites

- Basic Python Programming
- NumPy Fundamentals
- TensorFlow and Keras Fundamentals
- Matrix Operations and Linear Algebra
- Basic Understanding of Neural Networks
- Basic Understanding of Machine Learning
- Basic Understanding of Deep Learning
- Understanding of Attention Mechanisms

## Learning Objectives

- Understand the fundamentals of Transformer architecture.
- Learn how Self-Attention processes input sequences.
- Understand Query, Key and Value representations.
- Perform manual attention score calculations.
- Understand scaled dot-product attention.
- Learn how Softmax generates attention probabilities.
- Understand how positional encoding provides positional information to word embeddings.
- Explore how multiple attention heads process information.
- Understand Transformer encoder and decoder architectures.
- Learn masked self-attention and causal masking.
- Understand residual connections and layer normalization.

## Author

**Atharv Bhosale**
