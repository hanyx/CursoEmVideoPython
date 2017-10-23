dias = int(input('Quantos dias de aluguel? '))
km = int(input('Quantos km rodados? '))

val = 60*dias + 0.15*km

print('O preço a ser pago é de {}'.format(val))
