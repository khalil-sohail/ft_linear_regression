# ft_linear_regression

## ➢ Foreword
What i think is the best definition for machine learning :

“A computer program is said to learn from experience E with respect to some
class of tasks T and performance measure P, if its performance at tasks in
T, as measured by P, improves with experience E.”
Tom M. Mitchell


## 📌 Project Overview
This project implements a simple **Linear Regression model** to predict the price of a car based on its mileage. The model is trained using **Gradient Descent**, and predictions are made using the learned parameters.

## 📁 Project Structure
```
ft_linear_regression/
│── data/                   # Folder containing dataset files
│── ft_linear_regression.py # Training script (gradient descent)
│── predict.py              # Prediction script
│── precision.py            # Model evaluation script
│── FUNCTIONS.md            # Functions documentation
│── README.md               # Project documentation (this file)
```

## 🚀 How to Use

### 1️⃣ Train the Model
Run the following command to train the model:
```bash
python ft_linear_regression.py
```
- This will read data from `data/data.csv`
- Train a linear regression model using **Gradient Descent**
- Save the trained parameters (`theta0` and `theta1`) in a file named module.dat using pickle

### 2️⃣ Make Predictions
To predict the price of a car given its mileage:
```bash
python predict.py
```
- The program will prompt you for **mileage** input
- It will then use the trained model to predict the price

### 3️⃣ Evaluate Model Accuracy
To check how well the model performs:
```bash
python precision.py
```
- This script calculates:
  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **Mean Absolute Error (MAE)**
  - **R² Score (Coefficient of Determination)**

## 📊 Model Explanation
The model follows this hypothesis function:
```
price = theta0 + (theta1 * mileage)
```
Where:
- `theta0` (intercept) and `theta1` (slope) are learned using **Gradient Descent**
- The dataset is **scaled** using Min-Max normalization for better convergence

## 🛠️ Dependencies
Make sure you have **Python 3** installed along with the required dependencies:
```bash
pip install numpy pandas matplotlib
```

## 📝 Notes
- The dataset (`data/data.csv`) should contain **two columns**: `km` (mileage) and `price`
- The model parameters (`theta0` and `theta1`) are stored in `module.dat` and set to 0 before training
- Ensure that the dataset does not contain missing or corrupted values before training

## 📌 Author
khalil sohail - ft_linear_regression 42 Project

