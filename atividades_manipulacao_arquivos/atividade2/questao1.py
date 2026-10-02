def acr_aluno():
    aluno = input("Digite o nome do aluno: ")
    turma = int(input("Digite a turma do aluno: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    nota4 = float(input("Digite a quarta nota do aluno: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media > 7.0:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    with open("resultado.txt", "a") as arquivo:
        arquivo.write(f"{aluno};{turma};{nota1};{nota2};{nota3};{nota4};{resultado}\n")



# while True:
#     print("Escolha uma opção:\n"
#           "1)Acrescentar um aluno.\n"
#           "2)Calcular média de um aluno.\n"
#           "3)Consultar status da aprovação.\n"
#           "4)Mostrar a maior média da turma.\n"
#           "5)sair.")
#     opcao = int(input(":"))
#
acr_aluno()