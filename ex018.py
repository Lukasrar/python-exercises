from math import radians, sin, cos, tan

angle = float(input("Enter the angle in degrees: "))

radians = radians(angle)

sin = sin(radians)
cos = cos(radians)
tan = tan(radians)

print(f"The sine of {angle}° is: {sin:.2f}")
print(f"The cosine of {angle}° is: {cos:.2f}")
print(f"The tangent of {angle}° is: {tan:.2f}")