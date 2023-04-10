comprimento = float(input("Digite o comprimento da cozinhha: "))
altura = float(input("Digite a altura da cozinha:"))
largura = float(input("Digite a largura da cozinha: "))

area = (comprimento*altura*2) + (largura*altura*2)
caixas = round(area/1.5, 2)

print(f"O total de caixas de azuelos necessarias são: {caixas}")