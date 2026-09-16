"""
Imagine que você tem um orçamento total para uma viagem, por exemplo, R$ 500.
Escreva um programa que defina esse valor em uma variável e peça ao usuário para digitar o valor de cada gasto que ele
realizar.
Usando um laço while, o programa deve subtrair cada gasto do orçamento total e exibir o saldo restante.
O laço deve continuar pedindo novos gastos enquanto o orçamento for maior que zero.
Se o usuário gastar o dinheiro (ou seja, o orçamento chegar a zero ou ficar negativo), o programa deve encerrar o
laço e exibir a mensagem: "Atenção: Você ficou sem saldo ou estourou seu orçamento!"

"""
#Resposta
orcamento = 500
sobra = 0
gasto = 0
print(f"Você tem um orçamento de: R${orcamento}")
while orcamento > gasto:
    if gasto < orcamento:
        gasto += float(input("Digite o valor do gasto: "))
        sobra = orcamento - gasto
        if  gasto > orcamento:
            print("Orçamento estourado")
        print(f"Saldo R${sobra}")
    else:
        print("Orçamento estourado")
        print(f"Saldo R${sobra}")
print(f"O gasto sería de R${gasto}")

