with open("./Aulas/Manipulacao_arquivos/exercicios/1/1.txt", "r") as arquivo:
    somatorio = 0
    
    for linha in arquivo:
        somatorio += int(linha)

    print(somatorio)

arquivo.close()