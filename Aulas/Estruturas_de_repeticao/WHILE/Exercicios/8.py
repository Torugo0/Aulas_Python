# Escreva um algoritmo que solicite 10 números e informe qual foi o menor número digitado.

cont = 1
menor = float("inf")

while (cont <= 10):
    numero = int(input("Digite um número: "))
    if numero < menor:
        menor = numero
    cont += 1
print(f"O menor número digitado foi: {menor}")
