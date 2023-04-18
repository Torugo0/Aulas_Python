# Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i
print(fatorial)