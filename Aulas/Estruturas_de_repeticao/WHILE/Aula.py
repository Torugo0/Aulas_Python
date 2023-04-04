'''
cont = 1

while cont <= 10:
    print(cont)
    cont += 1
print("FIM")
'''

'''
# Ver se o número é par
cont = 1 
pares = 0 

while cont <= 10:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    cont += 1

print(f"A quantidade de pares é {pares}")
'''

'''
SOMA TODOS OS NÚMEROS NO INTERVALO DE 1 A 10

cont= 1
soma = 0   

while cont <= 10:
    soma += cont  
    cont+= 1
print(f'Somatório é {soma}')
'''

'''
EXIBE OS MULTIPLOS DE 3

cont = 1

while cont <= 20
    if cont % 3 == 0
    cont += 1 

'''

'''
CALCULADORA COM WHILE

'''
opcao = 0
while opcao != 5:

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao != 5:
        numero1 = float(input("Primeiro número: "))
        numero2 = float(input("Segundo número: "))

    if opcao == 1:
        resultado = numero1 + numero2
        print(f"A soma de {numero1} e {numero2} é {resultado}")
    elif opcao == 2:
        resultado = numero1 - numero2
        print(f"A subtração de {numero1} e {numero2} é {resultado}")
    elif opcao == 3:
        resultado = numero1 * numero2
        print(f"A multiplicação de {numero1} e {numero2} é {resultado}")
    elif opcao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"A divisão de {numero1} e {numero2} é {resultado}")
        else:
            print("ERRO: não é possivel fazer uma divisão por zero!!")
    elif opcao == 5:
        print("FIM DO PROGRAMA")
    else:
        print("Opção Inválida")