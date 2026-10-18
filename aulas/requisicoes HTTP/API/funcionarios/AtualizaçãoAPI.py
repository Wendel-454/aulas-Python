import requests, json

with open("dados_funcionarios_atualizados.json", encoding="utf-8") as dados:
    dados_json = json.load(dados)


    for i in dados_json:
        funcionario = i
        funcionario_atualizado = {
            "cargo": i['cargo'],
            "cep": i['cep'],
            "cidade": i['cidade'],
            "estado": i['estado'],
            "id": i['id'],
            "nome": i['nome'],
            "salario": i['salario'],
            "tempoEmpresa": i['tempoEmpresa']
        }


        id = funcionario["id"]
        atualizacao = requests.put(f"http://192.168.205.100:8080/funcionarios/"+str(id), json=funcionario_atualizado)
        print(f"{i['nome']} - {atualizacao.status_code}")
