# Write a Python program to swap the values of two variables using a temporary variable.

# Declare and initialize two variables
variable1 = 10
variable2 = 20

# Display the initial values
print("Before swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)

# Swap the values using a temporary variable
temp = variable1
variable1 = variable2
variable2 = temp

# Display the swapped values
print("After swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)
