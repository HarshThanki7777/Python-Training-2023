# Ask To User To Enter The Numbers and Enter The Min-Max Numbers
numbers = input('Enter a list of numbers separated by spaces: ')
numbers = [int(num) for num in numbers.split()]
max_num = max(numbers)
min_num = min(numbers)
print(f'Maximum number: {max_num}')
print(f'Minimum number: {min_num}')

# In the first example, the split() function splits the sentence into individual words using the default whitespace delimiter

# Here Is A Simple Example of Split 
# sentence = "Hello, how are you today?"
# words = sentence.split()  # Splitting using whitespace as delimiter
# print(words)
# Output: ['Hello,', 'how', 'are', 'you', 'today?']