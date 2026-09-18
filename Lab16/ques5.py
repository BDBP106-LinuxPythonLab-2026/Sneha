import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
   print("This is not a quadratic equation.")
else:
   discriminant = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

print("Root 1:", root1)
print("Root 2:", root2)
