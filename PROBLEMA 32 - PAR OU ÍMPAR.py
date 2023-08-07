vnumeros = []
vresto = []
saida = '\n=================================== \n \n'
for i in range(15):
    vnumeros.append(int(input('Digite um número inteiro: ')))
    pares = (vnumeros[i]%2)
    if pares == 0:
        vresto.append(str(' é par'))
    else:
        vresto.append(str(' é impar'))
    saida = saida + str(vnumeros[i]) + str(vresto[i]) + '\n'
    
print(saida)
    