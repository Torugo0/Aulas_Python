# Solicite dois números diferentes ao usuário (caso os números sejam iguais, o algoritmo deve solicitar os números novamente) e informe a diferença entre o maior e o menor número. 

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

while (numero1 == numero2):
    print("NÚMEROS IGUAIS, DIGITE NOVAMENTE !!")
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite um número: "))
if numero1 > numero2:
    maior = numero1
    menor = numero2
else: 
    maior = numero2
    menor = numero1

diferença = maior - menor

print(f"A diferença entre o maior e o menor número é: {diferença}")
