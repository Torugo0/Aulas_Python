import json 

pets = []

def inserir():
    '''Função que armazena os animais'''  
    with open('./Aulas/Manipulacao_arquivos/JSON/exercicios/3/pets.json', 'r') as json_file:
        pets = json.load(json_file)

    while True:
        raca = input("Raça do cachorro: ")
        nome = input("Nome do cachorro: ")  
        idade = int(input("Qual a idade do AuAu: "))
        adiciona = {"Raça": raca, "Nome": nome, "Idade":idade}
        pets.append(adiciona)
        
        continua = (input('''Deseja adicionar outro animal ?
Digite S ou N: '''))
        if continua.lower() != 's':
            break

    with open('./Aulas/Manipulacao_arquivos/JSON/exercicios/3/pets.json', 'w') as json_file:
        json.dump(pets, json_file, indent=2)


def menu():
    print('''1 - Inserir
2 - Excluir
3 - Listar todos
''')
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        inserir()
    elif opcao == 2:
        excluir()
    elif opcao == 3:
        listar()

inserir()