# Escreva um algoritmo que solicite 10 números e exiba o dobro de cada número digitado.


cont = 1
pares = 0

while (cont <= 10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0: 
        pares += 1
    cont += 1
print (f"A quantidade de números pares é: {pares}")