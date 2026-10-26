import pandas as pd

df = pd.read_csv('funcionarios.csv', sep=';')

print('Todos os cargos:')
print(df)

cargos_altos = df[df['salario']>6000]

print("\nCargos acima de 6000")
print(cargos_altos)

cargos_altos.to_csv('cargos_altos.csv', index=False, encoding='utf-8', sep=';')
print('Cargos acima de 6000')

nova_linha=[{
    'id': '31',
    'nome': 'Marcos Vinicius',
    'salario': '6300.0',
    'cargo': 'Arquiteto de Soluções',
}]

nova_linha = pd.DataFrame(nova_linha)

cargos_altos = pd.concat([cargos_altos, nova_linha],ignore_index=True,)

print('\nCargo adicionado:')
print(cargos_altos)

cargos_altos = cargos_altos.drop(index=[0,1])

print('\nIndex 0 e 1 excluidos:')
print(cargos_altos)

cargos_altos['tempo_empresa'] = [24,36,12,48]
cargos_altos['tempo_empresa'] = cargos_altos['tempo_empresa'].astype(int)

estagiario = [{
        'id': '32',
        'nome': 'Alexandre Queiroz',
        'salario': '1500.0',
        'cargo': 'Estagiário',
        'tempo_empresa': 5,
}]
estagiario = pd.DataFrame(estagiario)
cargos_altos = pd.concat([cargos_altos, estagiario],ignore_index=True)

print(f'\n{cargos_altos}')
cargos_altos.to_csv('cargos_altos.csv', index=False, encoding='utf-8', sep=';')
