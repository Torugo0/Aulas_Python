from random import randint

def preenche_matriz(lin: int, col: int) -> list: 
    '''Preenche a matriz com entradas do usuário '''
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n = int(input("Digite um número: "))
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibe_matriz_aleatoria(lin: int, col: int) -> list: 
    '''Preenche a matriz com números aleatórios '''
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            n = randint(1,50)
            linha.append(n)
        matriz.append(linha)
    return matriz

def exibe_matriz_aleatoria_nr(lin: int, col: int) -> list: 
    '''Preenche a matriz com números aleatórios '''
    matriz = []
    usados = []
    for i in range(lin):
        linha = []
        while len(linha) < col:
            n = randint(1,50)
            if n not in usados:
                usados.append(n)
                linha.append(n)
        matriz.append(linha)
    return matriz

def exibe_matriz(matriz: list) -> None:
    '''Exibe matriz'''
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()