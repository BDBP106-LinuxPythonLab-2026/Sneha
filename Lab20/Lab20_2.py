#enter a sentence
#count the vowels, consonants, digits and spaces
from orca.messages import spaces_count

sentence=input("Enter a sentence: ")
vowels=['a','e','i','o','u']
vowels_count=0
consonant_count=0
digits_count=0
space_count=0


for i in sentence:
    if i.isalpha():
        if i.lower() in vowels:
            vowels_count+=1
        else:
            consonant_count+=1
    elif i.isdigit():
        digits_count+=1
    elif i.isspace():
        space_count+=1
print("Vowel count is: ", vowels_count)
print("Consonant count is: ", consonant_count)
print("Digits count is: ", digits_count)
print("Space count is: ", space_count)