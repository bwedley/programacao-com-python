palavras = input("Digite palavras separadas por virgula: ").split(",")

curtas = []
longas = []

for palavra in palavras:
    if len(palavra.strip()) < 5:
        curtas.append(palavra.strip())
    else:
        longas.append(palavra.strip())

print("Palavras curtas (menos de 5 letras):", curtas)
print("Palavras longas (5 letras ou mais):", longas)