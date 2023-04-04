numero = float(input("Número: "))

print("Opção 1 - O dobro")
print("Opção 2 - A metade")
print("Opção 3 - 10% do número")

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        resultado = numero * 2
        print(f"O dobro de {numero} é {resultado}")
    case 2: 
        resultado = numero / 2
        print(f"A metade de {numero} é {resultado}")
    case 3:
        resultado = numero * 0.10
        print(f"10% de {numero} é {resultado}")
    case _:
        print("Opção inavalída")