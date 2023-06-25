def calculate_string_length(string):
    length = 0
    for char in string:
        length += 1
        return length
    
print(calculate_string_length("Hello"))       # 5
print(calculate_string_length("Python"))      # 6
print(calculate_string_length("OpenAI"))      # 6
print(calculate_string_length(""))            # 0