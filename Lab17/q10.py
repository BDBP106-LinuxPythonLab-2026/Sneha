A = [10, 15, 22, 33, 40, 51]
even_numbers = [] #put all the even numbers in the new list
for num in A:
    if num % 2 == 0:
        even_numbers.append(num) #add the new even number to the end of the list
print(even_numbers)
