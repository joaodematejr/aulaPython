""" Descrição do exercício: 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média. """
""" Autor: João Dematé """
""" Data: Qui 14 de mar 2019 """

dia = '14'
mes = '03'
ano = '2018'

print('Hoje é dia {0}/{1}/{2}'.format(dia, mes, ano))

print('Inicio do Programa !')

nota1 = float(input('Digite a primeiro nota '))

nota2 = float(input('Digite a segunda nota '))

nota3 = float(input('Digite a terceira nota '))

nota4 = float(input('Digite a quarta nota '))

""" Calcular 4 notas """
soma = nota1 + nota2 + nota3 + nota4

""" Quantidade da media """
media = 4

""" Recebe a soma das 4 notas e divide pela media """
resultado = soma / media

print('Soma das Seguintes Notas', nota1, '',
      nota2, '', nota3, '', nota4, ' Média final ', resultado)

print('Programa Encerrado com Sucesso !')
