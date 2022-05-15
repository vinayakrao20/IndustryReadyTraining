# 32. Write a program to read three sides a, b, c of a triangle and print the type of
# the triangle.

a = int(input("Enter triangle side a : "))
b = int(input("Enter triangle side b : "))
c = int(input("Enter triangle side c : "))
if (a == b) and (b == c) :
    print("All sides are equal it's an Equilateral Triangle")

elif (a == b) or (b == c) or (c == a) :
    print("Two sides are Equal it's an Isosceles Triangle")

else :
    print("No Sides are Equal it's an Scalene Triangle")
