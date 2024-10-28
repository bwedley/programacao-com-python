firstNum = float(input("Digite o primeiro numero: "))
secondNum = float(input("Digite o segundo número: "))

soma = firstNum + secondNum
subtracao = firstNum - secondNum
multiplicacao = firstNum * secondNum
divisao = firstNum / secondNum if secondNum != 0 else "impossível divisão por zero"
divisao_inteira = firstNum // secondNum if secondNum != 0 else "impossivel divisão por zero"

print("\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}")