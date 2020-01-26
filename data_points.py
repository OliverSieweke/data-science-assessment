from pathlib import Path
import csv
import itertools


# Task 1
def data_points():
    """Returns an iterator yielding the x, y data points as a list of floats."""
    data_points_file = open(Path('data', 'datapoints.csv'))
    reader = csv.reader(data_points_file)
    return itertools.starmap(
        lambda x, y: [float(x), float(y)],
        itertools.islice(reader, 1, None)  # Ignoring the headers
    )
