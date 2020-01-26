from data_points import data_points
from predicted_values import calculate_predicted_value


# Task 3:
def calculate_mse(coefficient, data=data_points):
    """
    Returns the MSE for a given coefficient.

    :param coefficient: coefficient for which to calculate the MSE
    :param data: function returning an iterator yielding the x, y data points as a list of floats
    """
    squared_errors_sum = 0
    number_of_data_points = 0

    for [x, y] in data():
        number_of_data_points += 1
        squared_errors_sum += (y - calculate_predicted_value(x, coefficient)) ** 2

    return squared_errors_sum / number_of_data_points
