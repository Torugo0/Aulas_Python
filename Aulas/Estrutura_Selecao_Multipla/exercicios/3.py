numero = int(input("Digite um número inteiro: "))

resto = numero % 3

match resto:
    case 0:
        print("Múltiplo de 3")
    case _: 
        print("Não é múltiplo de 3")