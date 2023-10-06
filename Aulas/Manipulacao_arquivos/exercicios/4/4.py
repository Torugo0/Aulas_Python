with open("./Aulas/Manipulacao_arquivos/exercicios/4/arquivo_impares.txt", "r") as arquivo_impares, open("./Aulas/Manipulacao_arquivos/exercicios/4/arquivo_pares.txt", "r") as arquivo_pares:

    resume = 1

    while resume != 0:
        resume = int(input("Digite números: "))

        if resume == 0:
            print('''Elementos adicionados
    Programa finalizado''')
            break

        if resume % 2 == 0:
            arquivo_pares.write(str(resume) + "\n") #Pode se usar o fstring
        else:
            arquivo_impares.write(str(resume) + "\n") #Pode se usar o fstring
