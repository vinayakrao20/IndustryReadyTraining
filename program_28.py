# 28. Write a program to check whether the given year is leap year or not.

year = int(input("Enter Year : "))

if year%4 == 0 :
    print(f"{year} is a Leap Year")    # leap is  divisible by 4 beacuse its come in every four year
else :
    print(f"{year} is not a Leap Year")