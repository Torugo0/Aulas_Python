import random

def random_number():
    aleatorio = random.random() *100
    format_aleatorio = (f"{aleatorio:.0f}")
    return format_aleatorio

def exibe_matriz(matriz):
    for linha in matriz:            # exibe a matriz formatada
        for item in linha:
            print(item, end='\t')
        print()

matriz = []

for linha in range(5):
    lista = []
    for coluna in range(5):
        n = int(random_number())
        lista.append(n)
    matriz.append(lista)
exibe_matriz(matriz)

somatorio = 0
for i in range(len(matriz)):
    somatorio += matriz[i][i]

print(somatorio)