# Fazer um algoritmo que soliciteum número indeterminado de idades de um grupo de indivíduos. A última idade, que não entrará nos cálculos, contém o valor da idade igual a zero. Calcule a média de idade deste grupo de indivíduos.

pessoas = int(input("Digite um número de pessoas: "))
cont = 1
soma = 0

while (cont < pessoas):
    idade = int(input("Digite uma idade: "))
    soma += idade
    cont += 1

pessoas = pessoas - 1
soma = soma / pessoas

print (f"A media de idade desse grupo é: {soma}")