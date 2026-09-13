#resposta
import random

funcionarios = []
add_funcionario = ""
contagem = 0

while add_funcionario != "sair":
    add_funcionario = input("Digite o nome do funcionário que deseja adicionar ou digite 'sair' para sair.\nDigite aqui:")
    if add_funcionario != "sair":
        funcionarios.append(add_funcionario)

print(f"Quantidade de funcionários: {len(funcionarios)}")

for i in funcionarios:
    contagem += 1
    print(f"Funcionário {contagem}: {i}")

for i in range(len(funcionarios)):
    faturamento = random.randint(0, 500)
    if faturamento < 250:
        print(f"O funcionário {funcionarios[i]} faturou este mês R${faturamento} e será demitido.")
    else:
        print(f"O funcionário {funcionarios[i]} faturou este mês R${faturamento} e receberá aumento.")


