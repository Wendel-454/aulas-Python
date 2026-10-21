import pandas as pd
df = pd.read_csv("funcionarios.csv", sep=";")

print("Salários menores que 3000 e maiores que 5000: ")
print(df[
          (df["salario"] < 3000) | (df["salario"] > 5000) | (df["salario"] == 3100)
      ])

print("\nCargos específicos:")
print(df[
          (df['cargo'] == "Analista de Dados") |
          (df['cargo'] == "Analista de Sistemas") |
          (df['cargo'] == "Desenvolvedor Java") |
          (df['cargo'] == "Cientista de Dados")
      ])

print("\nFuncionários com salário maior que 6000: ")
print(df[df['salario']> 6000][['nome', 'salario']])

print("\nFuncionários com id par")
print(df[df['id']%2 == 0][['id','nome']])










# print(df[df['salario'] > 6000][['nome', 'salario']])

