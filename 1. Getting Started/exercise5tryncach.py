#new script of exercise2
#the hourly rate for hours worked above 40 hours.
#adding error msge with try n cach

hours = input("Enter Hours: ")
try:
    rate = input("Enter Rate: ")
    pay = float(hours) * float(rate)
    print("Pay:", pay)
except:
    print("Error, please enter numeric input") 

