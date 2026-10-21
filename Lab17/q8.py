# Write a script to count the number of occurrences of a word, W, in a sentence, S.

S = input("Enter a sentence: ")
W = input("Enter the word: ")
words = S.split()
count = words.count(W)
print("Occurrences:", count)
