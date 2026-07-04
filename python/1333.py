import math
def area_of_circle(radius):
        return math.pi * radius ** 2

from geometry import area_of_circle
    r = float(input("Enter radius of circle: "))
area = area_of_circle(r)
print(f"Area of circle with radius {r} is {area:.2f}")