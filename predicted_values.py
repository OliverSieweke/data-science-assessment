from data_points import data_points


# Task 2:
def predicted_values(coefficient, data=data_points):
    """
    Generator yielding the predicted values.

    :param coefficient: slope coefficient used for calculating the predicted values
    :param data: function returning an iterator yielding the x, y data points as a list of floats
   """
    for [x, _] in data():
        yield calculate_predicted_value(x, coefficient)


def calculate_predicted_value(independent_variable, coefficient):
    """Returns the predicted value for a given input and coefficient"""
    return independent_variable * coefficient
