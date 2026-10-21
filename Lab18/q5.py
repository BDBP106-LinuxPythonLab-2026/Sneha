#Remove all duplicate words from a given sentence using a dictionary.

#asking input from the user
sentence=input("enter a sentence: ")
words=sentence.split()
unique=set(words)
without_duplicates=" ".join(unique)
print(without_duplicates)

# giving the test case
sentence = "My name is is is Sneha"
print(sentence)
words = sentence.split()
unique_words = set(words)
result = " ".join(unique_words)
print("Sentence without duplicates:")
print(result)
