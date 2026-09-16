"""
Faça um programa que peça ao usuário para digitar números inteiros repetidamente.
O programa deve continuar pedindo números até que o usuário digite o número 0 (zero).
Quando o usuário digitar 0, o laço deve ser encerrado e o programa deve exibir a soma de todos os números que foram
digitados até aquele momento.
"""
#Resposta
num = 0
soma = 0

while True:
    soma = int(input("Digite um número inteiro (Digite 0 se quiser parar): "))
    if soma == 0:
        break
    else:
        num += soma
print("total: ",num)
