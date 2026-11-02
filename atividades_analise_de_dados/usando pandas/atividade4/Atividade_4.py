import pandas as pd

# 1. Carregamento dos dados
df=pd.read_csv('estoque_supermercado.csv',
       dtype = {'preco': str,
                'quantidade':str,
                'setor':str,
                })

# 2. Execução das limpezas (Preço, Quantidade, Setor, Datas)
# (Seus códigos de tratamento aqui)
df['preco']=df['preco'].str.replace(r'[^\d.]','',regex=True)
df['preco']=pd.to_numeric(df['preco'],errors='coerce').astype('float')
df['preco']=df['preco'].fillna(df['preco'].mean()).round(2)

df['quantidade']=pd.to_numeric(df['quantidade'],errors='coerce')
df['quantidade']=df['quantidade'].fillna(0).astype(int)

df['setor']=df['setor'].str.strip().str.lower()
df['setor']=df['setor'].fillna('sem setor')

df['data_compra']=pd.to_datetime(df['data_compra'],format='%d/%m/%Y')
df['data_vencimento'] = pd.to_datetime(df['data_vencimento'],format='%d/%m/%Y')

df.insert(6,'soma_estoque',(df['quantidade']  * df['preco']).round(2))


# 3. Exibição do DataFrame Limpo
print("\n--- BASE DE DADOS LIMPA ---")
print(df.to_string())

# 4. Resultados das Análises

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
# (Seu filtro de alerta de vencimento)
produtos_a_vencer = df[(df['data_vencimento']>='2026-10-27') & (df['data_vencimento']<='2026-11-03')]
print(produtos_a_vencer.to_string())

print("\n--- MAIOR QUANTIDADE A VENCER ---")
# (Seu lógica de qualidade de estoque)
maior_vencimento = produtos_a_vencer.groupby('setor')['soma_estoque'].sum().reset_index()
print(f'{maior_vencimento.max().to_string()}')

print('\n===Produtos sem data de vencimento===')
print(df[df['data_vencimento'].isna()].to_string())

print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
# (Seu lógica de qualidade de estoque)

print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
# (Sua lógica de agrupamento e soma do valor total de estoque)
soma_setor = df.groupby('setor')['soma_estoque'].sum().reset_index()
print(f'{soma_setor.max().to_string()}')

df.to_csv('estoque_tratado.csv',index=False)





