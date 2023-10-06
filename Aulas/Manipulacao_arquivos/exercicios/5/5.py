with open("./Aulas/Manipulacao_arquivos/exercicios/4/arquivo_impares.txt", "r") as arquivo_impares, open("./Aulas/Manipulacao_arquivos/exercicios/4/arquivo_pares.txt", "r") as arquivo_pares:

    conteudo_pares = arquivo_pares.read()
    conteudo_impares = arquivo_impares.read()


# Combine os conteúdos em uma única lista
numeros = conteudo_pares.split() + conteudo_impares.split()

# Converta os números de strings para inteiros
numeros = [int(numero) for numero in numeros]

# Ordene a lista de números em ordem crescente
numeros.sort()

with open("./Aulas/Manipulacao_arquivos/exercicios/4/arquivo_ordenado.txt", "w") as arquivo_ordenado:
    # Escreva os números ordenados no novo arquivo
    for numero in numeros:
        arquivo_ordenado.write(str(numero) + "\n")

print("Números ordenados e salvos no arquivo 'arquivo_ordenado.txt'.")