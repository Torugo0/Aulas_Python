def notas_alunos():
    info_alunos = {}
    notas =[]
    return info_alunos, notas

notas_alunos = notas_alunos()

def add_info():
    ra = int(input("Digite o RA do aluno: "))
    for i in range (1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas_alunos[1].append(nota)
    notas_alunos[0][ra] = notas_alunos[1]

def calculo_media():
    soma = 0
    for i in range(len(notas_alunos[1])):
        soma += notas_alunos[1][i]
    media = soma / len(notas_alunos[1])
    return media


add_info()

for ra, notas in notas_alunos[0].items():
    print(f"{ra} - {notas} // Media: {calculo_media()}")



