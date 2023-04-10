# Escreva um algoritmo que solicite 10 números e informe quantos números entre 100 e 200 foram digitados.

cont = 1
numGrandes = 0

print("Digite apenas números inteiros de 0 a 200")

while (cont <= 10):
    numero = int(input("Digite um número: "))
    if numero >= 100 and numero <= 200:
        numGrandes += 1
    cont += 1
print(f"A quantidade de números entre 100 e 200 é: {numGrandes}")