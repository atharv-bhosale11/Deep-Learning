# 05. Loss Functions

This folder contains Python implementations of fundamental Loss Functions used in Machine Learning and Artificial Neural Networks.

Loss Functions measure the difference between actual values and predicted values. They help evaluate how accurately a model performs by calculating its prediction error.

## 📂 Programs

| Sr. No. | Program                                   | Description                                                                                                                |
| ------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 01      | `01_LossFunction_MSE.py`                  | Implements Mean Squared Error (MSE) to calculate the average of squared differences between actual and predicted values.   |
| 02      | `02_LossFunction_MAE.py`                  | Implements Mean Absolute Error (MAE) to calculate the average of absolute differences between actual and predicted values. |
| 03      | `03_LossFunction_Binary_Cross_Entropy.py` | Implements Binary Cross Entropy (BCE) to calculate prediction error for binary classification problems.                    |

## 📚 Concepts Covered

### 1. Mean Squared Error (MSE)

* Calculates the average of squared differences between actual and predicted values.
* Gives higher importance to larger prediction errors.
* Commonly used in regression problems.

**Formula:**

MSE = (1/n) × Σ(yᵢ - ŷᵢ)²

### 2. Mean Absolute Error (MAE)

* Calculates the average of absolute differences between actual and predicted values.
* Treats errors proportionally to their magnitude.
* Commonly used in regression problems.

**Formula:**

MAE = (1/n) × Σ|yᵢ - ŷᵢ|

### 3. Binary Cross Entropy (BCE)

* Measures the difference between actual binary labels and predicted probabilities.
* Commonly used in binary classification problems.
* Uses logarithmic loss to penalize incorrect predictions.
* Clips predicted probabilities to avoid calculating the logarithm of zero.

**Formula:**

BCE = -(1/n) × Σ[yᵢ log(pᵢ) + (1-yᵢ) log(1-pᵢ)]

## 🛠️ Technologies Used

* **Python** – Implementation of loss functions.
* **Math Module** – Mathematical logarithmic calculations.
* **Built-in Functions** – Used for calculations and error handling.

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the directory:

```bash
cd Deep-Learning/05_Loss_Functions
```

Run the programs:

```bash
python 01_LossFunction_MSE.py
python 02_LossFunction_MAE.py
python 03_LossFunction_Binary_Cross_Entropy.py
```

## 🎯 Learning Objectives

* Understand the purpose of loss functions.
* Calculate prediction errors using MSE and MAE.
* Understand Binary Cross Entropy for binary classification.
* Understand the difference between regression and classification loss functions.
* Learn how loss functions help evaluate machine learning models.

## 👨‍💻 Author

**Atharv Bhosale**
 

⭐ This folder is part of my **Deep Learning** repository, documenting my learning and implementation of fundamental neural network concepts.
