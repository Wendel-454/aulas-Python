import json

loja =\
{
    "nome": "TechStore",
    "produtos":[
        {
            "nome": "Teclado",
            "preco": 150.00,
            "quantidade": 10
        },
        {
            "nome": "Mouse",
            "preco": 80.00,
        },
        {
            "nome": "Monitor",
            "preco": 900.00,
            "quantidade": 5
        }
    ]
}
with open('estoque.json', 'w', encoding="utf=8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)

with open('estoque.json', 'r', encoding="utf=8") as arquivo:
    dados_lidos = json.load(arquivo)

for i in dados_lidos['produtos']:
    print(f"O produto {i['nome']} custa R${i['preco']} ")

dados_lidos['produtos'].append({
    "nome": "Fone de Ouvido",
    "preco": 99.00,
    "quantidade": 10
})

with open('estoque.json', 'w', encoding="utf=8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)