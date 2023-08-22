def concatenar():
    best = []
    worse = []
    for i in range(1,6):
        best_number = int(input("Lista das melhores notas da sala: "))
        best.append(best_number)
    for i in range(1,6):
        worse_number = int(input("Lista das piores notas da sala: "))
        worse.append(worse_number)
    all = best + worse
    all.sort()
    return best, worse, all

tupla = concatenar()

print(f'''Melhores notas: {tupla[0]}
Piores notas: {tupla[1]}
Nota de todos da turma em ordem crescente: {tupla[2]}
''')