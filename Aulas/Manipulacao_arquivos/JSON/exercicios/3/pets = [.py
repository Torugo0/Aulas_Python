import json 

pets = [
    
]

def inserir():
    '''Função que armazena os animais'''  
    while True:
        raca = input("Raça do cachorro: ")
        nome = input("Nome do cachorro: ")  
        idade = int(input("Qual a idade do AuAu: "))
        adiciona = {"Raça": raca, "Nome": nome, "Idade":idade}
        pets.append(adiciona)
        
        continua = int(input("Continua: "))
        if continua == 0:
            break

    with open('./Aulas/Manipulacao_arquivos/JSON/exercicios/3/pets.json', 'w') as json_file:
        json.dump(pets, json_file, indent=2)

inserir()