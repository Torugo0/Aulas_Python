def pesoideal(altura):
    sexo = input("Qual o seu sexo(M,F): ")
    sexo = sexo.upper()
    peso = float(input("Digite seu peso: "))
    peso = round(peso,2)

    if (sexo == "M"):
        pesoideal = (peso * altura) - 58
        print(f"Seu peso ideal é {pesoideal}")
    elif (sexo == "F"):
        pesoideal = (peso * altura) - 44.7
        print(f"O seu peso ideal é {pesoideal}")

altura = float(input("Digite sua altura: "))
altura = round(altura, 2)
pesoideal(altura)