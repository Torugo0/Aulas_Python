with open("./Aulas/Manipulacao_arquivos/exercicios/1/1.txt", "w") as arquivo:
    for i in range(10):
        n = int(input("Digite um número: "))
        arquivo.write(str(n) + "\n") #Pode se usar o fstring
    print("Números armazenados ao arquivo")

arquivo.close()  # Não se esqueça de fechar o arquivo quando terminar de escrever.


