import requests, json
log_cep = []

cep_solicitado = input("Digite o CEP: ")
link = f"https://viacep.com.br/ws/{cep_solicitado}/json/"
response = requests.get(link)


dicionario_recebido = response.json()
for i in dicionario_recebido:
    if i == "erro":
        print("Cep não encontrado.")


# if response.status_code == 200:
#
#     for i in dicionario_recebido:
#         if dicionario_recebido[i] == "":
#             continue
#
#         print(f"{i}: {dicionario_recebido[i]}")
#
#
#     try:
#         with open("historico_pesquisa.json", "r", encoding="utf-8") as file:
#             log_cep = json.load(file)
#
#     except FileNotFoundError:
#         print("Arquivo log não encontrado. Criando novo.")
#
#     finally:
#         log_cep.append(dicionario_recebido)
#
#         with open("historico_pesquisa.json", "w", encoding="utf-8") as arquivo:
#             json.dump(log_cep, arquivo, indent=4, ensure_ascii=False)








