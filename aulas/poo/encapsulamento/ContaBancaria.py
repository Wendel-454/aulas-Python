#Forma convencional não utilizada em python
class ContaBancaria():#nome da classe
    def __init__(self, titular, saldo):#metodo construtor
        self.titular = titular #self.atributo = valor do parametro
        self.__saldo = saldo #private

    #metodods Getters e Setters (Get = pegar e Set = inserir)
    def get_titular(self):
        senha = 1234
        senha_digitada = int(input('Digite sua senha: '))

        if senha == senha_digitada:
            return self.titular
        else:
            return "Senha incorreta"

    def set_titular(self, novo_titular):
        senha = 1234
        senha_digitada = int(input('Digite sua senha: '))

        if senha == senha_digitada:
             self.titular = novo_titular
             return "titular atualizado"
        else:
            return "Senha incorreta"


conta_banco = ContaBancaria('Maikon', 100)
print(conta_banco.titular)
print(conta_banco.get_titular())

conta_banco.set_titular("Marcos")
print(conta_banco.get_titular())