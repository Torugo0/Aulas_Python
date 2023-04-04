letra = input("Informe seu estado civil (D, C, F, V): ")

match letra:
    case "D" | "d":
        print("Divorciado(a)")
    case "C" | "c":
        print("Casado(a)")
    case "S" | "s":
        print("Solteiro(a)")
    case "V" | "v":
        print("Viúvo(a)")
    case _:
        print("Opção Inválida")