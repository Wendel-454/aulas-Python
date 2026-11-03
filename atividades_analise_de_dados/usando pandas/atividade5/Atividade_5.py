import pandas as pd

df=pd.read_csv('vendas_mercados.csv')

df['Lucro'] = (df['Preco_Unitario'] - df['Custo_Unitario']) * df['Quantidade']

tabela_lucro_por_mercado = df.groupby('Mercado',as_index=False)['Lucro'].sum()

#Questão 1
maior_lucro = tabela_lucro_por_mercado.loc[tabela_lucro_por_mercado['Lucro'].idxmax()]
print('Questão 1:')
print(f'O mercado que obteve maior lucro foi {maior_lucro["Mercado"]}'
      f' com o lucro de {maior_lucro["Lucro"]}.\n')

#Questão 2
tabela_forma_pagamento = df.groupby(
    ['Regiao','Forma_Pagamento']
).size().reset_index(name='Quantidade')
mais_utilizada = tabela_forma_pagamento.loc[tabela_forma_pagamento.groupby('Regiao')['Quantidade'].idxmax()]
print('Questão 2:')
print('Formas de pagamento mais utilizadas de cada região:')
print(mais_utilizada.to_string(index=False))

#Questão 3
print('\nQuestão 3:')
tabela_itens_vendidos = df.groupby('Produto', as_index=False)['Quantidade'].sum()

mais_vendido = tabela_itens_vendidos.loc[tabela_itens_vendidos['Quantidade'].idxmax()]
print(f'O produto mais vendido foi {mais_vendido["Produto"]} com {mais_vendido["Quantidade"]} itens vendidos.')

menos_vendido = tabela_itens_vendidos.loc[tabela_itens_vendidos['Quantidade'].idxmin()]
print(f'O produto menos vendido foi {menos_vendido["Produto"]} com {menos_vendido["Quantidade"]} itens vendidos.')



