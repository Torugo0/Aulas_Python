lado1 = float(input("Medida do primeiro lado: "))
lado2 = float(input("Medida do segundo lado: "))
lado3 = float(input("Medida do terceiro lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("Triangulo equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triangulo isósceles")
else:
    print("Triangulo escaleno")