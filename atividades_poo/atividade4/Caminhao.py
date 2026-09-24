from Frete import Frete

class Caminhao (Frete):
    def calcular(self, destino, distancia,peso_carga):  # metodo abstrato herdado
        print("Calculando frete via caminhão.")
        if distancia > 0:
            valor = 5.50 * distancia
            print("Valor de do frete: ", valor)
        else:
            print("Dados incorretos")

        if peso_carga > 1000:

            print("Carga acima do permitido (1000kg)")

