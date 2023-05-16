# Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, e os números ímpares em outra lista.Exiba as duas listas ao usuário.

pares = []
impares = []

for i in range(10):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f"Lista com números pares: \n{pares}")
print(f"Lista com números impares: \n{impares}")