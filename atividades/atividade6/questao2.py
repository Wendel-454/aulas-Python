"""
Escreva um programa que defina uma senha fixa no código (por exemplo, "123456").
Peça para o usuário digitar a senha.
Enquanto a senha digitada não for igual à senha correta, exiba a mensagem: "Senha incorreta. Tente novamente."
e peça a senha de novo (igual ao exemplo do "Joao" visto em aula). Quando o usuário acertar, exiba: "Acesso permitido!".
"""

#Resposta
senha_cadastrada = "123456"
senha_digitada = ""
while senha_digitada != senha_cadastrada:
    senha_digitada = input("Digite a sua senha: ")
    if senha_digitada == senha_cadastrada:
        print("Acesso permitido!")
    else:
        print("Senha incorreta. Tente novamente.")

