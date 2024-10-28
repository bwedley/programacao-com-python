
frase = input("Digite uma palavra ou frase: ")

frase_sem_espaços = frase.replace(" ", "").lower()

if frase_sem_espaços == frase_sem_espaços[::-1]:
    print("A entrada é um palíndromo.")
else:
    print("A entrada não é um palíndromo.")