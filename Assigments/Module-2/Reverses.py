def reverse_string_if_multiple_of_four(string):
    if len(string) % 4 == 0:
        return string[::-1]
    else:
        return string

# Test the function
input_string = input("Enter a string: ")
result = reverse_string_if_multiple_of_four(input_string)
print("Reversed String (if length is multiple of 4):", result)
