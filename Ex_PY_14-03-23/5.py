print("Calculo do imc")
p= float(input("Digite seu peso em Kg: "))
a= float(input("Digite sua altura em M: "))
imc= float(p/a**2)

print(f"O calculo do IMC é: {round(imc, 2)}")