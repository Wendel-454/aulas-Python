#questão 4
#Analise minuciosamente as 4 linhas do código sequencial abaixo:
'''
A = 8
B = 4
A = B
B = A + 5
print("Valor de A:", A)
print("Valor de B:", B)
'''
#Resposta:
#Resultado impresso na tela:
'''
Valor de A:4
Valor de B:9
'''
#O que aconteceu em cada linha:
#Variável A recebe o valor 8.
A = 8
#Variável B recebe o valor 4.
B = 4
#Variável A recebe o valor da variável B, que é 4.
A = B
#Variável B recebe o resultado da soma entre a variável A e o número 5.
B = A + 5
#Função print() imprime o conteúdo da variável A, que é 4.
print("Valor de A:", A)
#Função print() imprime o conteúdo da variável B, que é 9
print("Valor de B:", B)
