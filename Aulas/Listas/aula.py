'''
ANOTAÇÕES:

List = um tipo de dado que armazena uma sequencia de varios itens, organizados sequencialmente
    - Devem ser delimitados por colchetes [], e separados por virgulas
    - Uma lista pode ser atribuida a uma váriavel 
    - Em uma lista pode ter diferente tipos de dados (Strings, int, float)

Exemplo:
    numeros = [5,1,10,50]
    nomes = ["Vitor", "Ana", "Paulo"]
    lista = [] #LISTA VAZIA

ACESSANDO OS ITENS:
    - Para acessar os itens da lista, utilizamos os índices.
    - Cada posição é idntificada por um índice.
    - O primeiro número da lista é o índice 0, e os demais são incrementados por unidade.

    ÍNDICES NEGATIVOS:
        - Representam posições a partir do final da lista 
        - O índice -1 é o ultimo item, o índice -2 é o penúltimo

    COMO EXIBIR:
        - print(nomes[0]) # Printa "Vitor"
    
    OPERAÇÕES DENTRO DE LISTAS
    x = numeros[0] + numeros[2]
    # Quando printar X vai ser exibido 15
    # Podemos guardar essa soma em algum item da lista (numeros[1] = numeros[0] + numeros[2])

    TROCA DE ELEMENTO NA LISTA:
            NOMES[1] = "Ana clara"
            - Quando printar o nome da posição 1 vai ser trocada de "ana" para "ana clara"

    FUNÇÃO LEN():
        - Retorna o tamanho da lista 
        n = len(nomes)
        # Vai exibir o número 3, que é a quantidade de nomes na lista 

    FUNÇÃO APPEND():
        - Adiciona elementos na lista
        - Sempre se adiciona um item por vez
        - O item é adicionado ao fim da lista
    
        nome.append("José") # Adiciona o nome a lista

    FUNÇÃO POP():
        - Remove algum item da lista
        - Com parametro remove o desejado, sem parametro remove o ultimo item

        nomes.pop(0) # Remove o primeiro nome

'''

# Exemplo para preencher uma lista com itens a partir de entrada dos usuarios
''' 
numeros = []

# Com for: 
for i in range (5): #Lista com 5 itens
    n = int(input("Infrome um número: "))
    numeros.append(n)
print(numeros)


# Com while:
while True:
    n = int(input("Informe um número: "))
    if n == 0:
        break
    numeros.append(n)
print(numeros)
'''

# EXEMPLOS:

'''
1)

# Preenche uma lista
lista = []

for i in range (10): #Lista com 5 itens
    n = int(input("Infrome um número: "))
    lista.append(n)
print(lista)

# Percorre os itens da lista 

cont = 0
for item in lista:
    if (item % 2 == 0):
        cont += 1
print(f"Quantidade de numeros pares: {cont}")
'''

#2)

def busca(lista,item):
    for n in lista:
        if n == item:
            return True
    return False

# Preenche uma lista
lista = []
while True:
    n = int(input("Informe um número inteiro (0 para finalizar): "))
    if (n == 0):
        break
    lista.append(n)
print (lista)


item = int(input("Informe um número para buscar na lista: "))
if busca(lista,item):
    print("O número está contido na lista")
else:
    print(f"O {item} não está contido na lista")