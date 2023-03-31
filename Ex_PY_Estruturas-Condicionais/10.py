salario = float(input("Digite o salário do vendedor: "))

if salario <= 1500:
    aumento = salario * 3 /100
    total = salario + aumento
else:
    aumento1 = 1500 * 3 / 100 
    aumento2 = (salario - 1500) * 5 / 100
    total = salario + aumento1 + aumento2

print(f"Salário final: {total}")