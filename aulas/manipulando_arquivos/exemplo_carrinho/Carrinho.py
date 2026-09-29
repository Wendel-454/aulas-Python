from atividades_poo.atividade4.Caminhao import Caminhao

carrinho = []
while True:
    nome = input("Digite 'fim' para finalizar."
                 "\ndigite o nome do produto: ")
    if nome == "fim":
        break

    preco = float(input("digite  valor desse produto"))
    carrinho.append([nome, preco])
