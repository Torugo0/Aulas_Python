import json
# Converter de json para python
'''
- Uma string em formato JSON pode ser convertida em Python usando o metodo json.loads 
  - O resultado sera um dicionario Python

- Um dicionario Python pode ser convertido para um string em formato json usando o mtodo json.dumps()
    - Existe um parametro no dumps, o "indent" json.dumps(x, indent = 4)

- Ao converte de Python para JSON, os objetos Python são convertidos no equivalente JSON (JavaSript)
'''

# Exemplos
'''
dictionary = {
    "codigo" : 123,
    "nome" : "Vitor Hugo",
    "idade" : 18,
    "altura" : 1.78
}

texto = json.dumps(dictionary)

print(texto)
'''

dictionary1 = {
    "codigo" : 123,
    "nome" : "Vitor Hugo",
    "idade" : 18,
    "altura" : 1.78
}

dictionary2 = {
    "codigo" : 456,
    "nome" : "Ana Clara",
    "idade" : 19,
    "altura" : 1.70
}

lista = [dictionary1, dictionary2]

with open('./Aulas/Manipulacao_arquivos/JSON/dados.json', 'w') as arquivo:
    json.dump(lista, arquivo, indent = 4)