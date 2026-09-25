from Moto import Moto
from Caminhao import Caminhao


# 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
# Descomente a linha abaixo para testar e provar que o Python bloqueia:
# objeto_generico = Frete()

obj1 = Moto()
obj2 = Caminhao()

lote = [obj1, obj2]

for i in lote:
    i.iniciar_frete()
    i.calcular("Brasilia",50,200)