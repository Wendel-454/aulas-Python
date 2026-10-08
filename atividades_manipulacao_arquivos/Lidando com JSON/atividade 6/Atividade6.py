import json

lista_aniversariantes = []
dados1 = []
dados2 = []
dados3 = []

with open("base1.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    dados1.extend({
        "nome": dados["nome"],
        "aniversario": dados["aniversario"],
    })


lista_aniversariantes.extend(dados1)

for i in lista_aniversariantes:
    print(i)








