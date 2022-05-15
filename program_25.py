# 25. Write a program to find out the given number is odd or even.

a = int(input("Enter Number : "))
#condition for odd even

if (a%2 == 0):
    print(f"Given number {a} is Even") # when even is divided by 2 reminder will be always 0
else :
    print(f"Given Number {a} is Odd")

