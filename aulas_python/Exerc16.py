""" Descrição do exercício: Nada Nada  """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('Inicio do Programa !')

salarioLiquido = float(input('Digite um Salario'))

INSS = 0.08
FGTS = 0.11

descontoInss = salarioLiquido * INSS

descontoFGTS = salarioLiquido * FGTS

salarioFinal = salarioLiquido - (INSS + FGTS)


print('Salario Final é : ', salarioFinal)

print('Fim do Programa !')
