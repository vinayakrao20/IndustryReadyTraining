# 8. Write a program to find the volume of a cylinder.
import math
radius = int(input("Enter Radius  "))
pi = math.pi
height = int(input("Enter Height  "))
print(f' Radius of cylinder is {radius} and height is {height} and volume is {pi*height*(radius**2)}')
# volume of cylinder = pi*r^2*h