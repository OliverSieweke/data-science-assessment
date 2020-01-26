from data_points import data_points
from calculate_mse import calculate_mse
import matplotlib.pyplot as plt


def estimate_coefficient(data=data_points, start_coefficient=0, iterations=100, increment=0.1, plot=True):
    """
    Implements a procedure for estimating the regression coefficient.

    :param data: function returning an iterator yielding the x, y data points as a list of floats
    :param start_coefficient: initial coefficient from which to start the procedure
    :param iterations: number of iterations for the procedure
    :param increment: coefficient increment after each iteration
    :param plot: specifies whether a plot should be shown
   """
    current_mse = calculate_mse(start_coefficient)
    current_estimate = start_coefficient

    for _ in range(iterations):
        new_estimate = current_estimate + increment
        new_mse = calculate_mse(new_estimate)

        if new_mse < current_mse:
            current_mse = new_mse
            current_estimate = new_estimate
        else:
            break

    if plot:
        for [x, y] in data():
            plt.scatter(x, y, c="blue", alpha=0.5)

        plt.plot([0, current_estimate], c="red", alpha=0.5)
        plt.text(0, 2.8, f"a={round(current_estimate, 1)}", fontsize=11, c="red", alpha=0.5)
        plt.title("Linear Regression")
        plt.show()

    return {"estimate": round(current_estimate, 1), "mse": round(current_mse, 2)}
