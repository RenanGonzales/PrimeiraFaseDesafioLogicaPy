# PROBLEMA 29 CONVERSÃO CELSIUS-FAHRENHEIT

# Criar um algoritmo que imprima a tabela de conversão de graus
# Celsius-Fahrenheit para um intervalo definido pelo usuário. O
# algoritmo deve solicitar ao usuário o limite superior, inferior e o
# intervalo de decremento. Fórmula de Conversão: C = 5(F-32)/9

# C = 5(F-32)/9
# f=(9*c+160)/5

saida = '\n'
limiteSuperior = float(input('Digite o limite superior em Fahrenheit: '))
limiteInferior = float(input('Digite o limite inferior em Fahrenheit: '))
decremento = float(input('Digite o intervalo de decremento: '))

fahrenheit = limiteSuperior

while limiteSuperior >= limiteInferior:
    
    celsius = 5*(float(fahrenheit)-32)/9
    
    saida = saida + str(fahrenheit) + ' Fahrenheit = ' + str(celsius) + ' Celsius \n'
    
    limiteSuperior-=decremento
    fahrenheit-=decremento
    
print(saida)
