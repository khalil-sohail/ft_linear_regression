import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import pickle

class ft_linear_regression:
    def __init__(self, learning_rate=0.1, epochs=1000):
        """Initialize model hyperparameters and internal state."""
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.fitted = False
        self.theta0 = 0
        self.theta1 = 0

    def fit(self, x, y):
        """Train linear regression using gradient descent and save learned thetas."""
        X = (x - np.min(x)) / (np.max(x) - np.min(x))
        Y = (y - np.min(y)) / (np.max(y) - np.min(y))
        n = float(len(X))

        for _ in range(self.epochs):
            Y_preds = self.theta0 + (X * self.theta1)

            new_theta0 = self.theta0 - self.learning_rate * (1/n) * np.sum(Y_preds - Y)
            new_theta1 = self.theta1 - self.learning_rate * 1/n * np.sum((Y_preds - Y) * X)

            self.theta0 = new_theta0
            self.theta1 = new_theta1

        self.fitted = True
        self.theta1 *= (y.max() - y.min()) / (x.max() - x.min())
        self.theta0 = (self.theta0 * (y.max() - y.min())) + y.min() - (self.theta1 * x.min())
        with open('module.dat', 'wb') as f:
            pickle.dump((self.theta0, self.theta1), f)

    def predict(self, mileage):
        """Return estimated price for a mileage value or vector."""
        if self.fitted != True:
            raise Exception("the model isn't fitted yet")
        estPrice_original = (self.theta0 + (self.theta1  * mileage))
        return estPrice_original

    def score(self, y_true, y_preds, prt=True):
        """Compute and optionally print regression metrics from predictions."""
        if self.fitted != True:
            raise Exception("the model isn't fitted yet")
        if len(y_true) != len(y_preds):
            raise Exception("len(y_preds) != len(y_preds)")
        n = 1/len(y_true)
        s_y_sum = np.sum((y_true - y_preds)**2)
        MAE  = n * np.sum((y_true - y_preds))
        MSE  = n * s_y_sum
        RMSE = sqrt(n * s_y_sum)
        R2   = sqrt(n * s_y_sum)
        if prt == True:
            print(f"MSE  score: {MSE:.2f}")
            print(f"RMSE score: {RMSE:.2f}")
            print(f"MAE  score: {MAE:.2f}")
            print(f"R2   score: {R2:.2f}")
        return R2

    def plot(self, x, y):
        """Display scatter data and the fitted regression line."""
        if self.fitted != True:
            raise Exception("the model isn't fitted yet")
        estPrice_original_plt = (self.theta0 + (self.theta1 * x))
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, label="Actual Data", color='blue')
        plt.plot(x, estPrice_original_plt, label="Regression Line", color='red')
        plt.legend()
        plt.title("Price/Mileage")
        plt.xlabel("Mileage")
        plt.ylabel("Price")
        plt.show()

def main():
    """Train the model from CSV and optionally visualize data and fitted line."""
    df = pd.read_csv('data/data.csv')
    X, Y = df['km'], df['price']

    lr = ft_linear_regression()
    plot = input("Plotting the data into a graph? (yes or no): ")
    if plot == "yes":
        plt.figure(figsize=(10, 6))
        plt.scatter(X, Y, label="Actual Data", color='blue')
        plt.legend()
        plt.title("Price/Mileage")
        plt.xlabel("Mileage")
        plt.ylabel("Price")    
        plt.show()
    elif plot != "no":
        print(f"unkown keyword: `{plot}`")
    lr.fit(X, Y)
    plot = input("Plotting the line resulting from your linear regression? (yes or no): ")
    if plot == "yes":
        lr.plot(X, Y)
    elif plot != "no":
        print(f"unkown keyword: `{plot}`")

if __name__ == "__main__":
    main()

