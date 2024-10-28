print("Você acorda em uma floresta misteriosa com uma cidade flutuante acima, nos céus. Você vê duas opções.")
print("1. Seguir em frente, afinal você vê o topo de um castelo no horizonte.")
print("2. Buscar uma forma de subir para a cidade que você vê.")

escolha1 = input("Escolha 1 ou 2: ")

if escolha1 == '1':
    print("Você segue em frente e se depara com draconicos menores, o que você faz?")
    print("1. Procura algo para se defender, caso tentem te atacar.")
    print("2. Decide correr o mais rápido possível em frente, seguindo seu caminho.")
    
    escolha2 = input("Escolha 1 ou 2: ")
    
    if escolha2 == '1':
        print("Os draconicos te viram com um toco na mão e te atacaram, sua história termina aqui!")
    elif escolha2 == '2':
        print("Parece que os draconicos eram inofensivos, você segue seu caminho")
    else:
        print("Escolha inválida! A aventura termina aqui.")
        
elif escolha1 == '2':
    print("Você olha ao redor e vê que um grifo descansa na sombra de uma árvore.")
    print("1. Tentar se aproximar e fazer amizade com o grifo.")
    print("2. Não vale a pena, você vai procurar uma vila por perto e procurar informações.")
    
    escolha2 = input("Escolha 1 ou 2: ")
    
    if escolha2 == '1':
        print("O grifo é amigável, parece te conhecer, ele permite que você o monte e juntos vocês sobem pra cidade flutuante.")
    elif escolha2 == '2':
        print("Você chega em uma vila próxima, mas todos são hostis e não entendem seu idioma, sua aventura termina aqui.")
    else:
        print("Escolha inválida! A aventura termina aqui.")
        
else:
    print("Escolha inválida! A aventura termina aqui.")