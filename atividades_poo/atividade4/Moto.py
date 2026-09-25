from Frete import Frete


class Moto(Frete):
    def calcular(self, destino, distancia,peso_carga):#metodo abstrato herdado
        print(F"Calculando frete via moto, com destino a {destino}.")
        if distancia > 0:
            valor = 2.50 * distancia
            print(f"Valor do frete: {valor}")
        else:
            print("Dados incorretos")

        if peso_carga > 100:
            excedente = peso_carga - 100
            print(f"Carga {excedente} acima do permitido (100kg)")
        else:
            print("carga dentro do limite (100kg)")







