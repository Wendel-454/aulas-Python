import requests, json

cep_solicitado = input("Digite o CEP: ")
link = f"https://viacep.com.br/ws/{cep_solicitado}/json/"
response = requests.get(link)

dicionario_recebido = response.json()

for i in dicionario_recebido:
    if dicionario_recebido[i] == "":
        continue

    print(f"{i}: {dicionario_recebido[i]}")

with open("historico_pesquisa.json", "a", encoding="utf-8") as arquivo:
    json.dump(dicionario_recebido,arquivo, indent=4, ensure_ascii=False)
