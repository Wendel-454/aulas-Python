class Produto:
    def __init__(self, nome, preco, quantidade_estoque ):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade

        else:
            print("Erro: Quantidade invalida")

    def realizar_venda(self):
        quantidade = int(input('digite a quantidade da venda:'))
        if quantidade > self.__quantidade_estoque:
            print("Erro: Venda negada: Estoque insuficiente")
        else:
            self.__quantidade_estoque -= quantidade

    def aplicar_desconto(self, percentual):
        if percentual > 80 or percentual < 0:
            print("Erro: Desconto inválido")
        else:
            self.__preco = self.__preco * (percentual / 100)
            print(f"Desconto aplicado: {percentual}%")
            print(f"Valor atualizado: R${self.__preco}")

    def exibir_resumo(self):
        print(self.__dict__)

estoque = Produto('Maikon', 100, 1000)
estoque.quantidade_estoque = 20
estoque.exibir_resumo()

