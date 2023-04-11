#Faça  um  algoritmo  que  solicite  N  números  e  calcule  a  média  dos  números  pares  e  a média  dos  números  ímpares  (o  valor  de  N  deve  ser solicitado  aousuáriono  início  do programa).

par = 0
impar = 0
cont = 1
num = int(input("Digite quantos números vão ser solicitados: "))

while ( cont <= num):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar +=1
    cont+=1

print(f"A quantidade de números pares e impares digitados respectivamente foi: {par} e {impar}")