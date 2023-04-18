menor = float("inf")

for i in range (1,11):
    numero = int(input("Digite um número: "))
    if numero < menor:
        menor = numero
print(f"O menor número da sequencia digitada é: {menor}")