def count_substring_occurrences(string, substring):
    count = 0
    start = 0
    
    # Iterate through the string while searching for the substring
    while True:
        index = string.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    
    return count

# Test the function
input_string = input("Enter a string: ")
input_substring = input("Enter a substring: ")
occurrences = count_substring_occurrences(input_string, input_substring)
print(f"The substring '{input_substring}' occurs {occurrences} times in the string.")
