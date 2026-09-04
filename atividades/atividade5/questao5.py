#Resposta
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
operador = input("Digite o operador que deseja realizar: ")
match operador:
    case "+":
        resultado = num1 + num2
        print(f"O resultado é: {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"O resultado é: {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"O resultado é: {resultado}")
    case "/":
        resultado = num1 / num2
        print(f"O resultado é: {resultado}")
    case _:
        print("Operação inválida!")