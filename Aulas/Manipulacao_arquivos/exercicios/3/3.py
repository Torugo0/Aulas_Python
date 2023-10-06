with open("./Aulas/Manipulacao_arquivos/exercicios/3/arquivo.txt", "w") as arquivo:

    resume = True

    while resume:
        resume = input("Digite qualquer coisa: ")
        if resume == "0":
            print('''Elementos adicionados
    Programa finalizado''')
            break
        arquivo.write(resume + "\n") #Pode se usar o fstring