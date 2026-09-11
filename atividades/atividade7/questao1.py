#resposta
add_funcionario = ""
funcionarios = []
while add_funcionario != "0":
    add_funcionario = input("Digite o nome do funcionário que deseja adicionar ou digite 'sair' para sair.\nDigite aqui:")
    funcionarios.append(add_funcionario)
print(funcionarios)

