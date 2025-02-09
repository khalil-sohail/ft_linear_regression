def main():
    theta0 = 1.5
    theta1 = 1.5


    mileage = int(input("your mileage is: "))
    estPrice = theta0 + (theta1 * mileage)
    print(f"estimatePrice(mileage): {estPrice}")

if __name__ == '__main__':
    main()
