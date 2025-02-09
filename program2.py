import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class ft_linear_regression:
    def __init__(self, learning_rate=0.1, epochs=1000, theta0=0, theta1=0, xMin=0, yMin=0, xMax=0, yMax=0):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.theta0 = theta0
        self.theta1 = theta1
        self.xMin = xMin
        self.yMin = yMin
        self.xMax = xMax
        self.yMax = yMax
    
    def fit(self, x, y):
        xMin = np.min(x)
        yMin = np.min(y)
        xMax = np.max(x)
        yMax = np.max(y)

        X = (x - xMin) / (xMax - xMin)  # Min-Max Scaling
        Y = (y - yMin) / (yMax - yMin)


        scaler = yMax - yMin
        n = float(len(X))

        for i in range(self.epochs):
            Y_preds = self.theta0 + (X * self.theta1)


            # if i % 100 == 0:
            #     print(f"Iteration {i}: theta0={theta0}, theta1={theta1}")

            #     if input("plot?: ") != 'n':
            #         estPrice_original_plt = (theta0 + (theta1 * X)) * scaler + y.min()
            #         plt.figure(figsize=(10, 6))
            #         plt.scatter(x, y, label="Actual Data", color='blue')
            #         plt.plot(x, estPrice_original_plt, label="Regression Line", color='red')
            #         plt.legend()
            #         plt.show()

            self.theta0 -= self.learning_rate * (1/n) * np.sum(Y_preds - Y)
            self.theta1 -= self.learning_rate * 1/n * np.sum((Y_preds - Y) * X)

    def predict(self, mileage):
        scaledMileage = (mileage - self.xMin) / (self.xMax - self.xMin)
        estPrice_original = (self.theta0 + (self.theta1  * scaledMileage)) * self.scaler + self.yMin

        print(f"estimatePrice(mileage): {estPrice_original}")

    def score():
        pass

    def get_the_t0_t1():
        pass

def main():
    df = pd.read_csv('data/data.csv')
    X, Y = df['km'], df['price']

    # x, y = df['km'], df['price']
    # theta0 = 0
    # theta1 = 0
    
    # learning_r = 0.1
    # epochs = 1500
    # n = float(len(X))

    # X = (X - np.min(X)) / (np.max(X) - np.min(X))  # Min-Max Scaling
    # Y = (Y - np.min(Y)) / (np.max(Y) - np.min(Y))

    # scaler = (y.max() - y.min())

    # for i in range(epochs):
    #     Y_preds = theta0 + (X * theta1)
    #     if i % 100 == 0:
    #         print(f"Iteration {i}: theta0={theta0}, theta1={theta1}")

    #         if input("plot?: ") != 'n':
    #             estPrice_original_plt = (theta0 + (theta1 * X)) * scaler + y.min()
    #             plt.figure(figsize=(10, 6))
    #             plt.scatter(x, y, label="Actual Data", color='blue')
    #             plt.plot(x, estPrice_original_plt, label="Regression Line", color='red')
    #             plt.legend()
    #             plt.show()

    #     theta0 -= learning_r * (1/n) * np.sum(Y_preds - Y)
    #     theta1 -= learning_r * 1/n * np.sum((Y_preds - Y) * X)
    lr = ft_linear_regression()
    lr.fit(X, Y)

    mileage = int(input("your mileage is: "))
    lr.predict(mileage)

    # scaledMileage = (mileage - np.min(x)) / (np.max(x) - np.min(x))
    # estPrice_original = (theta0 + (theta1  * scaledMileage)) * scaler + y.min()
    # estPrice_original_plt = (theta0 + (theta1 * X)) * scaler + y.min()

    # print(f"estimatePrice(mileage): {estPrice_original}")
    # if input("plot?: ") == 'y':
    #     plt.figure(figsize=(10, 6))
    #     plt.scatter(x, y, label="Actual Data", color='blue')
    #     plt.plot(x, estPrice_original_plt, label="Regression Line", color='red')
    #     plt.legend()
    #     plt.show()
    

if __name__ == "__main__":
    main()



# def main():
#     df = pd.read_csv('data/data.csv')
#     X, Y = df['km'], df['price']
#     x, y = df['km'], df['price']
#     theta0 = 0
#     theta1 = 0
    
#     learning_r = 0.1
#     epochs = 1500
#     n = float(len(X))

#     X = (X - np.min(X)) / (np.max(X) - np.min(X))  # Min-Max Scaling
#     Y = (Y - np.min(Y)) / (np.max(Y) - np.min(Y))

#     scaler = (y.max() - y.min())

#     for i in range(epochs):
#         Y_preds = theta0 + (X * theta1)
#         if i % 100 == 0:
#             print(f"Iteration {i}: theta0={theta0}, theta1={theta1}")

#             if input("plot?: ") != 'n':
#                 estPrice_original_plt = (theta0 + (theta1 * X)) * scaler + y.min()
#                 plt.figure(figsize=(10, 6))
#                 plt.scatter(x, y, label="Actual Data", color='blue')
#                 plt.plot(x, estPrice_original_plt, label="Regression Line", color='red')
#                 plt.legend()
#                 plt.show()

#         theta0 -= learning_r * (1/n) * np.sum(Y_preds - Y)
#         theta1 -= learning_r * 1/n * np.sum((Y_preds - Y) * X)

#     mileage = int(input("your mileage is: "))

#     scaledMileage = (mileage - np.min(x)) / (np.max(x) - np.min(x))
#     estPrice_original = (theta0 + (theta1  * scaledMileage)) * scaler + y.min()
#     estPrice_original_plt = (theta0 + (theta1 * X)) * scaler + y.min()

#     print(f"estimatePrice(mileage): {estPrice_original}")
#     if input("plot?: ") == 'y':
#         plt.figure(figsize=(10, 6))
#         plt.scatter(x, y, label="Actual Data", color='blue')
#         plt.plot(x, estPrice_original_plt, label="Regression Line", color='red')
#         plt.legend()
#         plt.show()
    
