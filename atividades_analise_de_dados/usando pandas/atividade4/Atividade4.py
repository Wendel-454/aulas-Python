import pandas as pd

df=pd.read_csv('estoque_supermercado.csv',
       dtype = {'preco': str,
                'quantidade':str
                })

preco_padronizado=(df['preco']
                   .str.replace(r'[^\d. ]','',regex=True)
                   )

preco_padronizado=pd.to_numeric(preco_padronizado, errors='coerce')
df['quantidade']=pd.to_numeric(df['quantidade'],errors='coerce')

preco_padronizado=preco_padronizado.fillna(preco_padronizado.mean())

df.insert(2,'preco_padronizado',preco_padronizado)

df['preco_padronizado']                                                                                                                                                                                                                                                     =df['preco_padronizado'].round(2)

print(df.to_string())






