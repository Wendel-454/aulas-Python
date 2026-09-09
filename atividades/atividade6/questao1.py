"""
Crie um programa que exiba uma contagem regressiva para o lançamento de um foguete.
O programa deve definir uma variável iniciando em 10 e, usando o while, exibir os números de 10 até 1.
Ao final, quando o laço terminar, exiba a mensagem: "Foguete lançado!".
"""
import time

#Resposta
cont = 10
while cont > 0:
    print(cont)
    cont -= 1
    time.sleep(1)
print("Foguete lançado")

