# 16. Given the coordinates of two points (x1, y1) and (x2, y2). Write a program to 
# find the distance between these two points.
x1 = int(input("Enter x1 value : "))
x2 = int(input("Enter x2 value : "))
y1 = int(input("Enter y1 value : "))
y2 = int(input("Enter y2 value : "))
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(f'Distance between ({x1},{x2}) and ({y1},{y2}) is {distance})')