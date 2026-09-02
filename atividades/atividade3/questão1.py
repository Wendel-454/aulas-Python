"""
Crie um programa para um restaurante que funciona como uma calculadora de divisão de conta.
O sistema deve solicitar ao usuário o valor total da conta (ex: 150.00) e a quantidade de pessoas na mesa.
O programa deve calcular o valor que cada um deve pagar e exibir a mensagem: "O valor total foi de R$ [Total],
e cada pessoa deve pagar R$ [Valor Dividido]".
"""
#Resposta
valorTotal = float(input("Digite o valor total da conta: "))
quantidadePessoas = int(input("Digite a quantidade de pessoas a mesa: "))
valorDividido = valorTotal / quantidadePessoas
print("O valor total foi de R$", valorTotal, "e cada pessoa deve pagar R$", valorDividido)

