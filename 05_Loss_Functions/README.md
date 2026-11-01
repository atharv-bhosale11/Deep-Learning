# 05. Loss Functions

This folder contains Python implementations of fundamental Loss Functions used in Machine Learning and Artificial Neural Networks.

Loss Functions measure the difference between actual values and predicted values. They help evaluate how accurately a model performs by calculating its prediction error.

## 📂 Programs

| Sr. No. | Program                  | Description                                                                                                                |
| ------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| 01      | `01_LossFunction_MSE.py` | Implements Mean Squared Error (MSE) to calculate the average of squared differences between actual and predicted values.   |
| 02      | `02_LossFunction_MAE.py` | Implements Mean Absolute Error (MAE) to calculate the average of absolute differences between actual and predicted values. |

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

## 🛠️ Technologies Used

* **Python** – Implementation of loss functions.
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
```

## 🎯 Learning Objectives

* Understand the purpose of loss functions.
* Calculate prediction errors using MSE and MAE.
* Understand the difference between squared error and absolute error.
* Learn how loss functions help evaluate regression models.

## 👨‍💻 Author

**Atharv Bhosale**

Computer Engineering | Python | Machine Learning | Deep Learning

---

⭐ This folder is part of my **Deep Learning** repository, documenting my learning and implementation of fundamental neural network concepts.

