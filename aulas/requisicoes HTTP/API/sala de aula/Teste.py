import requests,json

link = "http://192.168.205.100:8080/usuarios"
resposta = requests.get(link)

print(f"status busca {resposta}")

meus_dados = {
    "nome": "Maikão",
    "email": "vou_de_jungle@gmail.com"
}

envio = requests.post(link, json=meus_dados)
print(f"status envio {envio}")
