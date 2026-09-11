#resposta
add_funcionario = ""
funcionarios = []
while add_funcionario != "sair":
    add_funcionario = input("Digite o nome do funcionário que deseja adicionar ou digite 'sair' para sair.\nDigite aqui:")
    if add_funcionario != "sair":
        funcionarios.append(add_funcionario)
print(funcionarios)

