#Write a program with a function to find whether a given triangle with sides a, b, c is isosceles, scalene or equilateral triangle
# also provide a test case output from the program.
def triangle_type(a, b, c):
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
# Test case
a = 7
b = 5
c = 8
print(triangle_type(a, b, c))