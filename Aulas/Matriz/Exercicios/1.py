def exibe_matriz(matriz):
    for linha in matriz:            # exibe a matriz formatada
        for item in linha:
            print(item, end='\t')
        print()

matriz = []
for linha in range(3):
    lista = []
    for coluna in range(5):
        n = int(input("Número: "))
        lista.append(n)
    matriz.append(lista)
    print()
exibe_matriz(matriz)