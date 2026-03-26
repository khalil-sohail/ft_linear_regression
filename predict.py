import pickle

def main():
    """Load saved model coefficients and estimate price from user mileage input."""
    try:
        with open('module.dat', 'rb') as f:
            theta0, theta1 = pickle.load(f)
    except FileNotFoundError:
        theta0, theta1 = (0, 0)
    except (pickle.UnpicklingError, EOFError, ValueError, TypeError):
        print("Error: model file 'module.dat' is corrupted or invalid.")
        return

    try:
        mileage = int(input("your mileage is: "))
        if mileage < 0:
            print("Error: mileage must be a non-negative integer.")
            return
    except ValueError:
        print("Error: please enter a valid integer for mileage.")
        return
    except KeyboardInterrupt:
        print("\nInput cancelled.")
        return

    estPrice = theta0 + (theta1 * mileage)
    print(f"estimatePrice(mileage): {estPrice}")


if __name__ == '__main__':
    main()
