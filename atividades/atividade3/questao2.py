"""
Uma fábrica empacota maçãs em caixas que cabem exatamente 12 unidades.
Crie um programa que pergunte ao usuário a quantidade total de maçãs colhidas no dia.
Utilizando o operador de módulo (%), calcule e exiba na tela quantas maçãs sobrarão fora das caixas
(ou seja, o resto da divisão por 12).
"""

quantMacas = int(input("Digite a quantidade total de maçãs colhidas no dia: "))
macasResto = quantMacas % 12
print("Ficarão fora das caixas",macasResto,"Maçãs")
