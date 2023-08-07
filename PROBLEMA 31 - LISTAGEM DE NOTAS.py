# PROBLEMA 31 - LISTAGEM DE NOTAS

# Criar um algoritmo que armazene o nome e duas
# notas de 5 alunos e imprima a listagem contendo
# nome, as duas notas e a média de cada aluno.

lNome = []
lNota1 = []
lNota2 = []
lMedia = []
saida = ''

for i in range(5):
    lNome.append(input('\nDigite seu nome: '))
    lNota1.append(input('Digite a primeira nota: '))
    lNota2.append(input('Digite a segunda nota: '))
    media = (float(lNota1[i]) + float(lNota2[i]))/2
    lMedia.append(media)
    
    saida = saida + '\nNome: ' + str(lNome[i]) + '\nPrimeira nota: ' + str(lNota1[i]) + '\nSegunda nota: ' + str(lNota2[i]) + '\nMedia: ' + str(lMedia[i]) + '\n'
    
print(saida)