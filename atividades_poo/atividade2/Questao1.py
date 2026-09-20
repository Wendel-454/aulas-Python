class Produto:
    def __init__(self, nome, preco, quantidade_estoque ):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade

        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade > self.__quantidade_estoque:
            print("Erro: Venda negada: Estoque insuficiente")
        elif quantidade <= 0:
            print("Valor inválido")
        else:
            self.__quantidade_estoque -= quantidade

    def aplicar_desconto(self, percentual):
        if percentual > 80 or percentual < 0:
            print("Erro: Desconto inválido")
        else:
            desconto = self.__preco * (percentual / 100)
            self.__preco = self.__preco - desconto
            print(f"Desconto aplicado: {desconto}R$")
            print(f"Valor atualizado: R${self.__preco}")

    def exibir_resumo(self):
        print(f"Nome do produto: {self.__nome}.\n"
              f"Preço:           {self.__preco:.2f}R$\n"
              f"Estoque:         {self.__quantidade_estoque} Und.\n")
        print(self.__dict__)

estoque = Produto('Carro', 25000, 4)
estoque.quantidade_estoque = 5
estoque.realizar_venda(10)
estoque.exibir_resumo()

