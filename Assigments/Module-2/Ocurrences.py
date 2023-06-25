def count_word_occurrences(sentence):
    word_count = {}
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the occurrences of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Print the word occurrences
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Test the function
input_sentence = input("Enter a sentence: ")
count_word_occurrences(input_sentence)
