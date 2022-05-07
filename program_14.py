# 14. The temperature of the city is input through the keyboard in Fahrenheit. 
# Write a program to convert into Celsius.
fahrenheit = float(input("Enter Temprature in Fahrenhiet "))
celsius = (fahrenheit - 32) * 5 / 9       #  converting fahrenheit to celsius
celsius_format = "{:.2f}".format(celsius) 
print(f' Temperature in Celsius is {celsius_format}')

