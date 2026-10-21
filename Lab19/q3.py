a = [i for i in range(1, 51)]
#i Using the join method.
#a Create a string by joining the numbers in the above list a using the comma.

s1 = ",".join([str(x) for x in a])
print(s1)
print()

#b Create a string by joining the numbers in the above list a using the period.

s2 = ".".join([str(x) for x in a])
print(s2)
print()

#c Create a string by joining the numbers in the above list a using the ‘—’.

s3 = "—".join([str(x) for x in a])
print(s3)
print()

#d Create a new string by first creating a list of squares of the elements in a, then listing them alongside the elements of a line by line. 
#In other words,we want a data set that looks like
"""1 1
   2 4
   3 9"""

square_data = "\n".join([f"{x} {x**2}" for x in a])
print(square_data)
print()

#ii Make a list of 10 people you know, and do the following:

people = ["John Smith", "Alice Brown", "David Wilson", "Mary Jones", "Robert Taylor", "Emma Davis", "James Miller", "Sophia Anderson", "Daniel Thomas", "Olivia Moore"]

#a Convert each element in the list to upper case using list comprehension

upper_people = [name.upper() for name in people]
print(upper_people)
print()

#b Swap the first name and surname of each element in the list

swapped = [" ".join(name.split()[::-1]) for name in people]
print(swapped)
print()

#c Join the first name and surname in each element as ’First.Last’. 
# Note that the first letter of the first name and first letter of the surname should be upper case.

first_last = [".".join(part.title() for part in name.split()) for name in people]
print(first_last)
print()

#iii Find the longest word in this sentence using list comprehension: 
# ”She sells sea shells that she collects from the sea floor”.

sentence = "She sells sea shells that she collects from the sea floor"
words = sentence.split()
longest = max([word for word in words], key=len)
print(longest)
print()

#iv Create a list of the words that are repeated in the above sentence.

sentence = "She sells sea shells that she collects from the sea floor"
words = sentence.lower().split()
repeated = [word for word in set(words) if words.count(word) > 1]
print(repeated)
