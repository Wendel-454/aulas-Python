"""
Desenvolva um algoritmo que simule um saque bancário.
O programa deve receber o saldo atual do cliente (ex: 500.00) e o valor que ele deseja sacar.
Se o valor do saque for menor ou igual ao saldo disponível, o programa deve subtrair o valor sacado, atualizar o saldo
e exibir: "Saque realizado com sucesso! Saldo atual: R$ [Novo Saldo]".
Caso o saque seja maior que o saldo, exiba: "Saldo insuficiente para realizar esta operação".

"""
#Resposta
saldo = 500.00
saque = int(input("Digite o valor do saque desejado: "))
if saque <= saldo:
    saldo = saldo - saque
    print("Saque realizado com sucesso! Saldo atual: R$", saldo)
else:
    print("Saldo insuficiente para realizar esta operação")
