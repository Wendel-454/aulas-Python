from aulas.funcoes import soma, olaUsuario

olaUsuario("João",22)

while True:
    valor = soma()
    print(valor)
    opcao = input("Quer finalizar? y/n")
    if opcao == "y":
        break
print("Finalizando execução.")
