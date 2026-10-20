number = int(input("Enter a number: "))
number = abs(number)       #    only take the positive integer.
total = 0
while number > 0:
    digit = number % 10    #    number % 10 extracts the last digit.
    total += digit         #    adds the extracted digit to the running sum.
    number //= 10          #    removes the last digit.
print("Sum of digits:", total)
