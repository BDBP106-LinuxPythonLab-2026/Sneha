L = ["apple", "banana", "ant", "cat", "apricot"]
print(L)
k = input("Enter any first letter from the list: ")
result = []
for word in L:
    if word[0] == k:
        result.append(word)
print(result)
