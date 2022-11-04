print("This program calculates the area and the circumference of the circle")
import math
radius=float(input("type the radius of the circle:"))
area=math.pi*(radius**2)
circumference=2*math.pi*radius

print("The are of the circle is",round((area),2))
print("The circumference of the circle",round((circumference),2))
