# Write a program to find the even numbers in a list, L.

L = [10, 15, 22, 33, 40, 51]
even_numbers = [] # create a new list to put all the even numbers in the new list
for num in L:
    if num % 2 == 0:
        even_numbers.append(num) #keep adding the new even number to the end of the list
print(even_numbers)
