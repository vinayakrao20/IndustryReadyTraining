# Write a program to print the area of a triangle if three sides are given.

a = int(input("Enter 1st side of triangle "))
b = int(input("Enter 2nd side of triangle "))
c = int(input("Enter 1st side of triangle "))

# here we are using heron's formula first we have t0 get s= semi perimeter

s = (a + b + c) * 0.5      # s=(a+b+c)*1/2

area = (s*(s-a)*(s-b)*(s-c)) ** .5
print(f"The area of three side Triangle is {area}")