import json

lista_aniversariantes = []
dados1 = []
dados2 = []
dados3 = []

with open("base1.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    for i in dados:
        dados1.append({
            "nome": i["nome"],
            "aniversario": i["aniversario"],
        })

with open("base2.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    for i in dados:
        dados2.append({
            "nome": i["nome"],
            "aniversario": i["aniversario"],
        })

with open("base3.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
    for i in dados:
        dados3.append({
            "nome": i["nome"],
            "aniversario": i["aniversario"],
        })

lista_aniversariantes.extend(dados1)
lista_aniversariantes.extend(dados2)
lista_aniversariantes.extend(dados3)

def pega_nome(item):
    return item["nome"]

lista_aniversariantes.sort(key = pega_nome)

with open("aniversariantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)






