# Fazer um algoritmo que exiba na tela todos os números ímpares de 1 a n, onde n é fornecido pelo usuário.

N= int(input("Digite um número: "))
cont = 1 
impares = 0
numero = 1

while (cont <= N):
    print(numero)
    if numero % 2 != 0:
        impares +=1
    numero += 1
    cont += 1
    
print(f"A quantidade de numeros impares de 1 a {N} foram: {impares}")