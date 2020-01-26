from predicted_values import predicted_values
from calculate_mse import calculate_mse
from estimate_coefficient import estimate_coefficient

# Task 2:
print("".ljust(100, "-"))
print(f"Task2:\n\nPredicted values with coefficient 10: {list(predicted_values(10))}")

# Task 3:
print("\n".ljust(100, "-"))
print(f"Task3:\n\nMSE with coefficient 10: {calculate_mse(10)}")

# Task 4:
estimation = estimate_coefficient()
print("\n".ljust(100, "-"))
print("Task4:\n" +
      "\nEstimated coefficient a:".ljust(32) + str(estimation['estimate']) +
      "\nCorresponding MSE:".ljust(32) + str(estimation['mse']))
print("\n".ljust(100, "-"))
