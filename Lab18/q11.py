def is_magic_date(day, month, year):
    # Get the last two digits of the year
    two_digit_year = year % 100
    if day * month == two_digit_year:
        return True
    else:
        return False
# Find all magic dates in the 20th century
for year in range(1900, 2000):
    for month in range(1, 13):
        for day in range(1, 32):
            if is_magic_date(day, month, year):
                print(day, "/", month, "/", year)