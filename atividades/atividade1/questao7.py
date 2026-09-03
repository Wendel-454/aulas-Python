#Questão 7
'''
Escreva um código que receba o valor total de uma compra (ex: 250.50). O programa deve calcular
um desconto automático de 15% sobre esse valor. No final, exiba três dados na tela: O valor
original da compra, o valor economizado (desconto) e o valor final que o cliente deverá pagar.
'''
#Reposta:
#Solicitando o valor da compra e atribuindo a variável por meio da função input() com o tipo float.
valorCompra = float(input("Digite o valor total da compra:"))
#Calculando o valor de desconto aplicado e atribuindo a variável.
valorDesconto = valorCompra * 0.15
#Calculando o valor final subtraindo o valor do desconto no valor da compra e atribuindo a uma variável.
valorComDesconto = valorCompra - valorDesconto
#imprimindo esses valores.
print("Valor total da compra:",valorCompra,"R$")
print("Valor economizado:",valorDesconto,"R$")
print("valor a ser pago:",valorComDesconto,"R$")