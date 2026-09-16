"""
Uma festa exclusiva possui regras específicas para a entrada de convidados.
Para ter o acesso liberado, a pessoa precisa atender a uma das seguintes combinações de condições:
*Ter idade maior ou igual a 18 anos E possuir o convite VIP;
*OU ser um dos organizadores do evento (independente da idade).

Crie um formulário no Python que solicite:
1 A idade da pessoa (inteiro);
2 Se ela possui convite VIP (digitar 1 para Sim, 0 para Não);
3 Se ela é organizadora do evento (digitar 1 para Sim, 0 para Não)

Escreva uma única estrutura if combinando os operadores and e or para validar a regra.
Se a condição for verdadeira, exiba: "Entrada PERMITIDA! Seja bem-vindo(a)".
Caso contrário (else), exiba: "Entrada NEGADA! Você não atende aos requisitos".
"""
#Resposta
idade = int(input("Digite sua idade: "))
vip = int(input("Possui convite VIP? (1 sim / 2 não): "))
org = int(input("É organizador do evento? (1 sim / 2 não: " ))

if idade >= 18 and vip == 1 or org == 1:
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:
    print("Entrada NEGADA! Você não atende aos requisitos")