from math import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class ft_linear_regression:
    def __init__(self, learning_rate=0.1, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.theta0 = 0
        self.theta1 = 0
        self.xMin   = 0
        self.yMin   = 0
        self.xMax   = 0
        self.yMax   = 0
        self.scaler = 0
        self.X      = []
        self.Y      = []
    
    def fit(self, x, y):
        self.xMin = np.min(x)
        self.yMin = np.min(y)
        self.xMax = np.max(x)
        self.yMax = np.max(y)

        self.X = (x - self.xMin) / (self.xMax - self.xMin)  # Min-Max Scaling
        self.Y = (y - self.yMin) / (self.yMax - self.yMin)


        self.scaler = self.yMax - self.yMin
        n = float(len(self.X))

        for i in range(self.epochs):
            Y_preds = self.theta0 + (self.X * self.theta1)
            self.theta0 -= self.learning_rate * (1/n) * np.sum(Y_preds - self.Y)
            self.theta1 -= self.learning_rate * 1/n * np.sum((Y_preds - self.Y) * self.X)

    def predict(self, mileage):
        scaledMileage = (mileage - self.xMin) / (self.xMax - self.xMin)
        estPrice_original = (self.theta0 + (self.theta1  * scaledMileage)) * self.scaler + self.yMin

        # print(f"estimatePrice(mileage): {estPrice_original}")
        return estPrice_original

    def score(self, y_true, y_preds):
        if len(y_true) != len(y_preds):
            raise Exception("len(y_preds) != len(y_preds)")
        RMSE = sqrt(1/len(y_true) * (np.sum((y_true - y_preds)**2)))
        print(f"RMSE score: {RMSE}")
        return RMSE

    # def get_the_t0_t1(self):
    #     return self.theta0, self.theta1

    def plot(self, x, y):
        estPrice_original_plt = (self.theta0 + (self.theta1 * self.X)) * self.scaler + self.yMin
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, label="Actual Data", color='blue')
        plt.plot(x, estPrice_original_plt, label="Regression Line", color='red')
        plt.legend()
        plt.show()

def main():
    df = pd.read_csv('data/data.csv')
    X, Y = df['km'], df['price']

    lr = ft_linear_regression()
    
    lr.fit(X, Y)


    mileage = int(input("your mileage is: "))
    print(f"estimatePrice(mileage): {lr.predict(mileage)}")
    y_preds = lr.predict(X)
    lr.score(Y, y_preds)
    lr.plot(X, Y)

if __name__ == "__main__":
    main()

