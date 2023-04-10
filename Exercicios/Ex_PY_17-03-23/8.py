nome = input("Digite o nome do funcionario: ")
sal = float(input("Digite o salário do funcioanrio: "))
aum = float(sal + (sal*25/100))
print(f"O sálario do(a) {nome} com aumento é de: R$:{aum}")