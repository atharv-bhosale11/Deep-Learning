# 07. Feedforward Neural Network Applications

This folder contains practical implementations of Feedforward Neural Networks (FNNs) for solving real-world regression and classification problems.

These projects demonstrate how neural networks can learn patterns from input data, make predictions, evaluate model performance, and solve different problems using supervised learning.

## 📂 Programs

| Sr. No. | Program                                           | Description                                                                                                                                                |
| ------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01      | `01_FNN_Salary_Prediction_Regression.py`          | Predicts employee salaries based on experience, education score, skill rating, and certifications using an FNN regression model.                           |
| 02      | `02_FNN_Student_Result_Classification.py`         | Predicts whether a student will pass or fail based on study hours, attendance, and assignment scores.                                                      |
| 03      | `03_FNN_Student_Result_Classification_Scaling.py` | Implements student pass/fail classification using feature scaling and stratified train-test splitting.                                                     |
| 04      | `04_FNN_Placement_Prediction.py`                  | Predicts student placement outcomes using an FNN classification model with data analysis, preprocessing, evaluation, visualization, and model persistence. |

## 📚 Concepts Covered

### 1. Feedforward Neural Network (FNN)

* Understanding feedforward neural network architecture.
* Input features and output predictions.
* Hidden layers and neurons.
* Activation functions.
* Training neural networks using Scikit-Learn.

### 2. Regression

* Employee salary prediction.
* Predicting continuous numerical values.
* MLPRegressor implementation.
* Mean Absolute Error (MAE) evaluation.

### 3. Classification

* Student pass/fail prediction.
* Student placement prediction.
* Binary classification using MLPClassifier.
* Model accuracy and classification reports.

### 4. Data Preprocessing

* Train-test splitting.
* Feature scaling using StandardScaler.
* Stratified train-test splitting.
* Handling input and output scaling.

### 5. Model Evaluation

* Accuracy Score.
* Mean Absolute Error.
* Confusion Matrix.
* Classification Report.
* Prediction Probabilities.

### 6. Model Saving and Loading

* Saving trained models using Joblib.
* Saving preprocessing scalers.
* Loading previously trained models.
* Reusing trained models for new predictions.

### 7. Data Visualization

* Placement class distribution.
* Aptitude vs. coding score visualization.
* Training loss curve.
* Actual vs. predicted placement comparison.

## 🛠️ Technologies & Libraries Used

* **Python** – Core programming language.
* **NumPy** – Numerical computations.
* **Pandas** – Dataset loading and data analysis.
* **Scikit-Learn** – Machine learning and neural network implementation.
* **Matplotlib** – Data visualization.
* **Joblib** – Model saving and loading.

## 📦 Prerequisites

Install the required Python libraries:

```bash
pip install numpy pandas scikit-learn matplotlib joblib
```

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the directory:

```bash
cd Deep-Learning/07_Feedforward_Neural_Network_Applications
```

Run individual programs:

```bash
python 01_FNN_Salary_Prediction_Regression.py
python 02_FNN_Student_Result_Classification.py
python 03_FNN_Student_Result_Classification_Scaling.py
python 04_FNN_Placement_Prediction.py
```

**Note:** The placement prediction program requires `placement_data.csv` in the working directory.

## 🎯 Learning Objectives

* Understand practical applications of Feedforward Neural Networks.
* Implement regression and classification models.
* Train neural networks using MLPRegressor and MLPClassifier.
* Understand feature scaling and data preprocessing.
* Evaluate model performance using different metrics.
* Visualize training results and model predictions.
* Save, load, and reuse trained machine learning models.
* Apply neural networks to real-world prediction problems.

## 👨‍💻 Author

**Atharv Bhosale**
