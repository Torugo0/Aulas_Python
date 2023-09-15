'''
Matriz é uma coleção de itens dispostos em uma tabela retangular organizada em linhas e colunas.

    - Para criar uma matriz se faz uma lista de listas
    matriz = [[1,2,3],
            [4,5,6],
            [7,8,9]]

'''
def exibe_matriz(matriz):
    for linha in matriz:            # exibe a matriz formatada
        for item in linha:
            print(item, end='\t')
        print()

#Criação de uma matriz
linhas = int(input("Quantidade de linhas: "))
colunas = int(input("Quantidade de colunas: "))

matriz = []
for linha in range(linhas):
    lista = []
    for coluna in range(colunas):
        n = int(input("Número: "))
        lista.append(n)
    matriz.append(lista)
exibe_matriz(matriz) 


# Percorrer os indices da matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 100
exibe_matriz(matriz)        

# Percorrer os itens da matriz
cont = 0
for linha in matriz:
    for item in linha:
        if item % 2 == 0:
            cont += 1
print(cont)