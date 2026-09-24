L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 2
result = []
for item in L:
    if L.count(item) > k and item not in result: #does this item appears more that twice and "item not in duplicates" checks has this item not already been added to the duplicates list?
        result.append(item) #add the item to the end of the list
print(result)
