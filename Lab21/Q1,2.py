#QUESTION1

import sys
"""program to convert temperature in Celsius to Fahrenheit using map function """

celsius = [0, 25, 37, 100]
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print()

#QUESTION2
"""Write the above program using lambda expression"""

celsius = [0, 25, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
