# PROBLEMA 27 - FATORIAL

# Criar um algoritmo que solicite um número inteiro
# apresente o cálculo do fatorial do número
# digitado.
# Ex.:
# Digite um número para o cálculo do fatorial: 5
# Resposta: 5! = 5 x 4 x 3 x 2 x 1 = 120

entrada = int(input('Digite um número para o cálculo do fatorial: '))
fatorial = 0
saida = ''
contador = entrada -1
resultado = entrada * contador
saida = saida + str(entrada) + '!=' + str(entrada) + 'x'

while contador < entrada and contador >0:
    saida = saida + str(contador) + 'x'
    contador-=1
    fatorial = fatorial + resultado * contador
    
saida = saida + '=' + str(fatorial)
print(saida)
