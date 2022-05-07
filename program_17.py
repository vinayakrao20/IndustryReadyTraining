#17. Rajesh’s basic salary is input through the keyboard. His D.A. is 40% of basic salary, and 
# H.R.A. is 20% of basic salary. Write a program to calculate his gross salary.

basic_salary = float(input("Enter Rajesh Basic salary : "))
# D.A is 40% and H.R.A is 20% of basic salary
da = basic_salary * .4
hra = basic_salary* .2
gross_salary = (basic_salary + da + hra)
print(f"Rajesh Gross Salary is {gross_salary}")