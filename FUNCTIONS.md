# Function Reference

Small documentation for functions in:
- `ft_linear_regression.py`
- `precision.py`
- `predict.py`

## `ft_linear_regression.py`

### `class ft_linear_regression`

#### `__init__(self, learning_rate=0.1, epochs=1000)`
Initializes model hyperparameters and state.

- **Parameters**:
  - `learning_rate` (`float`): Gradient descent step size.
  - `epochs` (`int`): Number of optimization iterations.
- **Sets**:
  - `self.fitted = False`
  - `self.theta0 = 0`, `self.theta1 = 0`

#### `fit(self, x, y)`
Trains a simple linear regression model using gradient descent on normalized data, then rescales parameters back to original units.

- **Parameters**:
  - `x` (`array-like`): Mileage feature values.
  - `y` (`array-like`): Target price values.
- **Behavior**:
  - Normalizes `x` and `y` to `[0, 1]`.
  - Updates `theta0` and `theta1` for `epochs` iterations.
  - Uses simultaneous assignment (`new_theta0`, `new_theta1`) per iteration.
  - Converts final thetas back to original data scale.
  - Saves `(theta0, theta1)` to `module.dat` using `pickle`.
  - Sets `self.fitted = True`.
- **Returns**: `None`.

#### `predict(self, mileage)`
Predicts estimated price from mileage using the trained model.

- **Parameters**:
  - `mileage` (`float` or array-like): Input mileage value(s).
- **Returns**:
  - Estimated price value(s): `theta0 + theta1 * mileage`.
- **Raises**:
  - `Exception` if model is not fitted.

#### `score(self, y_true, y_preds, prt=True)`
Computes error/fit metrics and optionally prints them.

- **Parameters**:
  - `y_true` (`array-like`): Ground truth target values.
  - `y_preds` (`array-like`): Predicted target values.
  - `prt` (`bool`): If `True`, prints metric values.
- **Computed metrics**:
  - `MAE`, `MSE`, `RMSE`, `R2` (as currently implemented in code).
- **Returns**:
  - `R2` value (current implementation).
- **Raises**:
  - `Exception` if model is not fitted.
  - `Exception` if input lengths differ.

#### `plot(self, x, y)`
Plots original data points and regression line.

- **Parameters**:
  - `x` (`array-like`): Feature values.
  - `y` (`array-like`): Target values.
- **Behavior**:
  - Displays scatter plot for data.
  - Displays fitted linear regression line.
- **Returns**: `None`.
- **Raises**:
  - `Exception` if model is not fitted.

### `main()`
CLI training/visualization entry point.

- Loads dataset from `data/data.csv`.
- Optionally plots raw data.
- Trains model by calling `fit`.
- Optionally plots fitted line via `plot`.
- Prints warning for unknown yes/no prompts.

---

## `precision.py`

### `main()`
Evaluates training quality quickly using existing class methods.

- Loads dataset from `data/data.csv`.
- Instantiates `ft_linear_regression`.
- Trains with `fit(X, Y)`.
- Predicts values using `predict(X)`.
- Computes and prints metrics with `score(Y, y_preds)`.

---

## `predict.py`

### `main()`
CLI prediction entry point using saved model parameters.

- **Model loading**:
  - Reads `(theta0, theta1)` from `module.dat`.
  - If file is missing, falls back to `(0, 0)`.
  - If file is invalid/corrupted, prints error and exits.
- **Input validation**:
  - Reads mileage from user input.
  - Rejects non-integer input.
  - Rejects negative mileage.
  - Handles `KeyboardInterrupt` gracefully.
- **Prediction**:
  - Computes `estimatePrice = theta0 + theta1 * mileage`.
  - Prints the estimate.
