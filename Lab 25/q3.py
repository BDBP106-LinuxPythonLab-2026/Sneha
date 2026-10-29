import re

pattern = r"^(?:00[0-9]|0[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

test_values = [
    "000",
    "001",
    "009",
    "010",
    "099",
    "100",
    "199",
    "249",
    "250",
    "255",
    "256",
    "999",
    "00",
    "1234",
    "-10"
]

for value in test_values:
    if re.fullmatch(pattern, value):
        print(value, "is valid")
    else:
        print(value, "is invalid")
