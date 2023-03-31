a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a < b and a < c:
    print(f"Menor número é {a}")
elif b < a and b < c:
    print(f"Menor número é {b}")
elif c < b and c < a:
    print(f"Menor número é {c}")
elif a==b and b==c:
    print("Três números iguais")
else:
    print("Dois números iguais")
