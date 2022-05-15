# 27. Write a program to find biggest of given three numbers.

a = int(input("Enter number : "))
b = int(input("Enter number : "))
c = int(input("Enter number : "))

if (a > b) and (a > c) :
    print(f"{a} is Biggest number ")

elif (b > a) and (b > c):
    print(f"{b} is Biggest number")

else :
    print(f"{c} is Largest number")