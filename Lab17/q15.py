# Write a program to extract words from a string list, L whose first character is k.

L = ["apple", "banana", "ant", "cat", "apricot" ,"kangaroo", "knight"]
print(L)
k = input("Enter any first letter from the list: ")
result = []
for word in L:
    if word[0] == k:
        result.append(word)
print(result)
