s = int(input("Digite o valor inteiro em segundos: "))
h = s//60//60
m = s//60%60
seg = s%60

print(f"{s} equivale a {h} hora {m} minutos e {seg} segundos")