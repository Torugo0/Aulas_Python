# Solicite vários números ao usuário (até que ele digite o número zero) e informe o somatório dos números digitados.

print("Digite 0 para parar a somatoria")

numero = None
soma = 0

while numero != 0:
    if numero != 0:
        numero = int(input("Digite um número: "))
        soma = numero + soma
print(f"A somatoria dos números digitados é: {soma}") 