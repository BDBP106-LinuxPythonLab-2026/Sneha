L = [1, 2, 3, 2, 4, 2, 5]
print(L)
element = int(input("Enter a number from the list:"))
while element in L:
    L.remove(element)
print(L)
