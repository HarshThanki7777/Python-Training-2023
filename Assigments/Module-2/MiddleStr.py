def insert_string_in_middle(original_string, insert_string):
    middle_index = len(original_string) // 2

    return original_string[:middle_index] + insert_string + original_string[middle_index:]

# Test the function
original = input("Enter the original string: ")
insert = input("Enter the string to insert: ")

result = insert_string_in_middle(original, insert)
print("Modified String:", result)
