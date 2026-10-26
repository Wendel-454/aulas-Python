import pandas as pd

dados = pd.read_csv('dados_despadronizados.csv',
                    dtype = {'cpf': 'string',
                             'numero': 'string',
                             'salario': 'string'})



dados.insert(2,'cpf_formatado',dados['cpf'].str.replace(r'[,.\- ]','', regex=True))
dados.insert(3,'cpf_validado',dados['cpf_formatado'].str.fullmatch(r'\d{11}'))

dados.insert(5,'num_formatado',dados['numero'].str.replace(r'[\D ]','', regex=True))
dados.insert(6,'num_validado',dados['num_formatado'].str.fullmatch(r'\d{11,13}'))

dados_sal_formatado = (dados["salario"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",",".", regex=False)
                              .astype(float)
                               )

dados.insert(8, "salario_formatado",dados_sal_formatado)

print(dados.to_string())


