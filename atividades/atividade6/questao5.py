"""
Crie um programa que peça ao usuário um número inteiro para o qual ele deseja ver a tabuada.
Utilizando uma variável de incremento (como visto no exemplo da idade), crie um laço while que vá de 1 até 10,
exibindo o resultado da multiplicação do número escolhido pelo contador.
Exemplo de saída esperada se o usuário digitar 5:
*5 x 1 = 5
*5 x 2 = 10
*... (até 10)

"""
#Resposta
import time

numero = int(input("Digite o número do qual deseja ver a tabuada: "))
contagem = 0
resultado = 0
while contagem < 10:
    time.sleep(0.5)
    contagem += 1
    resultado = numero * contagem
    print(f"{numero} x {contagem} = {resultado}")
