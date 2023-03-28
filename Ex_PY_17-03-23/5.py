tp = int(input("Digite quantas pessoas votaram: "))
vb = int(input("Digite o total de votos em branco: "))
vn = int(input("Digite o total de votos nulos: "))
vv = int(input("Digite o total de votos válidos: "))
cvb = round((vb*100/tp), 2)
cvn = round((vn*100/tp), 2)
cvv = round((vv*100/tp), 2)

print(f"Votaram {tp} pessoas \n {cvb}% votaram em branco, {cvn}% votaram nulo e {cvv}% foram votos válidos")