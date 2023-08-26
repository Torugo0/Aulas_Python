def formatar_cpf(cpf):
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado

def cliente():
    dados = {}
    while (len(dados) < 1):
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu cpf: ")
        formato = formatar_cpf(cpf)
        dados[formato] = nome
    return dados

dicionario_clientes = cliente()

print(dicionario_clientes)


# Busca do CPF no dicionario de clientes

busca_cpf = input("Digite um CPF para busca: ")
busca_formatado = formatar_cpf(busca_cpf)

for cpf, nome in dicionario_clientes.items():
    if cpf == busca_formatado:
        print(f"{nome} - {cpf}")
    else:
        print("CPF não encontrado !")