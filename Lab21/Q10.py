"""Write a program to extract all vowels in a given string using list comprehension"""

text=input("Enter a string: ")
vowels=[ch for ch in text if ch.lower() in "aeiou"]
print("Vowels: ",vowels)
