"""
Uma loja está em promoção: o cliente ganha frete grátis se o valor da compra for maior que R$ 200.00 OU
se ele possuir o cartão VIP da loja. Peça ao usuário o valor da compra e pergunte se ele é VIP
(peça para digitar 1 para "Sim, sou VIP" ou 0 para "Não sou VIP").
Crie a lógica usando o operador or e imprima True se ele tem direito ao frete grátis ou False caso não tenha.
"""
#Resposta
valorCompra = float(input("Digite o valor de sua compra: "))
vip = (input("Cliente vip? Se sim, digite 1. Se não, digite 0. "))
resultadoVip = vip == "1"
frete = valorCompra >= 200 or resultadoVip
print("Tem direito ao frete grátis? ", frete)

