import math
number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
   print("Factorial:", math.factorial(number))
