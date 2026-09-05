#Resposta
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
operador = input("Digite o operador que deseja realizar: ")
match operador:
    case "+":
        print(f"O resultado é: {num1 + num2}")
    case "-":
        print(f"O resultado é: {num1 - num2}")
    case "*":
        print(f"O resultado é: {num1 * num2}")
    case "/":
        print(f"O resultado é: {num1 / num2}")
    case _:
        print("Operação inválida!")