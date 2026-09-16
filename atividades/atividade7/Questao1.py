#resposta
import random

funcionarios = []
demitidos = []
mantidos = []
aumento = []
add_funcionario = ""
contagem = 0

while add_funcionario != "sair":
    add_funcionario = input("Digite o nome do funcionário que deseja adicionar ou digite 'sair' para sair.\nDigite aqui:")
    if add_funcionario != "sair":
        funcionarios.append(add_funcionario)

print(f"Quantidade de funcionários: {len(funcionarios)}")

for i in funcionarios:
    contagem += 1
    faturamento = random.randint(0, 500)
    print(f"O Funcionário: {i} faturou R${faturamento} Reais.")
    if faturamento < 300:
        demitidos.append(i)
    elif faturamento >= 400:
        aumento.append(i)
    else:
        mantidos.append(i)


print(f"Funcionários que serão demitidos: \n{demitidos}")
print(f"Funcionários que precisam melhorar seu rendimento: \n{mantidos}")
print(f"Funcionários que receberão aumento: \n{aumento}")







