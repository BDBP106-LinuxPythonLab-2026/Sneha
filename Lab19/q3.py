a = [i for i in range(1, 51)]
#i
#a
s1 = ",".join([str(x) for x in a])
print(s1)

print()
#b
s2 = ".".join([str(x) for x in a])
print(s2)

print()
#c
s3 = "—".join([str(x) for x in a])
print(s3)

print()
#d
squares = [x**2 for x in a]
square_data = "\n".join([f"{x} {x**2}" for x in a])
print(square_data)

print()
#ii
people = [
    "John Smith",
    "Alice Brown",
    "David Wilson",
    "Mary Jones",
    "Robert Taylor",
    "Emma Davis",
    "James Miller",
    "Sophia Anderson",
    "Daniel Thomas",
    "Olivia Moore"
]

#a
upper_people = [name.upper() for name in people]
print(upper_people)

print()
#b
swapped = [" ".join(name.split()[::-1]) for name in people]
print(swapped)

print()
#c
first_last = [
    ".".join(part.title() for part in name.split())
    for name in people
]

print(first_last)

print()
#iii
sentence = "She sells sea shells that she collects from the sea floor"
words = sentence.split()
longest = max([word for word in words], key=len)
print(longest)

print()
#iv
sentence = "She sells sea shells that she collects from the sea floor"
words = sentence.lower().split()
repeated = [word for word in set(words) if words.count(word) > 1]
print(repeated)






