#Resposta
mes = input("digite um mês do ano (em número):")
match mes:
    case "12"|"1"|"2":
        print("Verão")
    case "3"|"4"|"5":
        print("Outono")
    case "6"|"7"|"8":
        print("Inverno")
    case "9"|"10"|"11":
        print("Primavera")
    case _:
        print("Mês inválido!")
