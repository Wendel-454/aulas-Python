from csv import excel
from json import JSONDecodeError
from sys import exception

import requests
import json

link_funcionarios = "http://192.168.205.100:8080/funcionarios"

#                json    python
# dados vazios = null == None

resposta = requests.get(link_funcionarios) # enviando uma requisição do tipo GET



print(resposta.json()) # mostrando o que recebeu na requisição HTTP

lista_funcionarios = resposta.json()

print("--- LISTA DE FUNCIONARIOS SEM ENDEREÇO CADASTRADO ---\n")

for funcionario in lista_funcionarios:
    if funcionario['cep'] is None:
        print(f"O funcionário(a) {funcionario['nome']} não tem cep cadastrado")

        while True:
            try:
                cep_digitado = input("Digite um CEP válido: ")
                link_cep = f"https://viacep.com.br/ws/{cep_digitado}/json/"
                resposta = requests.get(link_cep)
                validacao = resposta.json()


                if resposta.status_code == 200:
                    dicionario_funcionario = resposta.json()
                    var_len = len(dicionario_funcionario)


                    for chave, valor in dicionario_funcionario.items():
                        if chave != "erro":

                            if chave == 'localidade':
                                funcionario['cidade'] = valor
                            if chave == 'estado':
                                funcionario['estado'] = valor
                            funcionario['cep'] = cep_digitado
                            print("Dados adicionados com sucesso!\n")
                            break

            except Exception as erro:
                print("Cep inválido")

# base de dados atualizada
for funcionario in lista_funcionarios:
    print(funcionario)

# inserir dados onde estiver algum dado vazio ok
# no cep, apenas aceitar CEPS válidos
#   (que tenham retorno de cidade, estado, etc...)
# salvar os dados preenchidos em um arquivo JSON
#   (ex: dados_funcionarios_atualizados.json)