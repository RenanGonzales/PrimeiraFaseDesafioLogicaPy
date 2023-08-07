# PROBLEMA 33 - EXIBE LUCRO

# Criar um algoritmo que leia o preço de compra e o
# preço de venda de 10 mercadorias. O algoritmo
# deverá imprimir quantas mercadorias apresentam:
# • Lucro menor do que 10 %
# • Lucro entre 10% e 20%
# • Lucro > 20%
texto = '\n===================================================== \n \n'
lcompra = []
lvenda = []

menor10 = []
entre10e20 = []
maior20 = []

menor10p = 0
entre10e20p = 0
maior20p = 0

for i in range(10):
    lcompra.append(float(input('Insira o valor de compra do item: ')))
    lvenda.append(float(input('Insira o valor de venda do item: ')))
    
    #Lucro menor que 10%
    if lvenda[i] < lcompra[i] + (float(lcompra[i])*0.1):
        menor10p = menor10p + 1
    
    #Lucro entre 10% e 20%
    elif lvenda[i] >= lcompra[i] + (float(lcompra[i])*0.1) and lvenda[i] < lcompra[i]+(float(lcompra[i]*0.2)):
        entre10e20p = entre10e20p + 1
    
    #Lucro maior que 20%
    elif lvenda[i] > lcompra[i] + (float(lcompra[i]*0.2)):
        maior20p = maior20p + 1
        
        
texto = texto + 'Itens com lucro menor que 10%: ' + str(menor10p) + '\nItens com lucro entre 10% e 20%: ' + str(entre10e20p) + '\nItens com lucro acima de 20%: ' + str(maior20p)
print(texto)
        