from abc import ABC, abstractmethod

class Frete(ABC):
    @abstractmethod
    def calcular(self,destino, distancia):
        pass

    def iniciar_frete(self):
        print("Iniciando frete.")


