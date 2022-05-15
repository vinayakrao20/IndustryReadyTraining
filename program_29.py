# 29. Write a program to find the roots of a given quadratic equation and print the nature of roots.

a = float(input("Enter value of a "))
b = float(input("Enter value of b "))
c = float(input("Enter value of c "))

#  Quadratic equation formula, x = (-b ± √ (b² - 4ac) )/2a.
# first we have to find value of d for nature of roots d=2b-4ac

d = 2*b - 4*a*c
print(f"Value of d is {d}")
# nature of roots based on d values
if d > 0 :
    r1 = (-b + (b**2 -4*a*c)**.5) / (2*a)
    r2 = (-b + (b**2 -4*a*c)**.5) / (2*a)
    print(f" The Roots are Real and diffrent {r1} and {r2}")
elif d == 0 :
    r1 = -b/(2*a)
    r2 = -b/(2*a)
    print(f"roots are real equal {r1} and {r2} ")
else :
    print("Roots are imaginary")

