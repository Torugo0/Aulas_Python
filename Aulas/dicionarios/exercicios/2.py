def produtos_function():
    produtos = {}

    return produtos

produtos = produtos_function()

def produtos_add():
    nome_produto = input("Digite o nome do produto: ")
    valor_produto = float(input("Digite o valor do produto: "))
    produtos[nome_produto] = valor_produto

while len(produtos) < 5:
    produtos_add()


for nome, valor in produtos.items():
    if valor >= 50.00:
        print(f"{nome} - R$: {valor}")