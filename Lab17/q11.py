L = [1, 2, 3, 2, 4, 5, 3, 6]
duplicates = []
for item in L:
    if L.count(item) > 1 and item not in duplicates: #does this item appears more that once and "item not in duplicates" checks has this item not already been added to the duplicates list?
        duplicates.append(item) #add the item to the end of the list
print(duplicates)
