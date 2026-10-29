import csv
import re

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

line = input("Enter a CSV line: ")

try:
    fields = next(csv.reader([line], strict=True))

    if len(fields) <= 3:
        print("Error: The CSV must contain more than 3 fields.")

    elif re.fullmatch(email_pattern, fields[2].strip()):
        print("The third field contains exactly an email address.")

    else:
        print("The third field does not contain exactly an email address.")

except csv.Error:
    print("Invalid CSV input.")
