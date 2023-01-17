count = 0
total = 0.0

while True:
    string_value = input("Enter a number: ")
    if string_value == "done" :
        break
    try:
        float_value = float(string_value)
    except:
        print("Invalid input")
        continue

    count = count + 1
    total = total + float_value

print("ALL DONE", total, count, total/count)