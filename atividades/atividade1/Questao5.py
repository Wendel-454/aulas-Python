#Questão 5
'''
Crie um programa que exija que o usuário digite o seu ano de nascimento e, em seguida, o ano em
que estamos. O programa deve calcular a idade do usuário subtraindo os anos e imprimir a
resposta de forma amigável no terminal.
'''
#Resposta
#Solicitando o ano de nascimento do usuário por meio da função input().
anoNasc = int(input("Digite o seu ano de nascimento:"))
#Solicitando o ano atual por meio da função input().
anoAtual = int(input("Digite o ano em que estamos:"))
#Fazendo o cálculo de subtração por meio do operador - e atribundo a variável.
resultado = anoAtual - anoNasc
#Imprimindo o resultado do cálculo matemático.
print("Sua idade é", resultado, "Anos")