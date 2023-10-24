import json

alunos = {}

with open('./Aulas/Manipulacao_arquivos/JSON/exercicios/notas.csv', 'r') as arquivo:
    cont = 0
    for linha in arquivo:
        if cont > 0: 
            partes = linha.split(';')
            rm = partes[0]
            nome = partes[1]
            notas = [float(nota) for nota in partes[2:6]]
            alunos[rm] = {'nome': nome, 'notas': notas}
        cont += 1

with open('./Aulas/Manipulacao_arquivos/JSON/exercicios/1/notas.json', 'w') as json_file:
    json.dump(alunos, json_file, indent=2)

print('Dados convertidos para JSON e salvos em "notas.json"')