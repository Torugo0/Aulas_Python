# Escreva um algoritmo que solicite 15 números e informe o somatório  de todos os números ímpares digitados.

cont = 1
somaImpar = 0

while (cont <= 15):
    numero = int(input("Digite um número: "))
    if numero % 2 != 0:
        somaImpar = numero + somaImpar
    cont += 1
print(f"A soma dos números impares digitados é: {somaImpar}")