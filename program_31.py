# 31. Write a program to read ten numbers and print their sum by using ‘if’ statement.

num = int(input("enter 10 numbers"))
result= 0
while num > 0 :
    didgit = num%10 # give last digit number
    result = result + didgit
    num = num // 10  # it will remove lst digit 123//10 = 12

print("Sum of Numbers is : ",result)