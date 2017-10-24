from datetime import date

ano = int(input('Qual seu ano de nascimento? '))
atual = date.today().year

idade = atual - ano

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')
