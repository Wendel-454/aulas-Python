import time


def acr_aluno():

    def pedir_nota(mensagem):
        while True:
            nota = float(input(mensagem))
            if nota >= 0.0 and nota <= 10.0:
                return nota
            print("A nota deve ser entre 0.0 e 10.0.")

    try:
        aluno = input("Digite o nome do aluno: ")
        turma = int(input("Digite a turma do aluno: "))
        nota1 = pedir_nota("Digite a primeira nota do aluno: ")
        nota2 = pedir_nota("Digite a segunda nota do aluno: ")
        nota3 = pedir_nota("Digite a terceira nota do aluno: ")
        nota4 = pedir_nota("Digite a quarta nota do aluno: ")
        media = (nota1 + nota2 + nota3 + nota4) / 4

        if media >= 7.0:
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"

        with open("alunos.txt", "a") as arquivo:
            decisao = input(
                f"Deseja adicionar o aluno {aluno};{turma};{nota1};{nota2};{nota3};{nota4};{resultado}?\n s/n:")
            if decisao == "s" or decisao == "S":
                arquivo.write(f"{aluno};{turma};{nota1};{nota2};{nota3};{nota4};{resultado}\n")
                print("Aluno adicionado com sucesso.")
            else:
                print("Aluno não adicionado.")
                time.sleep(3)

    except ValueError:
        print("Dados incorretos.")
        time.sleep(3)

def media_aluno():

        media = 0.0
        dados = []
        nome_comparado = ""

        while True:
            nome = input("Digite o nome do aluno: ")
            with open("alunos.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                dados = []
                for i in linhas:
                    if i.strip() == "":
                        continue
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

def cnslt_status():
    nome = input("Digite o nome do aluno: ")

    lista_alunos = []
    alvo = []

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for i in linhas:
            if i.strip() == "":
                continue
            i = i.strip().split(";")
            lista_alunos.append(i)

    for i in lista_alunos:
        if i[0] == nome:
            alvo = i

    try:
        print(f"O aluno {alvo[0]} foi {alvo[6]}")
    except IndexError:
        print("aluno não encontrado.")

def maior_media():
    aln_turma = []
    aln_media = []

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        turma = input("Digite a turma: ")
        linhas = arquivo.readlines()
        for i in linhas:
            if i.strip() == "":
                continue
            i = i.strip().split(";")
            if i[1] == turma:
                aln_turma.append([float(i[2]),float(i[3]),float(i[4]),float(i[5]),i[0]])

    for i in aln_turma:
        aln_media.append([((i[0]+i[1]+i[2]+i[3])/4),i[4]])

    try:
        mlhr_media = max(aln_media)
        print(f"A melhor média na turma {turma} foi {mlhr_media[0]} e pertence ao aluno(a) {mlhr_media[1]}.")
    except ValueError:
        print("Turma não encontrada.")



def main():

    while True:
        print("Escolha uma opção:\n"
              "1)Acrescentar um aluno.\n"
              "2)Calcular média de um aluno.\n"
              "3)Consultar status da aprovação.\n"
              "4)Mostrar a maior média da turma.\n"
              "5)sair.")
        opcao = input(":")
        match opcao:
            case "1":
                acr_aluno()
                time.sleep(3)
            case "2":
                media_aluno()
                time.sleep(3)
            case "3":
                cnslt_status()
                time.sleep(3)
            case "4":
                maior_media()
                time.sleep(3)
            case _:
                break

main()

