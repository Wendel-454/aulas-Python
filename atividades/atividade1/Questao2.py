#Questão 2
'''
Desenvolva um algoritmo em Python que solicite ao usuário o seu nome e as notas obtidas em 3
provas ao longo do semestre. Calcule a média aritmética dessas notas e exiba no final a frase: "Olá
[Nome], a sua média final foi de [Média]". Dica: atente-se à ordem de precedência das operações
matemáticas.
'''
#Resposta:
#Solicitando as informações necessárias por meio da função input().
nome = input("Digite seu nome:")
nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))
#Somando as 3 notas.
total = nota1 + nota2 + nota3
#Dividindo o total das notas para obter a média aritmética.
media = total / 3
#Mostrando o resultado do cálculo por meio da função print().
print("Olá,",nome,". A sua média final foi de:",media)
