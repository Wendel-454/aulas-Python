"""
Crie um programa que mostre repetidamente um menu com duas opções:
*1 - Mostrar saudação
*2 - Sair do programa
O programa deve pedir para o usuário escolher uma opção. Usando while:
*Se ele digitar 1, exiba "Olá, seja muito bem-vindo(a)!".
*Se ele digitar qualquer número diferente de 1 e 2, exiba "Opção inválida!".
*O programa só deve parar de repetir e encerrar quando o usuário digitar 2, exibindo a mensagem "Programa encerrado."

"""
#Resposta
import time


print("Escolha uma opção")
resposta = 0
while resposta != 2:
    resposta = int(input("1 - Mostrar saudação\n2 - Sair do programa\nSua escolha é:"))
    if resposta == 1:
        print("Olá, seja muito bem-vindo(a)!")
        time.sleep(1)
    elif resposta == 2:
        print("Programa encerrado.")
    else:
        print("Resposta inválida!")
        time.sleep(1)
