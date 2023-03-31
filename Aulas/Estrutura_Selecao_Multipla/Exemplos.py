'''

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case _:
        print("Nenhuma das opções anteriores")

| == ou

'''
# Bom usar quando tem multiplas verificações 

# Versão da calculadora com Match Case

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma opção: "))


match opcao:
    case 1:
        c = a + b
        print(f"A soma de {a} e {b} é {c}")
    case 2:
        c = a - b
        print(f"A subtração de {a} e {b} é {c}")
    case 3:
        c = a * b
        print(f"A multiplicação de {a} e {b} é {c}")
    case 4:
        if b != 0:
            c = a / b
            print(f"A divisão de {a} e {b} é {c}")
        else:
            print("Não é possivel fazer uma divisão por zero !!")
    case _:
        print("Nenhuma das opções anteriores")