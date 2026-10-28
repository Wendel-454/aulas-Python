import pandas as pd

df=pd.read_csv('estoque_supermercado.csv',
               dtype = {'preco': 'string'
                        })


df.insert(2,'preco_padronizado',df['preco'].str.replace(r'[^\d.,]','',regex=True))


print(df.to_string())
