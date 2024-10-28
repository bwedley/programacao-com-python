votos = {"opção1": 0, "opção2": 0, "opção3": 0}

numero_votos = int(input("Quantas pessoas vão votar? "))

for i in range(numero_votos):
    print("\nOpções de voto:")
    print("1. Zezinho")
    print("2. Mariazinha")
    print("3. Joãozinho")
    
    voto = int(input("Digite o número da sua opção (1, 2 ou 3): "))

    if voto == 1:
        votos["opção1"] += 1
    elif voto == 2:
        votos["opção2"] += 1
    elif voto == 3:
        votos["opção3"] += 1
    else:
        print("Voto inválido! Por favor, escolha 1, 2 ou 3.")

print("\nResultado da votação:")
print(f"Zezinho: {votos['opção1']} votos")
print(f"Mariazinha: {votos['opção2']} votos")
print(f"Joãozinho: {votos['opção3']} votos")