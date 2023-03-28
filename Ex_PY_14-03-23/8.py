n= input("Digite o nome do vendedor: ")
c= int(input("Quantidade de carros vendidos: "))
v= float(input("Valor total das vendas: "))

co= c*200
vt= v*2/100
sf= 2500+co+vt

print(f"O salário de {n} ao fim do mês vai ser: {sf}")