# Int (Inteiros)
a =20
b = -10
c = 0

# Float (Numeros reais)
a = 30.3
b = -3.5
c = 5.0

# str (Strings/Textos)
a = "Paulo"
b = 'Exemplo de texto'
c = '''1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão'''

# Função Type

a = 4.5
# print(type(a))

# Funções de conversão de tipos

a = 2
a = str(a)   #Converte para str

a = "25"
a = int(a)  #Converte para int

a = '4.56'
a = float(a)    # Converte para float

# Operadores aritmeticos

'''
+ -> Soma
- -> Subtração 
* -> Multiplicação
/ -> Divisão (2 / 3 = 0.667)
// -> Divisão inteira (2 // 3 = 0)
% -> Mod (pega o resto)  (2 % 3 = 2)
** -> Potência
'''

# Operadores relacionais 

'''
== -> Igualdade
!= -> Diferente
< -> Menor
> -> Maior
<= -> Menor ou igual
>= -> Maior ou igual 
'''

# Operadores lógicos 

'''
and -> E (2 == 2 and 3 == 4) Obriga que sejam verdadeiros 
or -> OU (2 == 2 or 3 == 4) Um ou o outro 
not -> NÃO (not 2 == 2) Altera o valor, exemplo (True vira False)
'''

# Operações de entrada (Input)
# AVISO: Input sempre retorna uma string, mesmo que insira um número

'''
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))
'''

# Estruturas de decisão

'''
numero = int(input("Informe um número: "))

if (numero % 2 == 0):
    print("Par")
elif (numero % 2 != 0):
    print("Impar")
else:
    (erro)
'''

# Estruturas de seleção (Match Case)
'''
opcao = int(input("Escolha uma opção (1, 2 ou 3): ))

match opcao:
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case_:
        print("Opção invalida")

'''

# Estruturas de repetição while
# Exibir os números inteiros de 1 a 10
'''
cont = 1
while cont < 10:
    print(cont)
    cont += 1 
'''

# solicitar 5 numeros e soma-los

'''
cont = 1
soma = 0
while cont <= 5:
    numero = int(input("Numero: "))
    soma += numero  # somadora
    cont += 1   # Contadora
print(soma)
'''

# Estrutura de repetição FOR

'''
for a in range (1,11):
    print (a)
'''

# Somatorio dos 5 numeros informados/solicitados
'''
soma = 0 
for a in range (1,6):
    numero = int(input("Numero: "))
    soma += numero

print(soma)
'''