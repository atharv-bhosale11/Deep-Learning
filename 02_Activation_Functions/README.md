# Activation Functions

## 📌 Overview

This folder contains Python implementations of commonly used activation functions in Artificial Neural Networks (ANN). The programs demonstrate how activation functions transform a neuron's weighted sum into an output.

## 📂 Programs

| Sr. No. | Program                            | Description                                                    | Concepts Covered                                        |
| ------- | ---------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------- |
| 1       | `01_Activation_Relu.py`            | Implements ReLU activation with a single artificial neuron.    | ReLU, Forward Propagation, Visualization                |
| 2       | `02_Activation_Sigmoid.py`         | Implements Sigmoid activation with a single artificial neuron. | Sigmoid, Forward Propagation, Visualization             |
| 3       | `03_Activation_Sigmoid_vs_ReLU.py` | Compares Sigmoid and ReLU activation functions.                | Activation Function Comparison, Graphical Visualization |

## 🛠️ Technologies Used

* **Python** – Programming language
* **NumPy** – Numerical computations
* **Matplotlib** – Data visualization

## 🧠 Key Concepts

### 1. ReLU (Rectified Linear Unit)

ReLU returns the input if it is positive; otherwise, it returns zero.

Formula:

`ReLU(x) = max(0, x)`

### 2. Sigmoid Activation Function

Sigmoid transforms input values into a range between 0 and 1.

Formula:

`Sigmoid(x) = 1 / (1 + e^(-x))`

### 3. Activation Function Comparison

Compares the output behavior of ReLU and Sigmoid using graphical representations.

## ▶️ How to Run

**Step 1:** Install the required libraries.

```bash
pip install numpy matplotlib
```

**Step 2:** Run any Python program.

```bash
python 01_Activation_Relu.py
```

## 🎯 Learning Objectives

* Understand the importance of activation functions in neural networks.
* Implement ReLU and Sigmoid using Python.
* Understand how activation functions transform weighted sums.
* Compare activation functions through graphical visualization.

## 👨‍💻 Author

**Atharv Bhosale**

Part of the **Deep-Learning** GitHub repository.

