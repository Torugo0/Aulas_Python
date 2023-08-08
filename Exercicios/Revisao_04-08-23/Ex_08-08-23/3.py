def quadrado(numero):
    elevado = numero ** 2
    return elevado

def soma_dos_quadrados(elevado1,elevado2):
    soma = elevado1 + elevado2
    return soma

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

elevado1 = quadrado(numero1)
elevado2 = quadrado(numero2)
soma_quadrados = soma_dos_quadrados(elevado1, elevado2)

print(f'''O quadrado de {numero1} = {elevado1}
O quadrado de {numero2} = {elevado2}
A soma dos quadrados de {numero1} e {numero2} = {soma_quadrados}
''')