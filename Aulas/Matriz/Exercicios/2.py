matriz = []
for linha in range(6):
    lista = []
    for coluna in range(6):
        if coluna == linha:
            n = 1
            lista.append(n)
        else:
            n = 0
            lista.append(n)
    matriz.append(lista)


for linha in matriz:
    for item in linha:
        print(item, end="\t")
    print()