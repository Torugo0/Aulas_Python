'''
SINTAXE

try:
    a = int(input("Informe um número: "))
    b = int(input("Informe um número: "))
    c = a/b
    print("A divisão é: ", c)
except TypeError:


RAISE = Permite forçar a ocorrência de uma exceção especifica, não precisa estar dentro de um try 

try:
    raise TypeError 
except NamerError:
    print("Ocorreu um erro")

Outro tipo:

try:
    raise TypeError('ERRO!')
except TypeError as mensagem:
    print(f"Ocorreu um erro: {mensagem}")



O não tratamento da exceção faz o programa parar, mas caso seja tratado, pode continuar o programa.
'''


# Função para somar dois números inteiros

# EXEMPLO 1
'''
def soma (a,b):
    if type(a) == int and type(b) == int and a > 0 and b > 0:
        c = a + b
        print(f'Resultado da soma: {c}')
    else:
        raise TypeError('Os tipos de parametros devem ser inteiros e positivos.')
    
while True:
    try:
        a = int(input("Informe o primeiro número: "))
        b = int(input("Informe o segundo número: "))
        if a == 0 and b == 0:
            break
        try:
            soma(a,b)
        except TypeError as msg:
            print(f'ERRO: {msg}')
    except ValueError:
        print("ERRO: os valores devem ser inteiros")
'''

# EXEMPLO 2 

#'''


#'''

while True:
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("ERRO: Você deve digitar um valor entre 1-5")
    else:
        if opcao == 5:
            print("Fim do Programa")
            break
    
        try:
            if opcao >= 1 and opcao <=4:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número: "))
        except ValueError:
            print("ERRO: Os valores informados não são números")
        else:
            if opcao == 1:
                print(f"Soma: {a+b}")
            elif opcao == 2:
                print(f"Subtração: {a-b}")
            elif opcao == 3:
                print(f"Multiplicação: {a*b}")
            elif opcao == 4:
                try:
                    print(f"Divisão: {a/b}")
                except ZeroDivisionError:
                    print("ERRO: ocorreu uma divisão por zero")
                else:
                    print("Opção inválida")
            else: 
                print("Opção invalída")
    