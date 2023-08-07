# PROBLEMA 26 – TABUADA COMPLETA

contador = 1
valor = 1
saida = ''
tabuada = input('Deseja visualizar a tabuada? ')

if tabuada == "S" or tabuada == "s":
    while contador <= 10 and valor <= 10:
        resultado = valor*contador
        saida += str(valor) + 'x' + str(contador) + '=' + str(resultado) + '\n'
        contador+=1
        
        if contador == 11:
            saida += '\n'
            contador = 1
            valor+=1
        
    print(saida)
    
else:
    print('Você não quer visualizar a tabuada.')