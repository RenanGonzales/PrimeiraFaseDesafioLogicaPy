# PROBLEMA 38 - CIRCUNFERÊNCIA

# Escreva um algoritmo para um programa que
# calcule a área e o perímetro de uma
# circunferência (em metros). Para isso o usuário
# deverá inserir o valor do raio (em metros). O
# programa deverá realizar os cálculos por meio das
# funções calcula_area e calcula_perimetro (com
# base unicamente no valor do raio).

pi = 3.14

def calcular_area(pRaio):
    return  (pi*(pRaio**2))
    
def calcular_perimetro(pRaio):
    return 2*pi*pRaio
    
pRaio = float(input('Insira o valor do Raio para que possamos começar:'))
calcular_area(pRaio)
calcular_perimetro(pRaio)
print(area)
print(perimetro)
    
    
    
    
# print('Olá... Boa noite, tudo bom? \n Hoje vamos estudar circulos') #Saudação
# raio = float(input('Insira o valor do Raio para que possamos começar:')) #Entrada
# diametro = (raio * 2) #Processo
# circunferencia = (diametro * 3.14) #Processo
# print('Diametro desse circulo é:', diametro) #Saida
# print('Circunferência desse circulo é:', circunferencia) #Saida
# print('Obrigado, boa noite!') #Saida