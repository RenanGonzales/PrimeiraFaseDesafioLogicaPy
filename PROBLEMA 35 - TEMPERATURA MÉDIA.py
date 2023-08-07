#PROBLEMA 35 - TEMPERATURA MÉDIA

# Criar um algoritmo que receba a temperatura
# média de cada mês do ano, em centigrados, e
# armazene essas temperaturas em um vetor. Além
# disso, imprimir as temperaturas de todos os meses, a
# maior e a menor temperatura do ano e em que
# mês aconteceram.

temperatura = []
texto = '\n'
mes = 0
lmes = []
menormes = ''
maiormes = ''
for i in range(12):
    mes+=1
    temperatura.append(float(input('Digite a temperatura média referente ao mês ' + str(mes) + ' de 12: ')))
    texto = texto + 'Mês ' + str(mes) + ' = ' + str(temperatura[i]) + 'º Celsius\n'
    
    if i == 0:
        maior = temperatura[0]
        maiormes = str(mes)
        menor = temperatura[0]
        menormes = str(mes)
    if i != 0:
        if maior <= temperatura[i]:
            maior = float(temperatura[i])
            maiormes = str(mes)
        elif menor >= temperatura[i]:
            menor = float(temperatura[i])
            menormes = str(mes)
        
texto = texto + '\nMenor temperatura foi no mês ' + str(menormes) + ' e fez ' + str(menor) + 'º Celsius'
texto = texto +'\nMaior temperatura foi no mês ' + str(maiormes) + ' e fez ' + str(maior) + 'º Celsius'
print(texto)