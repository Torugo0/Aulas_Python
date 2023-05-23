from random import randint
# Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50e exiba:
# a. A lista com todos os itens armazenados.
# b. O somatório de todos os números contidos na lista.
# c. O maior número da lista.
# d. O menor número da lista.

itens = []
soma = 0
menor = float("inf")
maior = 0

for i in range (20):
    n = randint(1,50)
    itens.append(n)
    soma = soma + n
    if (n < menor):
        menor = n
    if (n > maior):
        maior = n


print(f"A lista com os números sorteados: \n{itens}\n")
print(f"A soma de todos os itens da lista: \n{soma}\n")
print(f"O maior número da lista: {maior}")
print(f"O menor número da lista: {menor}")