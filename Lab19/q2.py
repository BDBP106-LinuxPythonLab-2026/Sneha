# (i)
a = [i for i in range(1, 51)]

sum_a = 0
for i in a:
    sum_a = sum_a + i

print(sum_a)

print()
# (ii)
b = [i for i in range(2, 51)
     if all(i % j != 0 for j in range(2, i))]

print(b)

print()
# (iii)
c = []

for i in a:
    if i in b:
        c.append(i)

print(c)
