# Write a program to read the marks of 3 subjects and display the total, average, class.

maths = float(input("Enter Marks of  Maths : "))
physics = float(input("Enter marks of physics : "))
chemistry = float(input("Enter marks of chemistry : "))

# formula of average (a+b+c)* no. of subjects

total = maths + physics + chemistry 

average = total/3    # average of 3 subjects
print(f"Total marks of subject's is {total} and average is {average}")
