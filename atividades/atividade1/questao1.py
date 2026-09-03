#Questão 1
'''
Explique detalhadamente por que esse código não funcionará e gerará um erro. 
Reescreva-o da maneira correta.
'''
print("Bem-vindo(a),", nome)
nome = input("Digite seu nome: ")

#Resposta:
'''
O código gera um erro, pois a função print() tenta utilizar a variável nome 
antes de ela ter sido declarada e recebido um valor.
'''

#Correção:
#declaração da variável e atribuição de valor por meio da função input().
nome = input("Digite seu nome: ")
#Utilização da função print() com o conteúdo da variável nome.
print("Bem-vindo(a),", nome)
