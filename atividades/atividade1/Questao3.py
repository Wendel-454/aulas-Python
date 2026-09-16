#questão 3
#Ao criar uma calculadora de somas simples, o seguinte código foi escrito:
n1 = input("Primeiro número: ")
n2 = input("Segundo número: ")
resultado = n1 + n2
print("O resultado da soma é:", resultado)

#Resposta:
'''
O Python une os valores digitados porque a função input() recebe os dados como
strings(texto). Dessa forma, ao utilizar o operador +, ocorre a concatenação e 
não uma soma matemática.
'''
#correção:
#declarando as variaveis e informando a entrada de dados como int().
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
resultado = n1 + n2
print("O resultado da soma é:", resultado)