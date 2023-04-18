# Solicite a quantidade de alunos de uma turma e a quantidade de notas. Para cada aluno, solicite as suas notas e exiba a sua respectiva média (a média deve ser arredondada para duas casas decimais).

alunos = int(input("Digite a quantidade de alunos da turma: "))
atividades = int(input("Digite a quantidade de atividades: "))

for i in range(1, alunos+1):
    print("Aluno", i)
    nota = []
    soma = 0
    for j in range (1, atividades+1):
        nota = float(input("Digite uma nota: "))
        nota = round(nota,2)
        soma += nota
    media = soma / atividades
    print(media)