def tamanho_string(palavra):
    return len(palavra)

frase = True
while frase:
    palavra = input("Digite uma palavra: ")
    if (palavra == "0"):
        frase = False
    else:
        print(f"O tamanho da palavra {palavra} é: {tamanho_string(palavra)}")
    