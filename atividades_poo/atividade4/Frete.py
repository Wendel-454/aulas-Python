from abc import ABC, abstractmethod

class Frete(ABC):
    @abstractmethod
    def calcular(self,valor_por_km, distancia):
        pass

    def iniciar_frete(self):
        print("Iniciando frete.")


