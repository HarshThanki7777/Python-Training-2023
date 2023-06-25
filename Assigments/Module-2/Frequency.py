def count_characters(string):
    char_frequency = {}
    
    # Count the frequency of each character
    for char in string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Print the character frequency
    for char, frequency in char_frequency.items():
        print(f"{char}: {frequency}")

# Test the function
input_string = input("Enter a string: ")
count_characters(input_string)
