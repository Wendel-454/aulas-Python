from Frete import Frete

class Caminhao (Frete):
    def calcular(self, destino, distancia,peso_carga):  # metodo abstrato herdado
        print(f"Calculando frete via caminhão, com destino a {destino}.")
        if distancia > 0:
            valor = 5.50 * distancia
            print(f"Valor de do frete: {valor}")
        else:
            print("Dados incorretos")

        if peso_carga > 1000:
            excedente = peso_carga - 1000
            print(f"Carga {excedente} acima do permitido (1000kg)")
        else:
            print("carga dentro do limite (1000kg)")

