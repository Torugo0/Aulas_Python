# PARÂMETRO DEFAULT
# Se você definir o parâmetro como dafault não irá dar erro caso não faça a chamada dos parâmetros na função

def calcular_media(matematica: float = 0,fisica: float = 0, quimica: float = 0):
    print(f"Matemática: {matematica}")
    print(f"Fisica: {fisica}")
    print(f"Química: {quimica}")
    media = (matematica + fisica + quimica) / 3
    return media

matematica = float(input("Digite a nota de matematica: "))
print(f"Média: {calcular_media()}")


# Parâmetros posicionais (respeitam a ordem dos valores)
# Pode usar parametros nomeados e posicionais juntos, e parametros posicionais precisam ser sempre antes dos nomeados

def calcular_media(matematica: float = 0,fisica: float = 0, quimica: float = 0):
    print(f"Matemática: {matematica}")
    print(f"Fisica: {fisica}")
    print(f"Química: {quimica}")
    media = (matematica + fisica + quimica) / 3
    return media

matematica = float(input("Digite a nota de matematica: "))
print(f"Média: {calcular_media(10, 8, 10)}")


# Parâmetros nomeados (não precisam respeitar a mesma ordem)
# Pode usar parametros nomeados e posicionais juntos, e parametros posicionais precisam ser sempre antes dos nomeados

def calcular_media(matematica: float = 0,fisica: float = 0, quimica: float = 0):
    print(f"Matemática: {matematica}")
    print(f"Fisica: {fisica}")
    print(f"Química: {quimica}")
    media = (matematica + fisica + quimica) / 3
    return media

print(f"Média: {calcular_media(quimica=10, matematica= 8, fisica= 10)}")