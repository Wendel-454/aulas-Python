from atividades_poo.atividade3.Animal import Animal


class Ave(Animal):
    def __init__(self,envergadura_asas,nome,idade,nivel_fome):
        super().__init__(self,nome,idade,nivel_fome)
        self.__envergadura_asas = envergadura_asas

    def voar(self):
        if self.__nivel_fome > 80:
            print(f"Voo negado: {self.__nome} está faminto demais para voar!")
        else:
            print(f"{self.__nome} voou com suas asas de {self.__envergadura_asas}cm!")


    def emitir_som(self):
        print(f"{self.__nome} canta um som melodioso!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Envergadura das asas: {self.__envergadura_asas}")