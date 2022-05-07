# 11. Write a program to convert speed of a vehicle given in km/hour to miles/hour.
speed = float(input("Enter Speed of a vehicle in km/hr "))
speed_miles = speed*0.62                          # converting km/hr to mi/hr
speed_miles_format = "{:.2f}".format(speed_miles) # coverting float upto 2 decimal
print(f' Speed in km/hr is {speed} and speed in Miles/hr is {speed_miles_format} ') 
