def combine_and_swap_strings(string1, string2):
    # Swap the first two characters of each string
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]

    # Combine the modified strings with a space
    result = new_string1 + ' ' + new_string2
    return result

def add_ing_or_ly(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'

# Test the functions
input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")

combined_swapped = combine_and_swap_strings(input_string1, input_string2)
print("Combined and Swapped String:", combined_swapped)

input_string3 = input("Enter a string to add 'ing' or 'ly': ")
modified_string = add_ing_or_ly(input_string3)
print("Modified String:", modified_string)
