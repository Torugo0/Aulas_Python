def ler_numero():
    numero = int(input("Digite um número: "))
    return numero

def tabuada():
    numero = None
    while (numero != 0):
        numero = ler_numero()
        for i in range (1,11):
            tabu = numero * i
            print(f"{numero} X {i} = {tabu}")
        print("\n")

tabuada()