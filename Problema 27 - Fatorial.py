# Problema 27 - Fatorial

numero = int(input('Digite um número para cálcular o fatorial:'))
contador = numero - 1
resultado = numero
texto = str(numero) + '!=' + str(numero)

while contador >=1:
    resultado = resultado * contador
    texto += 'x' + str(contador)
    contador-=1
texto+= '=' + str(resultado)
print(texto)