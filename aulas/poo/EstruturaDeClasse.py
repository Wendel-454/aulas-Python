class Aluno:
    nome_aluno = "joãos" #Atributo > faz referencia a uma variavel dentro da classe

    def mostrarNomeAluno(self):#metodo
        print(self.nome_aluno)

    def __init__(self, nome_do_aluno, registro):#metodo construtor
        #nome = novo atributo da classe
        #nome_do_aluno = parâmetro
        self.nome = nome_do_aluno
        self.registro = registro
        #todos os alunos, Obrigatoriamente precisam ter nome e registro

#aluno = objeto
aluno = Aluno("Jão",111)
print(aluno.nome_aluno, aluno.registro)
