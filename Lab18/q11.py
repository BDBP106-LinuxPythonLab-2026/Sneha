"""A magic date is a date where the date multiplied by the month is equal to the two-digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60 which is the two-digit year. Write a function that determines whether
or not a date is a magic date. Use your function to create a main program that finds
and displays all of the magic dates in the 20th century."""

def is_magic_date(day, month, year):
    two_digit_year = year % 100    # Get the last two digits of the year
    if day * month == two_digit_year:
        return True
    else:
        return False
# Find all magic dates in the 20th century
for year in range(1900, 2000):   # 20th century is the 100-year span from 1900 through 1999
    for month in range(1, 13):
        for day in range(1, 32):
            if is_magic_date(day, month, year):
                print(day, "/", month, "/", year)
