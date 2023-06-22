# Write a Python program to find the maximum value in a list of numbers using a variable.


# List of numbers
numbers = [5, 8, 3, 12, 10, 6]

# Initialize the maximum variable with the first element of the list
maximum = numbers[0]

# Find the maximum value in the list
for num in numbers:
    if num > maximum:
        maximum = num

# Display the maximum value
print("The maximum value is:", maximum)
