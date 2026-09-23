class Animal:
    def __init__(self,nome,idade,nivel_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = nivel_fome #0 a 100

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self,idade):
        if idade < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = idade

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self,nivel_fome):
        if nivel_fome < 0:
            self.__nivel_fome = 0
        elif nivel_fome > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = nivel_fome

    def alimentar(self,porcao):
        if porcao <= 0:
            print("Erro: Porção inválida.")
        else:
            self.nivel_fome -= porcao

    def emitir_som(self):
        print(f"{self.__nome} faz som genérico.")

    def exibir_resumo(self):
        print(f"Nome: {self.__nome}, Idade: {self.__idade}, Nivel de fome: {self.__nivel_fome}")




