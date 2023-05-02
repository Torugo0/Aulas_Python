def poligonos(lados):
    if (lados == 3):
        print("Triangulo")
    elif (lados == 4):
        print("Quadrado")
    elif (lados == 5):
        print("Pentagono")
    else:
        print("Valor inválido")
    
lados = int(input("Informe a quantidade de lados: "))
poligonos(lados)