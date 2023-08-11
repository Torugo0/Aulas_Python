def calcular_area_retangulo(base: float = 1, altura: float = 1):
    print(f'''Base: {base}
Altura: {altura}''')
    return base * altura

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

print(f"Área do retângulo: {calcular_area_retangulo(base, altura)}")