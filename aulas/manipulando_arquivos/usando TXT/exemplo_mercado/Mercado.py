produtos = []
produtos.append("Leite")
produtos.append("Macarrão")
produtos.append("carne")
produtos.append("Açaí")



with open("Recibo.txt", "w", encoding="UTF-8") as arquivo:
    for produto in produtos:
        arquivo.write(f"{produto}\n")

with open("Recibo.txt", "r", encoding="UTF-8") as arquivo:
    print(arquivo.read())