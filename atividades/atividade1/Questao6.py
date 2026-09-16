#questão 6
'''
Crie uma variável chamada X com o valor inicial de 15, e uma variável Y com o valor inicial de 30.
Escreva a lógica necessária em Python para inverter os valores. Ao final, o print(X) deve
mostrar 30 e o print(Y) deve mostrar 15. Regra: Você está proibido de digitar os números 15 e
30 novamente no código. Use a lógica de variáveis para fazer a troca!
'''
#Resposta:
#Atribuindo o valor 15 a variável x.
x = 15
#Atribuindo o valor 30 a variável y.
y = 30
#Guardando o valor da variável x momentaneamente na variável deposito.
deposito = x
#Transferindo o valor 30 da variável y para a variável x.
x = y
#Atribuindo a variável y o valor que anteriormente pertencia a variável x.
y = deposito
#Imprimindo os valores atuais.
print("Valor de x:",x)
print("Valor de y:",y)
