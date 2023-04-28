def media():
    prova = 2
    soma = 0
    for i in range(1, prova + 1):
        nota = float(input("Digite a nota:"))
        nota = round(nota,2)
        soma += nota
    mfinal = soma/prova
    print(mfinal)

media()
