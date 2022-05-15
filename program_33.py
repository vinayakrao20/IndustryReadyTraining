# 33. Write a program to calculate the monthly income of a person using the
# following commission schedule:
''' Monthly sales income
>= Rs.50,000 Rs.375 + 16% sales.
>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales.
<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales.
<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales.
<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales.
<= Rs.10,000 Rs. 200+3% sales. '''
# after reading income below are the different conditions
income = float(input("Enter Monthly Income : "))
if (income >= 50000) :
    commission =  375 + (income * 0.16)    # 16% = 0.16 because of by 100
elif (income <= 50000) and (income >= 40000) :
    commission = 350 + (income * 0.14)
elif (income <= 40000) and (income >= 30000) :
    commission = 325 + (income * 0.12)
elif (income <= 30000) and (income >= 20000) :
    commission = 300 + (income * 0.09)
elif (income <= 20000) and (income >= 10000) :
    commission = 250 + (income * 0.05)
elif (income <= 10000) :
    commission = 200  + (income * 0.02)
salary = income + commission
print(f"Based on Income {income} Total Commission is {commission} and Salary is {salary}")
