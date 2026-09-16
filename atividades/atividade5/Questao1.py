#Resposta
cachoroQuente = "Cachorro-quente:R$10,00"
hamburguer = "Hambúrguer:R$15,00"
batataFrita = "Batata Frita:R$8,00"
refrigerante = "Refrigerante:R$5,00"

produto = (input("Digite o número produto: "))
match produto:
    case "1":
        print(cachoroQuente)
    case "2":
        print(hamburguer)
    case "3":
        print(batataFrita)
    case "4":
        print(refrigerante)
    case _:
        print("Código invalido!")

