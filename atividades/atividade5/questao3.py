#Resposta
print("Digite seu turno:\n'M' ou 'm' para Matutino\n'V' ou 'v' para Vespertino\n'N' ou 'n' para Noturno")
turno = input("Turno:")
match turno:
    case "M"|"m":
        print("Bom Dia!")
    case "V"|"v":
        print("Boa Tarde!")
    case "N"|"n":
        print("Boa Noite!")
    case _:
        print("Turno inválido")