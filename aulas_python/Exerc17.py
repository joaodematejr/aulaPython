""" Descrição do exercício: Nada Nada  """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('__________________Inicio do Programa !__________________')

primeiroNumero = int(input('Primeiro Numero '))

segundoNumero = int(input('Segundo Numero '))


if primeiroNumero > segundoNumero:
    print('Esse maior numero: ', primeiroNumero)
if primeiroNumero < segundoNumero:
    print('Esse maior numero: ', segundoNumero)
if primeiroNumero == segundoNumero:
    print('Numero iguais')

print('__________________Fim do Programa !__________________')
