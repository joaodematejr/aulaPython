""" Descrição do exercício: Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido
mês. """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('Inicio do Programa !')

salario = float(input('Digite o salario'))

calculoBonificacao = salario / 10

resultadoFinal = calculoBonificacao + salario

print('Valor Final', resultadoFinal)

print('Fim do Programa !')
