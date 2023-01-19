fname = input("Enter file name: ")
handle = open(fname)
lista = list()
count = 0

for line in handle:
    if line.startswith("From:"):
        mail = line.split(" ")
        lista.append(mail[1].rstrip())
    else:
        continue

for address in lista:
    print(address)
    count = count + 1

print ("There were", count, "lines in the file with From as the first word")