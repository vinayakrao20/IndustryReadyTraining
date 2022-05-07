# 9. Write a program to find your age in days.
from datetime import datetime  # imports datetime package
date_of_birth = datetime(1996, 12, 20)   # need to  pass year , month,day
count_days = datetime.today() - date_of_birth  # subtract D.O.B with current date  
print (f'Your Age in Days are {count_days.days}')  #  printing age in days