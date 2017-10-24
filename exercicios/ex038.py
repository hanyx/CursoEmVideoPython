v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

if v1 > v2:
    print('{} é maior que {}'.format(v1, v2))
elif v2 > v1:
    print('{} é maior que {}'.format(v2, v1))
else:
    print('Os valores são iguais')
