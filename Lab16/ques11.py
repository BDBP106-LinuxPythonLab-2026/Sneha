letter = input("Enter a letter: ").lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single alphabetic letter.")
elif letter in "aeiou":
    print("The letter is a vowel.")
else:
    print("The letter is a consonant.")
