print("Lembre-se que o raio de um circulo é a metade do diâmetro \n EX: Caso o diâmetro seja 45, o raio vai ser 22,5")
raio = float(input("Digite o raio do círculo: "))
pi = float(3.1415)
area = round((pi*raio**2), 2)

print(f"A área do circulo com raio {raio} é igual a: {area}")