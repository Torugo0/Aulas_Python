def parimpar(num):
    return (num % 2 == 0)

    
numero = int(input("Digite um número inteiro: "))
if parimpar(numero):
    print(parimpar(numero))
else:
    print("O número é ímpar")