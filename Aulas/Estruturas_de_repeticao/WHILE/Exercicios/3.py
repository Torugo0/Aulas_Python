# Escreva  um  algoritmo  que solicite a  idade  de  15  pessoas  e  informe  a  quantidade  de pessoas com idade inferior a 18 anos.

cont = 1
menores = 0

while (cont <= 15):
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        menores += 1
    cont += 1
print(f"A quantida de menores de idade é: {menores}")