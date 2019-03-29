""" Descrição do exercício: Nada Nada  """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('__________________Inicio do Programa !__________________')

velocidade = int(input('Digite velocidade '))


if velocidade > 80:
    calculoVelocidade = velocidade-80
    valorMulta = calculoVelocidade * 5
    print('Você foi multado, valor da multa é : R$', valorMulta)


print('__________________Fim do Programa !__________________')
