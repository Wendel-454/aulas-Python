import pandas as pd

df=pd.read_csv('estoque_supermercado.csv',
       dtype = {'preco': str,
                'quantidade':str,
                'setor':str,
                })

df['preco']=df['preco'].str.replace(r'[^\d.]','',regex=True)
df['preco']=pd.to_numeric(df['preco'],errors='coerce').astype('float')
df['preco']=df['preco'].fillna(df['preco'].mean()).round(2)

df['quantidade']=pd.to_numeric(df['quantidade'],errors='coerce')
df['quantidade']=df['quantidade'].fillna(0).astype(int)

df['setor']=df['setor'].str.strip().str.lower()
df['setor']=df['setor'].fillna('sem setor')

print(df.to_string())






