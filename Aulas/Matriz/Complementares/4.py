from funcoes import exibe_matriz, exibe_matriz_aleatoria_nr

matriz = exibe_matriz_aleatoria_nr(6,6)
exibe_matriz(matriz)

for i in range(len(matriz)):
    maior = 0
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            
    for j in range(len(matriz[i])):
        matriz[i][j] = maior * matriz[i][j]

exibe_matriz(matriz)