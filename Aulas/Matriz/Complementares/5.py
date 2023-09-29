from funcoes import exibe_matriz, preenche_matriz

matriz = preenche_matriz(4,4)
exibe_matriz(matriz)
verifica = []
coluna = []

for i in range(len(matriz)):
    cont = 0
    for j in range(len(matriz[i])):
        cont += matriz[i][j]
    verifica.append(cont)

    col = 0
    for j in range(len(matriz[i])):
        col += matriz[j][i]
    coluna.append(col)

for i in range(len(verifica)):
    for j in range(len(verifica[i])):
        if verifica[i][j] == coluna[i][j]:
            print("ok")
        else:
            print("Não")

print(verifica)
print(coluna)