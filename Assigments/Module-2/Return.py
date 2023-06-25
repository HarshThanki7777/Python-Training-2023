'''In Python, def is a keyword used to define a function.
A function is a block of code that performs a specific task and can be called by its name. 
The def keyword is followed by the function name and a pair of parentheses, which may include parameters. 
The code block within the function is indented and starts with a colon (:).
'''

def check_values(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False

# Test cases
print(check_values(5, 5))  # True (Equal)
print(check_values(2, 3))  # True (Sum is 5)
print(check_values(8, 3))  # True (Difference is 5)
print(check_values(4, 4))  # False (Neither equal, sum, nor difference is 5)
