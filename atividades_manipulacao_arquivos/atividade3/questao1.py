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

def media_aluno():

        media = 0.0
        dados = []
        nome_comparado = ""

        while True:
            nome = input("Digite o nome do aluno: ")
            with open("resultado.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                dados = []
                for i in linhas:
                    i = i.strip().split(";")
                    if i[0] == nome:
                        dados = i[2:6]
                        nome_comparado = i[0]

            if nome_comparado == nome:
                for i in dados:
                    media += float(i)
                media = media / 4
                print(f"Média do aluno: {media}")
                break
            else:
                if nome == "sair":
                    break
                print("Aluno não encontrado. Tente novamente ou digite sair.")



def consulta_status():
    alunos = []


    nome = input("Digite o nome do aluno: ")
    aluno = []

    with open("resultado.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for i in linhas:
            i = i.strip().split(";")
            alunos.append(i)
#Resolver
    for i in alunos:
        if i[0] == nome:
            aluno.append(i)

    print(f" {aluno[0]}: {aluno[5]}")









# while True:
#     print("Escolha uma opção:\n"
#           "1)Acrescentar um aluno.\n"
#           "2)Calcular média de um aluno.\n"
#           "3)Consultar status da aprovação.\n"
#           "4)Mostrar a maior média da turma.\n"
#           "5)sair.")
#     opcao = int(input(":"))
#
consulta_status()