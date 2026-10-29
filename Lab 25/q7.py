import re

text = input("Enter a piece of text: ")

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

# Remove duplicates while preserving the original order
unique_emails = list(dict.fromkeys(emails))

print("Unique email addresses:")

for email in unique_emails:
    print(email)
