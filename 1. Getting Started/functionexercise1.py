#Rewrite your pay computation with time-and-a-half for overtime
#and create a function called computepay wich takes two parameters(hours and rate)


def computepay(hours, rate):
    return float(hours) * float(rate)

pay = computepay(input("Enter Hours: "), input("Enter Rate: "))
print("Pay:", pay)
