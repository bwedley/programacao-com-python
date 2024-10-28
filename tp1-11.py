import random

num_dados = int(input("Quantos dados você deseja lançar? "))

if num_dados <= 0:
    print("impossível lançar zero dados.")
else:
    resultados = []
    total = 0
    for _ in range(num_dados):
        resultado = random.randint(1, 6)
        total += resultado
        resultados.append(resultado)

    print(f"Resultados dos lançamentos: {resultados}")
    print(f"Resultado total: {total}")