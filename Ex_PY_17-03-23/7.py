cf = float(input("Digite o custo de fábrica do carro: "))
dis = round((cf - (cf*45/100)),2)
imp = round((cf - (cf*45/100)),2)
st = float(cf + dis + imp)

print(f"O valor do carro ao consumidor é de: R$:{st}")