valor_compra = float(input("Digite o valor da compra em R$: "))

desconto = 0

if valor_compra > 500:
    desconto = 0.25
elif valor_compra > 200:
    desconto = 0.15
elif valor_compra > 100:
    desconto = 0.10

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
