def exibe_matriz(matriz):
    for linha in matriz:            # exibe a matriz formatada
        for item in linha:
            print(item, end='\t')
        print()

matriz = []

for linha in range(3):
    lista = []
    for coluna in range(5):
        n = int(input("Digite um número: "))
        lista.append(n)
    matriz.append(lista)
exibe_matriz(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 100:
            matriz[i][j] = 0
exibe_matriz(matriz)