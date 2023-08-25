'''
- Estrutura de dados que associa uma chave(key) a um valor(value)
    - Chaves são utilizadas para acessas os valores armazenados no dicionario.

SINTAXE: 
    - São delimitados por chave {}
    - Itens separados por virgulo (,)
    - Cada item é composto por uma chave e valor (Obrigatorio os dois), separados por dois pontos (:)

dicionario ={
    "name": "Vitor",
    "age": 18,
    "job": "any",
    "city": "São Paulo"
}

CARACTERISTICAS:
    - Não possuem indicis sequenciais ([0],[1]...)
    - São estruturas heterogeneas (Podem ser de qualquer tipo)
    - São mutaveis 
        .Os valores podem ser alterados
        .As chaves NÃO podem ser alteradas

'''

## EXEMPLOS ##

# Cadastro de cliente
    # codigo de cliente // nome do cliente
cadastro ={
    123: "João", 532: "Paulo", 123:"Vitor" # Caso repita uma chave, o valor vai ser alterado 
}

print(cadastro) # Retorna o dicionario
print(cadastro[532]) # Retorna Paulo
# print(cadastro[345]) # Retorna um keyError 

# Alterar um item
cadastro[532] = "Ana" # Altera Paulo para Ana
print(cadastro)

# Inserir um item 
cadastro[652] = "Fernando" # Adiciona Fernando
print(cadastro)

# Remover um item
cadastro.pop(652)
print(cadastro) # caso insira um valor inexistente ira retornar um keyerror

# Busca uma chave especifica
'''
codigo = int(input("Digite o codigo do cliente: "))

if (codigo in cadastro):
    print(f"Cliente cadastrado: {cadastro[codigo]}")
else:
    print("Cliente não cadastrado")
'''

# Percorrer chaves do dicionario 
for codigo in cadastro.keys():
    print(codigo)

# Percorrer valores do dicionario
for nome in cadastro.values():
    print(nome)


# Percorrer itens do dicionario (chave e valor)
for codigo, nome in cadastro.items():
    print(f"{codigo} - {nome}")

# Preencher dicionario com inputs

# Jeito 1
'''
dados_cliente = {}
for i in range (3):
    codigo = int(input("Digite o codigo do cliente: "))
    nome = input("Digite o nome do cliente: ")
    dados_cliente[codigo] = nome
'''

# Jeito 2
'''
dados_cliente = {}

while (len(dados_cliente) < 3):
    codigo = int(input("Digite o codigo do cliente: "))
    nome = input("Digite o nome do cliente: ")
    if codigo not in dados_cliente:
        dados_cliente[codigo] = nome
    else:
        print("Codigo ja cadastrado, digite novamente")
print(dados_cliente)
'''

# Dicionario armazenando listas
# Cadastro de alunos (RM / Lista de notas)
alunos = {"Vitor": [9, 7, 8],
          4565: [6, 7, 5],
          2233: [8, 10, 9]}
print(alunos["Vitor"][0])

alunos["Vitor"][0] = 10
alunos[4565].append(4)
print(alunos)
