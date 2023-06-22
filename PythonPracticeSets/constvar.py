# How can you define a constant variable in Python that cannot be modified?
# Constant variable
PI = 3.14159

# Attempt to modify the constant (not recommended)
PI = 3.14  # This will generate a warning or error, but it's still possible

# Use the constant variable
radius = 5
area = PI * radius * radius
print("Area of the circle:", area)
