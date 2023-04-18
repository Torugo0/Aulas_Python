# Escreva um algoritmo que determine se um número N (digitado pelo usuário) é primo ou não.
numero = int(input("Digite um número: "))
divisores = 0

for i in range (1, numero+1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("Número primo")
else:
    print("Não é primo")