# STRINGS
'''
# SEQUENCIA DE CARACTERES 
# String funciona como uma lista, so que de caracteres

texto = "Exemplo de texto"
a = texto [0]
print(a) #RETORNA A LETRA (E)

for c in texto: 
    print(c)

# Tamanho da string
tamanho = len(texto)

# Operador in (busca)
if "texto" in texto:
    print("existe na string")

# Upper (converte para maiusculo) 
x = (texto.upper())
print(x)

# Lower (converte para minúsculo)
print(texto.lower())

# title (Coloca as iniciais de cada palavra em maiusculo)
print(texto.title())

# capitalize (Apenas o primeiro em maiusculo)
print(texto.capitalize())

# Strip (Remove os espaços em branco do inicio e do final)
# lstrip ->  remove apenas do começo
# rstrip -> Remove apenas do fim
texto = "   exemplo de texto    "
print(texto.strip().upper())

# Count (conta a quantidade de vezes que um caracter aparece a string)
texto = "exemplo de texto"
print(texto.count("e"))# Pode ser uma string("e") ou substring("texto")

# Replace (Substitui uma substring por outra)
texto = "Banana, Laranja e Maça"
texto = texto.replace("Laranja", "Melância")
print(texto)

# Split (Divide uma string de acordo com um separador) - retorna uma lista 
texto = "Banana, Laranja e Maça"
frutas = texto.split(", ") # Retorna Lista
print(frutas)
'''

# LISTAS
# Estrutura de dados
# Delimitadas por []

lista = [3, 4, 5, 6]
print(lista)

# Listas são heterogêneas (itens de tipos diferentes)
lista = [3, 266, "abc", 4, "Vitor"]
print(lista)

# Listas são mutaveis (Podem ser alteradas)
lista = [1, 2, 3, 4]
lista[0] = 100
print(lista)

# Listas são acessadas pelo indice, sempre começa com o indice 0 ([0])
print(lista[0])

# Indices negativos começam sempre em -1 (acessam a lista de tras pra frente)
lista = [0, 9, 8, 7]
print(lista[-1])

# Len, retorna o tamanho da lista
print(len(lista))

# Append, adiciona um elemento ao final da lista
lista.append(300)
print(lista)

# Insert -> para adicionar em uma posição especifica
lista.insert(0,99) #Primeiro o indice, deois o valor
print(lista)

# pop -> remove o ultimo elemento da lista
lista = [1,2,3,4]
lista.pop()
print(lista)

# pop(indice) -> Remove o item do indice especifico
lista.pop(-2)
print(lista)

# Remove -> Remove um item especifico
lista = [1,2,3,4]
lista.remove(2)
print(lista)

# count - conta quantas vezes um item aparece na lista
lista = [3,4,5,6,8,7,0]
print(lista.count(5))

# Index -> retorna o indice de um elemento
(print(lista.index(5)))

# Sort -> Ordena uma lista em ordem crescente
lista.sort()
print(lista)

lista.sort(reverse = True) # Ordem decrescente
print(lista)

#lista = ["Vitor", "Ana", "Zurich"]
lista.sort()
print(lista)

# Max -> Retorna o maior elemento da lista
print(max(lista))

# Min -> Retorna o menor elemento da lista
print(min(lista))

# sum -> Retorna o somatoria da lista 
print(sum(lista))

# media 
media = sum(lista) / len(lista)
print(media)

# Preencher lista com itens informados pelo usuario
lista = []
for i in range (5):
    n = int(input("Digite um número inteiro: "))
    lista.append(n)

print(lista)

# Percorrer item da lista 

lista = [4,5,67,9]
cont = 0 

for item in lista: # For cada item da lista
    print(item)
    cont += 1

# Percorrer indices da lista

for i in range (len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)


# Concatenação (juntar listas)
lista1 = [1,2,4]
lista2 = ["Vitor", "Ana", "Carol"]
lista3 = lista1 + lista2
print(lista3)