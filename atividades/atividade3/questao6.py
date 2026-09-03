"""
Um programador iniciante tentou criar um validador de senhas e escreveu o seguinte código:
senha_cadastrada = 1234
senha_digitada = input("Digite sua senha: ")
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)


Mesmo que o usuário digite os números 1234 no teclado, o programa sempre responde False.
Explique tecnicamente por que isso acontece (lembre-se dos tipos de dados estudados em sala) e reescreva o código
corrigindo o erro como comentário no seu próprio código (no arquivo .py).

"""
#Resposta
"""
O código retorna False pois todo imput() retorna uma string e não pode ser comparado com um inteiro.
"""
#Código corrigido
senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)