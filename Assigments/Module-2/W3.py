def get_string_chars(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]

# Test the function
input_string = input("Enter a string: ")
result = get_string_chars(input_string)
print("Modified String:", result)
