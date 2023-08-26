def contar_vogais(texto):
    vogais = "aeiou"
    dic_vogais = {v : 0 for v in vogais}

    for letra in texto:
        if letra.lower() in vogais:
            dic_vogais[letra.lower()] += 1

    return dic_vogais

texto = input("Digite uma frase: ")
resultado = contar_vogais(texto)

print(resultado)