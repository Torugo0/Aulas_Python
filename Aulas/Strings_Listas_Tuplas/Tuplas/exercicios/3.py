
def vogais(palavra):
    cont = 0
    lista = 'aeiou'
    for c in palavra.lower():
        if c in lista:
            cont += 1
    return cont

palavra = input("Digite uma palvra: ")

print(f"Quantidade de vogais: {vogais(palavra)}")