import random

numero_secreto = random.randint(1, 10)

print("Tente adivinhar o número secreto entre 1 e 10.")

while True:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")
