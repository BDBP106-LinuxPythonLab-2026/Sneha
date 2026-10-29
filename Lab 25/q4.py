import re

pattern = r"^(?:0|[1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

test_values = [
    "0",
    "1",
    "9",
    "10",
    "99",
    "100",
    "199",
    "249",
    "250",
    "255",
    "256",
    "999",
    "00",
    "007",
    "1234",
    "-1"
]

for value in test_values:
    if re.fullmatch(pattern, value):
        print(value, "is valid")
    else:
        print(value, "is invalid")
