#Write a program with a function to calculate the area of a triangle using the formula
# where a, b, c are sides of the triangle

import math
a=3
b=4
c=5
s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle ABC is ",area)

# using function

import math
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    return area
# Test case
a = 3
b = 4
c = 5
area = triangle_area(a, b, c)
print("Area of triangle =", area)
