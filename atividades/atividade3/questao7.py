"""
Crie um pequeno formulário para um hospital.
O programa deve perguntar a idade e o peso do doador.
As regras para doar sangue são:
ter idade maior ou igual a 16 anos, ter idade menor ou igual a 69 anos E pesar mais que 50kg.
Escreva a lógica que verifica se o doador atende a todas essas condições e exiba na tela o resultado (True ou False).
"""
#Resposta
idade = int(input("Digite sua idade: "))
peso = float(input("Digite sua peso: "))
resultado = idade >= 16 and idade <= 69 and peso >= 50
print("Pode ser doador?", resultado)