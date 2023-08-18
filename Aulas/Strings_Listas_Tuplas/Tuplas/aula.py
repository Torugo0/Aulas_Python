# Tuplas 
# Sequência de itens
# Estruturas imutáveis (Não podem ser modificadas)
# Parenteses ao inves de colchetes

tupla = (1,2,3,4)

# Tuplas são heterogêneas
tupla = (3, "abc", 3.5)

# Para acessar:
print(tupla[0])

# Index - retorna o indice de um determinado item
print(tupla.index(3))

# count - conta a quantidade de vezes que um item aparece na tupla
print(tupla.count(3))

# Operador in - busca um item na tupla e retorna true ou false
if 3 in tupla:
    print("Existe")
else:
    print("Não existe")

# Concatenação 
tupla1 = (1,2,3)
tupla2 = (20,30,60)
tupla3 = tupla1 + tupla2
print(tupla3)

def teste(a,b):
    soma = a + b
    subtracao = a - b
    return soma, subtracao

resultado = teste(30,7)[1] # --> Exemplo de como usar uma tupla ([1]) em lista
print(resultado)

# Tupla com 1 unico item
tupla = (10) # --> Não é uma tupla, identifica como um valor entre parenteses (int). Para tornar tupla, adicione uma virgula.

# list - copia os itens de  uma tupla para uma lista
tupla = (4,5,6)
lista = list(tupla)

# Tuple - copia os itens de umalista para uma tupla
lista = [10,5,8]
tupla = tuple(lista)

# Copia de lista ou de tupla
lista = [1, 2, 3]
lista2 = lista
lista2.append(100)
print(lista)
print(lista2)

# FATIAMENTO // SLICE
# Seleciona um pedaço de uma string (ou lista, ou tupla)
#[Inicio: Fim : Passo]

nome = "Vitor Hugo"
primeiro_nome = nome[0:5]
print(primeiro_nome)