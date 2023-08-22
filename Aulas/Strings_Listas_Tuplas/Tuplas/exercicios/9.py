def numbers_list():
    lista = []
    pares = []
    impares = []
    for i in range (1,11):
        number = float(input("Digite um numero: "))
        lista.append(number)
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return lista ,pares, impares

tupla = numbers_list()

print(f'''Lista de números: {tupla[0]}
Lista dos números pares: {tupla[1]}
Lista dos numeros impares: {tupla[2]}
''')