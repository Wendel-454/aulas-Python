"""
Construa um programa para um comerciante. O sistema deve receber três dados: o nome do produto, o custo de fábrica para comprá-lo e o preço pelo qual ele será vendido na loja.
Calcule o lucro em reais (Preço de Venda - Custo).
Verifique se o lucro é maior que 20 reais.
Exiba uma mensagem final mostrando: o nome do produto, o lucro obtido e o resultado da verificação (se o lucro foi bom = True ou False).
"""
#Resposta
nomeProduto = input("Digite o nome do produto: ")
custoFabrica = float(input("Digite o custo de fábrica: "))
valorVenda = float(input("Digite o valor de venda: "))
lucro = valorVenda - custoFabrica
valido = lucro > 20
print("nome do produto: ", nomeProduto, ". Lucro obtido: ", lucro, "R$. O lucro é bom?: ", valido)
