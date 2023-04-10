a= int(input("Valor do A: "))
b= int(input("Valor do B: "))
c= None

'''
c=a
a=b
b=c
'''
#Jeito mais facil de se fazer
a, b = b,a 

print(a)
print(b)