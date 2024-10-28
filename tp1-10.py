import random

personagemUm = ["uma sacerdotisa", "uma guerreira", "um paladino", "um mago", "um vampiro"]
personagemDois = ["um troll", "uma orquisa", "um elfo", "um tauren", "um vulpera"]
acoes = ["encontrou", "salvou", "se perdeu de", "desafiou", "transformou"]
locais = ["em um castelo", "na floresta encantada", "em uma cidade em ruínas", "na caverna secreta", "em um continente desconhecido"]

persoUm = random.choice(personagemUm)
persoDois = random.choice(personagemDois)
acao = random.choice(acoes)
local = random.choice(locais)

historia = f"Certa vez {persoUm} {acao} {persoDois} {local}."

print(historia)
