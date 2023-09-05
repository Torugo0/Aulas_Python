'''
# Sets são usados para armazear ma coleção de dados
    - Set é definido entre colchetes
    - Um set é uma coleção não ordenada e não indexada
    - Na hora de printar eles aparecem em ordem aleatoria

Ex: conjunto = {"Banana", "Apple", "Cherry"}
    - Não é possivel accesar itens consultando um indice ou uma chave  

Para adicionar algo a um conjunto se usa a função add() (Caso adicione um item repetido, será ignorado)

Para excluir pode se usar duas:
    1- remove(): Se o item a ser removido não existir, gerará um erro.
    2- discard(): Se o item a ser removido não exisir, NÃO gerará um erro.
    
Para CRIAR um conjunto VAZIO:
    conjunto_vazio = set()
    
Para juntar conjuntos:

set1 = {1, 2, 3}
set2 = {4, 5, 6}

set3 = set1.union(set2)

O metodo intersection retornara um conjunto que contem os itens que existem em ambos os conjuntos


O metodo difference retornara um cnjunto que contem os itens que existem apenas em um conjunto e não existem no outro

'''