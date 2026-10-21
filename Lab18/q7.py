#Write a program with a function to find whether a given triangle with sides a, b, c is isosceles, scalene or equilateral triangle
# also provide a test case output from the program.

def triangle(a,b,c):
    if a+b==c or b+c==a or a+c==b:
        return "Not a triangle"
    elif a==b==c:
        return "Equilateral"
    elif a==b or b==c or a==c:
        return "Isosceles"
    else:
        return "Scalene"
        
a=int(input("Enter side: "))
b=int(input("Enter side: "))
c=int(input("Enter side: "))

print(triangle(a,b,c))
