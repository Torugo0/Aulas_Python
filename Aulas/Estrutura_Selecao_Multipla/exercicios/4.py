print("1 - Palestra de Linux")
print("2 - Palestra de Banco de Dados")
print("3 - Palestra de Windows Server")
print("4 - Palestra de Logica e Programação")

opcao = int(input("Informe a opção desejada: "))

match opcao:
    case 1:
        print("Palestra no Auditório 1")
    case 2:
        print("Palestra no Auditório 2")
    case 3:
        print("Palestra no Auditório 3")
    case 4:
        print("Palestra no Auditório Principal")
    case _:
        print("Opção inexistente")