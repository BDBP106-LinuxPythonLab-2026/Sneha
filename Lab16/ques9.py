number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10             #    extracts the last digit.
    reverse = reverse * 10 + digit  #    adds that digit to the reversed number.
    number //= 10                   #    removes the last digit from the original number.

print("Reversed number:", reverse)
