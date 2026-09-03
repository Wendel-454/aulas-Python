#Questão 8:
'''
Escreva um código onde você solicite o Nome do usuário, a Idade e a Altura em metros (ex: 1.75).
Aplique o casting (conversão) em cada input para garantir que entrem com o formato adequado.
Para finalizar, escreva três print() usando o comando type() para comprovar na tela que você
obteve sucesso em criar uma string, um inteiro e um float.
'''
#Resposta:
#Solicitando o nome do usuário por meio da função input() e conventendo para string.
nome = str(input("Digite seu nome:"))
#Solicitando a idade do usuário por meio da função input() e convertendo para inteiro.
idade = int(input("Digite sua idade:"))
#Solicitando a altura do usuário por meio da função input() e convertendo para float.
altura = float(input("Digite sua altura em metros:"))
#imprimindo esses valores.
print(nome)
print(idade)
print(altura)
