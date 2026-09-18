x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("The point lies in the First Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the Second Quadrant.")
elif x < 0 and y < 0:
    print("The point lie in the Third Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the Fourth Quadrant.")
elif x == 0 and y == 0:
    print("The point is at the origin")
