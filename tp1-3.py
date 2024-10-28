import random

def combinar_nomes(nome1, nome2):
    pedacoUm = random.randint(1, len(nome1) - 1)
    pedacoDois = random.randint(1, len(nome2) - 1)
    
    # Combina as partes dos nomes
    parte1 = nome1[:pedacoUm]
    parte2 = nome2[pedacoDois:]
    
    novo_nome = parte1 + parte2
    return novo_nome.capitalize()

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

novo_nome = combinar_nomes(nome1, nome2)
print(f"O novo nome criado é: {novo_nome}")
