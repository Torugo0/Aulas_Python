#Fazer um algoritmo que soliciteum número inteiro Nqualquer e exiba a tabuada de N.

from unittest import result


nTabuada = int(input("Digite um número: "))
multi = 1
cont = 1

while (cont <= 10):
    resultado = nTabuada *multi
    print (resultado)
    multi += 1
    cont += 1