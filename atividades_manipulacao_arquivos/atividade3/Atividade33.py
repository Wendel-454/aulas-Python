def acrescentar_aluno():
    nome = input("Nome do aluno: ")
    turma = input("Turma: ")


    nota1 = float(input("Nota do 1º bimestre: "))
    nota2 = float(input("Nota do 2º bimestre: "))
    nota3 = float(input("Nota do 3º bimestre: "))
    nota4 = float(input("Nota do 4º bimestre: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4


    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"

    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{turma};{nota1};{nota2};{nota3};{nota4};{status}\n")

    print("Aluno cadastrado com sucesso!")


def calcular_media():
    nome = input("Digite o nome do aluno: ")
    encontrado = False

    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if dados[0] == nome:
                    nota1 = float(dados[2])

                    nota2 = float(dados[3])

                    nota3 = float(dados[4])

                    nota4 = float(dados[5])

                    media = (nota1 + nota2 + nota3 + nota4) / 4

                    print(f"A média de {nome} é {media:.2f}")
                    encontrado = True
                    break


        if encontrado == False:
            print("Aluno não encontrado.")


    except FileNotFoundError:
        print("Arquivo não encontrado.")


def consultar_status():
    nome = input("Digite o nome do aluno: ")
    encontrado = False


    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if dados[0] == nome:
                    print(f"{nome} está {dados[6]}")
                    encontrado = True
                    break


        if encontrado == False:
            print("Aluno não encontrado.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")



def maior_media():
    turma = input("Digite a turma: ")
    maior = -1
    aluno_maior = ""
    encontrado = False



    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")

                if dados[1] == turma:
                    nota1 = float(dados[2])
                    nota2 = float(dados[3])
                    nota3 = float(dados[4])
                    nota4 = float(dados[5])

                    media = (nota1 + nota2 + nota3 + nota4) / 4

                    if media > maior:
                        maior = media
                        aluno_maior = dados[0]

                    encontrado = True

        if encontrado == True:
            print(f"Maior média da turma {turma}: {maior:.2f}")
            print(f"Aluno: {aluno_maior}")
        else:
            print("Turma não encontrada.")


    except FileNotFoundError:
        print("Arquivo não encontrado.")





while True:
    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Acrescentar aluno")
    print("2 - Calcular média")
    print("3 - Consultar status")
    print("4 - Maior média da turma")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")



    match opcao:
        case "1":
            acrescentar_aluno()

        case "2":
            calcular_media()

        case "3":
            consultar_status()

        case "4":
            maior_media()

        case "5":
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida!")
