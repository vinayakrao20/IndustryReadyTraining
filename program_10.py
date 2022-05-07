# 10. Write a program to find the simple interest and compound interest.
principal = float(input("Enter Amount "))
rate = float(input("Enter Intrest rate "))
time = float(input("Enter Time Duration  "))
#formula of ci and si
simple_intrest = (principal*time*rate)/100
compound_intrest = principal * ((1+rate/100)**time - 1)
print(f' Simple Intrest is : {simple_intrest}')
print(f' Compound Intrest is : {compound_intrest}' )