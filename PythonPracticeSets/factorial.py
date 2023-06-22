# Write a Python program to calculate the factorial of a number using variables and a loop.
# Number to calculate factorial for
number = 5

# Initialize the factorial variable with 1
factorial = 1

# Calculate the factorial using a loop
for i in range(1, number + 1):
    factorial *= i

# Display the factorial
print("The factorial of", number, "is:", factorial)
