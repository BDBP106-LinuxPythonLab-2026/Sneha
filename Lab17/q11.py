# Write a program to print the duplicate elements in a list, L.

L = [1, 2, 3, 2, 4, 5, 3, 6]
duplicates = []
for i in L:
    if L.count(i) > 1 and i not in duplicates: # L.count() --> checks if element appears more that once
                    # i not in duplicates --> checks has this item not already been added to the duplicates list? if not then adds it to the list
        duplicates.append(i) #add the item to the end of the list
print(duplicates)
