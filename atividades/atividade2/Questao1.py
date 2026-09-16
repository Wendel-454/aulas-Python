#sistema de atendimento hospitalar
nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
plano = input("Tem plano?")
resultado = plano == "sim"
resultado= idade > 17 and idade < 65 and resultado == True
print("seu nome é ",nome,",sua idade é ", idade,"você tem plano?",plano,"você foi aceito?", resultado)
