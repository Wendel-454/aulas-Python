def media():
        nome = input("Digite seu nome: ")
        nota1 = float(input("Digite sua nota no primeiro bimestre: "))
        nota2 = float(input("Digite sua nota no segundo bimestre: "))
        nota3 = float(input("Digite sua nota no terceiro bimestre: "))
        nota4 = float(input("Digite sua nota no quarto bimestre: "))
        calcmedia = (nota1 + nota2 + nota3 + nota4) / 4
        if calcmedia >= 7:
            print(f"{nome}, sua média foi de {calcmedia:.2f} e você foi aprovado.")
        else:
            print(f"{nome}, sua média foi de {calcmedia:.2f} e você foi reprovado.")

media()
