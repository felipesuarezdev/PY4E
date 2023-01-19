fname = input("Enter file name: ")
fh = open(fname)
lista = list()

for line in fh:
    list_of_words = line.split()
    for word in list_of_words:
        if word in lista:
            continue
        else: 
            lista.append(word)

lista.sort()
print(lista)
