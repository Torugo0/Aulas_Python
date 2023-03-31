
letra = input("Digite uma letra: ")

letra = letra.lower() # Transforma as letras em minusculas

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
else:
    print("Consoante")


# -------------------------------------------------------------------------- #


vogais = "aeiouAEIOU"

if letra in vogais:  # Verifica se a letra está contida no texto
    print("Vogal")
else:
    print("Consoante")