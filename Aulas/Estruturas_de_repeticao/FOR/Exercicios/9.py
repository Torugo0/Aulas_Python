# Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número.

numero = int(input("Digite um número: "))

for i in range(1, numero+1):
    if numero % i == 0:
        print(i)