#Given a dictionary with a values list, extract the key whose value has the most unique values.

test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
unique_value=[]
unique_key=""
for key,value in test_dict.items():
    most_unique_value=set(value) # onlt unique elements can be inserted in the set
    if len(most_unique_value)>len(unique_value): # whichever set is having more numbers of elements becomes the unique_value
        unique_value.append(most_unique_value)
        unique_key=key
print(unique_key)
