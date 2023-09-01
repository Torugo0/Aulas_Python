def cadastra_alunos():
    infos = []

    for n in range(2):
        media = 0
        nome = input("Digite o nome do aluno(a): ")
        idade = int(input("Digite a idade: "))
        for a in range(3):
                nota = float(input(f"Digite a {a+1}ª nota: "))
                media += nota
        lista =[nome, idade, (media / 3)]
        tupla = tuple(lista)
        infos.append(tupla)

    return infos

infos = cadastra_alunos() 
def alunos_aprovados():
    aprovados = []

    for info in infos:
        nome,idade,media = info
        if media >= 7.0:
             aprovados.append(info)
    return aprovados

aprovados = alunos_aprovados()
print(aprovados)