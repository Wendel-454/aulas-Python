import json

catalogo_livros = []
catalogo_livros_load = []

#etapa1
with open("banco_livros.txt", encoding="utf-8") as arquivo:
    for i in arquivo:
        if i == "":
            continue
        i = i.strip().split(";")
        catalogo_livros.append({
                                "id":i[0],
                                "nome":i[1],
                                "descricao":i[2],
                                "preco":float(i[3]),
                                "em_estoque":int(i[4])
        })

#etapa2
with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)

#etapa3
catalogo_livros.extend([
    {
        "id":31,
        "nome":"O Poderoso Chefao",
        "descricao":"Saga familiar sobre crime e poder na mafia",
        "preco":49.90,
        "em_estoque":12
    },
    {
        "id":32,
        "nome":"O Silencio dos Inocentes",
        "descricao":"Suspense policial sobre um assassino serial",
        "preco":39.90,
        "em_estoque":18

    },
    {   "id":33,
         "nome":"Forrest Gump",
         "descricao":"Historia de um homem que atravessa momentos marcantes da historia americana",
         "preco":34.90,
         "em_estoque":20
     },
    {
        "id":34,
        "nome":"O Pianista",
        "descricao":"Relato dramatico de sobrevivencia durante o Holocausto",
        "preco":42.90,
        "em_estoque":10
    },
    {
        "id":35,
        "nome":"O Leitor",
        "descricao":"Drama sobre memoria, culpa e passado na Alemanha pos-guerra",
        "preco":36.90,
        "em_estoque":14
    }
])

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)

#Etapa4
with open("catalogo.json", "r", encoding="utf-8") as arquivo:
    catalogo_livros_load = json.load(arquivo)

def catalogo():
    estoque_total = 0.0

    for i in catalogo_livros_load:
        estoque_total += i["preco"]
        if i["em_estoque"] < 15:
            print(f"O livro {i['nome']} tem apenas {i['em_estoque']} livros em estoque.")

    print(f"Valor total do estoque é de R${estoque_total:.2f}")

catalogo()

