def calcular_salario(salario):
    if (salario >= 2000):
        porcentagem = salario * 0.07
        aumento = salario + porcentagem
        return aumento
    else:
        porcentagem = salario * 0.15
        aumento = salario + porcentagem
        return aumento

nome = input("Digite o nome do funcionario: ")
salario = float(input(f"Digite o salario do(a) {nome}: "))

print("AVISO: Se seu salario for superior a 2000 recebera um aumento de 7%, caso contario 15%\n")
print(f"O salario do funcionario(a) {nome} com aumento é: {calcular_salario(salario)}")