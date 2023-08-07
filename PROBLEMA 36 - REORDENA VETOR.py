# PROBLEMA 36 - REORDENA VETOR

# Criar uma algoritmo que leia os elementos de um
# vetor com 10 posições e escreva-o. Em seguida,
# troque o primeiro elemento pelo último, o segundo
# pelo penúltimo, o terceiro pelo antepenúltimo, a
# assim sucessivamente. Mostre o vetor depois das
# trocas.

lista = []
texto = '\n'


for i in range(10):
    lista.append(input('Insira o elemento ' + str(i+1) + ' de 10: '))
    texto+= str(lista[i]) + ' , '
    
print(lista[-9,0])