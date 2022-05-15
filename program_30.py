# 30. Write a program to read positive numbers continuously until negative number
# is given by using ‘if’.
i = 0
x = (10,20,30,40,23,-50,40,78,67) 
print("Given Nubmer")
print(x)
for i in x :    # Read Numbers continously 
    print(i)
    if(i < 0):   # it will break the loop
        print(f"{i} is negative so breaking the loop ")
        break;

