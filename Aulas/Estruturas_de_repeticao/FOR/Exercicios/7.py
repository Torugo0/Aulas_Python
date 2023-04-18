# Escreva  um  algoritmo  que  exiba  20  números  aleatórios  sorteados  entre  1  e  50  (Dica:  utilize  a biblioteca random).

import random
cont = 1

for i in range (20):
    aleatorio = random.randint(1 ,50)
    print(aleatorio)