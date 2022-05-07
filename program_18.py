#18. The distance between two cities in Km. is input through the keyboard. Write a program to 
# convert and print the result in meters and centimetres.

distance = float(input("Enter Distance of two cities in Km : "))
distance_meters = distance * 1000
distance_cm = distance * 100000
print(f"Distance of Two Cities in Meter is {distance_meters} and in Centimeter is {distance_cm}")