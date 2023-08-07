# PROBLEMA 34 - VERIFICA NÚMEROS

# Utilizando vetores (para armazenar e ler os dados),
# elaborar um algoritmo para ler um conjunto de 10
# números e informar:
# • Quantos números são iguais a 10.
# • Quantos números são maiores do que a média.
# • Quantos números são iguais a média.

valor = []
todosValores = []
texto = '\n'
valor10 = 0
soma = 0
maiorMedia = 0
menorMedia = 0

for i in range(10):
    entrada = float(input('Digite o valor: '))
    valor.append(float(entrada))
    
    if entrada == 10:
        valor10 = valor10 + 1
        
    todosValores.append(1)
    soma = soma + float(entrada)
    
media = soma/len(todosValores)

for i in range(10):
    if media <= valor[i]:
        maiorMedia+=1
    elif media >= valor[i]:
        menorMedia +=1


texto = texto + 'Quantidade de números iguais a 10: ' + str(valor10) + '\nQuantidade de números maiores do que a média: ' + str(maiorMedia) + '\nQuantidade de números menores do que a média: ' + str(menorMedia)
print(texto)