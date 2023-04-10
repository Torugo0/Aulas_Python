n= int(input("Digite um número inteiro com três digitos: "))

a= n//100
resto= n%100
b= resto//10
c= resto%10

print(f"O número invertido: {c}{b}{a}") 