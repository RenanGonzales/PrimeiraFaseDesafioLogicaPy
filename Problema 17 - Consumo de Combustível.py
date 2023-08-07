#Problema 17 - Consumo de Combustível
#Escreva um algoritmo que leia o percurso em km, o tipo de carro e informe o consumo estimado de combustível (em litros).
#Sabe-se que um carro tipo A faz 12 km com um litro de gasolina, um tipo B faz 9km e o tipo C, 8km por litro.

percurso = float(input('Digite quantos Km você percorreu: '))
modeloCarro = input('''\nEscolha seu modelo de carro:

[A ou a] Popular 1.0 (Faz 12Km por Litro)
[B ou b] Sport 1.6 (Faz 9Km por Litro)
[C ou c] Sport 2.0 Turbo (Faz 8Km por Litro)
                        
''')
if modeloCarro == "A" or modeloCarro == "a":
    consumo = 12
    media = percurso/consumo
    media = round(media,2)
    print('Sabendo que você percorreu',percurso,'Km e utiluzou o modelo:',modeloCarro,'\nVocê usou',media,'litros de gasolina.')
elif modeloCarro == "B" or modeloCarro == "b":
    consumo = 9
    media = percurso/consumo
    media = round(media,2)
    print('Sabendo que você percorreu',percurso,'Km e utiluzou o modelo:',modeloCarro,'\nVocê usou',media,'litros de gasolina.')
elif modeloCarro == "C" or modeloCarro == "c":
    consumo = 8
    media = percurso/consumo
    media = round(media,2)
    print('Sabendo que você percorreu',percurso,'Km e utiluzou o modelo:',modeloCarro,'\nVocê usou',media,'litros de gasolina.')
else:
    print('Modelo de carro inválido.')
