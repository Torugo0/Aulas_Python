def separar(frase):
    return frase.split( )

lista = []
frase = 0
while frase != "0":
    frase = input("Digite uma frase: ")
    if frase != "0":
        lista.append(separar(frase))
    else:
        break

for i in lista:
    print(i)