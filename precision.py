import pandas as pd
import pickle
from ft_linear_regression import ft_linear_regression

def main():
    df = pd.read_csv('data/data.csv')
    X, Y = df['km'], df['price']

    lr = ft_linear_regression()
    lr.fit(X, Y)

    y_preds = lr.predict(X)
    lr.score(Y, y_preds)

if __name__ == '__main__':
    main()
