# 24. Write a program to check whether the given number is positive or negative.

a = int(input("Enter number "))

# we are using if elif else for condition check

if a > 0 :
    print(f" Given number {a} is Positive")

elif a < 0 :
    print(f" Given number {a} is Negative")

else :
    print(f" given number {a} is zero") 