# Neural Network Fundamentals

## 📌 Overview

This folder contains Python implementations of fundamental Artificial Neural Network (ANN) concepts. The programs demonstrate how an artificial neuron processes inputs using weights, bias, and activation functions.

## 📂 Programs

| Sr. No. | Program                   | Description                            | Concepts Covered                                     |
| ------- | ------------------------- | -------------------------------------- | ---------------------------------------------------- |
| 1       | `01_ANN_Single_Neuron.py` | Implements a single artificial neuron. | Inputs, Weights, Bias, Weighted Sum, ReLU Activation |

## 🛠️ Technologies Used

* **Python** — Programming language
* **NumPy** — Numerical computations

## 🧠 Key Concepts

### 1. Artificial Neuron

An artificial neuron processes input values and produces an output.

### 2. Weights

Weights determine the contribution of each input to the neuron's output.

### 3. Bias

Bias is an additional parameter added to the weighted sum.

### 4. Weighted Sum

The neuron calculates the weighted sum using the formula:

`Z = (x₁ × w₁) + (x₂ × w₂) + ... + (xₙ × wₙ) + b`

### 5. ReLU Activation Function

The Rectified Linear Unit (ReLU) activation function is defined as:

`ReLU(Z) = max(0, Z)`

It returns the input when positive and zero otherwise.

## ▶️ How to Run

**Step 1:** Install NumPy.

```bash
pip install numpy
```

**Step 2:** Run the Python program.

```bash
python 01_ANN_Single_Neuron.py
```

## 🎯 Learning Objectives

* Understand the basic structure of an artificial neuron.
* Learn how inputs, weights, and bias work together.
* Calculate a neuron's weighted sum.
* Understand how ReLU transforms the weighted sum into an output. 

## 👨‍💻 Author

**Atharv Bhosale**

