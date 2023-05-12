# Crie uma função que receba três números como parâmetros, e retorne True se a soma de quaisquer pares de números gera a soma do terceiro número. Caso contrário retorne False.

def soma(a, b, c):
    if a<0 or b<0 or c<0:
        raise TypeError
    if (a+b == c):
        return True
    elif (a+c == b):
        return True
    elif (b+c == a):
        return True
    else:
        return False

while True: 
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        c = float(input("Digite o terceiro número: "))
        print(soma(a, b, c))
    except ValueError:
        print("ERRO: Os valores informados não são números!")
    except TypeError:
        print("ERRO: Os números são negativos, informe apenas positivos")
    else:
        print("Programa finalizado")
        break

