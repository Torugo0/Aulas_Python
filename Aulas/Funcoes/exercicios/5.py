def area(raio):
    pi = float(3.14)
    carea = float(pi * (raio*raio))
    carea = round(carea, 2)
    print(f"A área do circulo é: {carea}")
    return carea

def perimetro(raio):
    pi = float(3.14)
    cperimetro = float(pi * 2 * raio)
    cperimetro = round(cperimetro, 2)
    print(f"O perimetro do circulo é: {cperimetro}")
    return cperimetro

raio = int(input("Digite o raio do circulo: "))
area(raio)
perimetro(raio)