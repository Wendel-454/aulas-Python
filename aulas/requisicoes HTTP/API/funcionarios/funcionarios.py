import json, requests

link_funcionarios = "http://192.168.205.100:8080/funcionarios"
link_cep = "https://viacep.com.br/ws/01001000/json/"

resposta = requests.get(link_funcionarios)
print(resposta.json())

lista_funcionarios = resposta.json()

for i in lista_funcionarios:
    print(i['nome'])

cep = requests.get(link_cep)
dicionario_cep = cep.json()

for x, y in dicionario_cep.items():
    print(f"chave: {x}, valor: {y}")