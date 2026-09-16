"""
Construa um sistema para um radar de trânsito. O programa deve solicitar a velocidade atual de um carro em km/h.
A velocidade máxima permitida na via é de 80 km/h. Se o motorista estiver acima de 80 km/h, o programa deve exibir:
"Você foi multado por excesso de velocidade!".
Caso contrário, exiba: "Velocidade dentro do limite permitido. Boa viagem!".
"""
#resposta
veloc = int(input("Digite a velocidade aferida: "))
if veloc > 80:
    print("Você foi multado por excesso de velocidade!")
else:
    print("Velocidade dentro do limite permitido. Boa viagem!")
