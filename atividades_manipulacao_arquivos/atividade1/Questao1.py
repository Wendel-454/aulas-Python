produtos = []
resposta1 = ""
resposta2 = 0
texto_produto = ""
total = 0
cliente = input("Digite o nome do cliente: ")

while True:
    try:
        resposta1 = str(input("Digite o produto ou 'sair' para sair:"))
        if resposta1 == "sair":
            break
        resposta2 = float(input("Digite o valor do produto:"))
        produtos.append([resposta1, resposta2])
    except ValueError:
        print("Erro ao processar. Reiniciando operação.")

for i in produtos:
    texto_produto += f"{i[0]}: R${i[1]}\n"
for i in produtos:
    total += i[1]

with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Cliente: {cliente}\n")
    arquivo.write(texto_produto)
    arquivo.write(f"TOTAL: R${total:.2f}\n")

with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    recibo = arquivo.read()
    index = recibo.find("TOTAL")
    print(f"Compra processada com sucesso! Valor cobrado: {recibo[index+7:index+14]}")




