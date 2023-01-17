

def computepay(hours, rate):
    if float(hours) <= 40:
        return float(hours) * float(rate)
    elif float(hours) > 40:
        exhours = float(hours) - 40
        exrate = float(rate) * 1.5
        extrapay = float(exhours) * float(exrate)
        hours = float(hours) - float(exhours)
        return (float(hours) * float(rate)) + extrapay

pay = computepay(input("Enter Hours: "), input("Enter Rate: "))
print("Pay", pay)
