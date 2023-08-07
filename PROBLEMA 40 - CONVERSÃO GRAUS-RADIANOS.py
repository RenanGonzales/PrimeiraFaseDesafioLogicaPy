# PROBLEMA 40 - CONVERSÃO GRAUS-RADIANOS

# Criar uma função que converta valores em graus
# para radianos. Após isso, desenvolva um algoritmo
# para o teste dessa função.

# Fórmula: RADIANOS = g(graus)PI/180

PI = 3.14
def radianos(pGraus):
    return pGraus*PI/180
graus = float(input('Digite quantos graus você quer converter em radianos: '))

rad = radianos(graus)

print('\n'+str(graus) + 'º = ' + str(rad) + ' radianos')

