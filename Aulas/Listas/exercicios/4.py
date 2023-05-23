# Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as idades em outra lista. Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou igual a 18 anos.

nomes = []
idades = []

for i in range (10):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        nomes.append(nome)
        idades.append(idade)

print("Pessoas maiores de idade:")
for i in range(len(nomes)):
    print(f"{nomes[i]}: {idades[i]}")


print(nomes)
print(idades)