import math 

radius = float(input("Enter the radius of the circle: "))

circimference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Circumference: {circimference:.2f}")
print(f"Area: {area:.2f}")