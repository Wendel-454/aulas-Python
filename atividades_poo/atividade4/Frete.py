from abc import ABC, abstractmethod

class Frete(ABC):
    @abstractmethod
    def calcular(self,destino, distancia,peso_carga):
        pass

    def iniciar_frete(self):
        print("Iniciando frete.")


