class Mesa:
    def __init__(self,numero_mesa:int):
        self.numero_mesa = numero_mesa
        self.pedidos = []

    def adicionar_pedido(self, descricao, valor):
        try:
            valor = float(valor)
            self.pedidos.append(ItemPedido(descricao,valor))
        except ValueError:
            print(f"Erro: O valor para {descricao} deve ser estritamente numérico.")

    def somar_total(self):
        total = 0
        for y in self.pedidos:
            total += y.index
        print(f"Valor total: {total}")
        return total
    def fechar_conta(self, taxa_servico):
        print(f"Finalizando mesa {self.numero_mesa}")
        print("Itens consumidos:")
        for y in self.pedidos:
            print(f"{y.descricao}, valor: {y.index}")
        total_consumo = self.somar_total()
        servico = total_consumo * (taxa_servico/100)
        total = total_consumo + servico
        print(f"Valor a pagar: {total}")
        self.pedidos.clear()


class ItemPedido:
    def __init__(self, descricao:str,valor:float):
        self.descricao = descricao
        self.valor = valor



mesa1 = Mesa(1)
mesa1.adicionar_pedido("Pedido 1", 100)
mesa1.fechar_conta(10)
mesa1.fechar_conta(10)