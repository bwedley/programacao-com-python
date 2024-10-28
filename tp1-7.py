def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def categoria_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em centímetros: "))

imc = calcular_imc(peso, altura/100)

print(f"Seu IMC é: {imc:.2f}")
print("Categoria:", categoria_imc(imc))