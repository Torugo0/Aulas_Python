def list_numbers():
    lista = []
    for i in range(1,11):
        number = float(input("Digite um número inteiro: "))
        lista.append(number)
    maior = max(lista)
    menor = min(lista)
    media = sum(lista)/len(lista)
    return maior, menor, media

tupla = list_numbers()

print(f"O MAIOR numero da Lista é: {tupla[0]}")
print(f"O MENOR numero da Lista é: {tupla[1]}")
print(f"A MEDIA numero da Lista é: {tupla[2]}")
