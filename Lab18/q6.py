#Write a program with a function to calculate the area of a triangle using the formula
# where a, b, c are sides of the triangle

import math
a=3
b=4
c=5
s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle ABC is ",area)
