# PROBLEMA 30 – TABUADA COMPLETA COM FOR

# Criar um algoritmo que pergunte se o usuário
# deseja visualizar a tabuada. Em caso afirmativo (‘S’
# ou ‘s”), o programa exibe automaticamente a
# tabuada dos números de 1 até 10.
# Obs.: Na apresentação do resultado, utilizar o for e apenas um
# comando “print”.

contador = 1
# contador1 = 1
valor = 1
saida = ''
tabuada = input('Deseja visualizar a tabuada? ')

if tabuada == "S" or tabuada == "s":
    for contador1 in range (1,11):
        for contador in range (1,11):
            resultado = valor*contador
            saida += str(valor) + 'x' + str(contador) + '=' + str(resultado) + '\n'
            
            if contador == 11:
                saida += '\n'
                valor+=1
        
    print(saida)
    
else:
    print('Você não quer visualizar a tabuada.')