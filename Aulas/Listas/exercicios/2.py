# Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
#   a) A média aritmética dos números armazenados na lista.
#   b) O somatório dos números pares armazenados na lista.


aritmetica = []
pares = []
somapares = 0
soma = 0

for i in range(10):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        somapares = somapares + n
        pares.append(n)
    aritmetica.append(n)
    soma = soma + n
quantidade = len(aritmetica)

media = soma / quantidade

print(f"A media aritmetica dos números digitados é: {media}")
print(f"A soma dos pares é: {somapares}")
    
