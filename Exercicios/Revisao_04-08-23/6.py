def soma_divisores(numero):
    numeros = []
    soma = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            soma += i
            numeros.append(i)
    return soma, numeros

numero = int(input("Digite um número: "))
print(f"A soma de todos os divisores de {numero} é: {soma_divisores(numero)[0]} {soma_divisores(numero)[1]}")