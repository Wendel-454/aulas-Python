
class Coordenacao: #classe PAI
    def __init__(self,professores, cursos, alunos):
        self.__professores = professores
        self.__cursos = cursos
        self.__alunos = alunos

    #lista de GET
    @property
    def cursos(self):
        return self.__cursos

    @property
    def professores(self):
        return self.__professores

    @property
    def alunos(self):
        return  self.__alunos