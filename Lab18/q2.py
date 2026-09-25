#Write a program to sum all the values of a dictionary.
numbers = {"a": 10,"b": 20,"c": 30,"d": 40}
total = 0
for value in numbers.values():
    total += value
print("Sum =", total)
