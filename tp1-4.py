def calculadora(operacao, num1, num2):
    if operacao == "adição":
        return num1 + num2
    elif operacao == "subtração":
        return num1 - num2
    elif operacao == "multiplicação":
        return num1 * num2
    elif operacao == "divisão":
        return num1 / num2 if num2 != 0 else "divisão por zero impossível"
    else:
        return "Operação inválida"

print("Escolha uma operação: adição, subtração, multiplicação, divisão")
operacao = input("Digite a operação desejada: ").lower()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = calculadora(operacao, num1, num2)
print(f"O resultado da {operacao} é: {resultado}")