# PROBLEMA 39 - VELOCIDADE MÉDIA

# Criar uma função que calcule a velocidade média
# do veículo (em km/h). A função deverá receber
# como argumentos a distância percorrida (em km) e
# o tempo de viagem (em minutos). Após isso,
# desenvolva um algoritmo para o teste dessa
# função.

def vMedia(pDistancia,pTempo):
    return pDistancia/(pTempo/60)

distancia = float(input('Digite a distancia percorrida em Km: '))
tempo = float(input('Digite o tempo da viagem em minutos: ')) 

velocidadeMedia = vMedia(distancia,tempo)

print('Velocidade média da viagem: ' + str(velocidadeMedia)+' Km/h')
