from aulas.poo.heranca.diretoria.Coordenacao import Coordenacao


class Sala(Coordenacao):
    def __init__(self, laboratorio, tipo, professores, cursos, alunos):
        super().__init__(professores, cursos, alunos)
        self.__laboratorio = laboratorio
        self.__tipo = tipo
        self.__alunos = alunos


    def ter_aula(self):
        print(f"Aula de: {self.cursos}"
              f"no laboratório de {self.__tipo}"
              f"\n Com o professor {self.professores}"
              f"\n Com os alunos")
        for aluno in self.alunos:
            print(aluno)



sala_1 = Sala("Lab 7",
              "Tecnologia",
              "João",
              "Python",
              ["fulano", "Beltrano","Ciclano",])

sala_1.ter_aula()