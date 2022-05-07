# 12. Write a program to convert the given seconds into hours – minutes – seconds.
seconds = int(input("Enter seconds  "))
hour = seconds//3600
minute = (seconds%3600)//60
sec = (seconds%3600)%60
print(f' {hour} Hour')
print(f' {minute} Minute')
print(f' {sec} Seconds')