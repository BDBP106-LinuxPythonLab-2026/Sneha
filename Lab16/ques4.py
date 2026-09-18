import math

angle = float(input("Enter angle in degrees: "))

# Convert degrees to radians
radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print("sin =", sin_value)
print("cos =", cos_value)
print("tan =", tan_value)

# Handle undefined cosecant, secant and cotangent
if abs(sin_value) > 1e-10:
    print("cosec =", 1 / sin_value)
    print("cot =", 1 / tan_value)
else:
    print("cosec = undefined")
    print("cot = undefined")

if abs(cos_value) > 1e-10:
    print("sec =", 1 / cos_value)
else:
    print("sec = undefined")
