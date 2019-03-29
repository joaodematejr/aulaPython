""" Descrição do exercício: Nada Nada  """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('__________________Inicio do Programa !__________________')

letra = (input('Digite uma Letra '))

letraMaiscula = letra.lower()

if letraMaiscula == "a" or letraMaiscula == 'e' or letraMaiscula == 'i' or letraMaiscula == 'o' or letraMaiscula == 'u':
    print('Vogal')
else:
    print('Não é uma vogal')


print('__________________Fim do Programa !__________________')
