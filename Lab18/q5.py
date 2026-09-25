#Remove all duplicate words from a given sentence using a dictionary.
sentence = "My name is is is Sneha"
print(sentence)
words = sentence.split()
unique_words = set(words)
result = " ".join(unique_words)
print("Sentence without duplicates:")
print(result)