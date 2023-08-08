def media(valor1, valor2, valor3):
    aritmetica = (valor1 + valor2 + valor3) / 3
    return aritmetica

valor1= int(input("Digite o primeiro valor: "))
valor2= int(input("Digite o segundo valor: "))
valor3= int(input("Digite o terceiro valor: "))

print(f"A média aritmetica dos valores informados = {media(valor1,valor2,valor3)}")