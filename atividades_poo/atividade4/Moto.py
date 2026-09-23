from Frete import Frete


class Moto(Frete):
    def calcular(self, valor_km, distancia):#metodo abstrato herdado
        print("Calculando frete via moto.")
        if valor_km > 0 and distancia > 0:
            valor = valor_km * distancia
            print("Valor de do frete: ", valor)
        else:
            print("Dados incorretos")

moto = Moto()
moto.calcular(-10,100)







