#Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Por exemplo: 120 é triangular, pois 4 * 5 * 6 = 120. 2730 é triangular, pois 13 * 14 * 15 = 2730. Faça uma função que receba um número inteiro e retorne True se for um número triangular e False, caso contrário.

def triangular(numero):
    if type(numero) != int or numero < 0:
        raise TypeError

    for a in range(numero):
        if (a* (a+1) * (a+2) == numero):
            return True
    return False

while True:
    try:
        numero = int(input("Digite um número (0 para finalizar): "))
        if numero==0:
            break
        if triangular(numero) == True:
            print(f"O número {numero} é triangular")
        else:
            print(f"O número {numero} não é triangular")
    except ValueError:
        print("ERRO: O valor informado não é inteiro")
    except TypeError:
        print("O número deve ser natural")
    else:
        break