import json
import requests

link = "https://viacep.com.br/ws/01001000/json/"

resposta = requests.get(link)

print(resposta)

with open("viacep.json", "w", encoding="utf-8") as file:
    json.dump(resposta.json(), file, indent=4, ensure_ascii=False)