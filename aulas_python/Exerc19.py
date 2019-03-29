""" Descrição do exercício: Nada Nada  """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('__________________Inicio do Programa !__________________')

categoria = int(input('Digite uma categoria '))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print('Categoria invalida ')
    preco = 0

print('O preço do produto é : R$',  preco)

print('__________________Fim do Programa !__________________')
