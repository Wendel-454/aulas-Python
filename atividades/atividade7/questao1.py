#resposta
import random

funcionarios = []
add_funcionario = ""

while add_funcionario != "sair":
    add_funcionario = input("Digite o nome do funcionário que deseja adicionar ou digite 'sair' para sair.\nDigite aqui:")
    if add_funcionario != "sair":
        funcionarios.append(add_funcionario)

for i in range(len(funcionarios)):
    sorteio = random.randint(0, 1)
    if sorteio == 0:
        print(f"O funcionário {funcionarios[i]} será demitido")
    else:
        print(f"O funcionário {funcionarios[i]} Receberá aumento")


