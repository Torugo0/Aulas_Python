# Fazer  um  algoritmo  que  leia  um  número  inteiro  positivo,  calcule  e  escreva  se  o  número  lido  é  um  número perfeito ou não. Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao próprio número. Exemplo: 6 é um número perfeito porque 1 + 2 + 3 = 6.

numero = int(input("Digite um número: "))
cont = 1
soma = 0

while (cont < numero):
    if numero % cont == 0:
        soma += cont
    cont += 1

if soma == numero:
    print("Número perfeito")
else:
    print ("Número não perfeito")