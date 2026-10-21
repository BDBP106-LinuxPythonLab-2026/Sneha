# Write a program to remove all occurrences of an element from a list, L.

L = [1, 2, 3, 2, 4, 2, 5]
print(L)
element = int(input("Enter a number from the list:"))
if element in L:
    L.remove(element) # removes the first found occurence of the element
print(L)
