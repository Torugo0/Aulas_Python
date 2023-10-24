import json

foods = {}

with open('./Aulas/Manipulacao_arquivos/JSON/exercicios/foods.csv', 'r') as arquivo:
    cont = 0
    for linha in arquivo:
        if cont > 0:
            partes = linha.split(";")
            id = partes[1]
            nome = partes[0]
            food = partes[2]
            foods[id] = {'Name': nome, 'Food': food}
        cont += 1

with open('./Aulas/Manipulacao_arquivos/JSON/exercicios/2/foods.json', 'w') as json_file:
    json.dump(foods, json_file, indent=2)

print('Dados convertidos para JSON e salvos em "foods.json"')