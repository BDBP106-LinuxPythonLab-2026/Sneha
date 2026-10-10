"""Program to convert a tuple of angles into a list of tuples containing sine and cosine"""

import math
angles = (0, 30, 45, 60, 90)
#long format
def calculate(angle):
    radians = math.radians(angle)
    sine = math.sin(radians)
    cosine = math.cos(radians)
    return (round(sine, 2), round(cosine, 2))
result = list(map(calculate, angles))
print("Angles:", angles)
print("Sine and Cosine:", result)
print()

#compact version
result = list(map(lambda a: (round(math.sin(math.radians(a)), 2),round(math.cos(math.radians(a)), 2)),angles))
print("Angles:", angles)
print("Sine and Cosine:", result)

