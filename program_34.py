# 34. Write a program to read a 3-digit number and find whether the middle digit is numerically equal 
# to the sum of the other two digits and prints an appropriate response.

num = int(input("Enter 3 digit Number : "))
last_digit = num%10
first_digit = num//100
middle_digit = (num//10)%10
print(f"First Digit is {first_digit},middle_digit is {middle_digit} and last_digit is {last_digit}")
sum = first_digit + last_digit
if (sum == middle_digit):
    print(f"Sum of first and second number is {sum} and Middle Digit number {middle_digit} are same")
else :
    print(f"Sum of first and second number is {sum} and Middle Digit number {middle_digit} are Not same")