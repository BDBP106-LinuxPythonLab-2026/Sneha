S1 = input("Enter first word: ")
S2 = input("Enter second word: ")
if sorted(S1) == sorted(S2):
    print("Anagrams")
else:
    print("Not anagrams")
