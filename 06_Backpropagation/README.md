# 06. Backpropagation

This folder contains Python implementations demonstrating the Backpropagation algorithm in Artificial Neural Networks (ANNs).

Backpropagation is an important algorithm used to train neural networks. It calculates gradients by propagating errors backward through the network and helps update weights and biases using Gradient Descent.

## 📂 Programs

| Sr. No. | Program                                    | Description                                                                                                                               |
| ------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 01      | `01_Gradient_Backpropagation.py`           | Demonstrates ANN forward propagation, loss calculation, backpropagation, gradient calculation, and weight updates using Gradient Descent. |
| 02      | `02_Gradient_Backpropagation_Graphical.py` | Demonstrates the ANN training process through animated visualization using Matplotlib.                                                    |

## 📚 Concepts Covered

### 1. Forward Propagation

* Calculates the weighted sum using input values, weights, and bias.
* Applies the Sigmoid activation function.
* Produces the predicted output.

### 2. Loss Calculation

* Calculates prediction error using Mean Squared Error.
* Measures the difference between actual and predicted output.

### 3. Backpropagation

* Calculates gradients using the Chain Rule.
* Computes gradients with respect to weights and bias.
* Uses the derivative of the Sigmoid activation function.

### 4. Gradient Descent

* Updates weights and bias using calculated gradients.
* Uses a learning rate to control the update size.
* Repeats the training process over multiple epochs.

### 5. Animated Visualization

* Displays input neurons, weights, bias, and output.
* Visualizes forward propagation and training progress.
* Shows loss values and gradients during training.
* Animates the ANN learning process across epochs.

## 🛠️ Technologies Used

* **Python** – Implementation of backpropagation.
* **Math** – Mathematical calculations and activation functions.
* **Matplotlib** – Graphical visualization.
* **Matplotlib Animation** – Animated representation of ANN training.

## 📦 Prerequisites

Install the required libraries:

```bash
pip install matplotlib
```

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the directory:

```bash
cd Deep-Learning/06_Backpropagation
```

Run the programs:

```bash
python 01_Gradient_Backpropagation.py
python 02_Gradient_Backpropagation_Graphical.py
```

## 🎯 Learning Objectives

* Understand the Backpropagation algorithm.
* Learn how gradients are calculated using the Chain Rule.
* Understand the relationship between forward propagation and backpropagation.
* Calculate gradients for weights and bias.
* Understand how Gradient Descent updates network parameters.
* Visualize the ANN training process through animation.

## 👨‍💻 Author

**Atharv Bhosale**

Computer Engineering | Python | Machine Learning | Deep Learning

---

⭐ This folder is part of my **Deep Learning** repository, documenting my learning and implementation of Artificial Neural Network training algorithms.

