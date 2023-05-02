def menu():
    print("Calculadora feita em Python \n")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão \n") 
    opcao = int(input("Escolha uma opção: \n"))
    return opcao

def adicao():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    soma = num1 + num2
    return soma

def subtracao():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    sub = num1 - num2
    return sub

def multiplicacao():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    mult = num1 * num2
    mult = round(mult , 2)
    return mult

def divisao():
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    
    if (num2 != 0):
        div = num1 / num2
        div = round(div, 2)
        return div
    else:
        print("Não é possivel fazer uma divisão por zero !!")

def calculadora():
    opcao = None
    while (opcao != 5):
        opcao = menu()
        match opcao:
            case 1:
                print(f"{adicao()}\n")
            case 2:
                print(f"{subtracao()}\n")
            case 3:
                print(f"{multiplicacao()}\n")
            case 4:
                print(f"{divisao()}\n")
            case _:
                print("Digite uma opção valida !!")

calculadora()