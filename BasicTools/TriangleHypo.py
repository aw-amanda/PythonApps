# Find the hypotenuse of a right triangle (c = square root of a^2 + b^2)

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

    # To calculate, add together a^2 + b^2, then find the square root of that result:
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")