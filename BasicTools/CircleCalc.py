# Basic circumference and radius calculator (truncated)

import math

#1. Calculate the circumference of a circle (c = 2 * pi * r):

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is {round(circumference, 2)}")


#2. Calculate the area of a circle (A = pi * r^2) and round to 2 decimal places:

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)}^2")
