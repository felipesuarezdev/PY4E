#new script of exercise2 to give the employee 1.5 times 
#the hourly rate for hours worked above 40 hours.

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

if float(hours) <= 40:
    pay = float(hours) * float(rate)
elif float(hours) > 40:
    exhours = float(hours) - 40
    exrate = float(rate) * 1.5
    extrapay = float(exhours) * float(exrate)
    hours = float(hours) - float(exhours)
    pay = (float(hours) * float(rate)) + extrapay
        
print("Pay:", pay)