
largest_num_sofar = -1
smallest_num_sofar = 10
numeros = [3, 45, 66, 90, 105, 2, 1]

for num in numeros:
    if largest_num_sofar < num:
        largest_num_sofar = num

for num in numeros:
    if smallest_num_sofar > num:
        smallest_num_sofar = num

print(largest_num_sofar)
print(smallest_num_sofar)

