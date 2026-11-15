# Recurrent Neural Networks (RNN)

## Overview

This section contains Python implementations and practical examples of Recurrent Neural Networks (RNNs) using TensorFlow and Keras.

The programs demonstrate how sequential data is processed, how text is converted into numerical representations, and how RNNs use hidden states to retain information from previous time steps.

## Programs

| Sr. No. | Program Name | Description |
|---|---|---|
| 01 | RNN Character Prediction | Character prediction using SimpleRNN. |
| 02 | RNN Sentiment Analysis | Sentiment analysis using SimpleRNN and word embeddings. |
| 03 | RNN Sequence Prediction | Understanding sequence prediction using RNN. |
| 04 | RNN Dataset Display | Displaying training datasets and sentiment labels. |
| 05 | RNN Tokenization | Splitting sentences into individual words. |
| 06 | RNN Vocabulary Creation | Creating vocabulary manually and assigning word indices. |
| 07 | RNN Keras Tokenization | Automatically creating vocabulary using Keras Tokenizer. |
| 08 | RNN Text to Sequences | Converting text sentences into numeric sequences. |
| 09 | RNN Use of Padding | Understanding why padding is required for equal-length sequences. |
| 10 | RNN Padding using Keras | Applying Keras padding to create equal-length RNN sequences. |
| 11 | RNN Vocabulary Size | Calculating vocabulary size required for the RNN embedding layer. |
| 12 | RNN Output Labels | Understanding binary classification output labels for sentiment analysis. |
| 13 | RNN Manual Embedding | Demonstrating manual word embedding using numeric vectors. |
| 14 | RNN Embedding using Keras | Demonstrating the Keras Embedding layer and word vector representations. |
| 15 | RNN Time Steps | Explaining RNN time steps using sentence processing. |
| 16 | RNN Hidden State | Demonstrating RNN hidden state as sequential memory. |
| 17 | RNN Manual Calculations | Implementing manual RNN hidden state calculation using tanh. |
| 18 | RNN Tanh Activation | Demonstrating the tanh activation function used in SimpleRNN. |
| 19 | RNN Sigmoid Activation | Demonstrating sigmoid activation for binary classification. |
| 20 | RNN Binary Crossentropy Loss | Implementing binary crossentropy loss calculation for RNN classification. |
| 21 | RNN Architecture | Building RNN architecture using Embedding, SimpleRNN and Dense layers. |
| 22 | RNN Model Training | Compiling and training an RNN model for sentiment classification. |
| 23 | RNN Prediction Flow | Demonstrating the complete RNN sentiment prediction process. |
| 24 | RNN Complete Application | Building a complete RNN sentiment analysis application using TensorFlow. |
| 25 | RNN Graphical Version | Demonstrating detailed mathematical calculations of RNN sentiment analysis with graphical visualizations. |

## Key Concepts Covered

- Recurrent Neural Network (RNN) fundamentals
- Sequential data processing
- Character prediction
- Sentiment analysis
- Text preprocessing and tokenization
- Vocabulary creation and word indexing
- Text-to-sequence conversion
- Sequence padding
- Word embeddings
- Embedding layers using Keras
- Binary classification output labels
- Vocabulary size calculation
- Time steps and hidden states
- Manual RNN hidden-state calculations
- Tanh and Sigmoid activation functions
- Binary Crossentropy loss
- RNN architecture design
- Model compilation and training
- Sentiment prediction workflow
- RNN forward propagation
- Matrix-vector multiplication
- Input-to-hidden and hidden-to-hidden weight matrices
- Dense layer mathematical calculations
- Graphical visualization of embedding matrices and hidden states
- Complete RNN sentiment analysis pipeline

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

## Libraries

```python
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
```

## Prerequisites

- Basic Python programming
- NumPy fundamentals
- Basic understanding of Neural Networks
- Basic understanding of Machine Learning

## Learning Objectives

- Understand how RNNs process sequential data.
- Learn how text data is converted into numerical sequences.
- Understand vocabulary creation and tokenization.
- Learn why padding is required for sequence processing.
- Understand word embeddings and embedding layers.
- Understand how hidden states maintain information across time steps.
- Explore activation functions used in RNN architectures.
- Understand binary classification and loss calculation.
- Perform manual RNN hidden-state calculations.
- Understand RNN architecture and model training.
- Learn the complete sentiment prediction workflow.
- Understand mathematical operations inside RNN layers.


## Author

**Atharv Bhosale**
