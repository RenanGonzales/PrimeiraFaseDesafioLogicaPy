# Problema 30 - Tabuada Completa com For
saida = ''
condicao = str(input('Você quer ver a tabuada? '))

if condicao == 's' or condicao == 'S':
    for i in range(1,11):
        for j in range(1,11):
            multiplicacao = int(i) * int(j)
            saida = saida + str(i) + ' x ' + str(j) + ' = ' + str(multiplicacao) + '\n'
            if int(j) == 10:
                saida = saida + '\n'
    print(saida)

else:
    print('Sem tabuadas :(')