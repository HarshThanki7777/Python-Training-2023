def replace_not_poor(string):
    # Find the indexes of 'not' and 'poor'
    not_index = string.find('not')
    poor_index = string.find('poor')

    # Check if 'not' appears before 'poor' and replace the substring
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        string = string[:not_index] + 'good' + string[poor_index + 4:]

    return string

def find_longest_word(words):
    longest_length = 0

    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)

    return longest_length

# Test the functions
input_string = input("Enter a string: ")
result = replace_not_poor(input_string)
print("Modified String:", result)

input_words = input("Enter a list of words (space-separated): ").split()
longest_length = find_longest_word(input_words)
print("Length of the Longest Word:", longest_length)
