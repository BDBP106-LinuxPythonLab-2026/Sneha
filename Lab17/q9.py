# Write a script to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams.

S1 = input("Enter first word: ")
S2 = input("Enter second word: ")
if sorted(S1) == sorted(S2):
    print("Anagrams")
else:
    print("Not anagrams")
