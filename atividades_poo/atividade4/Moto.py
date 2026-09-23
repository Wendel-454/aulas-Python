from Frete import Frete


class Moto(Frete):
    def calcular(self, destino, distancia):#metodo abstrato herdado
        print("Calculando frete via moto.")
        if distancia > 0:
            valor = 2.50 * distancia
            print("Valor de do frete: ", valor)
        else:
            print("Dados incorretos")

moto = Moto()
moto.calcular(-10,100)







