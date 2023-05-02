'''
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
'''

def aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"A sua média foi {media}")
    if media >= 6:
        print("Você foi aprovado")
    else: 
        print("Você foi reprovado")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

aprovacao(nota1, nota2) 