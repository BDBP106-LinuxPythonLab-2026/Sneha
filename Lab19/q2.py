# (i) Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.
a = [i for i in range(1, 51)]
sum_a = 0
for i in a:
    sum_a = sum_a + i
print(sum_a)
print()

# (ii) Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
b = [i for i in range(2, 51) if all(i % j != 0 for j in range(2, i))]   #    i --> The number added to the list if the condition is satisfied
                                                                        #    all() returns True if every condition inside it is true.
print(b)
print()

# (iii) Using a do loop structure, collect all the common numbers in a and b into a new  list c.
c = []
for i in a:
    if i in b:
        c.append(i)
print("Common numbers: " ,c)

#list comprehension:
c=[i for i in a if i in b]
print("Common numbers: " ,c)
