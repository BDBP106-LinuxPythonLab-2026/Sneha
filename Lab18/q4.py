#Given a dictionary with a values list, extract the key whose value has the most unique values.
test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
maximum = 0
answer = ""
for key, values in test_dict.items():
    unique_values = set(values)
    if len(unique_values) > maximum:
        maximum = len(unique_values)
        answer = key
print(answer)