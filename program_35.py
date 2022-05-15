#35. A Company insures its drivers in the following cases.
# 1. If the driver is married.
# 2. If the driver is unmarried, male and above 30 years of age.
# 3. if the driver is unmarried, female and above 25 years of age.
# In all other cases, the driver is not insured. If the marital status, sex, age of the driver 
# are the inputs, write a program to determine whether the driver is insured or not.
marital_status = input("Enter Marital Status [ m / u] : ")
driver_gender = input("Enter Gender [m / f] : ")
driver_age = int(input("Enter Age : "))

if marital_status == 'm':
    print("Driver insures because he/she is married")

elif (driver_gender == 'm' and driver_age >= 30) or (driver_gender == 'f' and driver_age >=25):
    print("Driver is Unmarried but insured")

else:
    print("Driver is Not Insured because he/she not full filling the criteria")
