# Write a Python program to sort a list of numbers using variables.
# List of numbers
numbers = [7, 2, 5, 1, 9, 3]

# Initialize an empty list to store the sorted numbers
sorted_numbers = []

# Iterate through the numbers and find the smallest number
while numbers:
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    # Append the smallest number to the sorted list
    sorted_numbers.append(smallest)
    # Remove the smallest number from the original list
    numbers.remove(smallest)

# Display the sorted list of numbers
print("Sorted numbers:", sorted_numbers)
