import pickle

def main():
    with open('data.dat', 'rb') as f:
        theta0, theta1 = pickle.load(f)


    mileage = int(input("your mileage is: "))
    estPrice = theta0 + (theta1 * mileage)
    print(f"estimatePrice(mileage): {estPrice}")

if __name__ == '__main__':
    main()
