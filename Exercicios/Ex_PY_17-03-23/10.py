nome = input("Digite o nome do encanador: ")
trabalhados = int(input("Digite a quantidade de dias trabalhados pelo encanador: "))
dia = float(80)
diast = float(80*trabalhados)
ir = float(diast - (diast*8/100))

print(f"O valor líquido a ser pago ao {nome} é: R$: {ir}")