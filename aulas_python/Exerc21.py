""" Descrição do exercício: Nada Nada  """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('__________________Inicio do Programa !__________________')

primeiroNumero = int(input('Digite uma 1º Numero '))

segundoNumero = int(input('Digite uma 2º Numero '))

terceiroNumero = int(input('Digite uma 3º Numero '))


if (primeiroNumero > segundoNumero) or (primeiroNumero > terceiroNumero):
    print('Numero maior é :', primeiroNumero)
elif (segundoNumero > primeiroNumero) or (segundoNumero > terceiroNumero):
    print('Numero maior é :', segundoNumero)
elif (terceiroNumero > primeiroNumero) or (terceiroNumero > segundoNumero):
    print('Numero maior é :', terceiroNumero)


print('__________________Fim do Programa !__________________')
