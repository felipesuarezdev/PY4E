#script to prompt the user for hourse and rate per hour to compute gross pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

pay = float(hours) * float(rate)
print("Pay:", pay)