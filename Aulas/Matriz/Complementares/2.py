from funcoes import preenche_matriz, exibe_matriz

matriz = preenche_matriz(5,5)
print(exibe_matriz(matriz))

transposta = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(matriz[j][i])
    transposta.append(linha)

print(exibe_matriz(transposta))

simetrica = True
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] != transposta[j][i]:
            simetrica = False
            break

if simetrica:
    print("A matriz é simetrica")
else:
    print("A matriz não é simetrica")