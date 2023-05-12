# Em um jogo de dados, pode ser sorteado qualquer número entre 1 e 6. Faça uma função que simule 1 milhão de lançamentos de dados e mostre quantas vezes cada número foi sorteado.

import random

def dado():
    for i in range (1,100001):
        jogo = random.randint(1,6)
        if jogo == 1:
            um = jogo
            um+= 1
        elif jogo == 2:
            dois = jogo
            dois+= 1
        elif jogo == 3:
            tres = jogo
            tres += 1
        elif jogo == 4:
            quatro = jogo
            quatro+= 1
        elif jogo == 5:
            cinco = jogo
            cinco+= 1
        elif jogo == 6:
            seis = jogo
            seis += 1
    print(um)
    print(dois)
    print(tres)
    print(quatro)
    print(cinco)
    print(seis)
        

dado()