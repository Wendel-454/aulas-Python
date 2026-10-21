import pandas as pd
df = pd.read_csv("funcionarios.csv", sep=";")

print("Salários menores que 3000 e maiores que 5000: ")
print(df[
          (df["salario"] < 3000) | (df["salario"] > 5000)
      ])

print("\nCargos específicos:")
print(df[
          (df['cargo'] == "Analista de Dados") |
          (df['cargo'] == "Analista de Sistemas") |
          (df['cargo'] == "Analista de Sistemassos") |
          (df['cargo'] == "Desenvolvedor Java") |
          (df['cargo'] == "Cientista de Dados")
      ])

print("\nPessoas com salário maior que 6000: ")
print(df[df['salario'] > 6000][['nome', 'salario']])

