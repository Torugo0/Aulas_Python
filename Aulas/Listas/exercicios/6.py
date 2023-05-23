# Solicite uma quantidade indeterminada de notas de alunos (até que seja informada uma nota menor que zero). Após a entrada de dados, exiba:
# a. A quantidade de notas que foram informadas.
# b. Todas as notas na ordem em que foram informadas.
# c. A média aritmética de todas as notas. 
# d. A quantidade de notas acima da média aritmética calculada.

notas = []
acima = []
soma = 0
cont = 0

while True:
    nota = float(input("Digite uma nota: "))
    if nota == 0:
        break
    notas.append(nota)
    soma =+ nota
    cont += 1
mediat = soma / len(notas)
if notas > mediat:
    acima.append(nota)


print(f"Foram digitadas {cont} notas\n")
print("Notas informadas: ")
for j in range(len(notas)):
    print(notas[j])
print("\n")

print(f"Notas acima da media geral: ")
for l in range(len(acima)):
    print(notas[l])
