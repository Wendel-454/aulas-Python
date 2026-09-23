from Animal import Animal
from Mamifero import Mamifero
from Ave import Ave

leao = Mamifero("Simba",5,70, 80)
gaviao = Ave("Sky",2,75,120)

leao.__nivel_fome = -999
leao.__idade = -10
print("Tentativa de alteração direta dos atributos privados (Proteção do Encapsulamento")
leao.exibir_resumo()
gaviao.exibir_resumo()
print("Testando ações que alteram o estado interno via Herança e Encapsulamento")
leao.correr()
gaviao.voar()
gaviao.voar()
leao.exibir_resumo()
gaviao.exibir_resumo()
print("Testando alimentação")
leao.alimentar(50)
leao.alimentar(-10)
leao.exibir_resumo()
print("\n--- RESUMO DO MAMÍFERO ---")
leao.emitir_som()
leao.exibir_resumo()
print("\n--- RESUMO DA AVE ---")
gaviao.emitir_som()
gaviao.exibir_resumo()




