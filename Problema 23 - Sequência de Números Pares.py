# Problema 23 - Sequência de Números Pares
# 
# Escreva um algoritmo de um programa que exiba todos os número pares compreendidos entre 1 e 100.
# Além dos números, o programa deve mostrar ao final da execução a soma dos número pares.
# 
# Obs.: Utilizar a estrutura de repetição while.

contador = 1 #Valor inicial do contador
soma = 0
while contador <= 100: #definir condição
    pares = (contador%2) #Encontrar valores pares
    
    if pares == 0: 
        print(contador)
        soma = soma + contador #para somar foi preciso fazer a soma "mais alguma coisa", nesse caso foi o contador... Assim acumulando...
        
    contador = contador + 1
    
print(soma)