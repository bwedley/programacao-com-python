def minutos_para_horas_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

def horas_minutos_para_minutos(horas, minutos):
    return horas * 60 + minutos

minutos = int(input("Digite o número de minutos para converter em horas e minutos: "))
horas, minutos_restantes = minutos_para_horas_minutos(minutos)
print(f"{minutos} minutos é {horas} horas e {minutos_restantes} minutos.")

horas = int(input("Digite a quantidade de horas para converter em minutos totais: "))
minutos = int(input("Digite a quantidade de minutos para converter em minutos totais: "))
total_minutos = horas_minutos_para_minutos(horas, minutos)
print(f"{horas} horas e {minutos} minutos é {total_minutos} minutos.")