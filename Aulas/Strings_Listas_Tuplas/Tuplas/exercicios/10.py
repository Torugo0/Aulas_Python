def names_age():
    names = []
    age = []
    maiores_name = []
    maiores_age = []
    name_str = None
    age_int = None
    while True:
        name_str = input("Digite o nome: ")
        if name_str == "":
            break
        else:
            age_int = int(input(f"Digite a idade do(a) {name_str}: "))
            names.append(name_str)
            age.append(age_int)
        if age_int >= 18:
            maiores_name.append(name_str)
            maiores_age.append(age_int)
    return names, age, maiores_name, maiores_age

tupla = names_age()

print('''Lista de pessoas com idades iguais ou superiores a 18''')
for n in range(len(tupla[2])):
    print(f"Nome: {tupla[2][n]}, Idade: {tupla[3][n]}")