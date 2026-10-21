# Write a program to extract elements of a list, if it occurs more than k times.

L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 2
result = []
for i in L:
    if L.count(i) > k and i not in result:       # L.count(i) checks if the element appears more that twice
                                            # i not in duplicates --> checks if the element has not already been added to the duplicates list? if not then append
        result.append(i) #add the element to the end of the list
print(result)
