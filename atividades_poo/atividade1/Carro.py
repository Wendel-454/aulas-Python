import time

class Carro:

    def __init__(self, nome,categoria, modelo, cor, ano, potencia, motor):
        self.nome = nome
        self.categoria = categoria
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.potencia = potencia
        self.motor = motor
        self.ligado = False
        self.trancado = False

    def __str__(self):
        return (f"Nome:      {self.nome}      \n"
                f"Categoria: {self.categoria} \n"
                f"Modelo:    {self.modelo}    \n"
                f"Cor:       {self.cor}       \n"
                f"Ano:       {self.ano}       \n"
                f"Potência:  {self.potencia}cv\n"
                f"Motor:     {self.motor}     \n")

    def ligar(self):
        if not self.ligado:
            print("Girando chave de ignição...")
            time.sleep(1)
            print("Motor de partida acionando...")
            time.sleep(1)
            self.ligado = True
            print("Motor funcionando!")
            time.sleep(1)
        else:
            print("Motor já está funcionando!")

    def desligar(self):
        if not self.ligado:
            print("Motor já está desligado!")
        else:
            print("Desvirando chave de ignição...")
            time.sleep(1)
            self.ligado = False
            print("Motor desligado!")
            time.sleep(1)

    def trancar(self):
        if not self.trancado:
            print("Acionando controle de alarme...")
            time.sleep(1)
            print("Carro trancado!")
        else:
            print("Carro já trancado!")

    def destrancar(self):
        if not self.trancado:
            print("Carro já está destrancado!")
        else:
            print("Acionando controle de alarme...")
            time.sleep(1)
            print("Carro destrancado!")

chevette = Carro("Chevette","Sedan","DL", "Vermelho", "1993", 81, "1.6/S (OHC)")
gol = Carro("Gol","Hatch","GL", "Prata","1992","98","AP 1.8")
palio = Carro("Palio","Hatch","EX", "Cinza","1998","61","Fiasa 1.0")
opala = Carro("Opala","Grand Sedan","Diplomata SE Collectors", "Preto","1992","121", "Opala 4100")
c10 = Carro("Chevrolet C-10","Caminhonete","Veraneio", "Azul","1971","151","Chevrolet 261")

carros = [chevette, gol, palio, opala, c10]
for i in carros:
    print(i)
