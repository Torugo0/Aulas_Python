from funcoes import exibe_matriz, exibe_matriz_aleatoria_nr

matriz = exibe_matriz_aleatoria_nr(7,7)
maiores = []

for i in range(len(matriz)):
    maior = 0
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    maiores.append(maior)

exibe_matriz(matriz)
print(maiores)