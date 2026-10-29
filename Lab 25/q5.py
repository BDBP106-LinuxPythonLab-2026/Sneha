import re

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

text = input("Enter a string: ")

if re.search(pattern, text):
    print("The string contains an email address.")
else:
    print("The string does not contain an email address.")
