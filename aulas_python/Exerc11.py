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

numero1 = float(input('Digite primeiro numero '))

operador = (input('Digite um operador '))

numero2 = float(input('Digite segundo numero '))

if operador == '+':
    print(numero1+numero2)
elif operador == '-':
    print(numero1-numero2)
if operador in '*':
    print(numero1*numero2)
elif operador in '/':
    print(numero1/numero2)
else:
    print('Operador Invalido')

print('Programa Encerrado com Sucesso !')
