#Faça  um  algoritmo  que  solicite  N  números  e  calcule  a  média  dos  números  pares  e  a média  dos  números  ímpares  (o  valor  de  N  deve  ser solicitado  ao usuáriono  início  do programa).

par = 0
impar = 0
cont = 1
somaimpar = 0
somapar = 0
num = int(input("Digite quantos números vão ser solicitados: "))

while ( cont <= num):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        somapar += numero
        par += 1
    else:
        somaimpar += numero
        impar +=1
    cont+=1

if par > 0:
    mediapar = somapar / par
    print(f"A media dos pares: {mediapar}")
else:
    print("Não há números pares") 

if impar > 0:
    mediaimpar = somaimpar / impar
    print(f"A media dos pares: {mediaimpar}")
else:
    print("Não há números impares") 
