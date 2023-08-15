def concatenar_strings(string1:str = "", separador:str = " - ", string2:str = "" ):
    return string1, separador, string2

string1 = input("Digite uma palavra: ")
string2 = input("Digite outra palavra: ")

print(concatenar_strings(string2)[2],concatenar_strings()[1],concatenar_strings(string2)[2])

#Refazer