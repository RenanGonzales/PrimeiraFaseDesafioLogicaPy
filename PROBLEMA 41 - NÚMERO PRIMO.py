# PROBLEMA 41 - NÚMERO PRIMO

# Crie uma função que tem o objetivo de verificar se um número
# recebido é um número primo. A função deve ser do tipo lógica,
# isto é, retornar verdadeiro (caso seja primo) ou falso (caso não seja primo).
# Obs.: Os Números Primos são números naturais maiores do que 1 que
# possuem somente dois divisores, ou seja, são divisíveis por 1 e por ele
# mesmo.
# Mais informações: https://www.todamateria.com.br/numeros-primos/


def primos(pValor):
    contador = 0
    for i in range(1,pValor+1):
        if int(pValor)/i == 1:
            contador+=1
            
    if contador == 1:
        return 'primo'
        
    else:
        return 'não é primo'
        
valor = int(input('Digite o valor: '))
chaveLogica = primos(valor)

print(chaveLogica)

        
