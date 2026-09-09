"""
Crie um programa onde o computador "pensa" em um número secreto (você pode definir um número fixo diretamente no código,
por exemplo, numero_secreto = 14).
O usuário deve tentar adivinhar qual é esse número.
Usando a estrutura while, o programa deve continuar pedindo um novo palpite enquanto o usuário não acertar.
Requisito extra: Crie uma variável para contar quantas tentativas o usuário fez.
Quando ele finalmente acertar o número, exiba a mensagem: "Parabéns! Você acertou o número secreto em [X] tentativas!"
(onde X é o número de vezes que ele tentou).

"""
#Resposta
import random

numero_secreto = random.randint(1, 10)
tentativas = 6
print