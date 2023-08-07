# PROBLEMA 28 - EMPRÉSTIMO BANCÁRIO

# Suponha que o “Banco Nacional da Família” faz empréstimos a juros
# zero para os clientes de baixa renda (renda familiar menor ou igual a
# um salário mínimo). Desenvolva um algoritmo de um programa que
# obtenha o nome do cliente, a renda familiar e o valor do
# empréstimo. Após isso, o programa deve mostrar o saldo estimado
# para cada mês pelos próximos 10 meses. Assuma que não há
# cobrança de juros nessa conta, que o cliente não faça novos
# empréstimos e que o cliente salde sua dívida em pagamentos
# mensais de 10% do valor original. Caso a renda familiar seja superior
# a um salário mínimo, o programa deve informar que não é possível
# realizar o empréstimo.

contador1 = 10
contador2 = 0
texto = ''
nome = str(input('Digite seu nome: '))
renda = float(input('Digite sua renda famíliar: '))
if renda < 1212:
    emprestimo = float(input('Digite o valor do empréstimo: '))
    while contador1 <= 10 and contador1 > 0:
        
        contador1-=1
        contador2+=1
        extrato = emprestimo*(contador1/100)
        extrato = round(extrato,2)
        texto += 'Mês ' + str(contador2) + ' valor em aberto: '+ str(extrato)
        texto+= '\n'
        
    print(texto)
else:
    print('Não é possível realizar o empréstimo.')

        