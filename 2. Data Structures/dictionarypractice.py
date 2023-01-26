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

py_dict = dict()
for sender in lista:
    py_dict[sender] = py_dict.get(sender, 0) + 1
    # print(py_dict)

bigcount = None
bigsender = None
for sender,count in py_dict.items():
    if bigcount is None or count > bigcount:
        bigsender = sender
        bigcount = count

print(bigsender, bigcount)

