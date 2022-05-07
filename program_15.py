# 15. Two numbers are input into two locations ‘a’ and ‘b’. Write a program to interchange the contents 
# of ‘a’ and ‘b’ without using temporary variables.

x = 6
y = 10
print("Before swapping")
print("value of x : ", x ," and y : ", y)
print("After Swapping")
x, y = y, x       #this method works for any datatypes
print("value of x : ", x ," and y : ", y)
