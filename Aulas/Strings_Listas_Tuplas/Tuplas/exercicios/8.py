def numbers_list():
    lista = []
    pares = 0
    impares = 0
    for i in range (1,11):
        number = float(input("Digite um numero: "))
        lista.append(number)
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += n
    return pares, impares

tupla = numbers_list()

print(f"A quantidade de pares na lista é: {tupla[0]}")
print(f"A soma dos impares é: {tupla[1]}")
